from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.corpus_helpers import canonical_pages, ensure_image_record, image_records, synthesis_pages

ROOT = Path(__file__).resolve().parents[1]
PREPARE = ROOT / "scripts" / "prepare-wiki-content.py"
OVERVIEW = ROOT / "scripts" / "prepare-overview-projections.py"


def load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def managed_hashes(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for directory in ("wiki", "wiki-assets")
        for path in sorted((root / directory).rglob("*"))
        if path.is_file()
    }


class ExactConsumerContractTest(unittest.TestCase):
    def test_checked_in_managed_inputs_exactly_match_head_git_blobs(self):
        tracked = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", "-z", "HEAD", "--", "wiki", "wiki-assets"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout.rstrip(b"\0").split(b"\0")
        expected_paths = {item.decode("utf-8") for item in tracked if item}
        actual_paths = set(managed_hashes(ROOT))
        self.assertEqual(actual_paths, expected_paths)
        for relative in sorted(expected_paths):
            expected = subprocess.run(
                ["git", "show", f"HEAD:{relative}"],
                cwd=ROOT,
                check=True,
                stdout=subprocess.PIPE,
            ).stdout
            self.assertEqual((ROOT / relative).read_bytes(), expected, relative)

    def test_consumer_paths_and_build_order_are_explicit_and_disjoint(self):
        self.assertTrue(PREPARE.is_file())
        self.assertTrue(OVERVIEW.is_file())
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertIn("source = '.generated/wiki'", config)
        self.assertIn("source = '.generated/wiki-projections'", config)
        self.assertIn("source = '.generated/data'", config)
        self.assertNotIn("source = 'wiki'", config)
        build = (ROOT / "build.sh").read_text(encoding="utf-8")
        ordered = [
            "prepare-overview-projections.py",
            "prepare-wiki-content.py",
            "prepare-wiki-content.py --check",
            "--cleanDestinationDir",
            "verify_pages_output.py",
        ]
        positions = [build.index(item) for item in ordered]
        self.assertEqual(positions, sorted(positions))

    def test_repository_has_no_semantic_or_model_entrypoint(self):
        protocol = (ROOT / "AGENTS.md").read_text(encoding="utf-8").casefold()
        self.assertIn("must never run a coding agent or perform semantic synthesis", protocol)
        for forbidden in (
            ROOT / "tools/ingest.py",
            ROOT / "tools/lint.py",
            ROOT / "tools/synthesis.py",
            ROOT / ".claude/commands/wiki-ingest.md",
        ):
            self.assertFalse(forbidden.exists(), str(forbidden))
        for path in (PREPARE, OVERVIEW):
            text = path.read_text(encoding="utf-8").casefold()
            for token in (
                "openai",
                "anthropic",
                "codex",
                "claude",
                "from tools import synthesis",
                "import tools.synthesis",
                "-m tools.synthesis",
            ):
                self.assertNotIn(token, text, f"{path}: {token}")

    def test_consumer_has_no_retired_producer_runtime(self):
        tools = ROOT / "tools"
        self.assertFalse(tools.exists() and any(tools.rglob("*")))
        verifier = (ROOT / "scripts/verify_pages_output.py").read_text(encoding="utf-8")
        for forbidden in ("tools.validate_publish", "prepare-wiki-content", "prepare_overview"):
            self.assertNotIn(forbidden, verifier)

    def test_projection_derives_source_only_evidence_and_preserves_canonical(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki")
        before = managed_hashes(ROOT)
        report = prepare.prepare(ROOT)
        expected_counts = {
            section: len(canonical_pages(ROOT, section))
            for section in ("concepts", "entities", "sources")
        }
        self.assertEqual(report.concepts, expected_counts["concepts"])
        self.assertEqual(report.entities, expected_counts["entities"])
        self.assertEqual(report.sources, expected_counts["sources"])
        self.assertEqual(managed_hashes(ROOT), before)
        signals = json.loads((ROOT / ".generated/data/wiki_knowledge_signals.json").read_text())
        expected_synthesis = synthesis_pages(ROOT)
        self.assertEqual(set(signals["pages"]), {page[0] for page in expected_synthesis})
        for key, _title, section, metadata in expected_synthesis:
            signal = signals["pages"][key]
            sources = metadata["sources"]
            self.assertEqual(signal["source_note_count"], len(dict.fromkeys(sources)))
            self.assertNotIn("episode_count", signal)
            self.assertNotIn("show_count", signal)
            self.assertEqual([item["key"] for item in signal["sources"]], sources)
            projected = ROOT / ".generated/wiki" / section / f"{key}.md"
            canonical = ROOT / "wiki" / section / f"{key}.md"
            self.assertEqual(projected.read_bytes(), canonical.read_bytes())
        for source_key, filename, alt in image_records(ROOT):
            source = (ROOT / ".generated/wiki/sources" / source_key / "index.md").read_text()
            self.assertIn(f"![{alt}]({filename})", source)

    def test_section_landings_include_every_canonical_identity(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki_landings")
        prepare.prepare(ROOT)
        for section in ("concepts", "entities"):
            landing = (ROOT / ".generated/wiki" / section / "_index.md").read_text(encoding="utf-8")
            for page in sorted((ROOT / "wiki" / section).glob("*.md")):
                self.assertIn(f"  - key: {json.dumps(page.stem)}", landing)

    def test_check_detects_drift_and_write_removes_owned_stale_files(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki_stale")
        prepare.prepare(ROOT)
        stale = ROOT / ".generated/wiki/entities/stale.md"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.write_text(prepare.GENERATED_NOTICE + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "stale generated output"):
            prepare.prepare(ROOT, check=True)
        prepare.prepare(ROOT)
        self.assertFalse(stale.exists())
        prepare.prepare(ROOT, check=True)

    def test_unowned_collision_is_never_overwritten(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki_collision")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            shutil.copytree(ROOT / "wiki", fixture / "wiki")
            shutil.copytree(ROOT / "wiki-assets", fixture / "wiki-assets")
            page = (canonical_pages(fixture, "concepts") + canonical_pages(fixture, "entities"))[0]
            collision = fixture / ".generated/wiki" / page[2] / f"{page[0]}.md"
            collision.parent.mkdir(parents=True)
            collision.write_text("manual\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unowned output collision"):
                prepare.prepare(fixture)
            self.assertEqual(collision.read_text(), "manual\n")

    def test_unowned_stale_binary_is_never_deleted(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki_binary_collision")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            shutil.copytree(ROOT / "wiki", fixture / "wiki")
            shutil.copytree(ROOT / "wiki-assets", fixture / "wiki-assets")
            collision = fixture / ".generated/wiki/sources/manual/unowned.jpg"
            collision.parent.mkdir(parents=True)
            collision.write_bytes(b"manual binary")
            with self.assertRaisesRegex(ValueError, "unowned stale output"):
                prepare.prepare(fixture)
            self.assertEqual(collision.read_bytes(), b"manual binary")

    def test_manifest_digest_allows_generated_image_lifecycle(self):
        prepare = load_script(PREPARE, "prepare_personal_wiki_binary_lifecycle")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            shutil.copytree(ROOT / "wiki", fixture / "wiki")
            shutil.copytree(ROOT / "wiki-assets", fixture / "wiki-assets")
            ensure_image_record(fixture)
            prepare.prepare(fixture)
            images = image_records(fixture)
            source_key = images[0][0]
            source_assets = fixture / "wiki-assets" / source_key
            manifest_path = source_assets / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            removed = manifest["images"].pop()
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            (source_assets / removed["file"]).unlink()
            generated = fixture / ".generated/wiki/sources" / source_key / removed["file"]
            self.assertTrue(generated.is_file())
            prepare.prepare(fixture)
            self.assertFalse(generated.exists())
            prepare.prepare(fixture, check=True)


if __name__ == "__main__":
    unittest.main()

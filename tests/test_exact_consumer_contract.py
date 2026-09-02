from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

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
    def test_checked_in_managed_inputs_are_exact_producer_fixture(self):
        expected = json.loads(
            (ROOT / "tests/fixtures/producer-managed-sha256.json").read_text(encoding="utf-8")
        )
        self.assertEqual(managed_hashes(ROOT), expected)

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
            for token in ("openai", "anthropic", "codex", "claude", "tools.synthesis"):
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
        self.assertEqual(report.concepts, 3)
        self.assertEqual(report.entities, 3)
        self.assertEqual(report.sources, 1)
        self.assertEqual(managed_hashes(ROOT), before)
        signals = json.loads((ROOT / ".generated/data/wiki_knowledge_signals.json").read_text())
        signal = signals["pages"]["AIProductionPipeline"]
        self.assertEqual(signal["source_note_count"], 1)
        self.assertNotIn("episode_count", signal)
        self.assertNotIn("show_count", signal)
        self.assertEqual(signal["sources"][0]["key"], "ai-guide-for-humanities-workers")
        self.assertEqual(signal["sources"][0]["url"], "/wiki/sources/ai-guide-for-humanities-workers/")
        projected = (ROOT / ".generated/wiki/concepts/AIProductionPipeline.md").read_bytes()
        self.assertEqual(projected, (ROOT / "wiki/concepts/AIProductionPipeline.md").read_bytes())
        source = (ROOT / ".generated/wiki/sources/ai-guide-for-humanities-workers/index.md").read_text()
        self.assertIn("## Images", source)
        self.assertIn("![测试时的流程例子](0001-c6a9ce8a8360b26d.jpg)", source)

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
            collision = fixture / ".generated/wiki/concepts/AIProductionPipeline.md"
            collision.parent.mkdir(parents=True)
            collision.write_text("manual\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "unowned output collision"):
                prepare.prepare(fixture)
            self.assertEqual(collision.read_text(), "manual\n")


if __name__ == "__main__":
    unittest.main()

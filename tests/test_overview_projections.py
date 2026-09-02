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
SCRIPT = ROOT / "scripts/prepare-overview-projections.py"


def load_script(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class OverviewProjectionTest(unittest.TestCase):
    def test_compact_synthesis_and_open_questions_are_projected_without_semantic_work(self):
        overview = load_script("personal_overview")
        before = hashlib.sha256((ROOT / "wiki/overview.md").read_bytes()).hexdigest()
        report = overview.project(ROOT)
        self.assertEqual(report.synthesis_source, "compact")
        self.assertEqual(report.source_count, 1)
        namespace = (ROOT / ".generated/wiki-projections/_index.md").read_text()
        self.assertIn("render: never", namespace)
        self.assertIn("list: never", namespace)
        current = (ROOT / ".generated/wiki-projections/current-synthesis.md").read_text()
        self.assertIn('url: "/wiki/current-synthesis/"', current)
        self.assertIn('synthesis_source: "compact"', current)
        self.assertIn("## Executive Summary", current)
        self.assertNotIn("episode_count:", current)
        questions = (ROOT / ".generated/wiki-projections/open-questions.md").read_text()
        self.assertIn("不同人文学科任务需要怎样的最低证据", questions)
        history = (ROOT / ".generated/wiki-projections/update-history/_index.md").read_text()
        canonical = (ROOT / "wiki/overview.md").read_text(encoding="utf-8")
        canonical_intro = overview._overview_sections(canonical)[1]
        self.assertTrue(canonical_intro)
        self.assertIn(canonical_intro, history)
        self.assertEqual(hashlib.sha256((ROOT / "wiki/overview.md").read_bytes()).hexdigest(), before)

    def test_first_sync_history_never_labels_consumer_commit_as_producer_revision(self):
        overview = load_script("personal_overview_first_sync")
        overview.project(ROOT)
        history = (ROOT / ".generated/wiki-projections/update-history/_index.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("First synchronized canonical overview", history)
        self.assertNotIn("e1a9c4ac63a1", history)
        self.assertNotIn("Canonical overview revision", history)

    def test_check_and_owned_stale_cleanup_are_deterministic(self):
        overview = load_script("personal_overview_stale")
        overview.project(ROOT)
        overview.project(ROOT, check=True)
        stale = ROOT / ".generated/wiki-projections/stale.md"
        stale.write_text(overview.GENERATED_NOTICE + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "stale overview projection"):
            overview.project(ROOT, check=True)
        overview.project(ROOT)
        self.assertFalse(stale.exists())
        overview.project(ROOT, check=True)

    def test_invalid_compact_digest_fails_closed(self):
        overview = load_script("personal_overview_invalid")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            shutil.copytree(ROOT / "wiki", fixture / "wiki")
            current = fixture / "wiki/_generated/synthesis/current.md"
            current.write_text(current.read_text() + "tampered\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "digest"):
                overview.project(fixture)

    def test_tampered_topic_and_matching_manifest_digest_fail_closed(self):
        overview = load_script("personal_overview_tampered_topic")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            shutil.copytree(ROOT / "wiki", fixture / "wiki")
            synthesis = fixture / "wiki/_generated/synthesis"
            topic = synthesis / "topics/ai-and-technology.md"
            original_topic = topic.read_text(encoding="utf-8")
            tampered_topic = original_topic.replace(
                "Humanistic AI practice is strongest",
                "Tampered topic prose claims AI is infallible",
                1,
            )
            self.assertNotEqual(tampered_topic, original_topic)
            topic.write_text(tampered_topic, encoding="utf-8")
            manifest_path = synthesis / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["topics"]["ai-and-technology"]["output_digest"] = hashlib.sha256(
                topic.read_bytes()
            ).hexdigest()
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "topic synthesis bundle"):
                overview.project(fixture)

    def test_complete_bundle_inventory_ledger_and_global_identity_are_authenticated(self):
        overview = load_script("personal_overview_complete_bundle")
        mutations = ("extra-topic", "ledger-coverage", "global-overview")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as td:
                fixture = Path(td)
                shutil.copytree(ROOT / "wiki", fixture / "wiki")
                synthesis = fixture / "wiki/_generated/synthesis"
                if mutation == "extra-topic":
                    (synthesis / "topics/injected.md").write_text("injected\n", encoding="utf-8")
                elif mutation == "ledger-coverage":
                    ledger_path = synthesis / "paragraph-ledger.json"
                    ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
                    ledger["coverage"]["assigned_paragraph_ids"] = []
                    ledger_path.write_text(
                        json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8",
                    )
                else:
                    manifest_path = synthesis / "manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["global"]["overview_digest"] = "0" * 64
                    manifest_path.write_text(
                        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                        encoding="utf-8",
                    )
                with self.assertRaisesRegex(ValueError, "(?:topic synthesis bundle|global identity)"):
                    overview.project(fixture)

    def test_duplicate_keys_in_release_synthesis_json_fail_closed(self):
        overview = load_script("personal_overview_duplicate_json")
        files_and_keys = (
            ("manifest.json", '  "schema_version": 1,\n'),
            (
                "paragraph-ledger.json",
                '  "overview_commit": "9dbf2381f5120326a4ba2dc4f5bd66cae5636d7e",\n',
            ),
            (
                "claims/ai-and-technology.json",
                '      "status": "supported",\n',
            ),
        )
        for relative, field in files_and_keys:
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as td:
                fixture = Path(td)
                shutil.copytree(ROOT / "wiki", fixture / "wiki")
                target = fixture / "wiki/_generated/synthesis" / relative
                original = target.read_text(encoding="utf-8")
                self.assertEqual(original.count(field), 1)
                target.write_text(original.replace(field, field + field, 1), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "topic synthesis bundle has invalid"):
                    overview.project(fixture)


if __name__ == "__main__":
    unittest.main()

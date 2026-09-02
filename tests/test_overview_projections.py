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


if __name__ == "__main__":
    unittest.main()

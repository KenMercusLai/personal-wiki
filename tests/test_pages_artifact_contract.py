from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/verify_pages_output.py"
PUBLIC = ROOT / "public"


def load_verifier(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class PagesArtifactContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["./build.sh"], cwd=ROOT, check=True)

    def test_built_artifact_has_required_routes_and_dom_signals(self):
        verifier = load_verifier("personal_artifact")
        report = verifier.verify_site(PUBLIC, ROOT)
        self.assertEqual(report.html_pages, 72)
        self.assertEqual(report.wiki_pages, 71)
        self.assertEqual(report.local_images, 2)

    def test_hidden_canonical_pages_and_projection_namespace_are_absent(self):
        for route in (
            "wiki/index/index.html",
            "wiki/log/index.html",
            "wiki/overview/index.html",
            "wiki/_generated/index.html",
            "wiki-projections/index.html",
        ):
            self.assertFalse((PUBLIC / route).exists(), route)

    def test_wrong_html_and_generated_projection_cannot_fool_independent_oracle(self):
        verifier = load_verifier("personal_artifact_independent")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            copied = fixture / "public"
            shutil.copytree(PUBLIC, copied)
            repository = fixture / "repository"
            for directory in ("wiki", "wiki-assets", ".generated"):
                shutil.copytree(ROOT / directory, repository / directory)
            generated = repository / ".generated/data/wiki_knowledge_signals.json"
            generated.write_text(
                generated.read_text(encoding="utf-8").replace('"source_note_count": 1', '"source_note_count": 9'),
                encoding="utf-8",
            )
            page = copied / "wiki/concepts/aiproductionpipeline/index.html"
            page.write_text(
                page.read_text(encoding="utf-8").replace("data-source-count=1", "data-source-count=9", 1),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "source-derived knowledge signal mismatch"):
                verifier.verify_site(copied, repository)

    def test_public_image_bytes_are_checked_against_canonical_sidecar(self):
        verifier = load_verifier("personal_artifact_image")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            image = copied / "wiki/sources/ai-guide-for-humanities-workers/0001-c6a9ce8a8360b26d.jpg"
            image.write_bytes(image.read_bytes() + b"tampered")
            with self.assertRaisesRegex(ValueError, "image bytes differ"):
                verifier.verify_site(copied, ROOT)

    def test_broken_internal_link_is_detected(self):
        verifier = load_verifier("personal_artifact_broken")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            page = copied / "wiki/concepts/aiproductionpipeline/index.html"
            page.write_text(page.read_text().replace("wiki/concepts/materialstimestaste/", "wiki/concepts/missing/", 1))
            with self.assertRaisesRegex(ValueError, "unresolved internal URL"):
                verifier.verify_site(copied, ROOT)


if __name__ == "__main__":
    unittest.main()

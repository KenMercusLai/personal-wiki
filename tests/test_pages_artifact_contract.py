from __future__ import annotations

import importlib.util
from pathlib import Path
import re
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

    def test_unresolved_wikilink_in_non_html_public_text_is_rejected(self):
        verifier = load_verifier("personal_artifact_text_wikilink")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            (copied / "index.xml").unlink(missing_ok=True)
            (copied / "leaked-feed.xml").write_text(
                "<rss><description>See [[AIProductionPipeline]]</description></rss>\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "unresolved canonical syntax"):
                verifier.verify_site(copied, ROOT)

    def test_entity_encoded_wikilink_in_non_html_public_text_is_rejected(self):
        verifier = load_verifier("personal_artifact_encoded_text_wikilink")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            (copied / "index.xml").unlink(missing_ok=True)
            (copied / "leaked-feed.xml").write_text(
                "<rss><description>See &#91;&#91;AIProductionPipeline&#93;&#93;</description></rss>\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "unresolved canonical syntax"):
                verifier.verify_site(copied, ROOT)

    def test_synthesis_pages_require_the_exact_complete_ordered_h2_schema(self):
        verifier = load_verifier("personal_artifact_exact_h2_schema")
        cases = (
            (
                "concept-wrong-heading",
                "wiki/concepts/aiproductionpipeline/index.html",
                "<h2 id=definition>Definition</h2>",
                "<h2 id=wrong>Wrong</h2>",
            ),
            (
                "concept-extra-heading",
                "wiki/concepts/aiproductionpipeline/index.html",
                "<h2 id=current-synthesis>Current Synthesis</h2>",
                "<h2 id=unexpected>Unexpected</h2><h2 id=current-synthesis>Current Synthesis</h2>",
            ),
            (
                "concept-misordered-headings",
                "wiki/concepts/aiproductionpipeline/index.html",
                "<h2 id=definition>Definition</h2>",
                "<h2 id=current-synthesis>Current Synthesis</h2>",
            ),
            (
                "entity-wrong-heading",
                "wiki/entities/funes/index.html",
                "<h2 id=overview>Overview</h2>",
                "<h2 id=wrong>Wrong</h2>",
            ),
            (
                "entity-extra-heading",
                "wiki/entities/funes/index.html",
                "<h2 id=current-profile>Current Profile</h2>",
                "<h2 id=unexpected>Unexpected</h2><h2 id=current-profile>Current Profile</h2>",
            ),
            (
                "entity-misordered-headings",
                "wiki/entities/funes/index.html",
                "<h2 id=overview>Overview</h2>",
                "<h2 id=current-profile>Current Profile</h2>",
            ),
        )
        for name, relative, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(PUBLIC, copied)
                page = copied / relative
                text = page.read_text(encoding="utf-8")
                if "misordered" in name:
                    other = new
                    self.assertIn(old, text)
                    self.assertIn(other, text)
                    text = text.replace(old, "__H2_SWAP__", 1).replace(other, old, 1).replace("__H2_SWAP__", other, 1)
                else:
                    text = text.replace(old, new, 1)
                self.assertNotEqual(text, page.read_text(encoding="utf-8"))
                page.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "exact ordered H2 schema"):
                    verifier.verify_site(copied, ROOT)

    def test_relationship_anchors_match_exact_canonical_targets_and_titles(self):
        verifier = load_verifier("personal_artifact_exact_relationships")
        cases = (
            (
                "concept-existing-source-route",
                "wiki/concepts/aiproductionpipeline/index.html",
                "/wiki/concepts/aiworkflowforhumanitiesworkers/",
                "/wiki/sources/ai-guide-for-humanities-workers/",
            ),
            (
                "concept-unrelated-existing-route",
                "wiki/concepts/aiproductionpipeline/index.html",
                "/wiki/concepts/aiworkflowforhumanitiesworkers/",
                "/wiki/entities/funes/",
            ),
            (
                "concept-wrong-label",
                "wiki/concepts/aiproductionpipeline/index.html",
                ">人文工作者的 AI 工作流</a>",
                ">Wrong relationship label</a>",
            ),
            (
                "entity-existing-source-route",
                "wiki/entities/funes/index.html",
                "/wiki/entities/hanyang/",
                "/wiki/sources/ai-guide-for-humanities-workers/",
            ),
            (
                "entity-wrong-label",
                "wiki/entities/funes/index.html",
                ">汉洋</a>",
                ">Wrong relationship label</a>",
            ),
        )
        for name, relative, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(PUBLIC, copied)
                page = copied / relative
                text = page.read_text(encoding="utf-8")
                relationship_id = "related-concepts" if "/concepts/" in relative else "relationships"
                prefix, relationship = text.split(f"<h2 id={relationship_id}>", 1)
                changed = relationship.replace(old, new, 1)
                self.assertNotEqual(changed, relationship)
                page.write_text(prefix + f"<h2 id={relationship_id}>" + changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "relationship anchor mismatch"):
                    verifier.verify_site(copied, ROOT)

    def test_sources_inventory_matches_exact_canonical_key_route_and_title(self):
        verifier = load_verifier("personal_artifact_exact_sources_inventory")
        cases = (
            (
                "wrong-key",
                "data-source-key=ai-guide-for-humanities-workers",
                "data-source-key=wrong-source-key",
            ),
            (
                "wrong-existing-route",
                "/wiki/sources/ai-guide-for-humanities-workers/",
                "/wiki/concepts/aiproductionpipeline/",
            ),
            (
                "reviewer-wrong-title",
                ">给人文工作者的 AI 使用指南</a>",
                ">Wrong source title</a>",
            ),
        )
        for name, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(PUBLIC, copied)
                page = copied / "wiki/concepts/aiproductionpipeline/index.html"
                text = page.read_text(encoding="utf-8")
                prefix, inventory = text.split("<section class=wiki-knowledge-sources", 1)
                changed = inventory.replace(old, new, 1)
                self.assertNotEqual(changed, inventory)
                page.write_text(prefix + "<section class=wiki-knowledge-sources" + changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "source inventory link/title mismatch"):
                    verifier.verify_site(copied, ROOT)

    def test_every_verifier_json_input_rejects_duplicate_keys_at_any_depth(self):
        verifier = load_verifier("personal_artifact_strict_duplicate_json")
        cases = (
            (
                "reviewer-synthesis-manifest-top-level",
                "wiki/_generated/synthesis/manifest.json",
                '  "schema_version": 1,',
                '  "schema_version": 1,\n  "schema_version": 1,',
            ),
            (
                "synthesis-manifest-nested",
                "wiki/_generated/synthesis/manifest.json",
                '      "source_count": 1',
                '      "source_count": 1,\n      "source_count": 1',
            ),
            (
                "paragraph-ledger",
                "wiki/_generated/synthesis/paragraph-ledger.json",
                '  "schema_version": 1',
                '  "schema_version": 1,\n  "schema_version": 1',
            ),
            (
                "claims-nested",
                "wiki/_generated/synthesis/claims/ai-and-technology.json",
                '      "global_candidate": true,',
                '      "global_candidate": true,\n      "global_candidate": true,',
            ),
            (
                "image-sidecar-nested",
                "wiki-assets/ai-guide-for-humanities-workers/manifest.json",
                '      "file": "0001-c6a9ce8a8360b26d.jpg",',
                '      "file": "0001-c6a9ce8a8360b26d.jpg",\n      "file": "0001-c6a9ce8a8360b26d.jpg",',
            ),
            (
                "generated-wiki-links",
                ".generated/data/wiki_links.json",
                '    "url": "/wiki/concepts/aiproductionpipeline/"',
                '    "url": "/wiki/concepts/aiproductionpipeline/",\n    "url": "/wiki/concepts/aiproductionpipeline/"',
            ),
            (
                "generated-knowledge-signals-nested",
                ".generated/data/wiki_knowledge_signals.json",
                '      "source_note_count": 1,',
                '      "source_note_count": 1,\n      "source_note_count": 1,',
            ),
            (
                "generated-prepare-manifest",
                ".generated/data/prepare-wiki-manifest.json",
                '  "_generated_by": "scripts/prepare-wiki-content.py",',
                '  "_generated_by": "scripts/prepare-wiki-content.py",\n  "_generated_by": "scripts/prepare-wiki-content.py",',
            ),
        )
        for name, relative, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                repository = Path(td) / "repository"
                for directory in ("wiki", "wiki-assets", ".generated"):
                    shutil.copytree(ROOT / directory, repository / directory)
                path = repository / relative
                text = path.read_text(encoding="utf-8")
                changed = text.replace(old, new, 1)
                self.assertNotEqual(changed, text)
                path.write_text(changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, r"strict JSON object.*duplicate JSON key"):
                    verifier.verify_site(PUBLIC, repository)

    def test_verifier_json_inputs_reject_constants_malformed_and_nonobject_roots(self):
        verifier = load_verifier("personal_artifact_strict_invalid_json")
        cases = (
            (
                "synthesis-nan",
                "wiki/_generated/synthesis/manifest.json",
                '  "schema_version": 1,',
                '  "schema_version": NaN,',
            ),
            (
                "paragraph-ledger-nonobject",
                "wiki/_generated/synthesis/paragraph-ledger.json",
                None,
                "[]\n",
            ),
            (
                "claims-negative-infinity",
                "wiki/_generated/synthesis/claims/ai-and-technology.json",
                '      "global_candidate": true,',
                '      "global_candidate": -Infinity,',
            ),
            (
                "image-sidecar-infinity",
                "wiki-assets/ai-guide-for-humanities-workers/manifest.json",
                '  "version": 1,',
                '  "version": Infinity,',
            ),
            (
                "generated-wiki-links-nan",
                ".generated/data/wiki_links.json",
                '    "section": "concepts",',
                '    "section": NaN,',
            ),
            (
                "generated-knowledge-signals-malformed",
                ".generated/data/wiki_knowledge_signals.json",
                None,
                "{\n",
            ),
            (
                "generated-prepare-manifest-nonobject",
                ".generated/data/prepare-wiki-manifest.json",
                None,
                '"not an object"\n',
            ),
        )
        for name, relative, old, replacement in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                repository = Path(td) / "repository"
                for directory in ("wiki", "wiki-assets", ".generated"):
                    shutil.copytree(ROOT / directory, repository / directory)
                path = repository / relative
                original = path.read_text(encoding="utf-8")
                changed = replacement if old is None else original.replace(old, replacement, 1)
                self.assertNotEqual(changed, original)
                path.write_text(changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, r"strict JSON object"):
                    verifier.verify_site(PUBLIC, repository)

    def test_rendered_jsonld_uses_the_independent_strict_object_parser(self):
        verifier = load_verifier("personal_artifact_strict_jsonld")
        cases = (
            (
                "duplicate-top-level",
                '"@type":"WebSite"',
                '"@type":"WebSite","@type":"WebSite"',
            ),
            (
                "duplicate-nested",
                '{"@context"',
                '{"probe":{"key":1,"key":1},"@context"',
            ),
            (
                "non-standard-constant",
                '{"@context"',
                '{"probe":NaN,"@context"',
            ),
        )
        for name, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(PUBLIC, copied)
                page = copied / "index.html"
                text = page.read_text(encoding="utf-8")
                changed = text.replace(old, new, 1)
                self.assertNotEqual(changed, text)
                page.write_text(changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, r"strict JSON object"):
                    verifier.verify_site(copied, ROOT)

    def test_section_scoped_schema_date_provenance_and_jsonld_are_enforced(self):
        verifier = load_verifier("personal_artifact_section_scopes")

        def strip_anchors(text: str, start: str, end: str) -> str:
            prefix, remainder = text.split(start, 1)
            section, suffix = remainder.split(end, 1)
            stripped = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", section)
            self.assertNotEqual(stripped, section)
            return prefix + start + stripped + end + suffix

        def mutate(name: str, copied: Path) -> None:
            if name in {"evidence-anchor", "relationship-anchor", "sources-scope"}:
                page = copied / "wiki/concepts/aiproductionpipeline/index.html"
                text = page.read_text(encoding="utf-8")
                if name == "evidence-anchor":
                    text = strip_anchors(text, "<h2 id=evidence>", "<h2 id=counterevidence--qualifications>")
                elif name == "relationship-anchor":
                    text = strip_anchors(text, "<h2 id=related-concepts>", "</div><section class=wiki-knowledge-sources")
                else:
                    pattern = re.compile(
                        r"(<section class=wiki-knowledge-sources\b.*?<ol>)(<li data-source-key=.*?</li>)(</ol>)"
                    )
                    match = pattern.search(text)
                    self.assertIsNotNone(match)
                    assert match is not None
                    text = text[: match.start()] + match.group(2) + match.group(1) + match.group(3) + text[match.end() :]
                page.write_text(text, encoding="utf-8")
                return
            page = copied / "wiki/current-synthesis/index.html"
            text = page.read_text(encoding="utf-8")
            if name == "current-date":
                changed = text.replace(
                    "class=synthesis-updated>Updated <time datetime=2026-09-02",
                    "class=synthesis-updated>Updated <time datetime=not-a-date",
                    1,
                )
            else:
                changed = text.replace(
                    '"name":"Current Synthesis · Ken 的个人知识 Wiki"',
                    '"name":"Wrong synthesis identity"',
                    1,
                )
            self.assertNotEqual(changed, text)
            page.write_text(changed, encoding="utf-8")

        for mutation in (
            "evidence-anchor",
            "relationship-anchor",
            "sources-scope",
            "current-date",
            "jsonld-name",
        ):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(PUBLIC, copied)
                mutate(mutation, copied)
                with self.assertRaisesRegex(ValueError, "(?:Evidence|Related Concepts|source inventory|date|JSON-LD name)"):
                    verifier.verify_site(copied, ROOT)


if __name__ == "__main__":
    unittest.main()

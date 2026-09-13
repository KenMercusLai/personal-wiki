from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

from tests.corpus_helpers import (
    build_schema_fixture,
    duplicate_scalar_key,
    expected_html_routes,
    image_records,
    replace_scalar_with_constant,
    synthesis_topic_ids,
)

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


class CanonicalMarkdownVisibleTextTest(unittest.TestCase):
    def test_inline_code_delimiters_are_not_expected_in_rendered_questions(self):
        verifier = load_verifier("personal_artifact_canonical_markdown")
        self.assertEqual(
            verifier._canonical_markdown_visible_text(
                "How should developers back up WSL before `wsl --unregister`?"
            ),
            "How should developers back up WSL before wsl --unregister?",
        )

    def test_unclosed_code_delimiters_remain_visible(self):
        verifier = load_verifier("personal_artifact_unclosed_code")
        self.assertEqual(
            verifier._canonical_markdown_visible_text("Keep the unmatched ` delimiter"),
            "Keep the unmatched ` delimiter",
        )


class CanonicalContractTest(unittest.TestCase):
    def test_contract_uses_current_source_inventory_when_global_compaction_lags(self):
        verifier = load_verifier("personal_artifact_lagging_global")
        with tempfile.TemporaryDirectory() as td:
            repository = Path(td) / "repository"
            for directory in ("wiki", "wiki-assets", ".generated"):
                shutil.copytree(ROOT / directory, repository / directory)
            synthesis = repository / "wiki/_generated/synthesis"
            manifest_path = synthesis / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            canonical_count = manifest["corpus"]["source_count"]
            lagging_count = canonical_count - 1
            current = synthesis / "current.md"
            current_text = current.read_text(encoding="utf-8")
            current_text = current_text.replace(
                f"episode_count: {canonical_count}\n",
                f"episode_count: {lagging_count}\n",
                1,
            ).replace(
                f"source_count: {canonical_count}\n",
                f"source_count: {lagging_count}\n",
                1,
            )
            current.write_text(current_text, encoding="utf-8")
            manifest["global"]["corpus"] = {
                "episode_count": lagging_count,
                "source_count": lagging_count,
            }
            manifest["global"]["output_digest"] = hashlib.sha256(
                current.read_bytes()
            ).hexdigest()
            manifest_path.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

            contract = verifier._load_contract(repository)

            self.assertEqual(canonical_count, contract.synthesis["source_count"])


class PagesArtifactContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        subprocess.run(["./build.sh"], cwd=ROOT, check=True)
        cls.schema_temporary = tempfile.TemporaryDirectory()
        (
            cls.schema_root,
            cls.schema_public,
            cls.source_key,
            cls.source_title,
            cls.concept_key,
            cls.entity_key,
        ) = build_schema_fixture(ROOT, Path(cls.schema_temporary.name) / "repository")

    @classmethod
    def tearDownClass(cls):
        cls.schema_temporary.cleanup()

    def test_built_artifact_has_required_routes_and_dom_signals(self):
        verifier = load_verifier("personal_artifact")
        report = verifier.verify_site(PUBLIC, ROOT)
        expected_routes = expected_html_routes(ROOT)
        actual_routes = set()
        for path in PUBLIC.rglob("index.html"):
            parent = path.relative_to(PUBLIC).parent
            actual_routes.add("/" if parent == Path(".") else f"/{parent.as_posix()}/")
        self.assertEqual(actual_routes, expected_routes)
        self.assertEqual(report.html_pages, len(expected_routes))
        self.assertEqual(report.wiki_pages, sum(route.startswith("/wiki/") for route in expected_routes))
        self.assertEqual(report.local_images, len(image_records(ROOT)))

    def test_visible_prose_normalizes_hugo_smart_quotes_only(self):
        verifier = load_verifier("personal_artifact_smart_quotes")
        self.assertEqual(
            verifier._normalize_visible_prose("the source\u2019s \u201cclaim\u201d"),
            verifier._normalize_visible_prose("the source's \"claim\""),
        )
        self.assertNotEqual(
            verifier._normalize_visible_prose("the source omits a claim"),
            verifier._normalize_visible_prose("the source includes a claim"),
        )

    def test_hidden_canonical_pages_and_projection_namespace_are_absent(self):
        for route in (
            "wiki/index/index.html",
            "wiki/log/index.html",
            "wiki/overview/index.html",
            "wiki/_generated/index.html",
            "wiki-projections/index.html",
        ):
            self.assertFalse((PUBLIC / route).exists(), route)

    def test_open_questions_inline_code_is_verified_as_rendered_text(self):
        verifier = load_verifier("personal_artifact_open_question_inline_code")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            page = copied / "wiki/open-questions/index.html"
            text = page.read_text(encoding="utf-8")
            changed, count = re.subn(
                r"<li>How should developers back up or export WSL distributions before "
                r"destructive cleanup steps such as <code>wsl --unregister</code>\?</li>",
                "",
                text,
                count=1,
            )
            self.assertEqual(count, 1)
            page.write_text(changed, encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Open Questions projection omitted"):
                verifier.verify_site(copied, ROOT)

    def test_wrong_html_and_generated_projection_cannot_fool_independent_oracle(self):
        verifier = load_verifier("personal_artifact_independent")
        with tempfile.TemporaryDirectory() as td:
            fixture = Path(td)
            copied = fixture / "public"
            shutil.copytree(self.schema_public, copied)
            repository = fixture / "repository"
            for directory in ("wiki", "wiki-assets", ".generated"):
                shutil.copytree(self.schema_root / directory, repository / directory)
            generated = repository / ".generated/data/wiki_knowledge_signals.json"
            signals = json.loads(generated.read_text(encoding="utf-8"))
            count = signals["pages"][self.concept_key]["source_note_count"]
            signals["pages"][self.concept_key]["source_note_count"] = count + 1
            generated.write_text(json.dumps(signals, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            page = copied / f"wiki/concepts/{self.concept_key.casefold()}/index.html"
            page.write_text(
                page.read_text(encoding="utf-8").replace(
                    f"data-source-count={count}", f"data-source-count={count + 1}", 1
                ),
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "source-derived knowledge signal mismatch"):
                verifier.verify_site(copied, repository)

    def test_public_image_bytes_are_checked_against_canonical_sidecar(self):
        verifier = load_verifier("personal_artifact_image")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(self.schema_public, copied)
            source_key, filename, _alt = image_records(self.schema_root)[0]
            image = copied / "wiki/sources" / source_key / filename
            image.write_bytes(image.read_bytes() + b"tampered")
            with self.assertRaisesRegex(ValueError, "image bytes differ"):
                verifier.verify_site(copied, self.schema_root)

    def test_broken_internal_link_is_detected(self):
        verifier = load_verifier("personal_artifact_broken")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(self.schema_public, copied)
            page = copied / f"wiki/concepts/{self.concept_key.casefold()}/index.html"
            expected = f"wiki/entities/{self.entity_key.casefold()}/"
            changed = page.read_text().replace(expected, "wiki/entities/missing/", 1)
            self.assertNotEqual(changed, page.read_text())
            page.write_text(changed)
            with self.assertRaisesRegex(ValueError, "unresolved internal URL"):
                verifier.verify_site(copied, self.schema_root)

    def test_unresolved_wikilink_in_non_html_public_text_is_rejected(self):
        verifier = load_verifier("personal_artifact_text_wikilink")
        with tempfile.TemporaryDirectory() as td:
            copied = Path(td) / "public"
            shutil.copytree(PUBLIC, copied)
            (copied / "index.xml").unlink(missing_ok=True)
            (copied / "leaked-feed.xml").write_text(
                "<rss><description>See [[InjectedWikiTarget]]</description></rss>\n",
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
                "<rss><description>See &#91;&#91;InjectedWikiTarget&#93;&#93;</description></rss>\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "unresolved canonical syntax"):
                verifier.verify_site(copied, ROOT)

    def test_synthesis_pages_require_the_exact_complete_ordered_h2_schema(self):
        verifier = load_verifier("personal_artifact_exact_h2_schema")
        concept = f"wiki/concepts/{self.concept_key.casefold()}/index.html"
        entity = f"wiki/entities/{self.entity_key.casefold()}/index.html"
        cases = (
            ("concept-wrong-heading", concept, "<h2 id=definition>Definition</h2>", "<h2 id=wrong>Wrong</h2>"),
            ("concept-extra-heading", concept, "<h2 id=current-synthesis>Current Synthesis</h2>", "<h2 id=unexpected>Unexpected</h2><h2 id=current-synthesis>Current Synthesis</h2>"),
            ("concept-misordered-headings", concept, "<h2 id=definition>Definition</h2>", "<h2 id=current-synthesis>Current Synthesis</h2>"),
            ("entity-wrong-heading", entity, "<h2 id=overview>Overview</h2>", "<h2 id=wrong>Wrong</h2>"),
            ("entity-extra-heading", entity, "<h2 id=current-profile>Current Profile</h2>", "<h2 id=unexpected>Unexpected</h2><h2 id=current-profile>Current Profile</h2>"),
            ("entity-misordered-headings", entity, "<h2 id=overview>Overview</h2>", "<h2 id=current-profile>Current Profile</h2>"),
        )
        for name, relative, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(self.schema_public, copied)
                page = copied / relative
                text = page.read_text(encoding="utf-8")
                if "misordered" in name:
                    self.assertIn(old, text)
                    self.assertIn(new, text)
                    text = text.replace(old, "__H2_SWAP__", 1).replace(new, old, 1).replace("__H2_SWAP__", new, 1)
                else:
                    text = text.replace(old, new, 1)
                self.assertNotEqual(text, page.read_text(encoding="utf-8"))
                page.write_text(text, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "exact ordered H2 schema"):
                    verifier.verify_site(copied, self.schema_root)

    def test_relationship_anchors_match_exact_canonical_targets_and_titles(self):
        verifier = load_verifier("personal_artifact_exact_relationships")
        concept = f"wiki/concepts/{self.concept_key.casefold()}/index.html"
        entity = f"wiki/entities/{self.entity_key.casefold()}/index.html"
        concept_route = f"/wiki/concepts/{self.concept_key.casefold()}/"
        entity_route = f"/wiki/entities/{self.entity_key.casefold()}/"
        source_route = f"/wiki/sources/{self.source_key}/"
        cases = (
            ("concept-existing-source-route", concept, entity_route, source_route),
            ("concept-unrelated-existing-route", concept, entity_route, concept_route),
            ("concept-wrong-label", concept, ">Consumer Contract Entity</a>", ">Wrong relationship label</a>"),
            ("entity-existing-source-route", entity, concept_route, source_route),
            ("entity-wrong-label", entity, ">Consumer Contract Concept</a>", ">Wrong relationship label</a>"),
        )
        for name, relative, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(self.schema_public, copied)
                page = copied / relative
                text = page.read_text(encoding="utf-8")
                relationship_id = "related-concepts" if "/concepts/" in relative else "relationships"
                prefix, relationship = text.split(f"<h2 id={relationship_id}>", 1)
                changed = relationship.replace(old, new, 1)
                self.assertNotEqual(changed, relationship)
                page.write_text(prefix + f"<h2 id={relationship_id}>" + changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "relationship anchor mismatch"):
                    verifier.verify_site(copied, self.schema_root)

    def test_sources_inventory_matches_exact_canonical_key_route_and_title(self):
        verifier = load_verifier("personal_artifact_exact_sources_inventory")
        cases = (
            ("wrong-key", f"data-source-key={self.source_key}", "data-source-key=wrong-source-key"),
            ("wrong-existing-route", f"/wiki/sources/{self.source_key}/", f"/wiki/concepts/{self.concept_key.casefold()}/"),
            ("reviewer-wrong-title", f">{self.source_title}</a>", ">Wrong source title</a>"),
        )
        for name, old, new in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                copied = Path(td) / "public"
                shutil.copytree(self.schema_public, copied)
                page = copied / f"wiki/concepts/{self.concept_key.casefold()}/index.html"
                text = page.read_text(encoding="utf-8")
                prefix, inventory = text.split("<section class=wiki-knowledge-sources", 1)
                changed = inventory.replace(old, new, 1)
                self.assertNotEqual(changed, inventory)
                page.write_text(prefix + "<section class=wiki-knowledge-sources" + changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "source inventory link/title mismatch"):
                    verifier.verify_site(copied, self.schema_root)

    def test_every_verifier_json_input_rejects_duplicate_keys_at_any_depth(self):
        verifier = load_verifier("personal_artifact_strict_duplicate_json")
        topic_id = synthesis_topic_ids(self.schema_root)[0]
        image_source = image_records(self.schema_root)[0][0]
        cases = (
            ("reviewer-synthesis-manifest-top-level", "wiki/_generated/synthesis/manifest.json", False),
            ("synthesis-manifest-nested", "wiki/_generated/synthesis/manifest.json", True),
            ("paragraph-ledger", "wiki/_generated/synthesis/paragraph-ledger.json", False),
            ("claims-nested", f"wiki/_generated/synthesis/claims/{topic_id}.json", True),
            ("image-sidecar-nested", f"wiki-assets/{image_source}/manifest.json", True),
            ("generated-wiki-links", ".generated/data/wiki_links.json", True),
            ("generated-knowledge-signals-nested", ".generated/data/wiki_knowledge_signals.json", True),
            ("generated-prepare-manifest", ".generated/data/prepare-wiki-manifest.json", False),
        )
        for name, relative, nested in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                repository = Path(td) / "repository"
                for directory in ("wiki", "wiki-assets", ".generated"):
                    shutil.copytree(self.schema_root / directory, repository / directory)
                path = repository / relative
                text = path.read_text(encoding="utf-8")
                path.write_text(duplicate_scalar_key(text, nested=nested), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, r"strict JSON object.*duplicate JSON key"):
                    verifier.verify_site(self.schema_public, repository)

    def test_verifier_json_inputs_reject_constants_malformed_and_nonobject_roots(self):
        verifier = load_verifier("personal_artifact_strict_invalid_json")
        topic_id = synthesis_topic_ids(self.schema_root)[0]
        image_source = image_records(self.schema_root)[0][0]
        cases = (
            ("synthesis-nan", "wiki/_generated/synthesis/manifest.json", "constant", "NaN", False),
            ("paragraph-ledger-nonobject", "wiki/_generated/synthesis/paragraph-ledger.json", "whole", "[]\n", False),
            ("claims-negative-infinity", f"wiki/_generated/synthesis/claims/{topic_id}.json", "constant", "-Infinity", True),
            ("image-sidecar-infinity", f"wiki-assets/{image_source}/manifest.json", "constant", "Infinity", False),
            ("generated-wiki-links-nan", ".generated/data/wiki_links.json", "constant", "NaN", True),
            ("generated-knowledge-signals-malformed", ".generated/data/wiki_knowledge_signals.json", "whole", "{\n", False),
            ("generated-prepare-manifest-nonobject", ".generated/data/prepare-wiki-manifest.json", "whole", '"not an object"\n', False),
        )
        for name, relative, mode, replacement, nested in cases:
            with self.subTest(name=name), tempfile.TemporaryDirectory() as td:
                repository = Path(td) / "repository"
                for directory in ("wiki", "wiki-assets", ".generated"):
                    shutil.copytree(self.schema_root / directory, repository / directory)
                path = repository / relative
                original = path.read_text(encoding="utf-8")
                changed = replacement if mode == "whole" else replace_scalar_with_constant(
                    original, replacement, nested=nested
                )
                self.assertNotEqual(changed, original)
                path.write_text(changed, encoding="utf-8")
                with self.assertRaisesRegex(ValueError, r"strict JSON object"):
                    verifier.verify_site(self.schema_public, repository)

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
                page = copied / f"wiki/concepts/{self.concept_key.casefold()}/index.html"
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
                changed, count = re.subn(
                    r"(class=synthesis-updated>Updated <time datetime=)[0-9]{4}-[0-9]{2}-[0-9]{2}",
                    r"\1not-a-date",
                    text,
                    count=1,
                )
                self.assertEqual(count, 1)
            else:
                changed, count = re.subn(
                    r'"name":"Current Synthesis · [^"]+"',
                    '"name":"Wrong synthesis identity"',
                    text,
                    count=1,
                )
                self.assertEqual(count, 1)
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
                shutil.copytree(self.schema_public, copied)
                mutate(mutation, copied)
                with self.assertRaisesRegex(ValueError, "(?:Evidence|Related Concepts|source inventory|date|JSON-LD name)"):
                    verifier.verify_site(copied, self.schema_root)


if __name__ == "__main__":
    unittest.main()

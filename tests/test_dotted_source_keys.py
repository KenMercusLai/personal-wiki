from __future__ import annotations

import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from tests.test_exact_consumer_contract import ROOT, load_script


class DottedSourceKeyTest(unittest.TestCase):
    def test_dotted_source_keeps_identity_title_route_and_references(self):
        prepare = load_script(ROOT / "scripts/prepare-wiki-content.py", "prepare_dotted_key")
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for section in prepare.PUBLIC_SECTIONS:
                (root / "wiki" / section).mkdir(parents=True)
            source = root / "wiki/sources/2603.20617.md"
            original = '---\ntitle: "The AI Layoff Trap"\ntype: source\n---\n\nPaper summary.\n'
            source.write_text(original, encoding="utf-8")
            concept = root / "wiki/concepts/Automation.md"
            concept.write_text(
                '---\ntitle: "Automation"\ntype: concept\n'
                'knowledge_schema: synthesis-v1\nsources: [2603.20617]\n'
                'last_updated: 2026-10-13\n---\n\nSee [[2603.20617]].\n',
                encoding="utf-8",
            )
            pages = prepare.discover_pages(root)
            warnings = io.StringIO()
            with contextlib.redirect_stderr(warnings):
                links, references = prepare.make_link_data(pages, root)
            self.assertEqual(references, 1)
            self.assertEqual(warnings.getvalue(), "")
            self.assertEqual(links["2603.20617"], {
                "section": "sources", "title": "The AI Layoff Trap",
                "url": "/wiki/sources/2603.20617/",
            })
            signals = prepare._knowledge_signals(pages)
            self.assertEqual(signals["pages"]["Automation"]["sources"], [{
                "key": "2603.20617", "title": "The AI Layoff Trap",
                "url": "/wiki/sources/2603.20617/",
            }])
            self.assertEqual(source.read_text(encoding="utf-8"), original)

    def test_both_independent_gates_accept_internal_dots_only(self):
        for script in ("prepare-wiki-content.py", "verify_pages_output.py"):
            module = load_script(ROOT / "scripts" / script, "dot_gate_" + script.replace("-", "_"))
            for key in ("2603.20617", "paper.v2", "example", "example-key", "Example_key"):
                with self.subTest(script=script, key=key):
                    self.assertIsNotNone(module.KEY_RE.fullmatch(key))
            for key in (".", "..", ".paper", "paper.", "paper..v2", "../paper", "paper/name", "paper\\name", "paper name", "paper%2Fname"):
                with self.subTest(script=script, key=key):
                    self.assertIsNone(module.KEY_RE.fullmatch(key))

    def test_casefolded_dotted_keys_still_collide(self):
        prepare = load_script(ROOT / "scripts/prepare-wiki-content.py", "prepare_dot_collision")
        pages = [
            prepare.WikiPage(key, key, "sources", Path(f"wiki/sources/{key}.md"), {})
            for key in ("Paper.v2", "paper.v2")
        ]
        with self.assertRaisesRegex(ValueError, "case-folded canonical path collision"):
            prepare._validate_identities(pages)

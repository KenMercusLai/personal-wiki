from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"


class ContentContractTest(unittest.TestCase):
    def test_source_bundles_match_their_declared_keys_and_local_assets_exist(self):
        for source_path in sorted((WIKI / "sources").glob("*/index.md")):
            source_key = source_path.parent.name
            text = source_path.read_text(encoding="utf-8")
            self.assertIn(f'source_key: "{source_key}"', text, str(source_path))
            self.assertNotIn("_MD5", text, str(source_path))
            for target in re.findall(r"!\[[^]]*\]\(([^)]+)\)", text):
                if "://" in target:
                    continue
                relative = pathlib.PurePosixPath(target)
                self.assertFalse(relative.is_absolute(), str(source_path))
                self.assertNotIn("..", relative.parts, str(source_path))
                self.assertTrue((source_path.parent / relative).is_file(), target)

    def test_public_wiki_contains_no_raw_obsidian_image_embeds(self):
        for path in WIKI.rglob("*.md"):
            self.assertNotIn("![[", path.read_text(encoding="utf-8"), str(path))

    def test_every_derived_page_cites_each_declared_source(self):
        source_keys = {
            path.parent.name for path in (WIKI / "sources").glob("*/index.md")
        }
        derived = [
            path
            for section in ("concepts", "entities")
            for path in (WIKI / section).glob("*.md")
            if path.name != "_index.md"
        ]
        for path in derived:
            text = path.read_text(encoding="utf-8")
            match = re.search(r"^source_keys:\s*\[(.*?)\]", text, flags=re.MULTILINE)
            if match is None:
                self.fail(str(path))
            declared = re.findall(r'"([^"]+)"', match.group(1))
            self.assertTrue(declared, str(path))
            for source_key in declared:
                self.assertIn(source_key, source_keys, str(path))
                self.assertIn(f"/wiki/sources/{source_key}.md", text, str(path))

    def test_ingest_protocol_accepts_the_exact_parent_selected_source(self):
        protocol = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
        self.assertIn("Read exactly the source file named by the parent prompt", protocol)
        self.assertNotIn("ephemeral input snapshot", protocol)
        self.assertNotIn("## Lint workflow", protocol)
        self.assertNotIn("python3 -m tools.validate_publish", protocol)

    def test_raw_source_directories_are_not_hugo_mounts(self):
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertNotIn("source = 'raw'", config)
        self.assertNotIn("source = 'inbox'", config)


if __name__ == "__main__":
    unittest.main()

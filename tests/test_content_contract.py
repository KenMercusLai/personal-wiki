from __future__ import annotations

import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
SOURCE_KEY = "wei-jie-pun-translation-woman-communication"


class ContentContractTest(unittest.TestCase):
    def test_expected_ingest_pages_exist(self):
        expected = {
            "sources/wei-jie-pun-translation-woman-communication/index.md",
            "concepts/semantic-retrieval-for-pun-translation.md",
            "concepts/functional-equivalence-in-pun-localization.md",
            "concepts/weak-guidance-in-game-localization.md",
            "entities/woman-communication.md",
            "entities/wei-jie.md",
        }
        actual = {
            str(path.relative_to(WIKI))
            for path in WIKI.rglob("*.md")
            if path.name != "_index.md"
        }
        self.assertEqual(actual, expected)

    def test_source_note_preserves_provenance_and_publishes_selected_images(self):
        bundle = WIKI / "sources" / SOURCE_KEY
        text = (bundle / "index.md").read_text(encoding="utf-8")
        self.assertIn("https://zhuanlan.zhihu.com/p/1957143907134603895", text)
        self.assertIn('image_status: "15个原始图片引用已全部读取；精选4张公开嵌入"', text)

        selected = {
            "semantic-search-candidates.png": "程序输出展示语义相近的谐音候选",
            "localized-character-name.png": "《女性交流》中文本地化后的角色姓名示例",
            "weak-guidance-japanese.png": "日文画面标出やりチン与チンゲ的重叠部分",
            "weak-guidance-chinese.jpg": "中文画面标出口鲍与鲍鱼的重叠部分",
        }
        for filename, alt in selected.items():
            self.assertTrue((bundle / filename).is_file(), filename)
            self.assertIn(f"![{alt}]({filename})", text)

        self.assertEqual(text.count("!["), len(selected))
        self.assertNotIn("_MD5", text)

    def test_public_wiki_contains_no_raw_obsidian_image_embeds(self):
        for path in WIKI.rglob("*.md"):
            self.assertNotIn("![[", path.read_text(encoding="utf-8"), str(path))

    def test_every_derived_page_cites_the_registered_source(self):
        for section in ("concepts", "entities"):
            for path in (WIKI / section).glob("*.md"):
                if path.name == "_index.md":
                    continue
                text = path.read_text(encoding="utf-8")
                self.assertIn(SOURCE_KEY, text, str(path))
                self.assertIn("/wiki/sources/wei-jie-pun-translation-woman-communication.md", text, str(path))

    def test_raw_source_directories_are_not_hugo_mounts(self):
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertNotIn("source = 'raw'", config)
        self.assertNotIn("source = 'inbox'", config)


if __name__ == "__main__":
    unittest.main()

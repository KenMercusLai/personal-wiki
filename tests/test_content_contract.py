from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"

SOURCES = {
    "wei-jie-pun-translation-woman-communication": {
        "path": "sources/wei-jie-pun-translation-woman-communication/index.md",
        "url": "https://zhuanlan.zhihu.com/p/1957143907134603895",
        "image_status": 'image_status: "15个原始图片引用已全部读取；精选4张公开嵌入"',
        "selected": {
            "semantic-search-candidates.png": "程序输出展示语义相近的谐音候选",
            "localized-character-name.png": "《女性交流》中文本地化后的角色姓名示例",
            "weak-guidance-japanese.png": "日文画面标出やりチン与チンゲ的重叠部分",
            "weak-guidance-chinese.jpg": "中文画面标出口鲍与鲍鱼的重叠部分",
        },
    },
    "shensiquan-private-data-chatgpt-langchain": {
        "path": "sources/shensiquan-private-data-chatgpt-langchain/index.md",
        "url": "https://mp.weixin.qq.com/s/naiVMuXHAScRb_jSEJN3zg",
        "image_status": 'image_status: "17个原始图片引用已全部读取；精选3张公开嵌入"',
        "selected": {
            "rag-query-flow.png": "带聊天历史与向量检索的问答流程",
            "document-embedding-vectorstore.png": "文档切片、生成嵌入并写入向量库的流程",
            "generative-ai-stack.jpg": "生成式人工智能技术栈中的模型、框架与应用层",
        },
    },
}

EXPECTED_DERIVED = {
    "concepts/semantic-retrieval-for-pun-translation.md",
    "concepts/functional-equivalence-in-pun-localization.md",
    "concepts/weak-guidance-in-game-localization.md",
    "entities/woman-communication.md",
    "entities/wei-jie.md",
    "concepts/retrieval-augmented-generation-pipeline.md",
    "concepts/document-chunking-retrieval-tradeoff.md",
    "entities/langchain.md",
}


class ContentContractTest(unittest.TestCase):
    def test_expected_ingest_pages_exist(self):
        expected = EXPECTED_DERIVED | {source["path"] for source in SOURCES.values()}
        actual = {
            str(path.relative_to(WIKI))
            for path in WIKI.rglob("*.md")
            if path.name != "_index.md"
        }
        self.assertEqual(actual, expected)

    def test_source_notes_preserve_provenance_and_publish_selected_images(self):
        for source_key, contract in SOURCES.items():
            source_path = WIKI / contract["path"]
            text = source_path.read_text(encoding="utf-8")
            self.assertIn(f'source_key: "{source_key}"', text)
            self.assertIn(contract["url"], text)
            self.assertIn(contract["image_status"], text)

            bundle = source_path.parent
            for filename, alt in contract["selected"].items():
                self.assertTrue((bundle / filename).is_file(), filename)
                self.assertIn(f"![{alt}]({filename})", text)

            self.assertEqual(text.count("!["), len(contract["selected"]))
            self.assertNotIn("_MD5", text)

    def test_public_wiki_contains_no_raw_obsidian_image_embeds(self):
        for path in WIKI.rglob("*.md"):
            self.assertNotIn("![[", path.read_text(encoding="utf-8"), str(path))

    def test_every_derived_page_cites_each_declared_source(self):
        for relative in EXPECTED_DERIVED:
            path = WIKI / relative
            text = path.read_text(encoding="utf-8")
            match = re.search(r"^source_keys:\s*\[(.*?)\]", text, flags=re.MULTILINE)
            if match is None:
                self.fail(str(path))
            source_keys = re.findall(r'"([^"]+)"', match.group(1))
            self.assertTrue(source_keys, str(path))
            for source_key in source_keys:
                self.assertIn(source_key, SOURCES, str(path))
                self.assertIn(f'/wiki/sources/{source_key}.md', text, str(path))

    def test_raw_source_directories_are_not_hugo_mounts(self):
        config = (ROOT / "hugo.toml").read_text(encoding="utf-8")
        self.assertNotIn("source = 'raw'", config)
        self.assertNotIn("source = 'inbox'", config)


if __name__ == "__main__":
    unittest.main()

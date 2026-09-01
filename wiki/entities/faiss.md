---
title: "FAISS"
description: "FAISS 是教程中用于保存文本 Embedding 并支持相似度检索的向量数据库组件。"
type: "entity"
updated: "2026-09-01"
source_keys: ["shensiquan-private-data-chatgpt-langchain"]
entity_kind: "software"
---

FAISS 是来源 [深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 中用于保存向量数据的检索组件。教程先把上传的私域文本切分成片段，再通过 OpenAI Embeddings 转成向量，并将结果保存到 FAISS 向量数据库中。

在用户提问时，系统会把问题也转成向量，再到 FAISS 中做相似度检索，找出与问题相关的文本片段。随后，这些片段会和当前问题、历史问答一起作为上下文交给大模型生成答案。

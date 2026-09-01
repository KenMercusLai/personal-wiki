---
title: "检索增强生成"
description: "RAG 通过先检索外部知识、再把相关内容交给大语言模型生成回答，使模型能够利用知识库或私域数据中的证据。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution", "shensiquan-private-data-chatgpt-langchain"]
---

检索增强生成（Retrieval-Augmented Generation, RAG）是一种把检索系统和大语言模型生成能力组合起来的问答架构。来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 将它拆成两个基本问题：如何检索到更有用的知识，以及如何让模型更好地利用这些知识生成回复。

文章中的 RAG 包含离线和在线两条链路。离线阶段会加载文档、切分文本、生成向量并存入向量数据库；在线阶段则接收用户查询，检索相关文档，把检索结果拼成上下文，再由大语言模型根据提示词生成答案。

[深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 从更早的入门实践角度描述了同一类流程：导入私域文本，切分成片段，调用 OpenAI Embeddings 生成向量并写入 FAISS；用户提问时再次向量化问题，通过相似度检索找回片段，再把问题、历史问答和片段一起交给大模型生成回答。

这个概念的价值在于把模型回答锚定到外部知识库，而不是完全依赖模型参数记忆。文章后续讨论的 Native RAG、工具驱动 Agentic RAG 和强化学习驱动 Agentic RAG，都是围绕检索策略和证据利用深度展开的不同实现。

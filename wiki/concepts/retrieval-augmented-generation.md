---
title: "检索增强生成"
description: "RAG 通过先检索外部知识、再把相关内容交给大语言模型生成回答，使模型能够利用知识库或私域数据中的证据。"
type: "concept"
updated: "2026-09-02"
source_keys: ["yuan-chaofa-agentic-rag-evolution", "shensiquan-private-data-chatgpt-langchain", "wei-jie-pun-translation-woman-communication", "roriri-persona-summary"]
---

检索增强生成（Retrieval-Augmented Generation, RAG）是一种把检索系统和大语言模型生成能力组合起来的问答架构。来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 将它拆成两个基本问题：如何检索到更有用的知识，以及如何让模型更好地利用这些知识生成回复。

文章中的 RAG 包含离线和在线两条链路。离线阶段会加载文档、切分文本、生成向量并存入向量数据库；在线阶段则接收用户查询，检索相关文档，把检索结果拼成上下文，再由大语言模型根据提示词生成答案。

[深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 从更早的入门实践角度描述了同一类流程：导入私域文本，切分成片段，调用 OpenAI Embeddings 生成向量并写入 FAISS；用户提问时再次向量化问题，通过相似度检索找回片段，再把问题、历史问答和片段一起交给大模型生成回答。

[魏杰的《女性交流》翻译笔记]({{< relref "/wiki/sources/wei-jie-pun-translation-woman-communication.md" >}}) 展示了 RAG 思路在问答之外的创意生产用法。作者为谐音梗翻译预先收集真实对话、筛出含同音词的候选句、向量化并入库；翻译时再把原句向量化，检索语义相近的目标语言候选，交给译者或大模型改写。

[螺莉莉的人格摘要文章]({{< relref "/wiki/sources/roriri-persona-summary.md" >}}) 从另一个角度强调 RAG 的实用边界：如果使用者在乎的是某个人的资料和历史输出，而不是让模型扮演那个人，一般 RAG 比人格 Cosplay 更直接。来源建议严肃应用至少接入检索资料的 RAG 或 MCP，否则人格外壳会削弱回答的可用性。

这个概念的价值在于把模型回答锚定到外部知识库，而不是完全依赖模型参数记忆。文章后续讨论的 Native RAG、工具驱动 Agentic RAG 和强化学习驱动 Agentic RAG，都是围绕检索策略和证据利用深度展开的不同实现。

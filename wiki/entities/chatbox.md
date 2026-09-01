---
title: "Chatbox"
description: "Chatbox 是文章用来解释工具驱动 Agentic RAG 的开源 LLM Chat 项目，其知识库工具支持搜索、元数据查看和片段读取。"
type: "entity"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
entity_kind: "software"
---

Chatbox 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 用来解释工业级 Agentic RAG 实现的开源 LLM Chat 项目。作者认为它较早把 naive chat 推向 Agentic Chat，并且因为离线聊天场景对时延约束较少，可以更激进地让大语言模型参与检索决策。

文章关注的是 Chatbox 知识库工具设计。`query_knowledge_base` 负责语义搜索，`get_files_meta` 帮助模型查看候选文件元信息，`read_file_chunks` 用于读取具体 chunk，`list_files` 用于线索不足时浏览文件清单。这个工具组合让模型能先粗后细地收集证据，而不是只接受一次 Top-K 拼接结果。

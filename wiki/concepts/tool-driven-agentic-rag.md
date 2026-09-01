---
title: "工具驱动的 Agentic RAG"
description: "工具驱动的 Agentic RAG 通过搜索、查看元数据、读取片段和列出文件等工具，把 RAG 从固定流水线改造成多步取证流程。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
---

工具驱动的 Agentic RAG 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 重点说明的一种实现路径。它通过提示词约束和工具调用，把检索能力暴露给大语言模型，让模型在回答前执行多轮搜索、观察和读取。

文章以 Chatbox 的知识库工具为例，列出四类工具：`query_knowledge_base` 用于语义搜索候选线索，`get_files_meta` 用于查看文件名、大小和 chunk 数量等元信息，`read_file_chunks` 用于精读指定文件片段，`list_files` 用于搜索线索不足时浏览文件清单。

这种流程的策略是先粗后细：先找候选文件或片段，再查看元信息，最后读取少量最相关的 chunk。文章用中文查询和英文术语不匹配的例子说明，模型可以根据第一次低相关命中自动改写为 Function Calling 或 Tool Calling；也可以在命中片段上下文不完整时读取前后 chunk 补全证据。

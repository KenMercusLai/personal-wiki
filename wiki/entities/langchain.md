---
title: "LangChain"
description: "LangChain 是文章示例中用于构建 Native RAG 和工具化 Agentic RAG 的大语言模型应用开发框架。"
type: "entity"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
entity_kind: "software"
---

LangChain 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 示例代码使用的大语言模型应用开发框架。文章在 Native RAG 示例中使用 LangChain 的文档加载、文本切分、向量库和提示词组件，展示离线入库与在线检索生成流程。

文章还把 LangChain 放进 Agentic RAG 示例场景：当用户用中文询问“函数调用”而知识库使用 Function Calling 或 Tool Calling 等英文术语时，Agentic RAG 可以根据首次检索反馈自动改写查询。工具化示例则结合 LangChain 工具定义和 LangGraph 的 ReAct Agent 创建函数，把知识库搜索、元数据查看、片段读取和文件列表变成模型可调用的工具。

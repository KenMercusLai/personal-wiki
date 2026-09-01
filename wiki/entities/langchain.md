---
title: "LangChain"
description: "LangChain 是大语言模型应用开发框架，可封装模型调用、提示词、链、记忆、智能体、文档处理和向量检索等组件。"
type: "entity"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution", "shensiquan-private-data-chatgpt-langchain"]
entity_kind: "software"
---

LangChain 是来源 [深思圈的私域数据 ChatGPT 教程]({{< relref "/wiki/sources/shensiquan-private-data-chatgpt-langchain.md" >}}) 的核心工具。作者把它定义为面向大模型应用的开发框架，能够帮助开发者把大模型同外部数据和 API 连接起来，快速构建私域数据 ChatGPT 这类应用。

在该教程中，LangChain 贯穿文档导入、文本切分、OpenAI Embeddings、FAISS 向量库、PromptTemplate、Chains、Memory 和 Agents 等环节。作者认为它主要解决大模型应用开发中的三类问题：接入外部数据、保留上下文记忆，以及调用外部工具。

LangChain 也是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 示例代码使用的大语言模型应用开发框架。文章在 Native RAG 示例中使用 LangChain 的文档加载、文本切分、向量库和提示词组件，展示离线入库与在线检索生成流程。

文章还把 LangChain 放进 Agentic RAG 示例场景：当用户用中文询问“函数调用”而知识库使用 Function Calling 或 Tool Calling 等英文术语时，Agentic RAG 可以根据首次检索反馈自动改写查询。工具化示例则结合 LangChain 工具定义和 LangGraph 的 ReAct Agent 创建函数，把知识库搜索、元数据查看、片段读取和文件列表变成模型可调用的工具。

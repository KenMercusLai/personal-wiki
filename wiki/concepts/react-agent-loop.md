---
title: "ReAct 智能体循环"
description: "ReAct 智能体循环让模型在推理、调用工具和观察结果之间迭代，是文章中工具化 Agentic RAG 的常见实现方式。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
---

ReAct 智能体循环是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 用来解释工具化 Agentic RAG 的实现模式。文章把它概括为思考、行动、观察的循环：模型先判断下一步需要什么证据，再调用工具，随后根据观察结果继续决策。

在 RAG 场景中，ReAct 循环让模型不必一次性接受 Top-K 拼接结果。它可以先调用搜索工具寻找线索，再查看文件元数据，必要时列出文件，最后读取具体 chunk 并基于这些片段作答。

文章给出的最小示例使用 LangGraph 的 `create_react_agent` 绑定知识库工具，并在系统提示中要求模型先搜索、必要时查看元数据或浏览文件，最终必须读取少量最相关片段并列出引用。

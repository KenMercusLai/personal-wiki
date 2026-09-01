---
title: "Agentic RAG"
description: "Agentic RAG 让大语言模型作为具备自主决策能力的控制器，按需调用检索和阅读工具收集证据后再回答。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
---

Agentic RAG 是把智能体决策能力加入 RAG 流程后的系统形态。来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 强调，它的核心不是更复杂的模型，而是让模型学会做事：先制定策略，再调用工具逐步收集证据，最后基于证据作答并给出引用。

和 Native RAG 的一次性检索生成相比，Agentic RAG 会让大语言模型作为控制器，在任务过程中决定是否改写查询、追加搜索、查看文件元数据、读取关键片段，或在证据不足时换一种路径继续找。文章把这种能力称为 Agentic Search，只要 RAG 流程里存在模型自主决策，就可以归入 Agentic RAG。

Agentic RAG 的收益主要体现在复杂问题上。模型可以把问题拆成多步，先粗略定位候选，再精读少量片段，减少 Top-K 拼接带来的噪声，并让回答更容易追溯到具体证据。

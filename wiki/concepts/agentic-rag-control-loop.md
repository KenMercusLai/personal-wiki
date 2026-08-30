---
title: "Agentic RAG检索控制循环"
description: "让模型根据检索观察选择改写、追加搜索、读取证据或停止，并由预算和权限约束。"
type: "concept"
updated: "2026-08-30"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
featured: true
---

## 控制循环

固定RAG预先确定检索次数和流程；Agentic RAG把检索、元数据查询和片段读取暴露为动作：

1. 根据问题形成检索策略。
2. 调用工具并观察结果。
3. 判断证据是否足够；不足则改写查询、扩展上下文或更换工具。
4. 只基于实际读取的证据回答并引用。

自主决策必须有最大轮数、成本预算、工具权限、超时和停止条件。复杂问题可进入循环，简单问题仍可走固定[RAG流水线]({{< relref "/wiki/concepts/retrieval-augmented-generation-pipeline.md" >}})。取证动作可按[先粗后细]({{< relref "/wiki/concepts/coarse-to-fine-evidence-retrieval.md" >}})组织。

## 来源

- [《RAG进化之路》]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}})

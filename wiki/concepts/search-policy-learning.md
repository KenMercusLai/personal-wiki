---
title: "搜索策略学习"
description: "通过搜索轨迹与奖励优化模型何时搜索、如何改写查询以及何时停止。"
type: "concept"
updated: "2026-08-30"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
featured: false
---

## 学习对象

提示词可以规定固定策略；强化学习则尝试从轨迹中优化动作选择：继续推理、发起搜索、消费结果、再次搜索或输出答案。Search-R1把搜索结果插回推理序列，并依据最终答案奖励训练策略。

## 评价

只奖励最终正确率可能产生投机行为。完整评价还应覆盖：

- 答案正确性与引用支持率；
- 搜索次数、延迟和成本；
- 无效循环与停止质量；
- 对检索噪声和工具失败的鲁棒性；
- 训练分布外问题的泛化。

策略学习是[Agentic RAG控制循环]({{< relref "/wiki/concepts/agentic-rag-control-loop.md" >}})的一种实现路线，并不意味着每个系统都需要训练自己的模型。

## 来源

- [《RAG进化之路》]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}})

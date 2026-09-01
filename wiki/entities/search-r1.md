---
title: "Search-R1"
description: "Search-R1 是文章引用的强化学习搜索框架，用于训练模型在推理过程中自主生成搜索查询并利用检索结果。"
type: "entity"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
entity_kind: "research-project"
---

Search-R1 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 引用的代表性强化学习搜索工作。文章把它描述为复现 DeepSearch 思路的一类框架，用来训练大语言模型在推理过程中自主生成搜索查询并利用实时检索结果。

在文章的介绍中，Search-R1 的特点包括推理与搜索交织、自主决定何时搜索、多轮搜索交互、检索令牌掩码，以及基于最终答案正确性的奖励函数。训练流程从预训练模型初始化开始，生成包含推理和搜索动作的轨迹，再通过 PPO 或 GRPO 等强化学习算法优化策略。

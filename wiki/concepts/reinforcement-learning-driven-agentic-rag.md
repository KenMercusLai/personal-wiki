---
title: "强化学习驱动的 Agentic RAG"
description: "强化学习驱动的 Agentic RAG 让模型通过训练学习搜索策略，在推理过程中自主决定何时搜索、搜索什么以及如何利用结果。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
---

强化学习驱动的 Agentic RAG 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 用来概括 Search-R1 一类方法的概念。它不是依赖人工设计的固定提示词和规则，而是让模型从训练轨迹中学习更好的检索和取证策略。

文章指出，这条路线关注的是让 Agent 学会何时改写查询、何时追加读取、如何在推理中插入搜索，以及如何利用搜索结果继续推理。Search-R1 被介绍为代表性工作：模型在单次推理过程中可以多次生成搜索查询，获得检索结果后继续推理，形成推理、搜索、再推理的交织循环。

这种方式的优势是适应性高，能够处理更复杂的多轮搜索决策；代价是实现复杂度、训练成本和数据依赖更高。文章把它和传统 RAG、提示词驱动的 Agentic RAG 放在同一张比较表中，认为它的决策机制来自学习优化，而不是固定流程或手写规则。

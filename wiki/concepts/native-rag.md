---
title: "Native RAG"
description: "Native RAG 是固定的检索、拼接、生成流水线，通常先离线建库，再在线一次性取回 Top-K 文档生成回答。"
type: "concept"
updated: "2026-09-01"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
---

Native RAG 是来源 [袁超发的 Agentic RAG 文章]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}}) 对传统 RAG 的称呼，也对应文中提到的 Naive 或 Vanilla RAG。它的典型模式是预先通过检索排序把知识放进 Prompt，然后让大语言模型生成回复。

文章把 Native RAG 分成离线入库和在线应用。离线入库负责文档加载、文本切分、向量化和向量数据库持久化；在线应用负责用户查询、相似度检索、上下文拼接、提示词构造和模型回答。

Native RAG 的主要限制来自一次性流水线：系统通常不会让模型根据证据质量调整检索策略，也不会把复杂问题拆成定位文件、读取片段、比对总结等多步动作。面对术语不匹配、多跳问题或检索上下文不完整时，它容易停在首次 Top-K 结果上。

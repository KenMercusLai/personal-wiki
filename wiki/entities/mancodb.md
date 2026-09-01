---
title: "MancoDB"
description: "MancoDB 是魏杰为《女性交流》中文本地化搭建的谐音梗检索工作流，用向量化候选句辅助译者改写台词。"
type: "entity"
updated: "2026-09-01"
source_keys: ["wei-jie-pun-translation-woman-communication"]
entity_kind: "software"
---

MancoDB 是来源 [魏杰的《女性交流》翻译笔记]({{< relref "/wiki/sources/wei-jie-pun-translation-woman-communication.md" >}}) 中作者给自己翻译工作流起的名字。它面向《女性交流》这样谐音梗密集的游戏文本，用机器检索降低译者从零构思目标语言笑点的压力。

它的准备阶段包括整理敏感词表、收集大量真实对话文本、用拼音匹配筛出含同音词的候选句，并把候选句向量化后存入向量数据库。翻译阶段再将待翻译原句向量化，检索语义接近的候选句，供译者或大模型改写。

MancoDB 的角色更接近辅助检索系统，而不是自动翻译器。文章强调，机器负责扩大候选空间和提供语义近邻，最终仍要由人判断译文是否同时满足大意、谐音、角色语气和玩法需求。

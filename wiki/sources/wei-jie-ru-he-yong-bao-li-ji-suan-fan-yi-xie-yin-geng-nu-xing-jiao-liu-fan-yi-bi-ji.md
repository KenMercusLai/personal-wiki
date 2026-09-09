---
title: "如何用暴力计算翻译谐音梗——《女性交流》翻译笔记"
type: source
tags: [translation, wordplay, game-localization, semantic-search]
date: 2026-02-05
source_file: "Articles/魏杰 - 如何用暴力计算翻译谐音梗——《女性交流》翻译笔记.md"
---

## Summary

魏杰复盘《女性交流》的中文本地化：先从真实对话中筛出含目标同音词的句子并向量化，再以语义搜索为译者或大模型提供候选，从而把大规模谐音梗翻译从纯灵感劳动改造成机器辅助检索。文章还说明了如何归化双关人名，以及如何协调台词、教程、注意力负荷和字形位置，在中文中重建原版引导玩家发现隐藏机制的体验。

## Key Claims

- [[MachineAssistedPunTranslation]] 可以把敏感词表、拼音匹配、真实语料、向量数据库和人工判断串成候选生成流程，在尽量保持语义或主题的同时提高数百个谐音梗的处理效率。
- 语义相似候选只是搜索空间的压缩；最终译文仍依赖人类对语境、自然度、双关效果和文化接受度的反复判断。
- [[GameLocalizationDomestication]] 可通过改写姓名及故事舞台，让目标语言玩家获得与原语言玩家相近的双关体验，但会产生设定连续性和违和感方面的代价。
- [[WeakPlayerGuidance]] 可以通过预先曝光词汇、奖励点击首字、制造注意力负荷和安排重叠词位置，引导玩家在没有显式教程时发现“一箭双雕”机制。
- 中文重建的弱引导并非完全等价：单字重叠更难准确点击，“口鲍”的视觉显著性也可能让玩家提前识破设计。

## Key Quotes

> “用电脑的计算代替人脑的冥思苦想，大幅降低译者掉头发数量。”

> “当然，机器只是辅助，游戏中许多谐音梗的处理离不开人的反复斟酌。”

> “读者看到译文和原文时的内心活动应该是接近的，就像两个相似的高维向量。”

## Connections

- [[MachineAssistedPunTranslation]] — 文章提出的语料筛选、向量检索与人工定稿工作流。
- [[RetrievalAugmentedGeneration]] — 两者都先检索语义相关材料再交给人或模型，但本文目标是创造性翻译候选而非知识问答。
- [[GameLocalizationDomestication]] — 通过归化人名和舞台保存双关的功能与玩家体验。
- [[WeakPlayerGuidance]] — 通过文本重复、奖励规则和注意力调度暗示隐藏机制。
- [[MancoDB]] — 作者为机器辅助谐音梗检索系统所用名称。
- [[WomanCommunication]] — 该方法被用于本游戏的中文关卡文本与角色名本地化。
- [[WeiJie]] — 本文作者及中文本地化负责人。

## Contradictions

- No direct contradiction with the current wiki. The article qualifies its own success claim by noting that the Chinese weak-guidance sequence is less reliable than the Japanese original.

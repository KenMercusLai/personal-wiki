---
title: "「人格蒸馏」是一种愚蠢的谎言"
description: "螺莉莉批评所谓人格蒸馏只是人格摘要或角色卡写作，认为它无法复原人的数据生成过程，并进一步讨论个人实验、RAG 替代方案与 AI 内容 Farming 的流量异化。"
type: "source"
updated: "2026-09-02"
source_key: "roriri-persona-summary"
image_status: "not_selected"
source_date: "2026-04-13"
source_url: "https://roriri.one/notes/persona-summary"
---

## 摘要

这篇文章批评近期流行的所谓“人格蒸馏”。作者认为，这类做法在技术上并不是大语言模型蒸馏，而是把某个人的公开表达、惯用词、生活规律和风格特征整理成提示词或 Skill；更准确的名字是人格摘要、角色卡撰写或肖像摘要。

作者用数据生成过程解释为什么这种拟合无法“复活”一个人。人的输出来自过去经历的总和，也来自当下身体和环境中的实时刺激；大语言模型只能拟合人在某些时刻留下的输出，无法重建这些经历、身体状态和外界刺激构成的生成过程。即使未来能模拟大脑，也仍要面对外部环境是否被精确模拟的问题。

文章还记录了作者自己的实验：她把博客、社交媒体、频道内容和近十年的群聊记录都喂给模型，试图从外部视角与一个“我”的模型对话。结果模型可以模仿文本长度、emoji 和部分词汇，却漏掉许多作者认为关键的细节特质；当人格摘要变得很长时，上下文窗口和模型处理粗糙的问题也会放大。

作者因此建议，如果目标是做有用的资料问答，与其让模型费心做人格 Cosplay，不如接入 RAG 或 MCP 检索资料。人格摘要可以作为玩具，但不能把一个真实的人造出来。

文章最后把人格卡热潮连接到 AI 内容 Farming。作者批评一些人用很少材料批量制作知名人物提示词，或用 AI 生成音乐、视频 App 和广告流量套利，把低质内容推给算法和读者。她认为金钱与流量会异化创作者，使他们把算法污染和广告点击欺诈包装成努力和用户需求。

## 关键观点

- “人格蒸馏”如果只是整理人物表达特征，本质上是摘要和角色卡写作，不是模型蒸馏。
- 角色卡只能让模型按剧本表演一个人，不能重建一个人由生命经历和实时刺激构成的数据生成过程。
- 大量个人资料可以改善表面拟合，但上下文窗口、信息提取缺口和模型处理粗糙会让复杂人格摘要失真。
- 如果需求是查询资料，RAG 比人格 Cosplay 更直接；人格外壳不应替代证据检索。
- 低质人格卡、AI 音乐和广告化视频应用都可能成为内容 Farming，通过欺骗推荐算法获得不相称的流量和收益。
- 把流量诈骗解释成努力、技术方案或满足用户需求，会掩盖它对用户体验和内容生态的伤害。

## 相关知识

- [人格摘要不是模型蒸馏]({{< relref "/wiki/concepts/persona-summary-not-model-distillation.md" >}})
- [人格模拟的数据生成过程限制]({{< relref "/wiki/concepts/data-generation-process-limits-persona-simulation.md" >}})
- [检索增强生成]({{< relref "/wiki/concepts/retrieval-augmented-generation.md" >}})
- [AI 创作中的材料与品味]({{< relref "/wiki/concepts/materials-and-taste-in-ai-creation.md" >}})
- [AI 内容 Farming 的算法污染]({{< relref "/wiki/concepts/ai-content-farming-algorithmic-pollution.md" >}})

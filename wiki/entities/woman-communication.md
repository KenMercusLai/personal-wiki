---
title: "《女性交流》"
description: "以识别日常对话中的敏感词为核心机制的日本独立游戏，也是机器辅助谐音梗本地化的案例。"
type: "entity"
entity_kind: "game"
updated: "2026-08-29"
source_keys: ["wei-jie-pun-translation-woman-communication"]
featured: true
---

## 概览

《女性交流》（日文标题《ウーマンコミュニケーション》）是一款日本独立游戏。玩家扮演学校风纪委员，在角色的日常对话中找出无意出现的敏感词。

根据译者[魏杰]({{< relref "/wiki/entities/wei-jie.md" >}})的复盘，游戏包含数百个依赖日语语音和文字结构的谐音梗。中文版需要重写大量对话、角色姓名和机制提示，不能仅进行逐字翻译。

## 中文本地化特点

- 使用[语义检索和同音匹配]({{< relref "/wiki/concepts/semantic-retrieval-for-pun-translation.md" >}})生成候选表达。
- 角色姓名采用较彻底的归化策略，以同时维持姓名自然度和谐音效果。
- 为“一箭双雕”等机制重新设计中文重叠词和前文铺垫。
- 以玩家能否获得接近的笑点和操作体验作为[功能对等]({{< relref "/wiki/concepts/functional-equivalence-in-pun-localization.md" >}})目标。

## 来源边界

本页只根据译者文章整理，尚未独立核验游戏版本、商店信息或玩家反馈。

## 来源

- [《如何用暴力计算翻译谐音梗——〈女性交流〉翻译笔记》]({{< relref "/wiki/sources/wei-jie-pun-translation-woman-communication.md" >}})

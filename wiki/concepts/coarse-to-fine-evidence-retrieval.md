---
title: "先粗后细的证据检索"
description: "先定位候选文件与片段，再按需读取邻近上下文，以减少噪音并保持可追溯证据。"
type: "concept"
updated: "2026-08-30"
source_keys: ["yuan-chaofa-agentic-rag-evolution"]
featured: false
---

## 两阶段取证

- **粗定位：** 搜索候选文件或片段，查看标题、来源、大小和chunk范围。
- **细读取：** 选择少量高价值候选，读取命中片段及必要的前后文，再组织答案。

这种方式缓解单次Top-K把不完整片段直接塞入上下文的问题，也与[切片—检索权衡]({{< relref "/wiki/concepts/document-chunking-retrieval-tradeoff.md" >}})相关：小chunk有利于定位，却更可能需要相邻上下文。

系统应记录哪些文件和片段被实际读取，避免把搜索摘要或文件名当作证据。扩大上下文也要受预算、权限和敏感信息边界限制。

## 来源

- [《RAG进化之路》]({{< relref "/wiki/sources/yuan-chaofa-agentic-rag-evolution.md" >}})

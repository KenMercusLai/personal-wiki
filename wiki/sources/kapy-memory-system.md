---
title: "第一记忆模式和第二记忆模式：Kapy 的记忆系统设计"
type: source
tags: [ai, agents, memory, context-management]
date: 2026-02-27
source_file: /mnt/ken_personal_wiki/Articles/kapy-memory-system.md
---

## Summary
[[YanLi]] presents [[Kapy]] as a general agent whose unified memory keeps the original per-turn work log as the source of truth and adds a compact node for routine context. Memory records form a causally linked DAG whose parent references are declared by the agent after it uses earlier records. Retrieval then combines a mandatory broad first pass with autonomous targeted inspection, a pattern formalized here as [[MemoryRetrievalModes]].

## Key Claims
- A memory record should correspond to one agent-human turn, where a turn includes the input, tool-call loop, and output rather than only an input-output pair.
- Raw tool activity is a work log rather than the interaction memory itself; compacting each turn's tool-call loop produces a smaller context node without replacing the original record.
- Unified storage avoids making threads the primary memory partition, while parent links among records represent temporal and causal dependence as a DAG.
- An agent can declare which earlier memory IDs it referenced, allowing the system to materialize causal links after task completion.
- The first memory mode is a mandatory or semi-mandatory high-level recall call with few parameters; Kapy retrieves recent records by thread and user plus keyword-matched records.
- The second memory mode is agent-directed, low-level investigation of specific records and raw logs through filesystem tools such as `rg` and `sed`.
- Keyword search is an adequate prototype but semantic and full-text retrieval could broaden autonomous recall.

## Key Quotes
> "tool call loop 不是记忆，而是工作日志。" — the source separates execution detail from interaction memory.

> "一个 memory record 对应一个 turn" — the record boundary chosen for Kapy.

> "两种记忆模式的并存" — the design principle joining broad injection with targeted search.

## Connections
- [[YanLi]] - author and builder describing the design after more than ten days of use.
- [[Kapy]] - general agent whose memory system is the source's implementation example.
- [[AgentMemory]] - broader persistence, recall, provenance, and maintenance capability refined by the design.
- [[MemoryRetrievalModes]] - distinction between mandatory broad recall and autonomous targeted investigation.
- [[MemoryCompaction]] - each turn's tool-call loop becomes a compact node while the raw log remains available.
- [[AgentFilesystem]] - stores records and exposes raw logs to ordinary search and inspection tools.
- [[Bub]] - cited as an agent that had already demonstrated a unified-memory direction.
- [[NowledgeMem]] - cited as valuable methodological work on memory.

## Contradictions
- The turn remains Kapy's memory-record and compaction boundary, while [[ru-he-she-ji-agent-zu-cheng-yun-xing-huan-jing-yu-sheng-ming-zhou-qi-yanli-yan-li]] argues that steering and asynchronous commands make turn-only lifecycle modeling incomplete. The two uses can coexist, but Kapy does not explain how a turn closes when work outlives its initiating exchange.
- Thread is rejected as the storage partition but retained as one recent-recall filter. This is a useful distinction rather than a logical contradiction, although cross-thread causality and thread identity still need explicit evaluation.
- The DAG, semantic search, and full-text search are stated directions rather than evaluated parts of the described prototype. The reported success is a first-person observation without retrieval, compaction-fidelity, latency, cost, conflict, privacy, or failure measurements.

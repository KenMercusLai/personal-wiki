---
title: "Memory Evolution"
type: concept
tags: [ai, agents, memory, temporal-data]
sources:
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryEvolution]] is the maintenance of memory as time-varying state whose facts can become current, superseded, historical, or temporarily valid.

## Current Synthesis
Appending a new vector beside an old one does not express that reality changed. Evolving memory needs explicit update or version semantics plus temporal metadata so retrieval can answer both “what is true now?” and “what was true then?” The source also distinguishes durable semantic preferences from short-lived episodes, implying that retention, retrieval, and expiry policies should vary by memory type.

## Key Claims
- Changed facts should update or version existing state instead of merely adding an unqualified record.
- Timestamps and validity windows are needed to distinguish current facts from historical facts.
- Confidence is part of state because a later weak inference should not automatically replace an earlier explicit statement.
- Episodic and semantic memories have different expected lifetimes and retrieval uses.
- Append-only evidence can coexist with a derived current-state view if corrections remain traceable.

## Evidence
- State transition: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] treats a move from New York to Seattle as supersession rather than two timeless residence facts.
- Explicit update: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] uses a switch from Python to Rust to distinguish updating from adding.
- Temporal model: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] proposes timestamps, confidence, and validity windows.
- Memory classes: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] contrasts a stable food preference with temporary travel in Tokyo.

## Counterevidence & Qualifications
The source does not specify how to infer validity windows, separate a durable change from a temporary exception, or handle recurring and uncertain states. Its cognitive-science analogy between episodic and semantic memory is architectural inspiration rather than evidence that an AI system should reproduce human memory categories exactly.

## What Changed
- Established temporal state and validity as part of memory representation.
- Separated current-state answers from historically valid versions.

## Related Concepts
- [[AgentMemory]] - evolving state is required for durable memory to remain useful.
- [[MemoryCompaction]] - consolidation produces state that later evidence may supersede.
- [[MemoryConflictResolution]] - temporal change is one explanation for apparently conflicting records.
- [[TapeAndAnchors]] - append-only history can preserve prior versions while views expose current state.
- [[LLMContextManagement]] - retrieval should select the temporally appropriate state for the active context.

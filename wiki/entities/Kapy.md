---
title: "Kapy"
type: entity
tags: [ai, agents, memory]
sources:
  - kapy-memory-system
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[Kapy]], short for Kapybara, is [[YanLi]]'s general agent and the implementation example for a unified, file-backed memory system built around per-turn records, compact views, causal links, and two recall modes.

## Current Profile
Kapy stores one memory record per turn, treating a turn as input, tool-call loop, and output. Each record keeps the original work log as authoritative evidence and a compact node for routine use. Records can name parent memories, forming a DAG whose edges express temporal or causal dependence rather than forcing all state into thread-local chains.

At the start of every turn, Kapy must call a high-level recall script. That script retrieves recent records by thread and user and accepts keywords for older material. After this broad orientation, the agent can inspect particular records and raw logs directly through filesystem tools, then report the memory IDs it actually referenced so causal links can be persisted.

## Key Characteristics
- Uses unified storage rather than separate thread-owned memory stores.
- Treats one full tool-using turn as the memory-record boundary.
- Preserves raw work logs beneath compact per-turn nodes.
- Represents causal continuity through agent-declared parent links in a DAG.
- Starts each turn with mandatory or semi-mandatory broad recall.
- Allows low-level, agent-directed search and inspection through filesystem tools.

## Evidence
- Record model: [[kapy-memory-system]] defines one record per turn containing its original work log and compact node.
- Causal structure: [[kapy-memory-system]] describes parent references among records as a Git-like DAG and asks the agent to return referenced memory IDs.
- Initial recall: [[kapy-memory-system]] requires the recall script as the first tool call and retrieves recent records by thread and user plus keyword matches.
- Targeted recall: [[kapy-memory-system]] lets the agent use `rg`, `sed`, and direct file inspection when compact context is insufficient.

## Qualifications
The profile rests on one first-person devlog after more than ten days of use. It provides no released repository, schema, workload, retrieval-quality measurement, compaction-loss evaluation, latency or token accounting, privacy or authorization model, conflict handling, retention policy, or failure analysis. The causal DAG is not yet used by the first recall mode, and semantic or full-text search remains proposed.

## What Changed
- Created Kapy's profile from its memory-system devlog.
- Recorded the raw-log/compact-node split, causal DAG, and paired recall modes.

## Relationships
- [[YanLi]] - creator and author of Kapy's memory-system account.
- [[AgentMemory]] - Kapy is a concrete file-backed memory implementation.
- [[MemoryRetrievalModes]] - Kapy combines mandatory broad recall with autonomous targeted inspection.
- [[MemoryCompaction]] - Kapy compacts a turn's tool-call loop while retaining the raw log.
- [[AgentFilesystem]] - Kapy stores memory records as files and exposes them to shell search.
- [[Bub]] - cited as prior evidence for unified agent memory.
- [[NowledgeMem]] - cited as related methodological work on memory.

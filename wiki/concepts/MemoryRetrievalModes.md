---
title: "Memory Retrieval Modes"
type: concept
tags: [ai, agents, memory, retrieval, context-management]
sources:
  - kapy-memory-system
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryRetrievalModes]] is a hybrid agent-memory policy that pairs a mandatory, low-parameter orientation pass with optional agent-directed investigation of specific historical evidence.

## Current Synthesis
The first mode protects a fresh turn from beginning with no identity, recent context, or broad task history. Its API is deliberately high level and mostly fixed: Kapy calls it first and receives recent memory records filtered by thread and user plus keyword-selected older records, primarily through compact nodes.

The second mode begins only after the agent knows what it wants. It exposes lower-level access to individual records and raw work logs, allowing ordinary filesystem search and inspection to refine a hypothesis or recover detail omitted by compaction. Together the modes separate recall for orientation from recall for evidence: the former favors coverage and predictable invocation, while the latter favors specificity, flexibility, and provenance.

## Key Claims
- A broad initial recall can supply identity, recent context, and likely relevant history before the agent has enough context to formulate a precise query.
- The initial API should minimize parameters and hard-code stable policy so invocation is reliable from a near-zero-context state.
- Targeted recall should expose flexible low-level access because the agent can state what information it is seeking.
- Compact records are appropriate for orientation, while original logs should remain available for evidence expansion.
- Combining fixed and autonomous recall avoids requiring either full-context injection or perfect one-shot retrieval.
- Recording the IDs actually consulted can connect recall behavior to causal provenance.

## Evidence
- Mandatory orientation: [[kapy-memory-system]] requires Kapy's recall script as the first tool call in every turn.
- Broad retrieval: [[kapy-memory-system]] describes recent-record paths by thread and user plus a keyword-driven path for older memories.
- Evidence expansion: [[kapy-memory-system]] lets the agent inspect raw logs and search files with `rg` or `sed` when compact nodes are insufficient.
- Provenance: [[kapy-memory-system]] asks the agent to return referenced memory IDs so the DAG can record causal parents.

## Counterevidence & Qualifications
The source reports a working prototype rather than a comparative evaluation. Mandatory recall can waste latency and tokens on self-contained turns, and its fixed paths can still miss relevant cross-user or cross-thread evidence. Keyword search depends on vocabulary overlap; semantic and full-text search are proposed but not implemented in the account. The source also does not measure whether the agent reports every consulted memory ID, whether compaction hides decisive details, or how malicious, private, stale, or conflicting records are filtered before injection.

## What Changed
- Created the two-mode distinction between broad fixed recall and targeted autonomous investigation.
- Connected compact orientation, raw-evidence expansion, and referenced-memory provenance in one retrieval policy.

## Related Concepts
- [[AgentMemory]] - retrieval modes determine which durable records enter active reasoning.
- [[LLMContextManagement]] - broad and targeted recall allocate a finite context budget at different stages.
- [[MemoryCompaction]] - compact nodes support orientation while raw logs preserve expandable evidence.
- [[AgentFilesystem]] - low-level file access implements the targeted mode in Kapy.
- [[AgenticRAG]] - the targeted mode lets an agent iteratively search and inspect rather than accept one retrieval result.
- [[RetrievalBudgeting]] - mandatory and optional paths trade coverage against latency, tokens, and search cost.
- [[TapeAndAnchors]] - compact anchors plus expandable history express a similar evidence-versus-view boundary.

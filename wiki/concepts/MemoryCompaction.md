---
title: "Memory Compaction"
type: concept
tags: [ai, agents, memory, knowledge-management]
sources:
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
  - kapy-memory-system
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryCompaction]] is the process of consolidating repeated or low-level interaction records into a smaller structured representation while retaining material distinctions and exceptions.

## Current Synthesis
Compaction is not ordinary summarization. It must decide when records form one durable fact, choose an abstraction level that remains useful, and preserve counterfacts that would make a broader statement false. One design compacts across repeated memories into snapshot-like state; [[Kapy]] instead uses the turn's tool-call loop as the minimum compaction boundary, storing a compact node beside the original work log. The granularities differ, but both require raw evidence to remain available when the compact view is insufficient.

## Key Claims
- Repeated interactions should not remain indefinitely as independent memories when they express the same stable state.
- A compactor must choose among specific, category-level, and overly broad representations according to intended future use.
- Similarity clusters can identify candidates for consolidation but do not prove that their contents can be safely merged.
- Exceptions and negative constraints must survive compression when omitting them would reverse the meaning.
- Periodic and similarity-triggered compaction are scheduling policies, not guarantees of semantic correctness.
- Turn-level compaction can remove execution detail from routine context without treating the underlying work log as disposable.

## Evidence
- Redundancy reduction: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] reduces several sushi-preference statements to one durable preference.
- Abstraction choice: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] asks whether sushi, ramen, and pizza preferences justify food or Japanese-food generalization.
- Exception preservation: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] shows that combining a sushi preference with a shellfish allergy into “likes seafood” is false.
- Trigger policies: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] names fixed-count and embedding-cluster triggers.
- Turn boundary and recoverability: [[kapy-memory-system]] creates one compact node from each turn's tool-call loop while retaining the original log in the same memory record.

## Counterevidence & Qualifications
The sources offer design examples rather than evaluated compaction algorithms. Neither defines a loss function or task-specific fidelity measure. The first omits reversibility, audit, and user-confirmation policy; Kapy retains raw logs but does not measure what compact nodes lose, how later corrections revise them, or whether the chosen turn boundary works for asynchronous jobs. An append-only design such as [[TapeAndAnchors]] may preserve evidence beneath compact views, reducing but not eliminating misleading synthesis.

## What Changed
- Established compaction as semantic consolidation rather than generic summarization.
- Made abstraction level and exception preservation explicit correctness constraints.
- Added per-turn work-log compaction as a recoverable context-management pattern.

## Related Concepts
- [[AgentMemory]] - compaction keeps long-lived memory bounded and usable.
- [[MemoryEvolution]] - compacted state must still change as later evidence arrives.
- [[MemoryConflictResolution]] - apparent duplicates may contain conflicts that must be preserved or reconciled.
- [[Embeddings]] - similarity can nominate compaction candidates but cannot validate a merged claim.
- [[TapeAndAnchors]] - durable raw history can remain available beneath compact summaries.
- [[MemoryRetrievalModes]] - compact views support broad orientation while targeted recall expands the original log.
- [[Kapy]] - uses one compact node plus one raw work log per turn.

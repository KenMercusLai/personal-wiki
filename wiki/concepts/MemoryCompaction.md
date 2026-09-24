---
title: "Memory Compaction"
type: concept
tags: [ai, agents, memory, knowledge-management]
sources:
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryCompaction]] is the process of consolidating repeated or low-level interaction records into a smaller structured representation while retaining material distinctions and exceptions.

## Current Synthesis
Compaction is not ordinary summarization. It must decide when records form one durable fact, choose an abstraction level that remains useful, and preserve counterfacts that would make a broader statement false. The article compares the shape to log compaction - raw interactions become a snapshot-like state - but the semantic judgment is harder because nearby statements can support an unsafe generalization.

## Key Claims
- Repeated interactions should not remain indefinitely as independent memories when they express the same stable state.
- A compactor must choose among specific, category-level, and overly broad representations according to intended future use.
- Similarity clusters can identify candidates for consolidation but do not prove that their contents can be safely merged.
- Exceptions and negative constraints must survive compression when omitting them would reverse the meaning.
- Periodic and similarity-triggered compaction are scheduling policies, not guarantees of semantic correctness.

## Evidence
- Redundancy reduction: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] reduces several sushi-preference statements to one durable preference.
- Abstraction choice: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] asks whether sushi, ramen, and pizza preferences justify food or Japanese-food generalization.
- Exception preservation: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] shows that combining a sushi preference with a shellfish allergy into “likes seafood” is false.
- Trigger policies: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] names fixed-count and embedding-cluster triggers.

## Counterevidence & Qualifications
The source offers design examples rather than an evaluated compaction algorithm. It does not define a loss function, reversibility requirement, audit trail, user-confirmation policy, or task-specific way to choose abstraction level. An append-only design such as [[TapeAndAnchors]] may retain raw evidence beneath compact views, reducing but not eliminating the risk of a misleading synthesis.

## What Changed
- Established compaction as semantic consolidation rather than generic summarization.
- Made abstraction level and exception preservation explicit correctness constraints.

## Related Concepts
- [[AgentMemory]] - compaction keeps long-lived memory bounded and usable.
- [[MemoryEvolution]] - compacted state must still change as later evidence arrives.
- [[MemoryConflictResolution]] - apparent duplicates may contain conflicts that must be preserved or reconciled.
- [[Embeddings]] - similarity can nominate compaction candidates but cannot validate a merged claim.
- [[TapeAndAnchors]] - durable raw history can remain available beneath compact summaries.

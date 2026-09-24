---
title: "Agent Memory"
type: concept
tags: [ai, llm, memory, retrieval]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - mu-jiang-chui-zi-ding-zi
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[AgentMemory]] is an LLM-agent capability that preserves experience outside the active prompt, maintains it as qualified state, and retrieves the appropriate evidence or current view when useful.

## Current Synthesis
The earlier sources place Memory in the same family as RAG: outside information is retrieved into context, and memory adds a write path through which an agent can decide what to preserve. The newest source draws an important boundary around that framing. A vector store plus embedding lookup, even when writeable, is a searchable log; mature memory must also represent what a record means, compress repetition, track change over time, and adjudicate conflicts.

PsiACE's essay adds a qualification: memory is often asked to solve a continuity problem created by assuming state must survive across sessions. In multi-person and multi-topic settings, memory can drift and require high calibration effort. [[TapeAndAnchors]] offers a narrower alternative in which durable history remains available, but only minimal anchors are carried forward by default.

The mihomo-rust case study narrows memory even further for coding work. Its Claude Code memories are feedback rules about agent behavior, such as avoiding `CatchPanic`, remembering limits of `tokio::time::pause()`, and respawning teammates at milestone boundaries. The source warns against storing code conventions, git history, fixed debugging plans, or temporary task state in memory when files or tools are more authoritative.

The newer Tape article presents a stronger architectural alternative to a detached memory subsystem. Immutable entries and anchors already preserve the timeline; [[AgentTopicLifecycle]] adds summaries and indexes over bounded ranges; and recall can insert a compact anchor referencing an earlier topic, then expand the original entries only if needed. Under this view, memory is an emergent ability to navigate durable history, although retrieval quality and summarization remain implementation problems.

These positions can be combined rather than treated as mutually exclusive. An append-only tape preserves evidence; [[MemoryCompaction]] and topic summaries derive smaller views; [[MemoryEvolution]] supplies current and historical state; [[MemoryConflictResolution]] records why one version is preferred; and a retrieval layer selects what enters the finite prompt. Graph, document, relational, and vector stores are implementation components, not the memory semantics themselves.

## Key Claims
- Memory addresses context limits by preserving information outside the active prompt and retrieving it selectively.
- Write access distinguishes agent memory from read-only RAG, but a writeable vector index is still only a persistence and retrieval layer.
- Durable memory requires compaction, temporal evolution, conflict resolution, provenance, and confidence in addition to similarity search.
- Append-only evidence and derived current-state views can coexist, preserving auditability while keeping recall compact.
- Memory should retain behavioral feedback that lacks a more authoritative home, not duplicate code, git history, or temporary task state.
- Broad continuity layers can drift; minimal anchors and bounded topic summaries reduce inherited-state and calibration costs.
- Storage technologies are composable implementation choices rather than substitutes for explicit memory semantics.

## Evidence
- RAG relationship: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Memory is the same class of problem as RAG.
- Write path: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] characterizes Memory as RAG with write capability.
- Composition example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] combines a Skill, Python tool, and NotebookLM-like external knowledge interface in one workflow.
- Continuity critique: [[mu-jiang-chui-zi-ding-zi]] says memory systems try to preserve personality or state across sessions, but drift and calibration costs can exceed expectations.
- Anchor alternative: [[mu-jiang-chui-zi-ding-zi]] proposes anchors as minimal state packets while history remains available on an append-only tape.
- Feedback memory: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] describes seven `feedback` memories used to prevent repeated agent mistakes and preserve milestone-reset procedure.
- Native temporal memory: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] argues that entries and anchors already provide time-travel-like recall without a separate memory service.
- Topic recall: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] retrieves earlier topic summaries into a recall anchor and preserves sequence indexes for selective expansion into raw entries.
- Searchable-log boundary: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] says vector storage and embedding similarity retrieve records but do not maintain knowledge.
- State maintenance: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] identifies compaction, evolution, and conflict resolution as the three missing operations.
- Metadata and versions: [[ai-memory-de-zhen-zheng-nan-dian-wei-shen-me-vector-store-embedding-yuan-yuan-bu-gou]] proposes timestamps, confidence, validity windows, provenance, and multiple time-bounded versions.

## Counterevidence & Qualifications
The sources do not fully discuss memory privacy, deletion, access control, retrieval evaluation, user correction, or how confidence should be calibrated. The newest architecture is conceptual and supplies no comparative benchmark for compaction triggers, conflict policies, or storage combinations. PsiACE's critique is strongest for detached continuity layers; calling Tape history itself “memory” preserves evidence but does not remove the need for indexing, summarization, temporal interpretation, and correction.

## What Changed
- Reclassified writeable retrieval as one layer of memory rather than a sufficient definition.
- Added compaction, temporal evolution, conflict resolution, provenance, confidence, and versioning to the current architecture.
- Reconciled append-only Tape evidence with derived summaries and current-state views.

## Related Concepts
- [[RetrievalAugmentedGeneration]] - agent memory is framed as RAG plus write capability.
- [[LLMContextManagement]] - memory keeps persistent facts out of the prompt until needed.
- [[DynamicContextCompression]] - dynamic compression can evict information into external memory.
- [[SecondBrain]] - personal knowledge systems can become memory-like external stores for agents.
- [[TapeAndAnchors]] - anchors are a lighter continuity mechanism than broad memory inheritance.
- [[AgentTeam]] - feedback memory supports role respawn across milestone boundaries.
- [[AgentTopicLifecycle]] - topic summaries and range indexes organize recall over durable history.
- [[MemoryCompaction]] - consolidates repeated interactions without discarding material exceptions.
- [[MemoryEvolution]] - represents current, superseded, temporary, and historical state.
- [[MemoryConflictResolution]] - adjudicates incompatible memories using time, confidence, provenance, and versions.
- [[VectorDatabase]] - supplies similarity retrieval but not memory semantics by itself.

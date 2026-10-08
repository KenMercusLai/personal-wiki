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
  - ai-infra-quan-jing-tu-agent-framework-diao-du-bian-pai-sha-xiang-ji-yi-guan-li-tracing-fen-ceng-chai-jie
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[AgentMemory]] is an LLM-agent capability that preserves experience outside the active prompt, maintains it as qualified state, and retrieves the appropriate evidence or current view when useful.

## Current Synthesis
The earlier sources place Memory in the same family as RAG: outside information is retrieved into context, and memory adds a write path through which an agent can decide what to preserve. Later sources draw an important boundary around that framing. A vector store plus embedding lookup, even when writeable, is a searchable log; mature memory must also represent what a record means, compress repetition, track change over time, adjudicate conflicts, allocate attention, and expose its judgments to user control.

PsiACE's essay adds a qualification: memory is often asked to solve a continuity problem created by assuming state must survive across sessions. In multi-person and multi-topic settings, memory can drift and require high calibration effort. [[TapeAndAnchors]] offers a narrower alternative in which durable history remains available, but only minimal anchors are carried forward by default.

The mihomo-rust case study narrows memory even further for coding work. Its Claude Code memories are feedback rules about agent behavior, such as avoiding `CatchPanic`, remembering limits of `tokio::time::pause()`, and respawning teammates at milestone boundaries. The source warns against storing code conventions, git history, fixed debugging plans, or temporary task state in memory when files or tools are more authoritative.

The newer Tape article presents a stronger architectural alternative to a detached memory subsystem. Immutable entries and anchors already preserve the timeline; [[AgentTopicLifecycle]] adds summaries and indexes over bounded ranges; and recall can insert a compact anchor referencing an earlier topic, then expand the original entries only if needed. Under this view, memory is an emergent ability to navigate durable history, although retrieval quality and summarization remain implementation problems.

These positions can be combined rather than treated as mutually exclusive. An append-only tape preserves evidence; [[MemoryCompaction]] and topic summaries derive smaller views; [[MemoryEvolution]] supplies current and historical state; [[MemoryConflictResolution]] records why one version is preferred; [[BitemporalMemory]] separates when something happened from when it was learned; [[MemoryForgetting]] controls salience without necessarily deleting evidence; and a retrieval layer selects what enters the finite prompt. Graph, document, relational, and vector stores are implementation components, not the memory semantics themselves.

The [[NowledgeMem]] account supplies one integrated implementation. Raw Traces become typed Units and, after corroboration from at least three sources, Crystals. Most queries use parallel vector, full-text, entity, community, label, and graph signals; harder queries add intent routing, HyDE, and LLM reranking, while source-thread pointers support on-demand expansion. Progression and validation are represented separately, and unresolved challenges remain visible for human adjudication.

Working memory in this implementation is attention prefetch rather than another permanent store: a background agent selects a small daily Markdown briefing from a much larger corpus. Scheduled and event-driven maintenance run behind debounce, rate, token, context, and code-level quality gates. Cross-tool continuity is then a lifecycle concern—inject before work, capture and distill after work—not merely an API endpoint.

Working, short-term, long-term, episodic, and semantic memory are useful retention classes only when paired with expiration, privacy and deletion, write admission, and recall policies. These controls must also preserve tenant and user boundaries; remembering more is not automatically correct or authorized.

## Key Claims
- Memory addresses context limits through progressive disclosure: durable evidence stays outside the prompt while compact views and pointers support selective retrieval and expansion.
- Write access distinguishes agent memory from read-only RAG, but a writeable vector index is still only a persistence and retrieval layer.
- Durable memory requires distillation, compaction, bitemporal state, evolution, conflict resolution, forgetting, provenance, confidence, retention, privacy, deletion, write admission, recall, and authorization in addition to similarity search.
- Append-only evidence and derived current-state views can coexist, preserving auditability while keeping recall compact.
- Memory should retain behavioral feedback that lacks a more authoritative home, not duplicate code, git history, or temporary task state.
- Broad continuity layers can drift; minimal anchors and bounded topic summaries reduce inherited-state and calibration costs.
- Storage technologies are composable implementation choices rather than substitutes for explicit memory and lifecycle semantics.

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
- Operational lifecycle: [[ai-infra-quan-jing-tu-agent-framework-diao-du-bian-pai-sha-xiang-ji-yi-guan-li-tracing-fen-ceng-chai-jie]] classifies working, short-term, long-term, episodic, and semantic memory and requires TTL, privacy, write, and recall policies.
- Progressive knowledge forms: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] moves from raw Trace to typed Unit to a Crystal requiring at least three sources.
- Hybrid retrieval: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] combines parallel fast signals with intent-routed deep search and source-thread expansion.
- Time and evolution: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] separates event from record time and progression from validation relationships.
- Attention and control: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] separates decay from confidence, protects important memories, uses conservative archive gates, and exposes conflicts for user review.
- Cross-tool lifecycle: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] connects agents through working-memory injection, capture, distillation, local formats, export, and graph visibility.

## Counterevidence & Qualifications
The infrastructure-stack source names privacy, deletion, and policy requirements but does not specify enforcement, tenant scoping, user correction, retrieval evaluation, or confidence calibration. The memory architectures supply no comparative benchmark for compaction triggers, conflict policies, recall strategies, temporal weights, decay curves, or storage combinations. PsiACE's critique is strongest for detached continuity layers; calling Tape history itself “memory” preserves evidence but does not remove the need for indexing, summarization, temporal interpretation, correction, retention, and authorization. Nowledge Mem is a first-party product account: its numerical gates, boosts, task budgets, and `confidence = max(new, old)` rule are implementation policies rather than validated general laws, and non-decreasing confidence can misrepresent evidence later shown unreliable.

## What Changed
- Reclassified writeable retrieval as one layer of memory and added compaction, temporal evolution, conflict resolution, provenance, confidence, and versioning.
- Reconciled append-only Tape evidence with derived summaries and current-state views.
- Added retention class, TTL, privacy/deletion, write, recall, and authorization as explicit lifecycle concerns.
- Added Trace-to-Unit-to-Crystal distillation, hybrid retrieval, bitemporal metadata, deliberate forgetting, attention prefetch, and cross-tool lifecycle hooks.
- Made user-visible conflict review and the limits of non-decreasing confidence explicit.

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
- [[AIInfrastructureStack]] - places memory between active context and evaluation/operations while making governance cross-cutting.
- [[BitemporalMemory]] - separates event time from record time and preserves temporal precision.
- [[MemoryForgetting]] - adjusts salience and archival without equating inactivity with falsity.
- [[NowledgeMem]] - supplies an integrated first-party implementation of the lifecycle described here.

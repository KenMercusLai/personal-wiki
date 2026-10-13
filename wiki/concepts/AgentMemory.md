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
  - effective-context-engineering-for-ai-agents-anthropic
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
last_updated: 2026-10-13
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

Anthropic's long-horizon guidance adds a deliberately small operational form: structured notes can preserve objectives, progress, maps, and learned tactics outside the prompt, then be reread after compaction or a context reset. This supports continuity with low active-token overhead, but a `NOTES.md`-style file is a persistence surface rather than a complete memory system; the existing requirements for admission, correction, provenance, retrieval, expiry, privacy, and user control still apply.

The [[DeepChat]] implementation makes the evidence-versus-view split operational: “Tape is the ledger; memory is the brain.” Session Tape records structured messages, tool calls and results, runtime events, and anchors, while memory keeps only minimal durable conclusions that retain pointers to their originating passages. Candidate writes are compared with the ten nearest existing memories and classified as new, updated, replaced, duplicated, or conflicting; unused items decay into soft archival rather than deletion; recall is relevance-ranked under a token budget; and health views expose unvisited, conflicted, or unvectorized records. Per-agent separation and content-free audit events add privacy boundaries, although self-update, insight formation, and some user-facing control remain incomplete.

## Key Claims
- Memory addresses context limits through progressive disclosure: durable evidence stays outside the prompt while compact views and pointers support selective retrieval and expansion.
- Write access distinguishes agent memory from read-only RAG, but a writeable vector index is still only a persistence and retrieval layer.
- Durable memory requires selective admission, distillation, compaction, bitemporal state, evolution, conflict resolution, soft forgetting, provenance, confidence, retention, privacy, deletion, bounded recall, user correction, observability, and authorization in addition to similarity search.
- Append-only evidence and derived current-state views can coexist, preserving auditability while keeping recall compact.
- Memory should retain behavioral feedback that lacks a more authoritative home, not duplicate code, git history, or temporary task state.
- Broad continuity layers can drift; minimal anchors, bounded topic summaries, and structured working notes reduce inherited-state and active-token costs.
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
- Structured notes: [[effective-context-engineering-for-ai-agents-anthropic]] describes file-backed goals, progress, maps, and tactics that can be restored after context resets without keeping the full trajectory active.
- Memory boundary: [[effective-context-engineering-for-ai-agents-anthropic]] demonstrates persistence and recall value, while its simple note pattern leaves write admission, conflict handling, expiry, privacy, and correction unspecified.
- Ledger and cognition split: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] describes Tape as the immutable factual record and Memory as traceable durable conclusions derived from it.
- Admission and conflict: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] limits writes to stable preferences, project facts, task outcomes, and lessons, then compares each candidate with ten similar memories before adding, updating, replacing, deduplicating, or recording conflict.
- Forgetting and recall: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] uses half-life-like decay, soft archival, relevance-ranked recall, and a strict token budget while preserving Tape for later re-expansion.
- Visibility and isolation: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports health snapshots, cited-memory inspection and soft deletion, per-agent memory separation, and body-free audit events.

## Counterevidence & Qualifications
The infrastructure-stack source names privacy, deletion, and policy requirements but does not specify enforcement, tenant scoping, user correction, retrieval evaluation, or confidence calibration. The memory architectures supply no comparative benchmark for compaction triggers, conflict policies, recall strategies, temporal weights, decay curves, or storage combinations. PsiACE's critique is strongest for detached continuity layers; calling Tape history itself “memory” preserves evidence but does not remove the need for indexing, summarization, temporal interpretation, correction, retention, and authorization. Nowledge Mem is a first-party product account: its numerical gates, boosts, task budgets, and `confidence = max(new, old)` rule are implementation policies rather than validated general laws, and non-decreasing confidence can misrepresent evidence later shown unreliable.

Anthropic's note-taking examples show coherence across resets but provide no controlled comparison with compaction or retrieval systems. A note file can also preserve stale, mistaken, sensitive, or overgeneralized state indefinitely unless a surrounding lifecycle governs it.

DeepChat's account is first-party and provides no memory-quality benchmark, false-write or false-recall rate, longitudinal decay evaluation, conflict-adjudication study, privacy audit, or measured token tradeoff. Comparing against ten nearby memories, using a cheaper model for adjudication, and applying half-life-like decay are implementation policies rather than established optimal values. Self-updating memory, higher-order insight, Skill generation, and parts of human conflict resolution remain roadmap items.

## What Changed
- Added a concrete Tape-to-Memory implementation that separates raw evidence from minimal durable conclusions.
- Made candidate admission, near-memory comparison, explicit conflict retention, soft archival, and token-bounded recall part of the current lifecycle judgment.
- Added memory health views, cited-memory deletion, per-agent isolation, and content-free audit events as user-control and privacy surfaces.
- Kept self-update, insight formation, and Skill synthesis as unvalidated roadmap capabilities rather than current system properties.

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
- [[DeepChat]] - supplies a second first-party implementation centered on Tape provenance, write adjudication, soft archival, and bounded recall.

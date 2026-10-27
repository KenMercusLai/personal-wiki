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
  - write-things-down
  - "2607.01224"
  - custom-llm-memory-layer
  - kapy-memory-system
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[AgentMemory]] is an LLM-agent capability that preserves experience outside the active prompt, maintains it as qualified state, and retrieves the appropriate evidence or current view when useful.

## Current Synthesis
The earlier sources place Memory in the same family as RAG: outside information is retrieved into context, and memory adds a write path through which an agent can decide what to preserve. Later sources draw an important boundary around that framing. A vector store plus embedding lookup, even when writeable, is a searchable log; mature memory must also represent what a record means, compress repetition, track change over time, adjudicate conflicts, allocate attention, and expose its judgments to user control.

This boundary also produces an infrastructure split. Search can optimize recall, cost, and programmability while returning a passage with its source and time; memory must still decide whether the passage was exploratory or settled, current or superseded, authorized for this task, and useful enough to enter the active context. Preserving original records and changing views is therefore preferable to overwriting history with one timeless user assertion. For short recent histories, direct reading or PostgreSQL may be simpler than a separate index; for years of sparse history, [[PersonalAgentRetrieval]] can first locate candidate originals and let the agent inspect them selectively.

PsiACE's essay adds a qualification: memory is often asked to solve a continuity problem created by assuming state must survive across sessions. In multi-person and multi-topic settings, memory can drift and require high calibration effort. [[TapeAndAnchors]] offers a narrower alternative in which durable history remains available, but only minimal anchors are carried forward by default.

The mihomo-rust case study narrows memory even further for coding work. Its Claude Code memories are feedback rules about agent behavior, such as avoiding `CatchPanic`, remembering limits of `tokio::time::pause()`, and respawning teammates at milestone boundaries. The source warns against storing code conventions, git history, fixed debugging plans, or temporary task state in memory when files or tools are more authoritative.

The newer Tape article presents a stronger architectural alternative to a detached memory subsystem. Immutable entries and anchors already preserve the timeline; [[AgentTopicLifecycle]] adds summaries and indexes over bounded ranges; and recall can insert a compact anchor referencing an earlier topic, then expand the original entries only if needed. Under this view, memory is an emergent ability to navigate durable history, although retrieval quality and summarization remain implementation problems.

These positions can be combined rather than treated as mutually exclusive. An append-only tape preserves evidence; [[MemoryCompaction]] and topic summaries derive smaller views; [[MemoryEvolution]] supplies current and historical state; [[MemoryConflictResolution]] records why one version is preferred; [[BitemporalMemory]] separates when something happened from when it was learned; [[MemoryForgetting]] controls salience without necessarily deleting evidence; and a retrieval layer selects what enters the finite prompt. Graph, document, relational, and vector stores are implementation components, not the memory semantics themselves.

The [[NowledgeMem]] account supplies one integrated implementation. Raw Traces become typed Units and, after corroboration from at least three sources, Crystals. Most queries use parallel vector, full-text, entity, community, label, and graph signals; harder queries add intent routing, HyDE, and LLM reranking, while source-thread pointers support on-demand expansion. Progression and validation are represented separately, and unresolved challenges remain visible for human adjudication.

Working memory in this implementation is attention prefetch rather than another permanent store: a background agent selects a small daily Markdown briefing from a much larger corpus. Scheduled and event-driven maintenance run behind debounce, rate, token, context, and code-level quality gates. Cross-tool continuity is then a lifecycle concern—inject before work, capture and distill after work—not merely an API endpoint.

Working, short-term, long-term, episodic, and semantic memory are useful retention classes only when paired with expiration, privacy and deletion, write admission, and recall policies. These controls must also preserve tenant and user boundaries; remembering more is not automatically correct or authorized.

Anthropic's long-horizon guidance adds a deliberately small operational form: structured notes can preserve objectives, progress, maps, and learned tactics outside the prompt, then be reread after compaction or a context reset. This supports continuity with low active-token overhead, but a `NOTES.md`-style file is a persistence surface rather than a complete memory system; the existing requirements for admission, correction, provenance, retrieval, expiry, privacy, and user control still apply.

The [[DeepChat]] implementation makes the evidence-versus-view split operational: “Tape is the ledger; memory is the brain.” Session Tape records structured messages, tool calls and results, runtime events, and anchors, while memory keeps only minimal durable conclusions that retain pointers to their originating passages. Candidate writes are compared with the ten nearest existing memories and classified as new, updated, replaced, duplicated, or conflicting; unused items decay into soft archival rather than deletion; recall is relevance-ranked under a token budget; and health views expose unvisited, conflicted, or unvectorized records. Per-agent separation and content-free audit events add privacy boundaries, although self-update, insight formation, and some user-facing control remain incomplete.

A turn-granular design can keep the raw tool-call loop as a work log beneath a compact node. In [[Kapy]], unified record storage avoids making threads the primary memory partition, while agent-declared parent IDs form a causal DAG. New [[MemoryRetrievalModes]] separates a mandatory first-call orientation pass—recent records by thread and user plus keyword matches—from autonomous low-level inspection of specific records and logs through filesystem tools. This makes broad context injection and targeted evidence search complementary, but the described prototype does not yet use its DAG for recall and supplies no retrieval or compaction evaluation.

Thompson adds a conceptual boundary around the simplest file-backed form. Markdown notes that preserve goals, progress, feedback, and pending work can let a fresh model invocation resume a project and can coordinate separate instances through shared artifacts. This is operational memory and a way to simulate continuity around a frozen model, not evidence that model weights learn continuously or that the resulting system has a persistent self, volition, or moral agency.

The [[AutoMem]] study adds a distinct proficiency layer. Its agent exposes file operations as actions beside gameplay actions, allowing complete-trajectory review to improve both the scaffold—prompts, schemas, validation, and action vocabulary—and the model policy that chooses when to write, search, read, or update. Reported game results suggest that memory structure and [[Metamemory|memory-use skill]] can be optimized separately: coordinate-keyed upserts, auto-synchronized state, bounded logs, strategy references, and action checks reduce memory waste, while a LoRA-trained specialist learns to consult existing files before writing. This does not remove the lifecycle and governance requirements above; the experiments reset memory each episode and do not test persistent conflicts, privacy, deletion, or cross-domain transfer.

[[AvishekBiswas]] supplies a compact implementation path inspired by [[Mem0]]. [[DSPy]] extracts atomic user factoids, [[Qdrant]] stores embeddings under an application-supplied `user_id`, and a ReAct response agent decides whether retrieval is needed before a second agent chooses add, update, delete, or no-op. The design usefully makes retrieval and mutation optional rather than automatic. It also demonstrates why implementation is not evaluation: the published extraction output reverses the user's stated tea preference, several snippets contain mismatched identifiers, and no accuracy, isolation, latency, cost, or lifecycle benchmark is supplied.

## Key Claims
- Memory addresses context limits through progressive disclosure; fixed orientation, autonomous evidence search, optional tool use, and learned operation policies can serve different retrieval states.
- Write access distinguishes agent memory from read-only RAG, but a writeable vector index is still only a persistence and retrieval layer.
- Durable memory requires selective admission, distillation, compaction, bitemporal state, evolution, conflict resolution, soft forgetting, provenance, confidence, retention, privacy, deletion, bounded recall, user correction, observability, and authorization in addition to similarity search.
- Append-only evidence and derived current-state views can coexist, preserving auditability while keeping recall compact.
- Memory should retain behavioral feedback that lacks a more authoritative home, not duplicate code, git history, or temporary task state.
- Broad continuity layers can drift; minimal anchors, bounded topic summaries, and structured working notes reduce inherited-state and active-token costs while simulating continuity around otherwise stateless or frozen model calls.
- Storage and search technologies are composable implementation choices; retrieval relevance does not establish present truth, authority, task usefulness, or permission to place a record in context.

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
- Practical continuity: [[write-things-down]] describes Markdown notes and status boards preserving active work, waiting states, feedback, and future tasks across agent sessions.
- Learning boundary: [[write-things-down]] distinguishes file-restored context from continuous learning in the model's weights and rejects persistence alone as proof of AGI or personhood.
- Trainable memory actions: [[2607.01224]] places file reads, searches, writes, appends, creates, and updates in the agent action space so memory decisions are traceable and optimizable.
- Scaffold optimization: [[2607.01224]] reports that coordinate-keyed maps, auto-synced inventory and status, bounded logs, strategy references, and action validation reduce redundant memory and unproductive behavior.
- Proficiency optimization: [[2607.01224]] selects the base agent's own good memory traces for LoRA training of a dedicated specialist while leaving the task-action model frozen.
- Long-horizon results: [[2607.01224]] reports roughly 2–4× progression gains over the initial file-memory agent across Crafter, MiniHack, and NetHack, with fewer writes per search after specialist training.
- Minimal implementation lifecycle: [[custom-llm-memory-layer]] separates atomic extraction, per-user vector storage, optional retrieval, and add/update/delete/no-op maintenance.
- Trusted tenant filter: [[custom-llm-memory-layer]] supplies `user_id` from application state and applies it as an indexed Qdrant payload filter rather than asking the model to invent it.
- Selective recall: [[custom-llm-memory-layer]] gives a ReAct response agent a search tool so memory lookup can be skipped when the active transcript is sufficient.
- Persistence and correction example: [[custom-llm-memory-layer]] shows a name corrected from AVB to Avishek and retrieved after the program restarts.
- Turn record and compaction boundary: [[kapy-memory-system]] stores one memory record per input-tool-loop-output turn with both the raw work log and a compact node.
- Causal provenance: [[kapy-memory-system]] links records through agent-reported parent memory IDs rather than forcing unified storage into thread-local chains.
- Two retrieval modes: [[kapy-memory-system]] requires a broad first recall call, then permits targeted filesystem search and raw-log inspection as the agent's information need becomes specific.
- Retrieval-versus-interpretation boundary: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] shows how a historically accurate passage can misrepresent a user's current belief when it records exploration or a superseded view.
- Selective original reading: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] argues that an index should locate source material while the agent decides whether to open revisions, discussions, or authoritative system state for the present task.
- Sparse-history infrastructure: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] separates many durable but intermittently active tenant datasets from the memory product's admission and context-use policies.

## Counterevidence & Qualifications
The infrastructure-stack source names privacy, deletion, and policy requirements but does not specify enforcement, tenant scoping, user correction, retrieval evaluation, or confidence calibration. The memory architectures supply no comparative benchmark for compaction triggers, conflict policies, recall strategies, temporal weights, decay curves, or storage combinations. PsiACE's critique is strongest for detached continuity layers; calling Tape history itself “memory” preserves evidence but does not remove the need for indexing, summarization, temporal interpretation, correction, retention, and authorization. Nowledge Mem is a first-party product account: its numerical gates, boosts, task budgets, and `confidence = max(new, old)` rule are implementation policies rather than validated general laws, and non-decreasing confidence can misrepresent evidence later shown unreliable.

Anthropic's note-taking examples show coherence across resets but provide no controlled comparison with compaction or retrieval systems. A note file can also preserve stale, mistaken, sensitive, or overgeneralized state indefinitely unless a surrounding lifecycle governs it.

DeepChat's account is first-party and provides no memory-quality benchmark, false-write or false-recall rate, longitudinal decay evaluation, conflict-adjudication study, privacy audit, or measured token tradeoff. Comparing against ten nearby memories, using a cheaper model for adjudication, and applying half-life-like decay are implementation policies rather than established optimal values. Self-updating memory, higher-order insight, Skill generation, and parts of human conflict resolution remain roadmap items.

Thompson's agent examples are personal and architectural analogies rather than controlled evidence about task success, memory fidelity, identity, or continuous learning. External files can preserve stale, incorrect, sensitive, or adversarial state and require the same admission, provenance, correction, authorization, and expiry controls identified by the other sources.

AutoMem supplies controlled within-harness task measurements but remains narrow evidence: three games, one base-model family, small fixed-seed evaluations, separate per-environment scaffolds and specialists, and fresh memory each episode. Its results do not establish a universal memory policy, cross-domain transfer, persistent-memory safety, matched serving economics, or human-like introspection. Because the full system changes both scaffold code and a memory-model adapter, “memory alone” means the gameplay model is frozen rather than the complete agent remaining unchanged.

The Mem0-inspired tutorial is architectural and pedagogical rather than evaluative. Its 64-dimensional embeddings, similarity threshold, top-k, and ReAct iteration limits are unvalidated settings; the extraction example itself produces facts contrary to the input; and undefined or mismatched variables make several snippets non-runnable as printed. It also leaves provenance, temporal validity, retention, deletion, authorization, user review, and cross-tenant testing outside the worked implementation.

Kapy's account is likewise a first-person design report rather than comparative evidence. More than ten days of satisfactory use does not establish recall quality, compact-node fidelity, causal-link completeness, latency, token cost, conflict behavior, privacy, or authorization. Mandatory first-call recall can impose unnecessary work on self-contained turns, keyword search can miss semantically related records, and the unused DAG does not yet demonstrate causality-aware retrieval.

The personal-agent retrieval analysis is also a practitioner argument, not a comparative memory evaluation. Its Turbopuffer, Mem0, and Linear details are relayed from first-party documentation or customer cases, and its Todaypuffer figures come from one prototype workload. It supports separating infrastructure metrics from memory quality, but supplies no false-belief, context-admission, longitudinal preference, permission, or end-to-end task benchmark.

## What Changed
- Added memory-operation proficiency as a separately trainable layer above storage and retrieval architecture.
- Added trajectory-level scaffold revision and consult-before-write training evidence from three long-horizon games.
- Added a minimal optional retrieval-and-maintenance implementation while preserving its extraction and code-quality failures as evidence against treating a tutorial architecture as validated memory.
- Added Kapy's raw-log/compact-node split, causal record DAG, and fixed-versus-autonomous retrieval modes.
- Separated search infrastructure metrics from memory interpretation, authorization, and context-admission quality.

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
- [[ArtificialGeneralIntelligence]] - external continuity does not by itself settle whether a system learns continuously.
- [[HumanAgencyInAI]] - stored state and coordination do not establish volition or moral agency.
- [[Metamemory]] - frames memory use as learned monitoring and control over encoding, retrieval, and organization.
- [[AutoMem]] - supplies a two-loop implementation for optimizing memory structure and operation proficiency.
- [[Mem0]] - supplies the extraction and update architecture adapted by the newest tutorial.
- [[DSPy]] - supplies structured extraction and ReAct tool loops for retrieval and maintenance.
- [[Qdrant]] - supplies filtered vector persistence in the tutorial implementation.
- [[MemoryRetrievalModes]] - separates mandatory broad orientation from autonomous targeted evidence search.
- [[Kapy]] - implements per-turn records, compact views, causal parent links, and two recall modes.
- [[PersonalAgentRetrieval]] - locates historical evidence while leaving present-tense interpretation and context admission to the memory and agent layers.

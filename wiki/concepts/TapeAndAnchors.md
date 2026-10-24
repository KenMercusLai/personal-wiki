---
title: "Tape and Anchors"
type: concept
tags: [ai, agents, context-management, memory]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
  - tapexbee
  - deepchat-tape
  - deepseek-harness-source-analysis
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[TapeAndAnchors]] is a context-management model that treats interaction history as an append-only tape and uses entries, compact anchors, selectable views, and handoff to reconstruct the context needed for a task.

## Current Synthesis
The sources argue that many session, memory, compact, fork, merge, and handoff designs share an expensive premise: state must continue and history must not be lost. Tape relaxes that premise by preserving every interaction as an immutable entry while allowing active context to contain only selected material. Anchors identify or summarize recoverable moments, views collect relevant entry ranges, and handoff advances the working window after writing a state-bearing anchor. The newer source makes the specification more concrete and shows how [[AgentTopicLifecycle]] can map business topics onto bounded Tape ranges without coupling the model to local files, databases, object storage, or vector retrieval.

An operational Tape can record structured messages, tool calls and results, runtime events, and key anchors, then expose `tape_info`, `tape_search`, `tape_context`, `tape_anchors`, and `tape_handoff` operations, as [[DeepChat]] does. DeepChat's fuller implementation separates three readers: a mutable message-table projection for people, a freshly assembled Tape view for the model, and immutable evidence plus request traces for investigators. ViewManifest records the entries, anchor, budget allocation, and prompt and tool hashes used for one request without duplicating the request body. Memory is derived rather than substituted: compact conclusions retain pointers back to source passages, so the system can recall a small statement first and expand the original evidence only when needed.

[[DeepSeekHarness]] independently supplies a narrower Log-and-Surface implementation of the same separation. Its append-only Session Log retains messages, calls, results, and execution state, while Surface derives the current model messages. A summary can be appended and marked as replacing an earlier interval in Surface even though the earlier events remain in Log. Unlike the fuller Tape accounts, the source does not describe model-controlled search over the retained history, anchors as a general context API, or a per-request selection manifest.

Anchors also decouple retention from active-window reduction. DeepChat can advance the read boundary when summarization fails or is not shorter, provided the next assembled view is genuinely smaller; omitted facts remain searchable on Tape. Bee adds a workflow specialization: task, node, and DAG-checkpoint anchors divide long work into retryable context ranges and preserve external-call results, while the completed workflow still finalizes as one Topic. These mechanisms improve contextual recovery and observability but do not make external side effects idempotent or keep separate state projections transactionally consistent with Tape.

## Key Claims
- Infinite history should be treated as a material library, not a burden automatically inherited by every task.
- Entries preserve user, model, tool, and runtime facts by append; corrections or withdrawals add new facts instead of mutating old records.
- Anchors change the default read boundary, while views select related entries without deleting source history.
- Context assembly is an exploration-and-selection process whose transient result can be recorded through a manifest of provenance and fingerprints.
- Handoff or compaction can advance an overloaded active window independently of summary generation when the resulting view is demonstrably smaller.
- Stable abstractions can sit over different storage, retrieval, observability, topic-lifecycle, and workflow infrastructure.
- Preserved context improves recovery and auditability but does not by itself make external effects transactional, idempotent, or safely replayable.

## Evidence
- Shared premise critique: [[mu-jiang-chui-zi-ding-zi]] says compact, summary, fork, merge, handoff, memory, and context strategies often assume state must be continued and history cannot be lost.
- Tape design: [[mu-jiang-chui-zi-ding-zi]] describes one endless tape where interactions are appended as facts and never modified.
- Anchor design: [[mu-jiang-chui-zi-ding-zi]] describes anchors as minimal state packets written at stage changes.
- Context assembly: [[mu-jiang-chui-zi-ding-zi]] says new tasks should explore raw fragments and select sufficient context.
- Core specification: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] distinguishes session-scoped Tape, immutable entries, special anchor entries, views, and handoff.
- Infrastructure flexibility: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] allows local JSONL, databases, object stores, vector retrieval, and token observability beneath the same abstractions.
- Domain extension: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] and its four retained diagrams show topic ranges, recall anchors, normal finalization, and unfinished-topic recovery.
- Product implementation: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports DeepChat recording conversation, tool, runtime, and anchor events in Session Tape and exposing search, context, anchor, and handoff tools.
- Independent runtime pattern: [[deepseek-harness-source-analysis]] shows Session Log retaining original events while a derived Surface replaces an older interval with an appended summary for subsequent model requests.
- Provenance path: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] says derived memories retain links to the sentences and fragments from which they were distilled.
- Workflow checkpoints: [[tapexbee]] places task, node, and whole-DAG anchors around ordinary agent entries so retries can recover progress and external-call results.
- Reader separation: [[deepchat-tape]] distinguishes editable human-facing state, per-request model views, and immutable investigative evidence, then documents DeepChat's dual-store migration.
- View provenance: [[deepchat-tape]] describes ViewManifest recording selected Tape entries, omissions, the active anchor, budget allocation, and prompt and tool-definition hashes.
- Boundary-only compaction: [[deepchat-tape]] reports that an anchor may advance without a new summary when the new view is smaller, while earlier facts remain searchable.
- Inspection and effects: [[deepchat-tape]] and its retained screenshot show the same timeline supporting model-context inspection and paired tool dispatch/outcome evidence.

## Counterevidence & Qualifications
The first two sources give a conceptual model and proposed lifecycle, while DeepChat and Bee supply first-party implementation accounts rather than independent benchmarks; the DSH source is a version-bound code analysis without full application testing. The combined evidence does not resolve concurrency, anchor-schema evolution, retrieval ranking, topic-boundary accuracy, privacy, access control, physical deletion, multi-agent conflict, storage growth, or how much context is sufficient for high-stakes work. DeepChat still renders ordinary chat from a mutable message table, while Bee projects DAG state into `task.json`; both leave consistency across Tape and another state representation incompletely evaluated. DSH's Log and Surface demonstrate retained history plus derived context, but not the full Tape search, anchor, view-manifest, and topic-lifecycle model. Neither anchors nor immutable history provide exactly-once effects, rollback, compensation, or proof that a dispatched external action completed. Append-only history requires an explicit compliance strategy where data must be corrected or erased.

## What Changed
- Added DSH's independent Session Log versus derived Surface implementation.
- Distinguished that narrower pattern from a full Tape search, anchor, manifest, and topic lifecycle.
- Preserved the external-effect and append-only deletion boundaries.

## Related Concepts
- [[LLMContextManagement]] - tape and anchors offer a model for assembling context on demand.
- [[AgentMemory]] - anchors replace memory-like continuity with minimal state packets.
- [[DynamicContextCompression]] - the model reduces pressure to compress everything by default.
- [[RetrievalAugmentedGeneration]] - old history is retrieved as needed rather than inherited.
- [[AgentResumability]] - both concern continuation, but tape and anchors focus on context reconstruction rather than side-effect-safe execution recovery.
- [[AgentTopicLifecycle]] - builds explicit business-topic ranges and hooks over Tape primitives.
- [[AgentSystemTransparency]] - immutable entries and indexed ranges can support action and token-cost auditability.
- [[DeepChat]] - implements Tape as the evidence substrate beneath a separately derived memory layer.
- [[DeepSeekHarness]] - implements the narrower retained-Log and derived-Surface pattern for model history.
- [[AgentTaskOrchestration]] - uses Tape entries and frequent DAG anchors to make long-running work inspectable and resumable in context.

---
title: "Tape and Anchors"
type: concept
tags: [ai, agents, context-management, memory]
sources:
  - mu-jiang-chui-zi-ding-zi
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[TapeAndAnchors]] is a context-management model that treats interaction history as an append-only tape and uses entries, compact anchors, selectable views, and handoff to reconstruct the context needed for a task.

## Current Synthesis
The sources argue that many session, memory, compact, fork, merge, and handoff designs share an expensive premise: state must continue and history must not be lost. Tape relaxes that premise by preserving every interaction as an immutable entry while allowing active context to contain only selected material. Anchors identify or summarize recoverable moments, views collect relevant entry ranges, and handoff advances the working window after writing a state-bearing anchor. The newer source makes the specification more concrete and shows how [[AgentTopicLifecycle]] can map business topics onto bounded Tape ranges without coupling the model to local files, databases, object storage, or vector retrieval.

An operational Tape can record structured messages, tool calls and results, runtime events, and key anchors, then expose `tape_info`, `tape_search`, `tape_context`, `tape_anchors`, and `tape_handoff` operations, as [[DeepChat]] does. Memory is derived rather than substituted: compact conclusions retain pointers back to source passages, so the system can recall a small statement first and expand the original evidence only when needed. This supports the architectural synthesis while leaving performance, concurrency, retention, and compliance behavior unmeasured.

## Key Claims
- Infinite history should be treated as a material library, not a burden automatically inherited by every task.
- Entries preserve user, model, and tool interactions by append; corrections add new history instead of mutating old records.
- Anchors identify distilled or recoverable moments, and views select related entry sets without deleting source history.
- Context assembly is an exploration-and-selection process that can use summaries first and raw entries on demand.
- Handoff advances an overloaded active window after preserving prior state in an anchor.
- Stable abstractions can sit over different storage, retrieval, and observability infrastructure.
- Topic ranges demonstrate how domain-specific lifecycles can be built above Tape without changing its core history model.

## Evidence
- Shared premise critique: [[mu-jiang-chui-zi-ding-zi]] says compact, summary, fork, merge, handoff, memory, and context strategies often assume state must be continued and history cannot be lost.
- Tape design: [[mu-jiang-chui-zi-ding-zi]] describes one endless tape where interactions are appended as facts and never modified.
- Anchor design: [[mu-jiang-chui-zi-ding-zi]] describes anchors as minimal state packets written at stage changes.
- Context assembly: [[mu-jiang-chui-zi-ding-zi]] says new tasks should explore raw fragments and select sufficient context.
- Core specification: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] distinguishes session-scoped Tape, immutable entries, special anchor entries, views, and handoff.
- Infrastructure flexibility: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] allows local JSONL, databases, object stores, vector retrieval, and token observability beneath the same abstractions.
- Domain extension: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] and its four retained diagrams show topic ranges, recall anchors, normal finalization, and unfinished-topic recovery.
- Product implementation: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] reports DeepChat recording conversation, tool, runtime, and anchor events in Session Tape and exposing search, context, anchor, and handoff tools.
- Provenance path: [[zhuan-fang-deepchat-zuo-zhe-men-liao-liao-ben-di-you-xian-mcp-yu-agent-memory]] says derived memories retain links to the sentences and fragments from which they were distilled.

## Counterevidence & Qualifications
The first two sources give a conceptual model and proposed lifecycle, while DeepChat supplies a first-party implementation account rather than an independent benchmark. The combined evidence does not resolve concurrency, anchor-schema evolution, retrieval ranking, topic-boundary accuracy, privacy, access control, physical deletion, multi-agent conflict, storage growth, or how much context is sufficient for high-stakes work. Append-only history also requires an explicit compliance strategy where data must be corrected or erased.

## What Changed
- Added DeepChat as an implementation of conversation, tool, runtime, anchor, search, context, and handoff operations over Tape.
- Strengthened the distinction between immutable evidence and derived memory through traceable source pointers.
- Preserved the lack of independent evaluation and unresolved retention, deletion, concurrency, and retrieval questions.

## Related Concepts
- [[LLMContextManagement]] - tape and anchors offer a model for assembling context on demand.
- [[AgentMemory]] - anchors replace memory-like continuity with minimal state packets.
- [[DynamicContextCompression]] - the model reduces pressure to compress everything by default.
- [[RetrievalAugmentedGeneration]] - old history is retrieved as needed rather than inherited.
- [[AgentResumability]] - both concern continuation, but tape and anchors focus on context reconstruction rather than side-effect-safe execution recovery.
- [[AgentTopicLifecycle]] - builds explicit business-topic ranges and hooks over Tape primitives.
- [[AgentSystemTransparency]] - immutable entries and indexed ranges can support action and token-cost auditability.
- [[DeepChat]] - implements Tape as the evidence substrate beneath a separately derived memory layer.

---
title: "Agent Topic Lifecycle"
type: concept
tags: [ai, agents, context-management, memory, lifecycle]
sources:
  - tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi
  - tapexbee
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTopicLifecycle]] is a context-organization pattern that represents a user-facing topic as an indexed range of append-only agent interactions bounded by explicit start and finalization anchors.

## Current Synthesis
The pattern layers a business-level unit over [[TapeAndAnchors]] without changing the underlying history model. A `topic_initial` anchor opens a range; user, model, tool, reasoning, and other anchors accumulate inside it; and `topic_finalized` closes it with a summary. Topic metadata can record boundary sequence numbers, ownership, timestamps, and cost, while lifecycle hooks add recall, cleanup, fact extraction, or sharing behavior. A prior topic can be recalled compactly through its summary and index, expanded back to original entries when necessary, or automatically finalized when a new topic begins before the old one was closed.

Bee demonstrates that Topic profiles can specialize the same lifecycle. A `chat` profile supports ordinary conversation, while a `bee` profile represents a bounded Job or Cron workflow with an explicit goal, DAG nodes, review gates, and a final result. The completed Bee remains a Topic range usable by later chat or Bee recall, while more frequent node and DAG anchors keep long execution from collapsing into one oversized Turn.

## Key Claims
- Explicit boundary anchors turn an unbounded session tape into reusable user-facing topics.
- Topic summaries are compact views over preserved history, not replacements for the underlying entries.
- Monotonic sequence indexes make topic range search, replay, and entry accounting straightforward.
- Lifecycle hooks can add recall, finalization recovery, fact extraction, sharing, and token-cost accounting around a stable core.
- Recall can start with prior summaries and retain references for selective drill-down into full history.
- Oversized topics can use handoff anchors to create replayable segments without changing topic identity.
- Topic profiles can specialize lifecycle behavior while preserving one shared history and recall model.

## Evidence
- Topic boundaries: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] defines a topic as the entries and anchors between `topic_initial` and `topic_finalized`.
- Indexed storage: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] proposes initial and final sequence indexes plus summary, owner, and timestamp metadata.
- Hook points: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] places pre/post hooks around initialization and finalization.
- Recall flow: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] and its retained diagram show a recall anchor carrying prior-topic background and an index reference.
- Recovery and handoff: [[tape-x-topic-wo-dui-zhi-neng-ti-shang-xia-wen-de-zu-zhi-fang-shi]] closes an unfinished predecessor before a new topic and uses a `brain_overload` handoff anchor for oversized topics.
- Bee specialization: [[tapexbee]] defines `bee` as a Topic profile for Job and Cron work whose completed DAG still finalizes into the common Topic range.
- Cross-mode recall: [[tapexbee]] says chat and Bee can reuse each other's summarized and indexed Topic memory.

## Counterevidence & Qualifications
These are practitioner design proposals, not measured comparisons. They do not establish how reliably an LLM detects topic transitions, how concurrent writers or overlapping topics should be handled, how summaries and extracted facts are corrected, or how access control, retention, deletion, and cross-owner sharing work. Bee's Topic reuse also leaves state consistency, node replay, external-effect idempotency, and scheduler ownership unresolved. Automatic finalization and fact extraction may introduce model errors unless hooks remain auditable and reversible.

## What Changed
- Added profile-based specialization through Bee's Job and Cron lifecycle.
- Added cross-mode Topic memory reuse between chat and workflow execution.
- Qualified Topic-level retry with unresolved external-effect and scheduler semantics.

## Related Concepts
- [[TapeAndAnchors]] - provides the append-only entries, anchors, views, and handoff primitives beneath the topic layer.
- [[AgentMemory]] - topic summaries and index-backed replay provide a native recall mechanism.
- [[LLMContextManagement]] - topics select a bounded, reusable portion of durable session history.
- [[RetrievalAugmentedGeneration]] - finalized topic facts can become retrieval material for later questions.
- [[AgentSystemTransparency]] - explicit ranges, summaries, ownership, timestamps, and cost fields support auditing.
- [[AgentTaskOrchestration]] - Bee specializes a Topic into a DAG-shaped, reviewable execution unit.

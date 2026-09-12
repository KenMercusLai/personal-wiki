---
title: "Tape and Anchors"
type: concept
tags: [ai, agents, context-management, memory]
sources:
  - mu-jiang-chui-zi-ding-zi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[TapeAndAnchors]] is a context-management model that treats interaction history as an append-only tape and uses compact anchors plus on-demand retrieval to reconstruct the minimal context needed for a task.

## Current Synthesis
The source argues that many session, memory, compact, fork, merge, and handoff designs share an expensive premise: state must continue and history must not be lost. Tape and anchors relax that premise. The tape preserves all interaction facts as immutable history, anchors store only the minimal state needed at stage changes, and each new task rebuilds context by exploring raw fragments and selecting enough material for the present work.

## Key Claims
- Infinite history should be treated as a material library, not a burden automatically inherited by every task.
- An append-only tape can preserve facts without forcing all facts into active context.
- Anchors should store minimal stage state rather than full memory.
- Context assembly is an exploration-and-selection process.
- Tasks can end cleanly; the next task can start from an anchor and retrieve history only as needed.
- This model reduces assumptions behind memory, session continuity, compacting, forking, merging, and handoff.

## Evidence
- Shared premise critique: [[mu-jiang-chui-zi-ding-zi]] says compact, summary, fork, merge, handoff, memory, and context strategies often assume state must be continued and history cannot be lost.
- Tape design: [[mu-jiang-chui-zi-ding-zi]] describes one endless tape where interactions are appended as facts and never modified.
- Anchor design: [[mu-jiang-chui-zi-ding-zi]] describes anchors as minimal state packets written at stage changes.
- Context assembly: [[mu-jiang-chui-zi-ding-zi]] says new tasks should explore raw fragments and select sufficient context.

## Counterevidence & Qualifications
The source gives a conceptual model rather than an implementation protocol. It does not resolve anchor schema design, retrieval ranking, privacy, deletion, multi-agent conflict, or how much context is sufficient for high-stakes work.

## What Changed
- Created the initial concept page for the tape-and-anchors context model.

## Related Concepts
- [[LLMContextManagement]] - tape and anchors offer a model for assembling context on demand.
- [[AgentMemory]] - anchors replace memory-like continuity with minimal state packets.
- [[DynamicContextCompression]] - the model reduces pressure to compress everything by default.
- [[RetrievalAugmentedGeneration]] - old history is retrieved as needed rather than inherited.
- [[AgentResumability]] - both concern continuation, but tape and anchors focus on context reconstruction rather than side-effect-safe execution recovery.

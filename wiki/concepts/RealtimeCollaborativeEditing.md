---
title: "Real-Time Collaborative Editing"
type: concept
tags: [collaboration, distributed-systems, convergence]
sources:
  - figma-realtime-editing-of-ordered-sequences
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[RealtimeCollaborativeEditing]] is the coordination of near-simultaneous edits across clients that apply changes locally for responsiveness while still converging on the same shared document state.

## Current Synthesis
The Figma case frames collaboration as an eventual-convergence problem: clients optimistically apply their own edits, send operations to a server, and later receive other clients' work in potentially different orders. Correctness therefore depends on an operation and data model whose final state is independent of delivery order, plus explicit resolution for collisions the representation cannot handle alone. The appropriate mechanism is workload-dependent: text editing may justify [[OperationalTransformation]] and its non-interleaving behavior, while Figma's bounded ordered object lists make [[FractionalIndexing]] simpler and make occasional interleaving acceptable.

## Key Claims
- Immediate local application reduces interaction latency but allows replicas to observe concurrent edits in different orders.
- Convergence requires either transforming operations, choosing a representation whose operations commute sufficiently, or resolving exceptional collisions centrally.
- The edited data type matters: design-object ordering can tolerate tradeoffs that would be disruptive in character sequences.
- Simplicity can improve correctness and delivery speed when a more general algorithm's extra guarantees are not required.

## Evidence
- Convergence model: [[figma-realtime-editing-of-ordered-sequences]] describes local-first application followed by server relay and requires identical final documents despite different operation arrival orders.
- Workload fit: [[figma-realtime-editing-of-ordered-sequences]] says Figma's child lists are not enormous and that interleaving concurrently inserted design objects is usually tolerable or manually repairable.
- Collision handling: [[figma-realtime-editing-of-ordered-sequences]] assigns a unique server-generated position when concurrent inserts initially choose the same fractional index.

## Counterevidence & Qualifications
This is a first-party 2017 architecture explanation rather than a proof, benchmark, failure study, or complete multiplayer protocol. It does not specify transport guarantees, offline reconciliation, deletion conflicts, undo, persistence, permissions, server-failure behavior, or how unique replacement positions are selected and propagated. A workload that needs atomic multi-object moves, semantic conflict preservation, adversarial clients, or non-interleaving text may need stronger machinery.

## What Changed
- Established a workload-sensitive model of collaborative convergence rather than treating one sequencing algorithm as universal.
- Added the distinction between ordinary order-independent operations and collision cases that still need server arbitration.

## Related Concepts
- [[FractionalIndexing]] - Figma's selected representation for convergent object ordering.
- [[OperationalTransformation]] - rejected alternative with stronger text-editing behavior and higher implementation complexity.
- [[ReplicatedLog]] - contrasting approach that first establishes one shared operation order across replicas.

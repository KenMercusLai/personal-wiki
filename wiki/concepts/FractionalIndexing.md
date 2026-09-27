---
title: "Fractional Indexing"
type: concept
tags: [ordering, data-structures, collaboration]
sources:
  - figma-realtime-editing-of-ordered-sequences
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[FractionalIndexing]] represents sequence order by assigning each item a sortable position and creates space for insertion by choosing a value between neighboring positions.

## Current Synthesis
Figma assigns every child object an arbitrary-precision fractional index strictly between 0 and 1. Inserting between objects averages their positions; inserting at an edge averages the nearest position with 0 or 1; reordering changes only the moved object's index. Positions are stored as strings and use a broad ASCII digit set for compactness, avoiding fixed-width floating-point exhaustion while accepting that index strings can lengthen over time.

## Key Claims
- Sequence order can be derived by sorting independently stored item positions.
- An insertion or move usually changes only one object's position value.
- Open interval bounds preserve room for insertion at both ends.
- Arbitrary-precision string positions avoid fixed numeric precision limits.
- Repeated nearby insertions can lengthen indices, and concurrent inserts can interleave or initially collide.
- A server can resolve identical concurrent positions by assigning one insert a unique replacement.

## Evidence
- Insertion rule: [[figma-realtime-editing-of-ordered-sequences]] shows positions 0.3 and 0.4 producing a new position of 0.35, plus edge insertions at 0.05 and 0.5.
- Representation: [[figma-realtime-editing-of-ordered-sequences]] describes open-interval indices stored as arbitrary-precision strings with the leading `0.` omitted and a base-95-like ASCII alphabet.
- Tradeoffs: [[figma-realtime-editing-of-ordered-sequences]] accepts growing index length and possible interleaving for bounded design-object lists while handling identical positions at the server.

## Counterevidence & Qualifications
The source does not publish the encoding, comparison, averaging, normalization, tie-breaking, or security algorithm, nor measurements of index growth or production collision frequency. Averaging is conceptual: string implementations must define a canonical alphabet and ordering carefully. The approach may be a poor fit for huge sequences, text edits where concurrent runs must stay contiguous, offline peers without an arbitration path, or operations that require atomic ordering across multiple objects.

## What Changed
- Established fractional indexing as a workload-specific collaborative-ordering strategy, not merely a database reorder trick.
- Added open-boundary insertion, arbitrary-precision encoding, growth, interleaving, and duplicate-position qualifications.

## Related Concepts
- [[RealtimeCollaborativeEditing]] - concurrency setting in which Figma uses fractional positions.
- [[OperationalTransformation]] - more complex sequence-editing alternative rejected for Figma's workload.
- [[ReplicatedLog]] - contrasting model that derives convergence from a shared operation sequence.

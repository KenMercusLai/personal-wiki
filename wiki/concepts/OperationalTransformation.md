---
title: "Operational Transformation"
type: concept
tags: [collaboration, distributed-systems, sequence-editing]
sources:
  - figma-realtime-editing-of-ordered-sequences
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[OperationalTransformation]] is a collaborative-editing technique that rewrites a new operation against concurrent operations so its intended effect is preserved after their positions or context have changed.

## Current Synthesis
In Figma's example, an insertion before a concurrently deleted range shifts the delete's starting position, so transforming the delete preserves the intended removal. OT is attractive for very large text sequences because it can use little memory and linearize concurrent insertions instead of interleaving them. Figma rejected it for ordered design objects because correct transformation logic is difficult, every added operation must interact correctly with the others, and a move is commonly represented as a delete plus insert.

## Key Claims
- Transformation adjusts positional operations to preserve their intended effect after concurrent edits.
- OT can provide strong sequence-editing behavior with low overhead on very large sequences.
- Concurrent insertions can be linearized rather than interleaved.
- Correctness is difficult because each operation type must transform coherently against the others.
- Native reorder behavior may be awkward when movement is represented as deletion followed by insertion.

## Evidence
- Positional preservation: [[figma-realtime-editing-of-ordered-sequences]] shows `Delete(at: 1, n: 2)` becoming `Delete(at: 2, n: 2)` after an insertion at index 0 so the same characters are removed.
- Benefits: [[figma-realtime-editing-of-ordered-sequences]] attributes good performance, low memory overhead, and non-interleaved concurrent insertion to OT for large sequences.
- Complexity and fit: [[figma-realtime-editing-of-ordered-sequences]] cites historical subtle algorithmic errors, pairwise transformation burden among operation types, and inefficient reorder semantics as reasons not to use it at Figma.

## Counterevidence & Qualifications
The source deliberately gives only a simplified contrast, not a full OT specification or comparison across modern implementations. Its statement that complexity grows quadratically with the operation set describes Figma's design concern, not a universal implementation theorem. The article also acknowledges OT as viable and does not establish that fractional indexing would be preferable for text, huge sequences, or richer editing semantics.

## What Changed
- Added OT as a qualified alternative whose value depends on text-scale and insertion semantics.
- Recorded the concrete transformation rule and the operation-pair complexity that drove Figma's rejection.

## Related Concepts
- [[RealtimeCollaborativeEditing]] - problem domain in which OT preserves intent under concurrency.
- [[FractionalIndexing]] - simpler alternative chosen by Figma for ordered design objects.
- [[ReplicatedLog]] - alternative replication model based on agreement over operation order rather than pairwise transformation.

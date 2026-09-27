---
title: "Zero-Based Indexing"
type: concept
tags: [computer-science, indexing, sequences, programming-language-design]
sources:
  - e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[ZeroBasedIndexing]] assigns index 0 to the first element of a sequence, so an element's index equals the number of elements that precede it.

## Current Synthesis
When a length-N sequence is represented by a lower-inclusive, upper-exclusive range, starting at zero produces `0 ≤ i < N`; starting at one produces the less direct `1 ≤ i < N + 1`. Zero therefore makes the index simultaneously an ordinal offset, the count of preceding elements, and a value bounded directly by the sequence length. This is a structural simplicity argument grounded in [[HalfOpenIntervals]], not proof that every user-facing numbering system or inherited programming environment should begin at zero.

## Key Claims
- Index 0 naturally denotes the first element because no elements precede it.
- In a length-N sequence, valid zero-based indices satisfy `0 ≤ i < N`.
- The sequence length can serve directly as the exclusive upper bound without an added or subtracted one.
- Zero-based indexing inherits the range-length and adjacency benefits of half-open intervals.
- Language conventions that start at one or include both bounds may introduce avoidable boundary arithmetic in sequence operations.

## Evidence
- Ordinal interpretation: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] defines an element's subscript as the count of preceding elements and derives zero for the first position.
- Length-N notation: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] contrasts `1 ≤ i < N + 1` with the simpler `0 ≤ i < N`.
- Language-design comparison: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] criticizes FORTRAN, ALGOL 60, Pascal, and SASL conventions while citing Mesa experience in favor of lower-inclusive, upper-exclusive ranges.

## Counterevidence & Qualifications
The note is a short normative argument, not an empirical comparison of indexing schemes. Human-facing counts, mathematical traditions, domain standards, and compatibility constraints can favor one-based labels even when internal offsets remain zero-based. The source's claims about language design and programmer mistakes are not supported by quantitative data in the document.

## What Changed
- Created the concept around the ordinal-as-offset interpretation and the `0 ≤ i < N` sequence invariant.

## Related Concepts
- [[HalfOpenIntervals]] - supplies the endpoint convention from which Dijkstra derives zero-based sequence bounds.
- [[MultidimensionalArraySlicing]] - applies index ranges to selecting structured subsets of arrays.
- [[NumPyArrayModel]] - provides a modern array context in which zero-based positions and slicing are used.

---
title: "Half-Open Intervals"
type: concept
tags: [computer-science, intervals, indexing, notation]
sources:
  - e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[HalfOpenIntervals]] include one endpoint and exclude the other; for discrete sequence ranges, the convention defended here is inclusive at the lower bound and exclusive at the upper bound: `a ≤ i < b`.

## Current Synthesis
For consecutive integer positions, the lower-inclusive and upper-exclusive form aligns notation with useful arithmetic and composition rules. The range length is `b - a`, adjacent ranges can meet at the same boundary, a range can begin at the smallest natural number without naming a smaller one, and an empty prefix can end at that same smallest value. These properties make the convention especially coherent when paired with [[ZeroBasedIndexing]], but the available evidence is a concise design argument plus an unquantified report of Mesa programming experience rather than comparative error-rate research.

## Key Claims
- A discrete range `a ≤ i < b` contains `b - a` positions.
- Adjacent half-open ranges compose at a shared boundary without overlap or a one-unit gap.
- Lower-bound inclusion avoids inventing a predecessor below the smallest natural number for a range that starts there.
- Upper-bound exclusion represents an empty prefix without forcing its endpoint outside the natural numbers.
- Mesa's support for all four endpoint conventions reportedly gave practitioners reason to discourage the other three.

## Evidence
- Arithmetic and adjacency: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] compares four endpoint conventions and observes that the two mixed forms make length equal the difference between bounds and allow adjacent ranges to share a boundary.
- Boundary behavior: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] argues separately for including the lower endpoint at the smallest natural number and excluding the upper endpoint when the range is empty.
- Practitioner report: [[e-w-dijkstra-archive-why-numbering-should-start-at-zero-ewd-831]] says Mesa programmers, despite having notation for all four forms, were advised against the other three after repeated clumsiness and mistakes.

## Counterevidence & Qualifications
The source establishes internal consistency and ergonomic advantages, not universal superiority. Closed intervals can match domains where both endpoints are substantively included, and the note provides no controlled measurements of mistakes, language comparisons, or tasks where alternative conventions may be clearer. Its treatment also depends on discrete integer sequences and should not be generalized automatically to every mathematical interval.

## What Changed
- Created the concept from Dijkstra's arithmetic, adjacency, boundary, and Mesa-experience arguments.

## Related Concepts
- [[ZeroBasedIndexing]] - combines with a half-open range to express a length-N sequence as `0 ≤ i < N`.
- [[RobustProgramming]] - shares the goal of choosing representations that remove avoidable boundary mistakes.

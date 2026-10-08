---
title: "A* Search"
type: concept
tags: [algorithms, graph-theory, shortest-paths, pathfinding]
sources:
  - red-blob-games-improving-heuristics-for-a-star-search
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[AStarSearch]] is a shortest-path graph search that prioritizes nodes using path cost already incurred plus a heuristic lower bound on remaining cost to the goal.

## Current Synthesis
A* becomes faster when its heuristic closely reflects the graph's true remaining cost while staying admissible. Common geometric distances are cheap and reusable, but they ignore walls, corridors, and other topology, so they can direct exploration away from the actual route. A perfect goal-specific distance table would give ideal guidance but is usually too expensive to compute or store for every goal. [[DifferentialHeuristic]] occupies the middle ground: reuse exact distance tables for a small landmark set, strengthen the lower bound at query time, and leave the A* search procedure unchanged.

## Key Claims
- A* uses a heuristic to focus shortest-path exploration toward the goal.
- Search work falls when the heuristic is a tight lower bound on true remaining cost.
- Coordinate-distance heuristics can be weak when obstacles make geometric proximity diverge from graph distance.
- An exact distance-to-goal table is a perfect heuristic for that goal but is usually impractical to regenerate or retain for all goals.
- A reusable heuristic can combine a conventional geometric bound with precomputed graph-distance bounds and take their maximum.

## Evidence
- Heuristic behavior: [[red-blob-games-improving-heuristics-for-a-star-search]] contrasts paths aligned with geometric direction against paths that first travel away from the goal because of map structure.
- Perfect-versus-reusable guidance: [[red-blob-games-improving-heuristics-for-a-star-search]] explains that a perfect heuristic changes with the goal but not the start, making per-goal construction impractical for varied queries.
- Algorithm boundary: [[red-blob-games-improving-heuristics-for-a-star-search]] implements landmark guidance by replacing only the heuristic function and reports no change to A* itself.
- Workload dependence: [[red-blob-games-improving-heuristics-for-a-star-search]] demonstrates qualitatively that benefit varies with start, goal, landmark placement, and map topology.

## Counterevidence & Qualifications
The source is a practitioner tutorial rather than a proof, controlled benchmark, or production report. Its interactive demonstrations are not preserved with numeric outcomes in the archived Markdown, and the author says the method has not been used in a real project. A more informed heuristic is not free: landmark preprocessing, memory, query-time comparisons, and refresh policy must be justified by the workload. If a stale table overestimates after an edge-cost decrease, ordinary optimality guarantees no longer hold until the table is updated.

## What Changed
- Created the concept with the distinction between cheap geometric guidance, perfect goal-specific guidance, and reusable landmark guidance.
- Made heuristic admissibility and topology awareness the central performance and correctness boundary.

## Related Concepts
- [[DifferentialHeuristic]] - strengthens A* guidance with reusable landmark-distance lower bounds.
- [[DijkstrasAlgorithm]] - can precompute exact graph distances used by the landmark heuristic.
- [[GraphModeling]] - determines the directions, weights, and topology that path cost and heuristic admissibility must respect.

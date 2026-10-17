---
title: "A* Search"
type: concept
tags: [algorithms, graph-theory, shortest-paths, pathfinding]
sources:
  - red-blob-games-improving-heuristics-for-a-star-search
  - yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[AStarSearch]] is a shortest-path graph search that prioritizes nodes using path cost already incurred plus a heuristic lower bound on remaining cost to the goal.

## Current Synthesis
A* becomes faster when its heuristic closely reflects the graph's true remaining cost while staying admissible. Common geometric distances are cheap and reusable, but they ignore walls, corridors, and other topology, so they can direct exploration away from the actual route. A perfect goal-specific distance table would give ideal guidance but is usually too expensive to compute or store for every goal. [[DifferentialHeuristic]] occupies the middle ground: reuse exact distance tables for a small landmark set and strengthen the scalar lower bound at query time. A related [[FlowFieldPathfinding]] proposal instead reuses the cached direction toward a nearby landmark; that directional policy needs its own correctness and performance justification rather than inheriting differential-heuristic guarantees automatically.

## Key Claims
- A* uses a heuristic to focus shortest-path exploration toward the goal.
- Search work falls when the heuristic is a tight lower bound on true remaining cost.
- Coordinate-distance heuristics can be weak when obstacles make geometric proximity diverge from graph distance.
- An exact distance-to-goal table is a perfect heuristic for that goal but is usually impractical to regenerate or retain for all goals.
- A reusable heuristic can combine a conventional geometric bound with precomputed graph-distance bounds and take their maximum.
- A cached direction toward a landmark can add topology-aware steering, but using it for a different nearby goal is distinct from supplying A* with an admissible scalar heuristic.

## Evidence
- Heuristic behavior: [[red-blob-games-improving-heuristics-for-a-star-search]] contrasts paths aligned with geometric direction against paths that first travel away from the goal because of map structure.
- Perfect-versus-reusable guidance: [[red-blob-games-improving-heuristics-for-a-star-search]] explains that a perfect heuristic changes with the goal but not the start, making per-goal construction impractical for varied queries.
- Algorithm boundary: [[red-blob-games-improving-heuristics-for-a-star-search]] implements landmark guidance by replacing only the heuristic function and reports no change to A* itself.
- Workload dependence: [[red-blob-games-improving-heuristics-for-a-star-search]] demonstrates qualitatively that benefit varies with start, goal, landmark placement, and map topology.
- Obstacle example: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] shows why a goal east of a room can still require initially moving west through its only door.
- Directional variant: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] proposes following a precomputed landmark flow direction when its landmark-distance bound exceeds the straight-line estimate.

## Counterevidence & Qualifications
Both sources are practitioner explanations rather than controlled benchmarks or production reports. The interactive demonstrations in the first are not preserved with numeric outcomes, and its author says the method has not been used in a real project; the second provides neither an implementation nor search measurements. A more informed heuristic is not free: landmark preprocessing, memory, query-time comparisons, and refresh policy must be justified by the workload. If a stale table overestimates after an edge-cost decrease, ordinary optimality guarantees no longer hold until the table is updated. The second source's direct use of cached landmark directions is not proven equivalent to ordinary A* ordering and should remain a separate policy until its termination and optimality behavior are specified.

## What Changed
- Distinguished admissible landmark lower bounds from a source-specific policy that directly reuses landmark flow directions.
- Added a concrete wrong-way-door example and preserved the missing proof and benchmark boundary.

## Related Concepts
- [[DifferentialHeuristic]] - strengthens A* guidance with reusable landmark-distance lower bounds.
- [[DijkstrasAlgorithm]] - can precompute exact graph distances used by the landmark heuristic.
- [[GraphModeling]] - determines the directions, weights, and topology that path cost and heuristic admissibility must respect.
- [[FlowFieldPathfinding]] - caches exact directions toward fixed destinations and may supply a separate directional guidance policy.

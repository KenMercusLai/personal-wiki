---
title: "Differential Heuristic"
type: concept
tags: [algorithms, graph-theory, shortest-paths, pathfinding]
sources:
  - red-blob-games-improving-heuristics-for-a-star-search
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[DifferentialHeuristic]] is an A* heuristic that precomputes exact distances to selected landmark nodes and uses differences between those distances as triangle-inequality lower bounds on the cost between a search node and the goal.

## Current Synthesis
The method converts a small amount of reusable global graph knowledge into stronger per-query guidance. For each landmark, preprocess the shortest distance from every node to that landmark. At search time, the difference between the current node's and goal's landmark distances supplies a lower bound; for an undirected graph, its absolute value is valid. Taking the maximum across landmarks and a base geometric heuristic keeps the strongest bound available. The approach is attractive because it changes only the heuristic function, but its value depends on placing enough landmarks in positions useful for the actual route distribution without making preprocessing and storage excessive.

## Key Claims
- Triangle inequality turns two exact node-to-landmark distances into a lower bound on node-to-goal cost.
- A single landmark helps only some relative arrangements of start, goal, and landmark, so useful coverage normally requires several landmarks.
- The maximum across valid landmark bounds and a valid base heuristic is the strongest of those available lower bounds.
- Exact landmark distances can be precomputed with [[DijkstrasAlgorithm]], or breadth-first search when all edge weights equal one.
- Landmark placement should reflect probable paths, costly queries, topology, common destinations, and map stability.
- The principal resource cost is a table proportional to the number of landmarks times the number of graph nodes.

## Evidence
- Mathematical bound: [[red-blob-games-improving-heuristics-for-a-star-search]] derives `cost(B, X) ≥ cost(B, L) - cost(X, L)` from triangle inequality and uses an absolute difference for undirected graphs.
- Multiple-landmark aggregation: [[red-blob-games-improving-heuristics-for-a-star-search]] computes one bound per landmark and takes the maximum together with a Manhattan or other base heuristic.
- Preprocessing: [[red-blob-games-improving-heuristics-for-a-star-search]] stores a node-by-landmark cost array populated by one Dijkstra run per landmark, reversing edges for directed graphs when distances must lead to the landmark.
- Placement and adaptation: [[red-blob-games-improving-heuristics-for-a-star-search]] considers likely routes, long-path cost, common destinations, randomized map analysis, marginal contribution, and changing maps.
- Demonstrated scope: [[red-blob-games-improving-heuristics-for-a-star-search]] applies the method qualitatively to Dragon Age, Cogmind, open maps, room-and-corridor maps, and a maze.

## Counterevidence & Qualifications
Landmark usefulness is uneven: a poorly positioned landmark may add no information beyond the base heuristic, and broad coverage can require enough landmarks to make storage material. Placement recommendations are project-specific and the automated method is presented as a plausible randomized strategy rather than an established optimum. The archived demos do not retain numeric exploration counts, there is no controlled comparison of preprocessing and query costs, and the author reports no real-project use. Dynamic edge costs also require refresh discipline: decreases can invalidate admissibility and path optimality, while increases mainly weaken performance until recomputation.

## What Changed
- Created the concept around the reusable triangle-inequality distance bound.
- Distinguished mathematical admissibility from practical benefit, which depends on landmark coverage and table freshness.
- Added preprocessing, memory, directed-graph, and dynamic-map boundaries.

## Related Concepts
- [[AStarSearch]] - consumes the landmark-derived lower bound as its heuristic.
- [[DijkstrasAlgorithm]] - computes exact node-to-landmark distances during preprocessing.
- [[GraphModeling]] - supplies edge direction, weight, topology, and mutation semantics for the distance table.

---
title: "云风的 BLOG: 用地标改进 A star 寻路的启发函数"
type: source
tags: [algorithms, pathfinding, graph-theory, game-development]
date: 2026-08-09
source_file: "/mnt/ken_personal_wiki/Articles/云风的 BLOG- 用地标改进 A star 寻路的启发函数.md"
---

## Summary
[[YunFeng]] proposes using precomputed distances and next-step directions toward one or more landmarks to give [[AStarSearch]] constant-time, topology-aware guidance on maps where straight-line distance cannot see walls. The triangle inequality yields the familiar [[DifferentialHeuristic]] lower bound `d(S,L) - d(E,L)`, while a cached [[FlowFieldPathfinding]] map can also steer expansion toward a landmark when that bound exceeds the geometric estimate. The mechanism is plausible for fixed, reusable maps, but the article does not prove its direction-switching rule, benchmark it, or fully specify directed-graph behavior.

## Key Claims
- A* improves on uninformed [[DijkstrasAlgorithm]] exploration by using a cheap heuristic, but straight-line distance can badly mislead it when the correct route initially moves away from the goal to pass through a door or corridor.
- For a fixed landmark, one Dijkstra run can cache every node's exact distance and next movement toward that landmark, allowing a later query to retrieve landmark guidance in `O(1)` time.
- Triangle inequality gives `d(S,E) >= d(S,L) - d(E,L)`, so landmark distances can expose a much stronger lower bound than Euclidean distance when an obstacle separates the current node from the goal.
- The proposed policy follows the cached landmark direction when the geometric estimate is no greater than the landmark-derived bound, and otherwise falls back to conventional straight-line guidance.
- Landmark reachability can sometimes reject impossible destinations or establish connectivity, although the stated conclusions implicitly require compatible reachability semantics such as an undirected graph.
- Several landmarks can broaden coverage, and successful destinations can be retained as new landmarks for later route queries.
- The per-evaluation cost is constant only for a fixed number of landmarks; preprocessing, storage, landmark selection, and maintenance remain outside that claim.

## Key Quotes
> "最简单的方法是用一个地标。" — the article's central proposal for adding global map knowledge to a cheap heuristic.

> "因为三角形的任意两条边之和大于等于第三边，所以有 SE + EL >= SL。" — derivation of the landmark lower bound.

## Connections
- [[YunFeng]] — author presenting the landmark-guided pathfinding proposal.
- [[AStarSearch]] — search procedure whose geometric guidance the proposal seeks to strengthen.
- [[DifferentialHeuristic]] — triangle-inequality lower bound supplied by exact landmark distances.
- [[FlowFieldPathfinding]] — cached per-node direction toward a fixed landmark, reused by the proposed switching policy.
- [[DijkstrasAlgorithm]] — preprocessing method for exact landmark distances and shortest-path directions.

## Contradictions
- The article says the smaller `SL - EL` value among several landmarks decides which landmark path to use, whereas the existing differential-heuristic source takes the maximum of valid landmark lower bounds to obtain the strongest admissible scalar heuristic. The text does not establish that its smaller-bound directional choice preserves optimality or minimizes search work.
- Its reachability statements are sound under undirected connectivity but do not transfer unchanged to directed graphs: two nodes that can each reach the same landmark need not be mutually reachable.
- The claimed `O(1)` lookup applies to a fixed landmark count and excludes Dijkstra preprocessing, `landmarks × nodes` storage, and refresh after graph changes.

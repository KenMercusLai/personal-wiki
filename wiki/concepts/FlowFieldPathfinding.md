---
title: "Flow-Field Pathfinding"
type: concept
tags: [algorithms, graph-theory, shortest-paths, pathfinding]
sources:
  - yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[FlowFieldPathfinding]] precomputes, for a fixed destination, the shortest remaining cost and a next-step direction at every reachable node so many later travelers can reuse one global route map.

## Current Synthesis
Running [[DijkstrasAlgorithm]] from a fixed destination can produce more than a distance table: predecessor or successor information can assign every reachable node a local movement direction toward that destination. A query then retrieves the cached distance or direction in constant time. The representation is most useful when many searches share destinations or when selected landmarks can stand in for nearby goals, but its preprocessing, node-scale storage, graph-direction semantics, and refresh cost must be included in the design.

## Key Claims
- One fixed-destination shortest-path computation can serve route guidance from every reachable node.
- Storing a next-step direction turns exact shortest-path data into a locally executable flow field.
- A cached field can supply topology-aware guidance where geometric direction cannot see walls, doors, or corridors.
- Per-node lookup is `O(1)`, while construction and storage scale with the graph and with the number of retained destinations or landmarks.
- Reusing a nearby landmark's direction for another goal is a heuristic policy, not automatically the same as following the exact route to that goal.

## Evidence
- Fixed-destination preprocessing: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] proposes one Dijkstra computation that caches the shortest route from every map point to a landmark.
- Constant-time direction lookup: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] states that any current position can then retrieve its direction toward the landmark in `O(1)` time.
- Landmark reuse: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] uses the cached field as temporary guidance when the true goal lies near the landmark and suggests retaining reached destinations for later queries.

## Counterevidence & Qualifications
The source gives no implementation, complexity accounting for construction, memory measurement, controlled search comparison, or proof for the policy that temporarily follows a nearby landmark's direction. `O(1)` describes lookup for one stored field, not preprocessing or an unbounded landmark search. Directed graphs require explicit orientation: distances and next directions toward a landmark may need reverse-edge preprocessing, and shared landmark reachability alone does not establish mutual reachability.

## What Changed
- Created the concept to separate exact fixed-destination route maps from the weaker act of using one as guidance toward a nearby goal.

## Related Concepts
- [[DijkstrasAlgorithm]] - computes the exact distances and route tree from which a flow field can be derived.
- [[AStarSearch]] - can consume landmark flow directions as a source-scoped guidance policy.
- [[DifferentialHeuristic]] - uses the same landmark distances as admissible scalar lower bounds rather than cached movement commands.

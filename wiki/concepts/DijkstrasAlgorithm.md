---
title: "Dijkstra's Algorithm"
type: concept
tags: [algorithms, graph-theory, shortest-paths]
sources:
  - freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction
  - red-blob-games-improving-heuristics-for-a-star-search
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[DijkstrasAlgorithm]] is a greedy single-source shortest-path algorithm for weighted graphs whose edge weights are non-negative.

## Current Synthesis
The algorithm maintains tentative distances from a chosen source, initially zero for the source and infinity elsewhere. It repeatedly selects the unsettled node with the smallest tentative distance, treats that distance as final, and relaxes each outgoing edge by comparing the neighbor's current distance with the cost of reaching it through the selected node. Recording the predecessor that produced each improvement yields a shortest-path tree as well as the distances. Beyond answering a route query directly, the same procedure can preprocess exact distance tables for reusable heuristics: one run per landmark gives [[DifferentialHeuristic]] the graph-aware lower bounds used to guide later [[AStarSearch]] queries.

## Key Claims
- The algorithm solves the single-source shortest-path problem for every reachable node in a non-negatively weighted graph.
- Tentative distances represent the best routes found so far, not final answers until their nodes are settled.
- Each relaxation replaces a neighbor's tentative distance only when the route through the current node is cheaper.
- Choosing the smallest unsettled tentative distance is safe because non-negative later edges cannot create a cheaper route back to that node.
- Predecessor links from successful relaxations form a shortest-path tree rooted at the source.
- Repeated runs can preprocess exact distances from every node to selected landmarks for later pathfinding queries.

## Evidence
- Initialization and selection: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] initializes node 0 to 0, all others to infinity, and settles nodes by the smallest current distance.
- Relaxation: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] keeps node 3 at 7 through 0-1-3 after comparing it with the cost-14 route through node 2.
- Tree construction: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] marks predecessor edges in red and ends with distances 0, 2, 6, 7, 17, 22, and 19 for nodes 0 through 6.
- Historical origin: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] attributes the procedure and its 1959 publication to [[EdsgerWDijkstra]].
- Heuristic preprocessing: [[red-blob-games-improving-heuristics-for-a-star-search]] runs Dijkstra once per landmark to fill a node-by-landmark distance table; directed graphs reverse their edges when the needed values are distances to each landmark.

## Counterevidence & Qualifications
The sources are pedagogical explanations rather than proofs or controlled performance analyses. The introductory article's statement that weights must be positive is narrower than the standard requirement: zero-weight edges are allowed, but negative edges break the greedy finalization argument. It also describes adding nodes and edges to “the path,” whereas an implementation normally distinguishes the settled set, the tentative-distance table, and the predecessor tree. Neither source analyzes disconnected nodes, priority-queue implementations, tie handling, complexity, overflow, or alternatives for negative weights. The landmark application adds preprocessing and storage whose value depends on query volume and map stability; unit-weight graphs can use breadth-first search instead.

## What Changed
- Added repeated Dijkstra runs as preprocessing for landmark-based A* guidance.
- Added the directed-graph edge-reversal requirement for computing distances to landmarks.

## Related Concepts
- [[GraphModeling]] - supplies the nodes, edges, directions, and weights over which shortest paths are computed.
- [[EdsgerWDijkstra]] - designed and published the algorithm.
- [[DifferentialHeuristic]] - reuses precomputed exact landmark distances as graph-aware lower bounds.
- [[AStarSearch]] - consumes those lower bounds to prioritize goal-directed search.

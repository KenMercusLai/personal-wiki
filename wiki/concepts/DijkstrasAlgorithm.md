---
title: "Dijkstra's Algorithm"
type: concept
tags: [algorithms, graph-theory, shortest-paths]
sources:
  - freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[DijkstrasAlgorithm]] is a greedy single-source shortest-path algorithm for weighted graphs whose edge weights are non-negative.

## Current Synthesis
The algorithm maintains tentative distances from a chosen source, initially zero for the source and infinity elsewhere. It repeatedly selects the unsettled node with the smallest tentative distance, treats that distance as final, and relaxes each outgoing edge by comparing the neighbor's current distance with the cost of reaching it through the selected node. Recording the predecessor that produced each improvement yields a shortest-path tree as well as the distances. The visual source demonstrates the invariant on an undirected seven-node graph: once node 3 has distance 7 through 0-1-3, the alternative cost 14 through 0-2-3 cannot improve it.

## Key Claims
- The algorithm solves the single-source shortest-path problem for every reachable node in a non-negatively weighted graph.
- Tentative distances represent the best routes found so far, not final answers until their nodes are settled.
- Each relaxation replaces a neighbor's tentative distance only when the route through the current node is cheaper.
- Choosing the smallest unsettled tentative distance is safe because non-negative later edges cannot create a cheaper route back to that node.
- Predecessor links from successful relaxations form a shortest-path tree rooted at the source.

## Evidence
- Initialization and selection: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] initializes node 0 to 0, all others to infinity, and settles nodes by the smallest current distance.
- Relaxation: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] keeps node 3 at 7 through 0-1-3 after comparing it with the cost-14 route through node 2.
- Tree construction: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] marks predecessor edges in red and ends with distances 0, 2, 6, 7, 17, 22, and 19 for nodes 0 through 6.
- Historical origin: [[freecodecamp-dijkstras-shortest-path-algorithm-a-detailed-and-visual-introduction]] attributes the procedure and its 1959 publication to [[EdsgerWDijkstra]].

## Counterevidence & Qualifications
The source is a pedagogical walkthrough rather than a proof or performance analysis. Its statement that weights must be positive is narrower than the standard requirement: zero-weight edges are allowed, but negative edges break the greedy finalization argument. The walkthrough also describes adding nodes and edges to “the path,” whereas an implementation normally distinguishes the settled set, the tentative-distance table, and the predecessor tree. It does not discuss disconnected nodes, directed examples, priority-queue implementations, tie handling, complexity, overflow, or alternative algorithms for negative weights.

## What Changed
- Created the concept from a visual walkthrough of initialization, greedy selection, relaxation, and predecessor-tree construction.
- Corrected the source's positive-weight requirement to the standard non-negative-weight boundary.
- Distinguished tentative distances, settled nodes, and predecessor edges rather than treating them as one path.

## Related Concepts
- [[GraphModeling]] - supplies the nodes, edges, directions, and weights over which shortest paths are computed.
- [[EdsgerWDijkstra]] - designed and published the algorithm.

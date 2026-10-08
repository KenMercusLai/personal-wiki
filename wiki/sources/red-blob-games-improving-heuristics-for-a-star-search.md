---
title: "Red Blob Games: Improving heuristics for A* search"
type: source
tags: [algorithms, pathfinding, graph-theory, game-development]
date: 2026-07-01
source_file: "/mnt/ken_personal_wiki/Articles/Red Blob Games- Improving heuristics for A* search.md"
---

## Summary
[[RedBlobGames]] explains how landmark distance tables can make [[AStarSearch]] more informed about map structure without changing the search algorithm itself. The resulting [[DifferentialHeuristic]] uses triangle-inequality lower bounds from several precomputed landmarks, taking their maximum together with a conventional geometric heuristic. The technique can substantially reduce explored nodes on obstructed maps, but its benefit depends on landmark placement and costs memory proportional to landmarks times graph nodes.

## Key Claims
- A geometric A* heuristic can point search away from the true route because it represents coordinate distance but not walls, corridors, or other graph structure.
- A perfect distance-to-goal heuristic is impractical to recompute or store for every possible goal, but exact distances to a small reusable landmark set can provide admissible lower bounds for many goals.
- For a landmark `L`, triangle inequality yields a lower bound based on the difference between precomputed distances from the current node and goal to `L`; on undirected graphs, the absolute difference can be used.
- Taking the maximum bound across multiple landmarks and the existing geometric heuristic preserves the strongest available lower bound while extending coverage beyond what one landmark can provide.
- Landmark selection is workload-specific: useful positions depend on likely start-goal pairs, expensive routes, map topology, common destinations, and whether edge costs change.
- Preprocessing runs [[DijkstrasAlgorithm]] once per landmark, or breadth-first search for unit weights; directed graphs require reverse edges when computing costs to a landmark.
- Dynamic maps create asymmetric staleness: a decreased edge cost can make an old heuristic overestimate and produce a non-shortest route, whereas an increased edge cost leaves the heuristic admissible but weaker until refreshed.
- The implementation changes only the heuristic function, but adds storage of roughly `landmarks × nodes × number size`.

## Key Quotes
> "The change described on this page is to the heuristic function given to A*. We don’t need to change A* itself." — implementation boundary

> "Picking the number and placement of landmarks is project-specific." — qualification on optimization design

## Connections
- [[AStarSearch]] — graph-search algorithm whose guidance is improved without changing its core search procedure.
- [[DifferentialHeuristic]] — landmark-based lower bound derived from differences between precomputed exact distances.
- [[DijkstrasAlgorithm]] — preprocessing method used to compute the distance table for each landmark.
- [[GraphModeling]] — edge direction, weight, and map changes determine preprocessing and admissibility behavior.
- [[RedBlobGames]] — publisher of the interactive practitioner explanation and game-map demonstrations.

## Contradictions
- No direct contradiction with existing wiki content. The author explicitly has not used the technique in a real project, and the archived Markdown omits the interactive demos' numeric results, so the source supports the mechanism and qualitative examples but not a reproducible performance claim.

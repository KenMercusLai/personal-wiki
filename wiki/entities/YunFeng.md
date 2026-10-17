---
title: "云风"
type: entity
tags: [technical-writer, algorithms, game-development]
sources:
  - yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[YunFeng]] is the author of a technical blog article proposing landmark and flow-field guidance for A* pathfinding.

## Current Profile
In the available source, 云风 explains algorithms through spatial examples and turns precomputed shortest-path data into a practical heuristic proposal. The evidence supports this narrow authorship and technical-writing profile; it does not establish a broader biography, employment history, or production deployment record.

## Key Characteristics
- Explains pathfinding behavior through concrete rooms, walls, doors, and city-to-city navigation analogies.
- Connects triangle-inequality reasoning with reusable shortest-path preprocessing.
- Proposes an adaptive landmark cache that can retain successful destinations for later searches.

## Evidence
- Explanatory method: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] uses an eastward goal behind a wall and Beijing-to-Guangzhou travel to explain why geometric guidance can fail.
- Algorithm design: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] derives a landmark lower bound and proposes switching between cached landmark directions and geometric guidance.
- Adaptation proposal: [[yun-feng-de-blog-yong-di-biao-gai-jin-a-star-xun-lu-de-qi-fa-han-shu]] suggests promoting reached destinations into landmarks for future queries.

## Qualifications
This profile is based on one blog article. The source supplies no author biography, independent implementation, benchmark, or production-use evidence, so claims beyond the article's authorship and contents remain unsupported.

## What Changed
- Created the entity from the article's stated blog authorship and pathfinding argument.

## Relationships
- [[AStarSearch]] - subject of the author's landmark-guidance proposal.
- [[DifferentialHeuristic]] - mathematical technique used in the proposal.
- [[FlowFieldPathfinding]] - cached directional representation advocated for landmark reuse.

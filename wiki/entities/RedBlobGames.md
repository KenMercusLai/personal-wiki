---
title: "Red Blob Games"
type: entity
tags: [website, algorithms, game-development, education]
sources:
  - red-blob-games-improving-heuristics-for-a-star-search
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[RedBlobGames]] is represented here as the publisher of an interactive practitioner tutorial on improving [[AStarSearch]] with reusable landmark distances.

## Current Profile
The source presents Red Blob Games as an educational game-algorithm site that moves from geometric intuition through triangle-inequality derivation to compact implementation guidance and interactive demonstrations. Its differential-heuristic article emphasizes techniques that reuse existing shortest-path code and apply to graphs generally, even though its visual examples use grids and game maps. The page is unusually explicit about uncertainty: it separates theory and qualitative demos from production experience and states that the author has not used the method in a real project.

## Key Characteristics
- Publishes visual and interactive explanations of pathfinding algorithms.
- Connects mathematical reasoning to small implementation changes and practical resource tradeoffs.
- Uses game maps to demonstrate techniques intended for general graph structures.
- States limits in the author's reading and real-project experience rather than presenting the tutorial as production validation.

## Evidence
- Teaching format: [[red-blob-games-improving-heuristics-for-a-star-search]] organizes movable start, goal, and landmark demonstrations around a stepwise derivation of the heuristic.
- Implementation orientation: [[red-blob-games-improving-heuristics-for-a-star-search]] reduces the technique to landmark selection, distance-table preprocessing, and a modified heuristic loop.
- Generality: [[red-blob-games-improving-heuristics-for-a-star-search]] says landmarks work for any graph type, while its demonstrations use grids from games and benchmark maps.
- Epistemic boundary: [[red-blob-games-improving-heuristics-for-a-star-search]] says some cited papers have not been read and the technique has not been used by the author in a real project.

## Qualifications
This profile comes from one page and does not establish the site's ownership, full catalog, audience, publication history, or independent educational effectiveness. The archived Markdown omits the interactive graphics and live numeric outputs, so the wiki can assess the written derivation and stated design tradeoffs but not reproduce the complete experience from this source alone.

## What Changed
- Created a source-bounded profile from the differential-heuristic tutorial.

## Relationships
- [[AStarSearch]] - algorithm explained and optimized in the represented tutorial.
- [[DifferentialHeuristic]] - principal technique derived and demonstrated by the represented tutorial.
- [[DijkstrasAlgorithm]] - existing shortest-path algorithm reused for landmark preprocessing.

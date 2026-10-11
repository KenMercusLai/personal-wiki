---
title: "Topology-Aware Polygon Simplification"
type: concept
tags: [computational-geometry, gis, topology, polygons, simplification]
sources:
  - tzf-de-chun-ji-geng-xin-ringsaturn
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[TopologyAwarePolygonSimplification]] reduces polygon boundary detail while preserving shared-boundary relationships so adjacent polygons continue to meet without newly introduced gaps or overlaps.

## Current Synthesis
Simplifying each polygon independently can preserve each individual outline approximately while breaking the coverage formed by the set. Two adjacent rings may begin with the same boundary traversed in opposite directions, yet independent [[RamerDouglasPeuckerAlgorithm]] decisions can retain different vertices or produce different chords.

The tzf workflow makes adjacency explicit before reduction. It decomposes rings into directed edges, canonicalizes endpoint pairs to form an orientation-independent key, finds matching keys used in opposite directions by different rings, marks the resulting chains as shared, simplifies each shared chain once, and substitutes the same simplified geometry back into both polygons. Shared geometry can then also be stored once rather than duplicated.

## Key Claims
- Per-polygon geometric fidelity does not guarantee topology across a polygon coverage.
- A shared boundary is evidenced by the same canonical edge appearing in opposite directions in different rings.
- A common vertex alone is not enough to establish a shared boundary chain.
- Simplifying one shared representation and reusing it on both sides prevents the two sides from diverging independently.
- Shared-boundary recognition also enables storage deduplication and common polyline encoding.
- Extra rules that retain small details can make simplified data slightly larger before deduplication, illustrating that topology, precision, and size are separate objectives.

## Evidence
- Failure mode: [[tzf-de-chun-ji-geng-xin-ringsaturn]] includes a map where independently simplified red and green boundaries diverge near the Berlin/Zurich time-zone border.
- Recognition workflow: [[tzf-de-chun-ji-geng-xin-ringsaturn]] diagrams ring collection, edge indexing, reverse-direction matching, and shared-edge marking.
- Correctness mechanism: [[tzf-de-chun-ji-geng-xin-ringsaturn]] says the simplified common boundary is substituted back into both neighboring polygons.
- Storage effect: [[tzf-de-chun-ji-geng-xin-ringsaturn]] reports one-time shared-boundary storage plus polyline encoding as part of the reduction from roughly 90 MB to 17 MB for full precision.

## Counterevidence & Qualifications
The source is an implementation retrospective, not a formal proof or independent evaluation. It does not fully specify tolerance selection, floating-point normalization, invalid input repair, holes, antimeridian and polar behavior, non-manifold edges, multi-way boundaries, or how simplification avoids self-intersection. The illustrated edge-key rule explains the recognition core but not every production edge case. Smaller files do not imply smaller runtime memory, and preserving shared seams does not prove that every individual polygon remains valid or sufficiently accurate.

## What Changed
- Added polygon-set topology as a distinct correctness requirement beyond single-line shape preservation.

## Related Concepts
- [[RamerDouglasPeuckerAlgorithm]] - supplies geometric simplification but not shared-boundary consistency by itself.
- [[TrajectorySimplification]] - single-path reduction has different invariants from polygon-cover simplification.
- [[PointInPolygonIndexing]] - consumes the resulting polygons for fast coordinate lookup.
- [[Tzf]] - project applying the workflow to time-zone boundaries.

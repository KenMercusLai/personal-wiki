---
title: "Point-in-Polygon Indexing"
type: concept
tags: [computational-geometry, gis, spatial-index, performance]
sources:
  - tzf-de-chun-ji-geng-xin-ringsaturn
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[PointInPolygonIndexing]] precomputes structure that reduces the polygons or boundary segments examined when determining which region contains a coordinate.

## Current Synthesis
The tzf account separates two indexing scopes. Its adapted YStripes index reduces segment traversal inside an individual point-in-polygon test. GridIndex addresses the outer search: it divides the world into 360×180 one-degree cells, records which time-zone bounding boxes intersect each cell, and embeds that map in the distributed data file.

At query time, cell lookup is constant-time at the index level and usually reduces about 444 time zones to one to three candidates before exact geometry testing. A non-extreme cell with one candidate can sometimes skip the exact test; missing GridIndex data falls back to a full scan without changing the API. The resulting speed is therefore a composition of candidate generation, possible short-circuiting, exact point-in-polygon work, data precision, and memory residency.

## Key Claims
- Indexes can reduce work at both the candidate-polygon level and the within-polygon segment level.
- A fixed one-degree global grid converts a broad time-zone scan into a small cell-specific candidate set.
- Bounding-box intersection is a prefilter; multiple candidates still require exact point-in-polygon evaluation.
- A single safe candidate can enable a short-circuit, subject to geographic edge conditions.
- Embedding the index with the data makes lookup transparent to callers and enables version-compatible fallback.
- The source's speed gains come with additional memory and should be evaluated against workload, precision, and architecture.

## Evidence
- Layer distinction: [[tzf-de-chun-ji-geng-xin-ringsaturn]] says YStripes optimizes line traversal within PIP while GridIndex targets the fallback scan across time zones.
- Grid construction: [[tzf-de-chun-ji-geng-xin-ringsaturn]] describes 64,800 one-degree cells populated by intersections with time-zone bounding boxes.
- Candidate reduction: [[tzf-de-chun-ji-geng-xin-ringsaturn]] reports that cells usually narrow roughly 444 time zones to one to three candidates.
- Measured effect: [[tzf-de-chun-ji-geng-xin-ringsaturn]] reports 2.0–3.9× GridIndex improvement across four M3 Max fallback benchmarks and a substantial YStripes speed-memory tradeoff in Rust.

## Counterevidence & Qualifications
The source does not explain YStripes in enough detail to reconstruct or formally analyze it, instead referring readers to the upstream tg documentation. The GridIndex figures are first-party local microbenchmarks on one machine, omit build cost and index size, and do not provide distributions across cells, coastlines, poles, the antimeridian, or adversarial boundaries. O(1) cell lookup does not make total lookup O(1) when exact tests and candidate counts vary. The continuous charts show large step changes without attributing them to particular releases, and the retained FuzzyFinder layer means the simplest final architecture remains unsettled.

## What Changed
- Added the two-scope model of candidate filtering plus within-polygon segment acceleration.

## Related Concepts
- [[TopologyAwarePolygonSimplification]] - prepares consistent polygon data for indexed lookup.
- [[Tzf]] - project implementing YStripes and GridIndex for time-zone queries.
- [[DigitalCartography]] - broader context for geographic data and coordinate-based services.
- [[MapTrajectoryRendering]] - another geospatial workload where representation and query cost depend on geometry volume.

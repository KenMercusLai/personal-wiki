---
title: "tzf"
type: entity
tags: [project, geospatial, timezone, go, rust]
sources:
  - tzf-de-chun-ji-geng-xin-ringsaturn
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[Tzf]] is a family of Go, Rust, Python, and Swift projects for mapping geographic coordinates to time-zone names with local polygon data.

## Current Profile
The 2026 source presents tzf as a high-concurrency backend-oriented system that accepts memory residency in exchange for low lookup latency and useful boundary precision. Its data pipeline now recognizes shared polygon boundaries before simplification, stores shared geometry once with polyline encoding, and distributes the resulting data for reuse across language implementations.

Lookup acceleration is layered. YStripes reduces segment work within point-in-polygon tests, while a 1°×1° GridIndex narrows fallback candidates from the full set of roughly 444 time zones to usually one to three. Existing preindex-based FuzzyFinder behavior remains for compatibility while the maintainer evaluates whether a later architecture can simplify the stack.

## Key Characteristics
- Provides offline coordinate-to-time-zone lookup in multiple language implementations.
- Generates shared data through Go and reuses the results across Go, Rust, Python, and Swift.
- Uses [[TopologyAwarePolygonSimplification]] to keep neighboring simplified polygons consistent.
- Uses shared-boundary deduplication and polyline encoding to reduce distribution size.
- Uses [[PointInPolygonIndexing]] to exchange additional memory for lower lookup latency.
- Preserves old-data compatibility by falling back to a full scan when GridIndex is absent.

## Evidence
- Data pipeline: [[tzf-de-chun-ji-geng-xin-ringsaturn]] describes shared-edge recognition, one-time simplification, boundary deduplication, and polyline encoding.
- Distribution size: [[tzf-de-chun-ji-geng-xin-ringsaturn]] reports about 17 MB for full precision, 5.4 MB for topology-simplified data, and 2 MB for the fuzzy preindex.
- Lookup design: [[tzf-de-chun-ji-geng-xin-ringsaturn]] distinguishes YStripes segment traversal from GridIndex candidate reduction and reports compatible fallback for old files.
- Cross-language delivery: [[tzf-de-chun-ji-geng-xin-ringsaturn]] lists Go, Rust, Python, and Swift releases while noting that tzfpy's GridIndex publication still depends on a later dataset update.

## Qualifications
The profile rests on one maintainer-authored release retrospective. Its benchmarks use an Apple M3 Max and are intended for relative comparison, not cross-machine prediction; the continuous charts do not annotate the commits responsible for level shifts. Runtime memory remains material—roughly 100 MB for simplified data and around 500 MB for full precision by the author's broad description—and full-precision support is not planned for Python. The source does not provide correctness tests, competitor comparisons, production latency distributions, build times, or independent reproduction.

## What Changed
- Created the project profile around topology-safe data generation, compact distribution, and layered lookup indexes.

## Relationships
- [[Ringsaturn]] - maintainer and author of the 2026 update.
- [[TopologyAwarePolygonSimplification]] - preserves common boundaries during simplification.
- [[PointInPolygonIndexing]] - accelerates polygon tests and time-zone candidate selection.
- [[RamerDouglasPeuckerAlgorithm]] - base simplifier whose independent use created the original topology defect.

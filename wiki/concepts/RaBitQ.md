---
title: "RaBitQ"
type: concept
tags: [vector-quantization, approximate-nearest-neighbor-search, inner-products]
sources:
  - 2604.19528
  - "2411.12229"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[RaBitQ]] is a random-rotation vector-quantization method that maps rescaled coordinates to a shifted uniform integer grid and supports direct inner-product estimation from compressed codes.

## Current Synthesis
After normalization and shared random rotation, RaBitQ selects a rescaling factor and rounds each coordinate to one of `2^B` shifted integer-grid values. The stored code consists of `B` unsigned bits per coordinate plus one precomputed scalar that incorporates norm and angular correction for unbiased estimation, or a different scalar for reconstruction-oriented use.

The regular grid lets estimation use native integer arithmetic without codebook lookup. Its bit planes can also be accessed incrementally, producing a coarse estimate from the most significant bit before reading the remainder. The source claims a sub-Gaussian error tail with asymptotically optimal dependence on failure probability and reports stronger accuracy, recall, and same-hardware quantization speed than TurboQuant in most tested settings.

In [[SymphonyQG]], RaBitQ is adapted from IVF clusters to graph neighborhoods. Each neighbor is normalized around the current vertex, so one vector can have different codes at different adjacency lists. A decomposition moves center-dependent work into precomputed factors and lets the query-dependent FastScan table be shared across centers. Multiple independent center-relative estimates guide traversal, while exact distances are computed as vertices are visited.

## Key Claims
- RaBitQ combines random rotation, per-vector or shared rescaling, and a shifted uniform codebook.
- One scalar changes the same coordinate code from reconstruction-oriented scaling to unbiased inner-product estimation.
- Inner products can be estimated directly from unsigned codes without decoding through a centroid table.
- Bit-plane structure supports incremental estimates that trade code access for accuracy.
- The cited theory claims optimal `log log(1/delta)` bit-width dependence for probabilistic inner-product error.
- In the note's experiments, RaBitQ usually has tighter error, higher ANN recall, faster matched-hardware quantization, and better 2.5-bit KV-cache quality than TurboQuant.
- Center-relative RaBitQ codes can guide graph traversal with one reusable FastScan table, but duplicating codes for every adjacency consumes memory proportional to dimension times out-degree.

## Evidence
Representation and estimator:
- [[2604.19528]] derives the shifted-grid code, stored correction scalar, direct dot-product expression, and reconstruction alternative.

Theory:
- [[2604.19528]] attributes a sub-Gaussian tail and the Alon–Klartag-optimal space-distortion tradeoff to the multi-bit RaBitQ analysis.

Empirical comparison:
- [[2604.19528]] reports lower unbiased-estimator spread above one bit, higher Recall@1@k across three datasets, and lower GPU quantization time across three dimensions.
- [[2604.19528]] reports Needle-In-A-Haystack scores of 0.951 and 0.977 at 2.5 and 3.5 bits, close to the 0.987 full-precision score.

Graph integration:
- [[2411.12229]] derives center-independent lookup-table reuse, stores one-bit neighbor codes in 32-code batches, and reports that multiple estimates improve QPS-recall on every tested moderate-scale dataset.
- [[2411.12229]] reports more robust recall than PQ-based NGT-QG on MSong and ImageNet, but at a substantial duplicated-code memory cost.

## Counterevidence & Qualifications
Both sources include RaBitQ's authors. The fastest comparison results enable alternative rescaling and FWHT rotation, so they are not an unchanged one-variable comparison with every TurboQuant setup. The SymphonyQG evidence adds a complete graph index but is limited to CPU, in-memory Euclidean and cosine workloads, and a memory-heavy duplicated layout. The evidence does not establish RaBitQ superiority across all reconstruction workloads, hardware, models, bit allocations, metrics, or index families.

## What Changed
- Created the method page with its uniform-grid code, scaling choices, estimator, and incremental-access property.
- Recorded the claimed optimal tail guarantee and the interested-party status of the comparison.
- Added task-level evidence from ANN and KV-cache experiments.
- Added graph-neighborhood normalization, reusable FastScan tables, multiple estimates, and duplicated-code costs.

## Related Concepts
- [[VectorQuantization]] - broader compression family to which RaBitQ belongs.
- [[TurboQuant]] - closely related random-rotation method used as the primary comparison.
- [[ApproximateNearestNeighborSearch]] - original application for RaBitQ similarity estimates.
- [[KVCacheCompression]] - application tested with outlier-aware low-bit key-cache allocation.
- [[VectorDatabase]] - system context where compact vector codes reduce memory and similarity cost.
- [[SymphonyQG]] - graph index adapting RaBitQ to center-relative adjacency codes and batched traversal.

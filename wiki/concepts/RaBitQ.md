---
title: "RaBitQ"
type: concept
tags: [vector-quantization, approximate-nearest-neighbor-search, inner-products]
sources:
  - 2604.19528
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[RaBitQ]] is a random-rotation vector-quantization method that maps rescaled coordinates to a shifted uniform integer grid and supports direct inner-product estimation from compressed codes.

## Current Synthesis
After normalization and shared random rotation, RaBitQ selects a rescaling factor and rounds each coordinate to one of `2^B` shifted integer-grid values. The stored code consists of `B` unsigned bits per coordinate plus one precomputed scalar that incorporates norm and angular correction for unbiased estimation, or a different scalar for reconstruction-oriented use.

The regular grid lets estimation use native integer arithmetic without codebook lookup. Its bit planes can also be accessed incrementally, producing a coarse estimate from the most significant bit before reading the remainder. The source claims a sub-Gaussian error tail with asymptotically optimal dependence on failure probability and reports stronger accuracy, recall, and same-hardware quantization speed than TurboQuant in most tested settings.

## Key Claims
- RaBitQ combines random rotation, per-vector or shared rescaling, and a shifted uniform codebook.
- One scalar changes the same coordinate code from reconstruction-oriented scaling to unbiased inner-product estimation.
- Inner products can be estimated directly from unsigned codes without decoding through a centroid table.
- Bit-plane structure supports incremental estimates that trade code access for accuracy.
- The cited theory claims optimal `log log(1/delta)` bit-width dependence for probabilistic inner-product error.
- In the note's experiments, RaBitQ usually has tighter error, higher ANN recall, faster matched-hardware quantization, and better 2.5-bit KV-cache quality than TurboQuant.

## Evidence
Representation and estimator:
- [[2604.19528]] derives the shifted-grid code, stored correction scalar, direct dot-product expression, and reconstruction alternative.

Theory:
- [[2604.19528]] attributes a sub-Gaussian tail and the Alon–Klartag-optimal space-distortion tradeoff to the multi-bit RaBitQ analysis.

Empirical comparison:
- [[2604.19528]] reports lower unbiased-estimator spread above one bit, higher Recall@1@k across three datasets, and lower GPU quantization time across three dimensions.
- [[2604.19528]] reports Needle-In-A-Haystack scores of 0.951 and 0.977 at 2.5 and 3.5 bits, close to the 0.987 full-precision score.

## Counterevidence & Qualifications
The evidence inventory is currently dominated by a note written by RaBitQ authors in direct response to TurboQuant. The fastest RaBitQ results enable alternative rescaling and FWHT rotation, so they are not an unchanged one-variable comparison with every TurboQuant setup. The note does not benchmark optimized inner-product estimation against TurboQuant because TurboQuant released no comparable optimized path, and it does not establish RaBitQ superiority across all reconstruction workloads, hardware, models, or bit allocations.

## What Changed
- Created the method page with its uniform-grid code, scaling choices, estimator, and incremental-access property.
- Recorded the claimed optimal tail guarantee and the interested-party status of the comparison.
- Added task-level evidence from ANN and KV-cache experiments.

## Related Concepts
- [[VectorQuantization]] - broader compression family to which RaBitQ belongs.
- [[TurboQuant]] - closely related random-rotation method used as the primary comparison.
- [[ApproximateNearestNeighborSearch]] - original application for RaBitQ similarity estimates.
- [[KVCacheCompression]] - application tested with outlier-aware low-bit key-cache allocation.
- [[VectorDatabase]] - system context where compact vector codes reduce memory and similarity cost.

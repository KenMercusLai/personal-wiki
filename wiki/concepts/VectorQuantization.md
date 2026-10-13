---
title: "Vector Quantization"
type: concept
tags: [machine-learning, compression, vector-search, numerical-computing]
sources:
  - 2604.19528
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[VectorQuantization]] maps a high-dimensional vector to a compact code intended to preserve reconstruction quality, inner products, distances, or another downstream geometric quantity.

## Current Synthesis
The source separates quantization into an encoding stage and an estimation stage. Encoding may normalize and rotate a vector, map coordinates to codebook entries, and retain a small number of scales or norms. Estimation then reconstructs a vector or computes a downstream quantity directly from the code. Equal nominal bits per coordinate do not imply equal codes, metadata, decoding work, theoretical guarantees, or task performance.

[[RaBitQ]] and [[TurboQuant]] illustrate objective-dependent design. Both exploit the coordinate distribution induced by random rotation, but RaBitQ uses a rescaled uniform grid and direct arithmetic while TurboQuant uses a non-uniform centroid codebook and, for unbiased inner products, a separate signed residual sketch. Reconstruction MSE, estimator bias, tail error, quantization time, estimation time, and retrieval recall are therefore complementary rather than interchangeable evaluation axes.

## Key Claims
- A vector code must be evaluated against the geometric quantity and downstream task it is intended to preserve.
- Random rotation can make coordinate distributions more regular, enabling scalar codebooks while preserving inner products under a shared transform.
- Nominal bits per dimension omit scalar metadata, codebook access, decoding, rotation, residual correction, and hardware execution costs.
- An unbiased mean error does not determine variance, worst observed error, tail probability, nearest-neighbor recall, or attention quality.
- Reproducible comparison requires matched hardware, parallelism, preprocessing, variants, datasets, metrics, and released executable paths.

## Evidence
Method decomposition:
- [[2604.19528]] describes both methods through common preprocessing, codebook construction, quantization code, estimation path, and theoretical guarantee.

Objective dependence:
- [[2604.19528]] finds that unbiased variants are centered near zero, while reconstruction-oriented variants can be biased; it also reports TurboQuant's reconstruction variant outperforming its unbiased variant on nearest-neighbor recall.

System and task evaluation:
- [[2604.19528]] compares quantization time, error distributions, Recall@1@k, Needle-In-A-Haystack retrieval, and LongBench-E rather than treating reconstruction error as a complete proxy.

## Counterevidence & Qualifications
The framework comes from one contested comparison written by RaBitQ authors. Its experiments cover selected bit widths, datasets, implementations, hardware, and two application families; they do not establish a universal ranking across quantizers. Randomized rotations, metadata accounting, optimized kernels, reconstruction objectives, and integration-specific outlier handling can all change results.

## What Changed
- Created a task- and system-aware model of vector quantization from the RaBitQ–TurboQuant comparison.
- Distinguished nominal code width from metadata, decoding, preprocessing, and hardware costs.
- Separated unbiasedness and reconstruction error from tail behavior and downstream task quality.

## Related Concepts
- [[RaBitQ]] - uniform-grid vector quantizer designed for direct inner-product estimation.
- [[TurboQuant]] - non-uniform scalar quantizer with an optional residual sketch for unbiased estimation.
- [[ApproximateNearestNeighborSearch]] - uses compressed similarity estimates to rank candidates.
- [[KVCacheCompression]] - applies low-bit vector representations to attention state.
- [[BlockQuantization]] - shares scales over groups of tensor values rather than using only per-coordinate codebooks.
- [[QuantizationAwareTraining]] - adapts learned parameters to quantization effects during training.

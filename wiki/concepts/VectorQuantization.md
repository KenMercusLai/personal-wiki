---
title: "Vector Quantization"
type: concept
tags: [machine-learning, compression, vector-search, numerical-computing]
sources:
  - 2604.19528
  - p3049-ooi
  - "2411.12229"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[VectorQuantization]] maps a high-dimensional vector to a compact code intended to preserve reconstruction quality, inner products, distances, or another downstream geometric quantity.

## Current Synthesis
The source separates quantization into an encoding stage and an estimation stage. Encoding may normalize and rotate a vector, map coordinates to codebook entries, and retain a small number of scales or norms. Estimation then reconstructs a vector or computes a downstream quantity directly from the code. Equal nominal bits per coordinate do not imply equal codes, metadata, decoding work, theoretical guarantees, or task performance.

[[RaBitQ]] and [[TurboQuant]] illustrate objective-dependent design. Both exploit the coordinate distribution induced by random rotation, but RaBitQ uses a rescaled uniform grid and direct arithmetic while TurboQuant uses a non-uniform centroid codebook and, for unbiased inner products, a separate signed residual sketch. Reconstruction MSE, estimator bias, tail error, quantization time, estimation time, and retrieval recall are therefore complementary rather than interchangeable evaluation axes.

In a filter-and-refine objective, compressed codes only nominate candidates and full vectors determine the final ranking, so a learned 4-bit product quantizer need not reproduce every vector or score accurately. [[HAKESIndex]] instead preserves local similarity-score distributions among approximate neighbors. Fixed original code assignments plus separately learned search centroids also show that encoding and query-time interpretation can evolve independently, provided the training procedure explicitly preserves that contract.

[[SymphonyQG]] makes coding context-dependent: the same vector receives different RaBitQ codes when stored beside different graph vertices because each neighborhood uses its current vertex as the normalization center. That duplication improves locality and lets FastScan evaluate 32 neighbors together. Algebraic decomposition reuses one query lookup table across centers, and exact scoring on vertex visits removes final reranking, but memory grows with both vector dimension and graph out-degree.

## Key Claims
- A vector code must be evaluated against the geometric quantity and downstream task it is intended to preserve.
- Random rotation can make coordinate distributions more regular, enabling scalar codebooks while preserving inner products under a shared transform.
- An unbiased mean error does not determine variance, worst observed error, tail probability, nearest-neighbor recall, or attention quality.
- In filter-and-refine retrieval, candidate inclusion can matter more than globally accurate reconstruction or score estimation.
- Separating code assignment from query-time code interpretation can avoid bulk re-encoding, but only when training is consistent with the fixed assignments.
- Reproducible comparison requires matched hardware, parallelism, preprocessing, variants, datasets, metrics, and released executable paths.
- Quantization layout can deliberately duplicate context-specific codes to replace random vector reads with sequential SIMD batches, exchanging memory for query throughput.

## Evidence
Method decomposition:
- [[2604.19528]] describes both methods through common preprocessing, codebook construction, quantization code, estimation path, and theoretical guarantee.

Objective dependence:
- [[2604.19528]] finds that unbiased variants are centered near zero, while reconstruction-oriented variants can be biased; it also reports TurboQuant's reconstruction variant outperforming its unbiased variant on nearest-neighbor recall.

System and task evaluation:
- [[2604.19528]] compares quantization time, error distributions, Recall@1@k, Needle-In-A-Haystack retrieval, and LongBench-E rather than treating reconstruction error as a complete proxy.
- [[p3049-ooi]] combines 4-bit PQ with dimensionality reduction and exact reranking, then reports a leading high-recall throughput frontier on five one-million-scale embedding datasets.

Learned filter-stage compression:
- [[p3049-ooi]] jointly tunes dimensionality reduction and PQ centroids against local similarity-distribution mismatch and reports consistent recall improvement at fixed search parameters on two ten-million-scale datasets.
- [[p3049-ooi]] shows recall degrading when learned search parameters replace original insert parameters, grounding the need to keep code assignment and search interpretation separate.

Graph-local coding:
- [[2411.12229]] stores center-relative one-bit codes for every edge, derives reusable FastScan tables, and reports better recall-throughput than PQ-based NGT-QG, including datasets where NGT-QG fails or degrades.
- [[2411.12229]] derives a duplicated-code overhead of `DR` bits per vertex, equal to one or two raw-vector copies when out-degree is 32 or 64.

## Counterevidence & Qualifications
The RaBitQ–TurboQuant framework comes from one contested comparison written by RaBitQ authors. HAKES and SymphonyQG are also first-party evaluations. HAKES assumes a two-stage index with full vectors available for refinement, while SymphonyQG's context-specific duplication is practical only when enough memory is available. Across the sources, selected bit widths, datasets, implementations, hardware, rotations, metadata accounting, graph structure, optimized kernels, reconstruction objectives, and integration-specific handling can change results.

## What Changed
- Added candidate inclusion as a quantization objective for filter-and-refine retrieval.
- Added joint dimensionality-reduction and PQ learning against local similarity distributions.
- Added the fixed-assignment constraint behind changing search-time code interpretation without re-encoding.
- Added context-relative duplicated codes and memory-layout co-design for SIMD graph traversal.

## Related Concepts
- [[RaBitQ]] - uniform-grid vector quantizer designed for direct inner-product estimation.
- [[TurboQuant]] - non-uniform scalar quantizer with an optional residual sketch for unbiased estimation.
- [[ApproximateNearestNeighborSearch]] - uses compressed similarity estimates to rank candidates.
- [[KVCacheCompression]] - applies low-bit vector representations to attention state.
- [[BlockQuantization]] - shares scales over groups of tensor values rather than using only per-coordinate codebooks.
- [[QuantizationAwareTraining]] - adapts learned parameters to quantization effects during training.
- [[HAKESIndex]] - uses learned product quantization as an aggressive candidate filter before exact refinement.
- [[HAKES]] - turns compressed filtering into a separately scalable distributed service layer.
- [[SymphonyQG]] - duplicates center-relative codes to integrate quantization with graph traversal and layout.

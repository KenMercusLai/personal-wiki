---
title: "HAKES Index"
type: concept
tags: [vector-search, approximate-nearest-neighbor-search, vector-quantization]
sources:
  - p3049-ooi
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[HAKESIndex]] is a two-stage [[ApproximateNearestNeighborSearch]] index that filters with aggressively compressed IVF/PQ representations and refines selected candidates against full-precision vectors.

## Current Synthesis
The index puts dimensionality reduction before IVF partition selection and 4-bit product quantization so most search work occurs on small representations. Rather than optimizing global reconstruction error, it self-supervises on approximate neighbors and jointly tunes the query transform and PQ centroids to preserve local similarity-score distributions. Exact comparison of the resulting candidate set supplies the final TopK.

Its unusual update mechanism keeps initialized insert parameters separate from learned search parameters. Stored code assignments remain anchored to the initialized codebook, while learned centroids reinterpret those fixed codes during search. New vectors can therefore use the original assignment path and newly learned search parameters can be installed without rewriting all stored codes.

## Key Claims
- Filter-and-refine permits much more aggressive compression than a compressed index expected to return final rankings directly.
- Preserving local similarity-score distributions can improve candidate recall without ground-truth neighbors, labels, or embedding-model access.
- Separate search and insert parameters allow asynchronous retraining and low-contention append-style updates without re-indexing.
- Early termination can adapt partition-scan cost per query using candidate contribution counts rather than precise compressed similarity values.
- Partition-oriented writes avoid graph-neighborhood search and locking, improving mixed read-write throughput in the paper's tests.
- Full-vector storage still dominates memory and the index must be rebuilt after sufficiently large data growth or embedding-model change.

## Evidence
Design and training:
- [[p3049-ooi]] specifies dimensionality reduction, IVF, 4-bit PQ, exact refinement, and a KL-divergence objective over original, reduced, and quantized local similarity distributions.
- [[p3049-ooi]] reports that learned parameters improve recall across every displayed ten-million-vector search configuration without materially changing scan cost.

Updates and adaptivity:
- [[p3049-ooi]] shows stable recall under batched inserts only when initialized insert parameters remain separate from learned search parameters.
- [[p3049-ooi]] reports throughput gains from scalar-quantized IVF centroids and early termination on four of five datasets near 0.99 recall.

Comparative performance:
- [[p3049-ooi]] reports a leading throughput-recall frontier across five one-million-scale datasets and higher concurrent read-write throughput than graph and partitioning baselines.

## Counterevidence & Qualifications
The design is evaluated by its authors on normalized, in-memory vectors using inner product and selected 768-to-2,048-dimensional datasets. Early termination can miss true neighbors; moderate same-model drift is tested, but new embedding models or substantially different sources require separate indexes. The learned-search/fixed-insert technique depends on its specific fixed code-assignment training scheme and should not be generalized to arbitrary learned quantizers. Results lack independent reproduction.

## What Changed
- Created the concept from the HAKES paper.
- Distinguished local distribution preservation from reconstruction-error minimization.
- Recorded fixed insert assignments as the condition enabling search-parameter replacement without re-indexing.

## Related Concepts
- [[HAKES]] - serves the index through disaggregated filter and refine workers.
- [[ApproximateNearestNeighborSearch]] - is the search problem optimized by the index.
- [[VectorQuantization]] - supplies the compressed product codes used during filtering.
- [[IVFFlatIndex]] - shares centroid partitioning and tunable partition probing.
- [[HNSWIndex]] - offers a graph-based alternative with different update and sharding behavior.
- [[Embeddings]] - are the high-dimensional inputs compressed and searched by the index.

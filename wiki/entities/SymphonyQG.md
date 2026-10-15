---
title: "SymphonyQG"
type: entity
tags: [vector-search, graph-index, vector-quantization, open-source]
sources:
  - "2411.12229"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[SymphonyQG]] is an open-source in-memory [[ApproximateNearestNeighborSearch]] project that integrates graph traversal, [[RaBitQ]] codes, FastScan SIMD batches, and a locality-oriented data layout.

## Current Profile
The project treats its graph and quantizer as one execution design. Each vertex stores its raw vector, neighbor identifiers, and center-relative codes for those neighbors in one sequential block. Querying exactly scores each visited vertex while using batch estimates to decide which vertices to visit, eliminating a separate reranking pass.

Indexing begins with a random graph, repeatedly searches that graph for candidate neighbors using the same accelerated query path, applies NSG-style pruning, and supplements edges until each vertex's degree matches a FastScan batch. The source reports leading throughput-recall results and much faster construction than NGT-QG, but the replicated codes make its index substantially larger than conventional graph indexes.

## Key Characteristics
- Uses one-bit-per-dimension RaBitQ neighbor codes and 32-vector FastScan batches.
- Co-locates raw vectors, neighbor codes, graph edges, and estimator metadata for sequential access.
- Interleaves exact scoring with traversal as implicit reranking and retains multiple center-relative estimates.
- Builds graphs iteratively with accelerated candidate search and SIMD-aligned out-degrees.
- Supports Euclidean distance and cosine similarity in the described implementation.

## Evidence
Query architecture:
- [[2411.12229]] describes exact scoring on vertex visits, batched neighbor estimation, multiple stored estimates, prefetching, AVX-512 operations, and fast Hadamard rotation.

Index architecture:
- [[2411.12229]] gives the iterative construction algorithm and an adaptive angle-pruning rule that fills every target out-degree.

Reported performance:
- [[2411.12229]] reports 1.5–4.5× the strongest baseline's QPS at 95% Recall@10 across six moderate datasets, at least 2.5× the strongest baseline on two 100-million-vector datasets, and at least 8× faster indexing than NGT-QG.

Resource profile:
- [[2411.12229]] derives `n(32D + 32R + DR)` bits of storage and reports a clear memory premium over OG-LVQ, Glass-NSG, and HNSWlib.

## Qualifications
The only evidence is the authors' tuned CPU evaluation. The method is restricted to in-memory Euclidean and cosine search, duplicates a neighbor's code separately for each graph center, and leaves disk residence, distributed serving, dynamic updates, inner-product search, and memory reduction unevaluated.

## What Changed
- Established the project's co-designed query, layout, and graph-construction profile.
- Recorded the reported throughput, construction-time, scalability, and memory trade-offs.

## Relationships
- [[ApproximateNearestNeighborSearch]] - retrieval problem the project implements.
- [[RaBitQ]] - quantizer supplying compact, error-bounded neighbor estimates.
- [[VectorQuantization]] - compression family used to reduce exact distance work.
- [[HNSWIndex]] - conventional graph ANN baseline in the evaluation.
- [[VectorDatabase]] - system category that can use the project's in-memory index.

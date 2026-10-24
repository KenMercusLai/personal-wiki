---
title: "ANN v3"
type: entity
tags: [vector-search, approximate-nearest-neighbor-search, distributed-systems]
sources:
  - ann-v3
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[ANNv3]] is [[Turbopuffer]]'s vector-search implementation for a single logical index distributed across storage-dense machines.

## Current Profile
ANN v3 extends a SPFresh-derived centroid index into a roughly 100-way hierarchy. Queries navigate compressed centroids, scan promising one-bit leaf codes, retain every candidate whose [[RaBitQ]] error range could overlap the true top-k, fetch the corresponding full-precision vectors from local NVMe, and rerank exactly.

The placement follows access frequency and representation size: quantized upper levels fit in shared L3 cache, quantized leaves occupy DRAM, full-precision vectors stay on SSD, and durable data remains in object storage. A large index is randomly sharded; queries fan out to every shard and merge partial top-k results. This makes shard addition capacity-scalable but increases query work linearly.

## Key Characteristics
- Wide, shallow hierarchical centroid index derived from SPFresh.
- One-bit RaBitQ filtering followed by full-precision reranking.
- Tier-aware placement across L3, DRAM, NVMe, and object storage.
- Highly concurrent scatter-gather reads for the small rerank set.
- Random sharding with broadcast queries and global top-k merge.
- AVX-512 popcount optimization after compression shifts the bottleneck to compute.

## Evidence
Index and representation:
- [[ann-v3]] gives the 100-way hierarchy, 500-cluster scan example, 16–32× quantization ratio, error-bound filtering, and claimed sub-1% rerank fraction.

Hardware placement and scale:
- [[ann-v3]] derives cache, DRAM, and NVMe bandwidth budgets and reports a 100-billion-vector, 1,024-dimensional, top-10, 92%-recall production trace.

## Qualifications
The only evidence is a first-party launch article. The hierarchy parameters and less-than-1% rerank fraction are workload-specific; random sharding trades simple balance for all-shard fan-out; and the displayed charts omit cluster topology, filters, updates, cost, index construction, fault behavior, and sufficient methodology for reproduction. The latency trace also contains p99 intervals above the 200 ms headline.

## What Changed
- Established the hierarchical filter-and-refine data path.
- Recorded tier placement and the bandwidth-to-compute bottleneck transition.
- Added the random-sharding scale-out and linear query-cost boundary.

## Relationships
- [[Turbopuffer]] - company operating and publishing the system.
- [[NathanVanBenschoten]] - chief architect explaining the design.
- [[SPFresh]] - centroid index used as the design basis.
- [[RaBitQ]] - quantizer enabling compact candidate evaluation with error bounds.
- [[ApproximateNearestNeighborSearch]] - problem domain and recall-latency tradeoff.
- [[ArithmeticIntensity]] - framework diagnosing its changing bottlenecks.

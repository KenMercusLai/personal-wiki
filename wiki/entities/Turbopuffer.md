---
title: "Turbopuffer"
type: entity
tags: [vector-database, search, cloud-infrastructure]
sources:
  - ann-v3
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[Turbopuffer]] is a hosted search system represented here through its first-party architecture for large-scale vector retrieval.

## Current Profile
The described query tier is stateless over object storage and combines memory, local SSD caching, and compute. For a 100-billion-vector workload, Turbopuffer sizes storage-optimized machines so the entire ANN tree is cached on local NVMe, keeps compressed upper levels in CPU cache or DRAM, and uses object storage as the durable backing layer rather than the steady-state query path.

Its [[ANNv3]] design broadcasts queries across randomly assigned shards and merges shard-local results. The source says transparent namespace sharding supports up to 256 shards and can be combined with pinning to keep each shard warm on its SSD, but gives no independently reproducible deployment, availability, update, filter, or cost evidence.

## Key Characteristics
- Stateless compute and cache tier backed by cloud object storage.
- Local memory and NVMe used as a hierarchy rather than a single undifferentiated cache.
- Hierarchical, quantized, refine-stage ANN search optimized around hardware bottlenecks.
- Random shard assignment with query fan-out and global top-k merging.
- Vendor-reported production support for a single index containing 100 billion vectors.

## Evidence
Architecture and locality:
- [[ann-v3]] describes the object-storage, SSD, DRAM, cache, and CPU-register path and explains how clustering and quantization place data across it.

Scale and serving:
- [[ann-v3]] reports a 100-billion-vector, 1,024-dimensional workload at 92% recall, with charted latency and throughput plus namespace sharding across storage-dense machines.

## Qualifications
The profile comes from one vendor launch article. The company-wide claim of hosting more than one trillion documents, handling more than ten million writes per second, and serving more than one hundred thousand queries per second is promotional and not tied to the displayed ANN benchmark. Hardware count, shard count, pricing, update behavior, filtered-search performance, durability, recovery, and independent replication are absent.

## What Changed
- Established Turbopuffer's stateless object-storage-backed query architecture.
- Recorded ANN v3's memory-hierarchy placement and random-sharding model.
- Separated the displayed 100-billion-vector benchmark from broader company-scale claims.

## Relationships
- [[ANNv3]] - Turbopuffer vector-search implementation described in the source.
- [[NathanVanBenschoten]] - chief architect and author of the technical account.
- [[ApproximateNearestNeighborSearch]] - primary retrieval workload optimized by the system.
- [[RaBitQ]] - quantizer used for compact filtering before full-precision reranking.

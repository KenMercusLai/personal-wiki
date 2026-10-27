---
title: "Turbopuffer"
type: entity
tags: [vector-database, search, cloud-infrastructure]
sources:
  - ann-v3
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Turbopuffer]] is a hosted, object-storage-backed search system represented through its large-scale ANN architecture and a practitioner analysis of its namespace, indexing, full-text, filtering, aggregation, and customer workloads.

## Current Profile
The described query tier is stateless over object storage and combines memory, local SSD caching, and compute. Inactive namespaces can remain durable without a resident per-tenant process, while routing tries to reuse nodes that already cache queried data. One relayed vendor example reports 874 ms p50 for a cold query over one million documents versus 14 ms after cache warming; these figures describe one official workload, not a general latency guarantee.

Its [[ANNv3]] design broadcasts queries across randomly assigned shards and merges shard-local results. The source says transparent namespace sharding supports up to 256 shards and can be combined with pinning to keep each shard warm on its SSD, but gives no independently reproducible deployment, availability, update, filter, or cost evidence.

Writes are described as batched into a namespace WAL in object storage before separate workers build indexes. Queries can scan committed but not-yet-indexed data to preserve recent visibility until the unindexed backlog crosses a documented bound. This decouples durability from index construction but shifts extra work to query nodes when indexing falls behind.

The product is also moving beyond a vector-first physical layout. The practitioner account says Turbopuffer's planned v3 makes ANN secondary to document storage organized for batch reads and columnar execution, after vector-address placement caused data movement and poor fit for full-text blocks, scans, sorting, and `GROUP BY`. [[Mem0]] reportedly uses customer-scoped namespaces as an index over PostgreSQL-held memories, while [[Linear]] uses sorted-ID intersections for delta sync without vector similarity. These cases support a broader query-system profile, although their behavior and measurements remain first-party or relayed customer evidence.

## Key Characteristics
- Durable namespace state in object storage with shared stateless query compute and tiered memory/NVMe caches.
- Batched WAL persistence separated from asynchronous index construction, with bounded query-time scanning of recent writes.
- Hierarchical, quantized, refine-stage ANN search plus random-shard fan-out and global top-k merging.
- Namespace isolation used to constrain customer-scoped vector retrieval and avoid global post-filtering.
- Expansion from vector search into full-text, filtering, aggregation, scans, sorting, and set-intersection workloads.

## Evidence
Architecture and locality:
- [[ann-v3]] describes the object-storage, SSD, DRAM, cache, and CPU-register path and explains how clustering and quantization place data across it.

Scale and serving:
- [[ann-v3]] reports a 100-billion-vector, 1,024-dimensional workload at 92% recall, with charted latency and throughput plus namespace sharding across storage-dense machines.

Namespace durability and cache behavior:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes durable object-storage namespaces, shared query servers, cache-aware routing, cold-query cost, and Notion's reported interaction-triggered prewarming.

Write and index lifecycle:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] relays batched object-storage WAL commits, separate index workers, recent-data query scans, and the visibility boundary when unindexed data becomes too large.

Broader query workloads:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes the vector-address-layout constraint, the move toward secondary ANN and columnar document storage, Mem0's customer namespaces, and Linear's delta-sync set intersections.

## Qualifications
The profile rests on one vendor launch article plus a practitioner synthesis of first-party documentation and customer cases. The company-wide scale claims are promotional and not tied to the displayed ANN benchmark. The cold/warm latency figures, v3 aggregation improvement, Notion prewarming, Mem0 migration, and Linear design are workload-specific reports rather than independent guarantees. Hardware and shard counts, pricing, authorization failure tests, index-lag distributions, mixed-tenant cache behavior, filtered-search recall, outage recovery, and total synchronization cost remain absent. The planned broader physical layout was still being tuned, with some full-text tests reportedly slower than the production version.

## What Changed
- Established Turbopuffer's stateless object-storage-backed query architecture.
- Recorded ANN v3's memory-hierarchy placement and random-sharding model.
- Separated the displayed 100-billion-vector benchmark from broader company-scale claims.
- Added namespace WAL, asynchronous indexing, cold-cache, and recent-write visibility behavior.
- Reframed the product trajectory from vector service toward a broader query system while preserving migration and benchmark limits.

## Relationships
- [[ANNv3]] - Turbopuffer vector-search implementation described in the source.
- [[NathanVanBenschoten]] - chief architect and author of the technical account.
- [[ApproximateNearestNeighborSearch]] - primary retrieval workload optimized by the system.
- [[RaBitQ]] - quantizer used for compact filtering before full-precision reranking.
- [[PersonalAgentRetrieval]] - sparse long-lived tenant workload for which shared compute and durable namespaces may fit.
- [[Mem0]] - reported customer using Turbopuffer as a customer-scoped retrieval index over PostgreSQL records.
- [[Linear]] - reported customer using Turbopuffer for delta-sync set intersections rather than similarity search.
- [[ObjectStorageNativeDatabase]] - neighboring architecture where remote request cost, cache granularity, and physical layout dominate design.

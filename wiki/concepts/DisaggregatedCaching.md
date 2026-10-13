---
title: "Disaggregated Caching"
type: concept
tags: [caching, cloud-analytics, distributed-systems, resource-disaggregation]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[DisaggregatedCaching]] places shared cache servers outside compute nodes so cache capacity and query compute can scale independently.

## Current Synthesis
Private caches are simple and local but duplicate data across compute nodes. Distributed caches can pool capacity across those nodes but add placement, locality, load-balancing, and consistency coordination. A disaggregated cache instead becomes its own service, enabling stateless or serverless compute and independent memory or SSD provisioning, but every hit crosses a network boundary.

That boundary makes cached data representation and execution placement inseparable. Serving compressed Parquet minimizes cache memory and CPU but can saturate the network; decoding and filtering Parquet at the cache reduces traffic but can saturate modest cache CPUs; holding Arrow avoids decode CPU but multiplies memory use. [[LiquidCache]] is one proposed point in this design space: preserve Parquet on disk, maintain a compact element-addressable memory representation, and run selective filters in an embedded engine near the cache.

## Key Claims
- Independent cache scaling can improve resource pooling and keep compute nodes stateless.
- Shared caches reduce private-cache duplication but turn cache access into network traffic.
- File serving, Parquet pushdown, and Arrow pushdown shift the bottleneck among network, CPU, and memory.
- A cache-private representation can evolve faster than a durable interoperable file format.
- Data caching supports reuse across different filters more broadly than final-result caching.
- Cache-side execution needs operator limits so joins or expensive aggregations do not consume disproportionate shared resources.

## Evidence
Architecture comparison:
- [[p5662-hao-corrected]] contrasts private, distributed, and disaggregated caches and diagrams LiquidCache between object storage and several nearby compute nodes.

Resource tradeoff:
- [[p5662-hao-corrected]] shows the Parquet file server limited by traffic, Parquet pushdown by cache CPU, and Arrow pushdown by memory across selected ClickBench queries.

Cache organization:
- [[p5662-hao-corrected]] describes SSD-cached Parquet ranges, in-memory 8,192-row Liquid column batches, column-level LRU, disk spill, and file-granularity invalidation coordinated with the catalog.

## Counterevidence & Qualifications
The source demonstrates a prototype rather than a production control plane. It does not evaluate multi-tenant fairness, admission control, consistency during concurrent catalog changes, cache-server failure, replication, security isolation, encrypted transport, autoscaling stability, or total cost. Nearby cache placement and 10 Gbps networking are environment assumptions, while serverless and stateless-compute benefits are architectural possibilities rather than measured outcomes. A private cache may still be preferable for locality, isolation, simplicity, or non-shareable workloads.

## What Changed
- Established disaggregated caching as a three-way network, cache-CPU, and cache-memory tradeoff.
- Added cache-private representation as a compatibility-preserving optimization boundary.

## Related Concepts
- [[LiquidCache]] - proposed implementation of a pushdown-enabled disaggregated cache.
- [[FilterPushdown]] - reduces traffic across the cache/compute boundary.
- [[ApacheParquet]] - compact durable and disk-cache representation used by the system.
- [[ApacheDataFusion]] - embedded engine executing cache-side work.
- [[NetworkResilienceTradeoffs]] - broader balance among shared infrastructure, capacity, and failure boundaries.

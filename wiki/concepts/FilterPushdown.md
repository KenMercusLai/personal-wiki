---
title: "Filter Pushdown"
type: concept
tags: [database-systems, query-optimization, cloud-analytics, columnar-storage]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[FilterPushdown]] evaluates predicates closer to stored data so rows that cannot affect a query are discarded before later processing or network transfer.

## Current Synthesis
In disaggregated analytics, pushdown trades network work for storage- or cache-side computation. The trade is favorable when predicates are selective and the lower layer can evaluate them cheaply, but compressed analytical formats complicate that condition: Parquet pages must be decompressed and decoded before ordinary vectorized predicates run, so decoding can dominate the useful filter work.

[[LiquidCache]] changes the representation inside the cache rather than the durable object-store format. Independently decodable elements let an earlier predicate mask restrict later filter and projection decoding; compatible equality predicates can operate on encoded dictionary values; incompatible substring or ordering operations decode only to the representation they require. This turns pushdown quality into a joint decision about selectivity, compression, encoding, operator compatibility, and network representation rather than a rule that earlier filtering is always better.

## Key Claims
- Pushdown can reduce network traffic by orders of magnitude for highly selective analytical predicates.
- Compressed input decoding can cost much more CPU than evaluating the predicate itself.
- Element-selective decoding makes an early filter mask useful below Parquet's page granularity.
- Late filter materialization reduces later decoding and comparisons as earlier predicates remove rows.
- Encoding-aware predicates can avoid materialization when the encoding preserves the required operation.
- Non-selective pushdown can be slower than transferring compressed source data because filtered output may be larger and uncompressed.

## Evidence
Cost diagnosis:
- [[p5662-hao-corrected]] reports that decoding and decompression exceed 90% of ClickBench Q22 Parquet pushdown time and that cache CPU falls from roughly 27 to 2.7 seconds with LiquidCache.

Network and selectivity:
- [[p5662-hao-corrected]] reports similar low traffic among three pushdown systems on selective ClickBench queries and orders-of-magnitude higher traffic for a Parquet file server.
- [[p5662-hao-corrected]] reports the inverse case on Q27: 99% selectivity and 31% compression make LiquidCache about three times slower than file serving.

Execution mechanisms:
- [[p5662-hao-corrected]] diagrams element-selective decoding and late materialization and reports an ablation in which each stage removes additional Q22 latency.
- [[p5662-hao-corrected]] describes equality on encoded dictionaries and partial decoding for substring or prefix operations.

## Counterevidence & Qualifications
The evidence comes from one prototype, selected ClickBench queries, and scan-heavy TPC-H queries on one hardware environment. Selectivity alone is insufficient: source compression ratio, output encoding, predicate type, projection width, cache state, CPU/network balance, object-store latency, and engine implementation all affect the decision. LiquidCache currently lacks automatic cost-based selection, and encoded evaluation applies only to predicates compatible with the active encoding. Pushing more complex operators down can also consume memory and CPU needed for the cache's primary service role.

## What Changed
- Established decoding cost as a first-class limit on pushdown, separate from predicate complexity.
- Added selective decoding, late materialization, and encoded evaluation as representation-aware mechanisms.
- Added the compression-ratio boundary for non-selective predicates.

## Related Concepts
- [[LiquidCache]] - implements filter pushdown through a cache-private representation.
- [[DisaggregatedCaching]] - introduces the cache/compute network boundary pushdown seeks to reduce.
- [[ApacheParquet]] - durable format whose page decoding constrains ordinary pushdown.
- [[ColumnarStorageTradeoffs]] - connects predicate execution to compression and access granularity.
- [[DatabaseEngineeringTradeoffs]] - frames pushdown as workload- and resource-dependent rather than universally beneficial.

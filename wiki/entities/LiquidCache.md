---
title: "LiquidCache"
type: entity
tags: [database-systems, caching, cloud-analytics, parquet, datafusion]
sources:
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[LiquidCache]] is a research prototype for pushdown-enabled [[DisaggregatedCaching]] that progressively transcodes cached [[ApacheParquet]] data into an ephemeral representation optimized for [[FilterPushdown]].

## Current Profile
LiquidCache sits between object storage and compute nodes. It stores fetched Parquet bytes on local SSD, caches columns in independently encoded 8,192-row batches, embeds [[ApacheDataFusion]] to run supported scan operations, and returns filtered batches through Arrow Flight. Its Liquid representation uses cascading dictionary, FSST, frame-of-reference, FastLanes, and ALP encodings while preserving element-level independent decodability.

The system co-designs representation and execution. It selectively decodes projection values, materializes later filter columns only for rows surviving earlier predicates, evaluates compatible predicates directly on encoded dictionaries, and decodes incompatible operations only to the necessary intermediate form. On misses, queries can consume Arrow immediately while background tasks progressively transcode reusable columns into Liquid.

## Key Characteristics
- Separates a shared, memory-heavy cache from CPU-heavy analytical compute on commodity hardware.
- Preserves Parquet as the durable ecosystem boundary while keeping Liquid private to the cache.
- Pushes filters, projections, and inexpensive aggregations but leaves expensive operations such as `DISTINCT` on compute nodes.
- Stores logical column batches rather than final query results, allowing different predicates to reuse transcoded data.
- Combines selective decoding, late filter materialization, and encoding-aware predicate evaluation.
- Uses asynchronous fine-grained transcoding to hide conversion behind object-store I/O and compute gaps.
- Offers a manually selected local mode for cases where non-selective pushdown would expand network traffic.

## Evidence
Architecture and lifecycle:
- [[p5662-hao-corrected]] specifies the cache/compute split, Arrow Flight interface, SSD Parquet cache, in-memory Liquid batches, query-plan split, and background conversion path.

Representation and execution:
- [[p5662-hao-corrected]] describes the cascading string, integer, and floating-point encodings plus element-selective, late-materialized, and encoded predicate execution.

Evaluation:
- [[p5662-hao-corrected]] reports selected ClickBench latency below 0.5 seconds, roughly tenfold Q22 cache-CPU reduction from 27 to 2.7 seconds, Parquet-like memory, and large traffic reductions relative to a file server.
- [[p5662-hao-corrected]] reports strong TPC-H SF100 behavior when input exceeds the 8 GB cache and quantifies background-transcoding and ablation effects.

## Qualifications
LiquidCache is supported by a first-party prototype evaluation, not a production multi-tenant deployment. Its strongest results favor selective filters and warm transcoded data; a 99%-selective query runs about three times slower than file serving because filtered output is uncompressed. Cost-based pushdown, automatic local placement, Substrait interoperability, join pushdown, improved replacement policy, failure recovery, TLS overhead, and production tail behavior are unresolved. The format is deliberately private and ephemeral, so it gains evolvability by declining cross-implementation interoperability.

## What Changed
- Established LiquidCache's architecture, filter-aware encoding, asynchronous transcoding, and reported resource tradeoffs.
- Added non-selective filters and cold memory-speed input as explicit limits.

## Relationships
- [[XiangpengHao]] - lead author of the system paper.
- [[AndrewLamb]] - coauthor connected to DataFusion and StringView engineering.
- [[YiboWu]] - coauthor of the system paper.
- [[AndreaArpaciDusseau]] - coauthor of the system paper.
- [[RemziArpaciDusseau]] - coauthor of the system paper.
- [[ApacheDataFusion]] - embedded engine and implementation substrate.
- [[ApacheParquet]] - durable source format transcoded into cache-private Liquid data.
- [[FilterPushdown]] - principal execution optimization co-designed with the representation.
- [[DisaggregatedCaching]] - deployment architecture LiquidCache implements.
- [[ColumnarStorageTradeoffs]] - broader compression, access, decoding, and compatibility design space.

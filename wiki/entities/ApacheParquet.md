---
title: "Apache Parquet"
type: entity
tags: [software, data-engineering, columnar-storage, file-format]
sources:
  - data-wrangling-at-slack-several-people-are-coding
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - p5662-hao-corrected
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheParquet]] is a durable columnar file format represented across the wiki as an interoperable analytical-storage boundary whose scan, compression, page access, decoding, and implementation tradeoffs depend on workload and query-engine integration.

## Current Profile
Slack selected Parquet because Hive, Presto, and Spark could share it and because columnar storage improved query and space efficiency. The effective contract nevertheless extended beyond the specification: library versions, patches, null semantics, schema mapping, and encoding support varied across engines. Slack therefore sanitized inputs, constrained schema evolution, tested live reader/writer combinations, and ultimately pinned behavior behind owned input and output formats.

Physically, Parquet partitions files into row groups, column chunks, and pages, with common footer metadata. That hierarchy favors compression, scans, and distributed processing, but page-level access can amplify sparse reads, one row-group boundary can fit unequal-width columns poorly, and a wide footer can add projection overhead. LiquidCache adds a different limit: ordinary filter pushdown must decompress and decode relevant pages before vectorized predicates run, making decoding more expensive than the predicate in the evaluated selective queries. Its response is not to replace Parquet, but to retain Parquet as the durable interoperable layer and transcode hot cache data into a private representation.

## Key Characteristics
- Stores schema-bearing columnar files that served as a shared persistence layer across Hive, Presto, and Spark in the Slack account.
- Exposes implementation-dependent behavior around nulls, complex structures, field ordering, and encoding versions.
- Must remain compatible with table and partition metadata as schemas evolve.
- Can require an owned, version-pinned read/write boundary when engine-bundled libraries diverge.
- Uses row groups, column chunks, and pages as nested physical boundaries, with file-level metadata in the footer.
- Favors scan and compression behavior that can impose point-lookup, width-imbalance, metadata, or filter-decoding costs for selective workloads.
- Remains valuable as a durable ecosystem boundary even when a system uses a different private cache representation.

## Evidence
- Shared foundation: [[data-wrangling-at-slack-several-people-are-coding]] says all three engines supported Parquet and benefited from its query and storage efficiency.
- Divergent implementations: [[data-wrangling-at-slack-several-people-are-coding]] reports different library versions and bug-fix subsets across Hive, Spark, and Presto.
- Schema interaction: [[data-wrangling-at-slack-several-people-are-coding]] describes file, table, and partition schemas that had to remain aligned.
- Compatibility control: [[data-wrangling-at-slack-several-people-are-coding]] says Slack wrote a Parquet output format and Hive input format that pinned serialization behavior.
- Physical layout: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams row groups, column chunks, pages, page indexes, and the common footer.
- Workload limits: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] illustrates sparse-read amplification, row-group sizing tension with wide columns, and footer overhead for many-column projection.
- Pushdown cost: [[p5662-hao-corrected]] reports Parquet decoding and decompression above 90% of ClickBench Q22 pushdown time and about 27 seconds of cache CPU versus 2.7 seconds for LiquidCache.
- Durable boundary: [[p5662-hao-corrected]] keeps source and SSD-cached data in Parquet while progressively transcoding reusable in-memory batches into a cache-private representation.
- Integration dependence: [[p5662-hao-corrected]] reports Parquet outperforming similarly compressed ORC partly because DataFusion and DuckDB provide stronger Parquet integration.

## Qualifications
The interoperability evidence reflects one 2016 Slack deployment, not current implementations or present-day best practice. The Lance comparison is a secondary 2025 account largely translated from a competing format project's materials and supplies no reproduced benchmark. LiquidCache is a first-party prototype evaluated on selected ClickBench filters and scan-heavy TPC-H queries in one environment; its comparison is shaped by implementation maturity and usually favors warm transcoded data. Parquet can outperform pushdown for non-selective predicates, and its ecosystem maturity and durable compatibility may outweigh selective-access or decoding costs. The combined profile therefore identifies workload tradeoffs rather than establishing that Parquet is generally inferior.

## What Changed
- Created a source-bounded profile of Parquet as both Slack's common warehouse format and its main cross-engine compatibility boundary.
- Added the row-group, page, point-lookup, wide-column, and footer-metadata tradeoffs from the Lance comparison.
- Added filter-decoding CPU cost, query-engine integration, and Parquet's role as the durable boundary beneath an ephemeral cache format.

## Relationships
- [[LanceFormat]] - contrasting columnar design that removes shared row groups and makes column metadata independently addressable.
- [[ColumnarStorageTradeoffs]] - frames Parquet's scan strengths and selective-access costs as workload-dependent choices.
- [[LiquidCache]] - preserves Parquet at the durable boundary while transcoding hot cache batches.
- [[FilterPushdown]] - exposes the CPU cost of decompressing and decoding Parquet before predicate evaluation.
- [[ApacheDataFusion]] - query engine whose mature Parquet integration influences measured performance.
- [[Slack]] - company operating the multi-engine warehouse in the source.
- [[DataFormatInteroperability]] - Parquet is the concrete format through which incompatible implementations surfaced.
- [[APIBackwardCompatibility]] - related obligation to preserve existing consumers as encodings evolve.
- [[ChangeSafety]] - format and engine upgrades need explicit compatibility validation.

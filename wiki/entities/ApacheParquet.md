---
title: "Apache Parquet"
type: entity
tags: [software, data-engineering, columnar-storage, file-format]
sources:
  - data-wrangling-at-slack-several-people-are-coding
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
  - p5662-hao-corrected
  - vortex-one-format-for-any-shape
  - "2504.15247"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheParquet]] is a durable columnar file format represented across the wiki as an interoperable analytical-storage boundary whose scan, compression, page access, decoding, and implementation tradeoffs depend on workload and query-engine integration.

## Current Profile
Slack selected Parquet because Hive, Presto, and Spark could share it and because columnar storage improved query and space efficiency. The effective contract nevertheless extended beyond the specification: library versions, patches, null semantics, schema mapping, and encoding support varied across engines. Slack therefore sanitized inputs, constrained schema evolution, tested live reader/writer combinations, and ultimately pinned behavior behind owned input and output formats.

Physically, Parquet partitions files into row groups, column chunks, and pages, with common footer metadata. That hierarchy favors compression, scans, and distributed processing, but page-level access can amplify sparse reads, one row-group boundary can fit unequal-width columns poorly, and a wide footer can add projection overhead. The primary Lance paper shows that these are tunable tradeoffs rather than an inherent inability to perform point lookup: parquet-rs page-offset indexes and 8 KiB pages raised its small-scalar result from about 5,500 rows per second at defaults to about 350,000. The costs were configuration sensitivity, page-index RAM for large values, weaker dictionary results in random data, and row-group preferences that varied by data type.

LiquidCache adds a different limit: ordinary filter pushdown must decompress and decode relevant pages before vectorized predicates run, making decoding more expensive than the predicate in the evaluated selective queries. Its response is not to replace Parquet, but to retain Parquet as the durable interoperable layer and transcode hot cache data into a private representation.

Format evolvability creates another boundary. Parquet logical types must map onto a small set of prescribed physical types, encodings, and layout conventions, while new encodings require specification agreement and implementation by independent readers. A registrable design can instead make types, encodings, and layouts composable, although its readers then require extension code. From that design perspective, Parquet's PAX-style row-group, column-chunk, and page hierarchy is one reproducible layout choice rather than the only possible container structure.

## Key Characteristics
- Stores schema-bearing columnar files that served as a shared persistence layer across Hive, Presto, and Spark in the Slack account.
- Exposes implementation-dependent behavior around nulls, complex structures, field ordering, and encoding versions.
- Must remain compatible with table and partition metadata as schemas evolve.
- Can require an owned, version-pinned read/write boundary when engine-bundled libraries diverge.
- Uses row groups, column chunks, and pages as nested physical boundaries, with file-level metadata in the footer.
- Can deliver strong indexed point lookup with small pages, while trading page-index RAM, read amplification, and configuration sensitivity against scans.
- Remains valuable as a durable ecosystem boundary even when another system uses a private, extensible, or workload-specific representation.

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
- Extensibility boundary: [[vortex-one-format-for-any-shape]] contrasts Parquet's standardized physical types, encodings, layouts, and independently implemented readers with Vortex's registries and shared Rust implementation.
- Layout reproducibility: [[vortex-one-format-for-any-shape]] says composable Vortex layouts can recreate Parquet's row-group-to-column-chunk-to-page hierarchy.
- Tuned point lookup: [[2504.15247]] reports one page I/O per selected row, about 350,000 small-scalar rows per second with 8 KiB pages, and more than 60-fold improvement over default parquet-rs settings.
- Scan and metadata tradeoff: [[2504.15247]] reports data-dependent row-group preferences, comparable compression, underused disk bandwidth, and a projected 20 GiB page-offset cache per billion one-page values in parquet-rs.

## Qualifications
The interoperability evidence reflects one 2016 Slack deployment, not current implementations or present-day best practice. The new point-lookup evidence is stronger than the earlier secondary Lance account, but it is still a competing format team's benchmark on one device, parquet-rs 54, custom row-selection orchestration, warm indexes, and chosen page and row-group sweeps. It shows Parquet's capability when tuned, not the behavior of every reader or workload. LiquidCache and Vortex are likewise first-party comparisons with their own workload and maturity boundaries. Parquet's ecosystem maturity and durable compatibility may outweigh selective-access, decoding, or extension costs, and its implementations can improve without a format change.

## What Changed
- Added primary evidence that page-offset indexes and 8 KiB pages can make Parquet a strong NVMe point-lookup format.
- Added the page-index RAM, dictionary, row-group tuning, and scan-scheduling costs observed in that experiment.
- Preserved interoperability, durable-boundary, filter-decoding, and standardized-extension roles from the complete evidence set.

## Relationships
- [[LanceFormat]] - contrasting columnar design that removes shared row groups and makes column metadata independently addressable.
- [[ApacheArrow]] - contrasting dense multi-buffer layout with different point-access and decoding costs.
- [[ColumnarStorageTradeoffs]] - frames Parquet's scan strengths and selective-access costs as workload-dependent choices.
- [[LiquidCache]] - preserves Parquet at the durable boundary while transcoding hot cache batches.
- [[Vortex]] - extensible comparison format that can reproduce Parquet's physical hierarchy through composable layouts.
- [[FilterPushdown]] - exposes the CPU cost of decompressing and decoding Parquet before predicate evaluation.
- [[ApacheDataFusion]] - query engine whose mature Parquet integration influences measured performance.
- [[Slack]] - company operating the multi-engine warehouse in the source.
- [[DataFormatInteroperability]] - Parquet is the concrete format through which incompatible implementations surfaced.
- [[APIBackwardCompatibility]] - related obligation to preserve existing consumers as encodings evolve.
- [[ChangeSafety]] - format and engine upgrades need explicit compatibility validation.

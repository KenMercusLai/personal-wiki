---
title: "Apache Parquet"
type: entity
tags: [software, data-engineering, columnar-storage, file-format]
sources:
  - data-wrangling-at-slack-several-people-are-coding
  - lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheParquet]] is represented as the shared columnar file format in Slack's 2016 S3 data warehouse and as the boundary where supposedly compatible analytics engines exposed materially different behavior.

## Current Profile
Slack selected Parquet because Hive, Presto, and Spark could all use it and because columnar storage improved query and space efficiency. The source shows, however, that the effective format included more than a specification: each engine brought a different library version, patches, null semantics, schema mapping behavior, and encoding support. Slack ultimately pinned Parquet writing and Hive reading behind formats it owned so cluster upgrades would not silently redefine persisted data.

The Lance comparison adds the physical hierarchy and a workload-specific limit. Parquet horizontally partitions a file into row groups, vertically partitions each group into column chunks, and divides chunks into pages; a common footer stores schema, locations, and statistics. This supports column scans, compression, and distributed parallelism, but page-level indexing can still amplify sparse row reads, shared row-group sizing can be awkward for very unequal column widths, and projecting one column from a very wide file may still require loading common footer metadata.

## Key Characteristics
- Stores columnar files with a schema embedded in each file.
- Serves as a shared persistence layer across Hive, Presto, and Spark in the Slack account.
- Exposes implementation-dependent behavior around nulls, complex structures, field ordering, and encoding versions.
- Must remain compatible with table and partition metadata as schemas evolve.
- Can require an owned, version-pinned read/write boundary when engine-bundled libraries diverge.
- Uses row groups, column chunks, and pages as nested physical boundaries, with file-level metadata in the footer.
- Favors scan and compression behavior that can impose point-lookup, width-imbalance, or metadata costs for some AI workloads.

## Evidence
- Shared foundation: [[data-wrangling-at-slack-several-people-are-coding]] says all three engines supported Parquet and benefited from its query and storage efficiency.
- Divergent implementations: [[data-wrangling-at-slack-several-people-are-coding]] reports different library versions and bug-fix subsets across Hive, Spark, and Presto.
- Schema interaction: [[data-wrangling-at-slack-several-people-are-coding]] describes file, table, and partition schemas that had to remain aligned.
- Compatibility control: [[data-wrangling-at-slack-several-people-are-coding]] says Slack wrote a Parquet output format and Hive input format that pinned serialization behavior.
- Physical layout: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] diagrams row groups, column chunks, pages, page indexes, and the common footer.
- Workload limits: [[lance-mian-xiang-ai-chang-jing-de-shu-ju-cun-chu-ge-shi]] illustrates sparse-read amplification, row-group sizing tension with wide columns, and footer overhead for many-column projection.

## Qualifications
The interoperability evidence reflects one 2016 Slack deployment, not current implementations or present-day best practice. The Lance comparison is a secondary 2025 account largely translated from a competing format project's materials; it explains real layout differences but does not reproduce its performance claims or quantify file size, compression, write cost, ecosystem support, or operational maturity. The combined profile therefore identifies workload tradeoffs rather than establishing that Parquet is generally inferior.

## What Changed
- Created a source-bounded profile of Parquet as both Slack's common warehouse format and its main cross-engine compatibility boundary.
- Added the row-group, page, point-lookup, wide-column, and footer-metadata tradeoffs from the Lance comparison.

## Relationships
- [[LanceFormat]] - contrasting columnar design that removes shared row groups and makes column metadata independently addressable.
- [[ColumnarStorageTradeoffs]] - frames Parquet's scan strengths and selective-access costs as workload-dependent choices.
- [[Slack]] - company operating the multi-engine warehouse in the source.
- [[DataFormatInteroperability]] - Parquet is the concrete format through which incompatible implementations surfaced.
- [[APIBackwardCompatibility]] - related obligation to preserve existing consumers as encodings evolve.
- [[ChangeSafety]] - format and engine upgrades need explicit compatibility validation.

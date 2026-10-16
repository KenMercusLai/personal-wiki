---
title: "Data Pruning"
type: concept
tags: [query-optimization, analytics, data-layout]
sources:
  - beyond-indexes
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Definition
[[DataPruning]] is the exclusion of partitions, files, row groups, columns, or other physical regions that metadata proves cannot satisfy a query predicate.

## Current Synthesis
Pruning is the analytical counterpart to selective navigation: its value comes from avoiding I/O before or during a scan rather than locating individual rows through pointer chains. It requires both useful physical locality and metadata at the matching granularity. Partition values can eliminate guaranteed groups of files; file and row-group min/max ranges can eliminate regions whose ranges do not overlap a predicate; Bloom filters can prove absence for exact matches.

Metadata reflects layout quality. Sorting related values into narrow ranges makes min/max statistics selective, whereas mixing the full domain into every file produces broad overlapping ranges that cannot be skipped. Independent writes gradually weaken cross-file locality, so compaction is part of maintaining pruning effectiveness rather than only a file-count cleanup.

## Key Claims
- Pruning performance is jointly determined by data layout and metadata.
- Partition pruning is structurally strong when predicates match the partition transform.
- Sorting tightens min/max ranges within row groups and can improve file-level exclusion after compaction.
- Bloom filters answer absence probabilistically and complement, rather than replace, range statistics.
- Poor selectivity or layout drift can make every metadata check lead to a scan.

## Evidence
- Planning model: [[beyond-indexes]] defines most data skipping as planning which files must be scanned.
- Hierarchical pruning: [[beyond-indexes]] maps Iceberg manifest statistics to files and Parquet statistics to row groups.
- Layout dependence: [[beyond-indexes]] contrasts narrow sorted ranges with broad mixed ranges.
- Maintenance: [[beyond-indexes]] shows newly written sorted files overlapping until compaction produces fewer ordered ranges.

## Counterevidence & Qualifications
The source gives mechanisms, not measured speedups or metadata overhead. Engines differ in which predicates, statistics, null and NaN semantics, Bloom filters, and transforms they can exploit. False-positive Bloom-filter matches still require reads, min/max statistics can be weak for correlated or unordered data, and very fine partitioning can exchange scan savings for metadata and small-file cost.

## What Changed
- Created a hierarchy-aware synthesis connecting layout, metadata, and maintenance.

## Related Concepts
- [[OpenTableFormats]] - provide table-level metadata and maintenance boundaries for pruning.
- [[ApacheIceberg]] - supplies partition and manifest metadata in the main example.
- [[ApacheParquet]] - supplies row-group and column statistics below the table layer.
- [[ColumnarStorageTradeoffs]] - determines the granularity and cost of lower-level reads and metadata.

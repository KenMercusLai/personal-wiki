---
title: "Apache Iceberg"
type: entity
tags: [software, data-engineering, open-table-format]
sources:
  - beyond-indexes
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheIceberg]] is an open table format represented here as a snapshot-based metadata tree over immutable columnar data files, with performance driven by physical locality and metadata-guided [[DataPruning]].

## Current Profile
At one point in time, a table snapshot leads through a manifest list and manifest files to data files such as [[ApacheParquet]]. Those files are a catalogued set rather than a primary-key-ordered B-tree, so planners depend on partition transforms and per-file statistics to avoid irrelevant data. Sorting can tighten file and row-group value ranges, while compaction reduces small-file overhead and restores locality that becomes fragmented across independent writes.

The table still has one canonical physical layout. Coarse partitions should match common filters without exploding file counts, and sort keys should reflect selective predicates. Query patterns that require incompatible layouts may need separately maintained materialized projections rather than more row-level B-trees.

## Key Characteristics
- Selects a consistent snapshot through metadata before reading data files.
- Uses manifest lists and manifests to catalogue immutable files and their pruning metadata.
- Supports partitioning and sorting as distinct locality controls.
- Depends on compaction to consolidate small files and strengthen cross-file sort locality.
- Relies on file-format statistics for pruning below the table metadata layer.

## Evidence
- Metadata hierarchy: [[beyond-indexes]] diagrams a snapshot, manifest list, manifests, and data files as distinct layers.
- Layout controls: [[beyond-indexes]] explains partition pruning, within-partition sorting, and compaction across separately written files.
- Statistics: [[beyond-indexes]] says manifest min/max values prune data files and Parquet statistics prune row groups.
- Modeling: [[beyond-indexes]] recommends coarse time or region partitioning and selective sorting for large star-schema fact tables.

## Qualifications
The source is a conceptual practitioner explanation rather than an Iceberg specification, implementation audit, or controlled benchmark. Exact statistics, Bloom-filter support, optimizer use, transforms, file formats, and maintenance behavior vary by Iceberg version and query engine. A declared sort order does not itself guarantee globally useful ordering after many independent writes.

## What Changed
- Created a profile of Iceberg's query-performance structure and maintenance boundaries.

## Relationships
- [[OpenTableFormats]] - Iceberg is the primary example of this metadata and table-management layer.
- [[ApacheParquet]] - common immutable data-file format beneath Iceberg metadata.
- [[DataPruning]] - consumes partition values and statistics to avoid irrelevant data.
- [[ColumnarStorageTradeoffs]] - frames the file-level granularity and metadata costs beneath the table format.

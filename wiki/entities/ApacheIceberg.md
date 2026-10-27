---
title: "Apache Iceberg"
type: entity
tags: [software, data-engineering, open-table-format]
sources:
  - beyond-indexes
  - magnus-p4964-song
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheIceberg]] is an open table format represented here as a snapshot-based metadata tree over immutable columnar data files, with performance driven by physical locality and metadata-guided [[DataPruning]] and with extension points that production systems may specialize for machine-learning workloads.

## Current Profile
At one point in time, a table snapshot leads through a manifest list and manifest files to data files such as [[ApacheParquet]]. Those files are a catalogued set rather than a primary-key-ordered B-tree, so planners depend on partition transforms and per-file statistics to avoid irrelevant data. Sorting can tighten file and row-group value ranges, while compaction reduces small-file overhead and restores locality that becomes fragmented across independent writes.

The table still has one canonical physical layout. Coarse partitions should match common filters without exploding file counts, and sort keys should reflect selective predicates. Query patterns that require incompatible layouts may need separately maintained materialized projections rather than more row-level B-trees.

The [[Magnus]] case preserves Iceberg's snapshot, manifest-list, manifest, and data-file hierarchy but reports several pressure points at ML scale. Wide feature tables make unused per-column min/max statistics dominate manifest size and parsing; unsorted entries force single-partition planning toward full-manifest scans; standard updates rewrite too much data; and basic branches do not cover the merge and rebase workflows required by feature experiments. Magnus addresses these through selective statistics retention, partition-sorted manifests with sparse offsets, delta-based column updates, primary-key indexes, and metadata-only branch operations. These are implementation-specific extensions, not established properties of Iceberg itself.

## Key Characteristics
- Selects a consistent snapshot through metadata before reading data files.
- Uses manifest lists and manifests to catalogue immutable files and their pruning metadata.
- Supports partitioning and sorting as distinct locality controls.
- Depends on compaction to consolidate small files and strengthen cross-file sort locality.
- Relies on file-format statistics for pruning below the table metadata layer.
- Provides a foundation that downstream systems can extend with indexes, specialized formats, mutation rules, and richer branch semantics.

## Evidence
- Metadata hierarchy: [[beyond-indexes]] diagrams a snapshot, manifest list, manifests, and data files as distinct layers.
- Layout controls: [[beyond-indexes]] explains partition pruning, within-partition sorting, and compaction across separately written files.
- Statistics: [[beyond-indexes]] says manifest min/max values prune data files and Parquet statistics prune row groups.
- Modeling: [[beyond-indexes]] recommends coarse time or region partitioning and selective sorting for large star-schema fact tables.
- ML-scale extension pressure: [[magnus-p4964-song]] reports manifest-statistics overhead, partition-planning scans, update amplification, and missing merge or rebase workflows in its Iceberg baseline.
- Specialized response: [[magnus-p4964-song]] retains the snapshot hierarchy while adding manifest offsets, primary-key and search indexes, MOR deltas, and metadata-only branch operations.

## Qualifications
The sources are a conceptual practitioner explanation and a first-party paper about a proprietary extension rather than an Iceberg specification or neutral implementation audit. Exact statistics, Bloom-filter support, optimizer use, transforms, file formats, maintenance, branch behavior, and update performance vary by Iceberg version and query engine. A declared sort order does not itself guarantee globally useful ordering after many independent writes. Magnus's comparison sometimes uses Iceberg COW and sometimes MOR, so its results demonstrate workload-specific extension value rather than a universal limitation of every Iceberg deployment.

## What Changed
- Created a profile of Iceberg's query-performance structure and maintenance boundaries.
- Added ML-scale pressure on manifests, updates, and branch workflows while separating Magnus extensions from Iceberg's native contract.

## Relationships
- [[OpenTableFormats]] - Iceberg is the primary example of this metadata and table-management layer.
- [[ApacheParquet]] - common immutable data-file format beneath Iceberg metadata.
- [[DataPruning]] - consumes partition values and statistics to avoid irrelevant data.
- [[ColumnarStorageTradeoffs]] - frames the file-level granularity and metadata costs beneath the table format.
- [[Magnus]] - production system that extends Iceberg for ByteDance's ML data workloads.
- [[MachineLearningDataManagement]] - exposes cross-layer requirements beyond the base table specification.

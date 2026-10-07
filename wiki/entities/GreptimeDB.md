---
title: "GreptimeDB"
type: entity
tags: [database, time-series, lsm-tree, parquet]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
  - bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Overview
[[GreptimeDB]] is presented as an emerging time-series database with named, tagged series, multiple fields, and an LSM-tree storage engine using columnar Parquet files; a later practitioner comparison places its separated storage, replicas, remote compaction, and incremental views alongside architectural patterns attributed to Bigtable.

## Current Profile
The source places GreptimeDB inside its time-series data model while noting its relational borrowing. It describes SST files ordered by tags and then timestamp, a layout the author infers may preserve time-range scan performance while accommodating updates and point lookups.

A later source uses Bigtable as a comparison rather than documenting GreptimeDB independently. It says GreptimeDB chose object-storage-based storage-compute separation and outsourced metadata to a mature relational service, and compares its read replicas, remote compaction, and Flow design with Bigtable's workload-isolating replicas, external compaction, and watermark-driven materialized views. These are useful design correspondences, not claims of identical guarantees or implementations.

## Key Characteristics
- Represents series through a metric name and tags.
- Permits multiple fields within the model.
- Uses an LSM-tree storage engine.
- Stores SST data in columnar Parquet ordered by tags and timestamp.
- Is described as separating storage from compute and moving compaction to independently scalable remote work.
- Is compared with replica-based workload isolation and a watermark-driven incremental-view pipeline.

## Evidence
- Series model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says GreptimeDB uses metric names and tags and can carry several fields.
- Storage engine: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] identifies an LSM-tree design with Parquet SST files.
- Sort order: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] reports ordering by `(tag-1, ..., tag-m, timestamp)`.
- Architecture comparison: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] attributes object-storage separation, external metadata, read replicas, remote compaction, and Flow to GreptimeDB while comparing them with Bigtable mechanisms.

## Qualifications
The earlier article calls the performance rationale for the SST sort order a guess. The later comparison is written by GreptimeDB's affiliated author but supplies no version pins, protocol-level guarantee comparison, benchmark, or operational result for the named features. The evidence supports reported architectural direction more strongly than performance, equivalence with Bigtable, or production maturity.

## What Changed
- Established GreptimeDB's time-series model and its reported LSM-Parquet storage layout.
- Added source-scoped storage-compute separation, read-replica, remote-compaction, and Flow comparisons without treating them as implementation equivalence.

## Relationships
- [[TimeSeriesDatabase]] - GreptimeDB fits the source's name-label-series definition.
- [[InfluxDB]] - both expose a relationally influenced metric, tag, and field model.
- [[QuestDB]] - both use columnar structures but are classified differently by the source.
- [[EricFu]] - author providing the storage-layout interpretation.
- [[Bigtable]] - comparison system for replicas, background compaction, and materialized-view processing.
- [[StorageArchitectureEvolvability]] - frames whether new capabilities attach to stable mechanisms without rewriting foreground paths.
- [[CiJianDeShanLin]] - affiliated author making the architectural comparison.

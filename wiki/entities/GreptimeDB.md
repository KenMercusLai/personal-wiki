---
title: "GreptimeDB"
type: entity
tags: [database, time-series, lsm-tree, parquet]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
  - bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian
  - rethink-greptimedb-partition
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Overview
[[GreptimeDB]] is a time-series database with named, tagged series, multiple fields, and an LSM-tree storage engine using columnar Parquet files. Practitioner sources describe separated object-store durability, independently scalable work, and a Region abstraction now being narrowed after accumulating routing, ownership, cache, metadata, and maintenance responsibilities.

## Current Profile
The source places GreptimeDB inside its time-series data model while noting its relational borrowing. It describes SST files ordered by tags and then timestamp, a layout the author infers may preserve time-range scan performance while accommodating updates and point lookups.

A later source uses Bigtable as a comparison rather than documenting GreptimeDB independently. It says GreptimeDB chose object-storage-based storage-compute separation and outsourced metadata to a mature relational service, and compares its read replicas, remote compaction, and Flow design with Bigtable's workload-isolating replicas, external compaction, and watermark-driven materialized views. These are useful design correspondences, not claims of identical guarantees or implementations.

The newest architectural retrospective explains the consequences inside GreptimeDB. Frontend nodes route requests and can perform stateless batch-write preparation; Region Servers own Regions, caches, and LSM state; object storage is the durable source of truth; and a reliable KV or RDS service holds metadata. Time partitioning handles history, while explicit primary-key ranges distribute active load. Because Regions also accumulated file, metadata, cache, alteration, compaction, versioning, and lifecycle duties, repartitioning became a coordinated operational procedure rather than a cheap rule change.

The proposed correction is to move validation, encoding, file construction, and upload into elastic Frontends, leaving Regions to register completed files and focus placement on query load. Independent multidimensional ranges support pruning on any partition column and workload-derived hotspot detection. Treating each immutable file as a partition is a personal future idea, not a GreptimeDB roadmap commitment, and fully automatic query-led placement remains incomplete.

## Key Characteristics
- Represents series through a metric name and tags while permitting multiple fields.
- Uses an LSM-tree storage engine.
- Stores SST data in columnar Parquet ordered by tags and timestamp.
- Is described as separating storage from compute and moving compaction to independently scalable remote work.
- Is compared with replica-based workload isolation and a watermark-driven incremental-view pipeline.
- Uses implicit time partitioning plus explicit primary-key Region ranges to separate retention from active-load distribution.
- Is moving stateless batch-write preparation ahead of Region ownership so Regions can focus more directly on query-serving work.

## Evidence
- Series model: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says GreptimeDB uses metric names and tags and can carry several fields.
- Storage engine: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] identifies an LSM-tree design with Parquet SST files.
- Sort order: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] reports ordering by `(tag-1, ..., tag-m, timestamp)`.
- Architecture comparison: [[bigtable-er-shi-nian-jia-gou-de-bu-bian-yu-bian]] attributes object-storage separation, external metadata, read replicas, remote compaction, and Flow to GreptimeDB while comparing them with Bigtable mechanisms.
- Partition architecture: [[rethink-greptimedb-partition]] diagrams Frontends, Region Servers, metadata services, and shared object storage, and distinguishes implicit time slices from multidimensional primary-key Regions.
- Abstraction pressure: [[rethink-greptimedb-partition]] depicts the Mito2 Region state machine and reports that repartitioning spans five metadata groups, flushing, file reassignment, rollback, online traffic, cache work, and later recompaction.
- Write and query separation: [[rethink-greptimedb-partition]] describes Frontend-built files registered by Regions and independent column ranges whose predicates can inform hotspot detection.

## Qualifications
The earliest article calls the performance rationale for the SST sort order a guess. The two later accounts are affiliated practitioner interpretations without version pins, controlled benchmarks, or independent operational results. The partition retrospective does not quantify repartitioning cost, batch-write latency, cache effects, or automatic-placement quality; its file-as-partition idea is explicitly off-roadmap, and the end-to-end query-feedback loop remains unfinished. The evidence supports architectural direction more strongly than performance, equivalence with Bigtable, or production maturity.

## What Changed
- Established GreptimeDB's time-series model and its reported LSM-Parquet storage layout.
- Added source-scoped storage-compute separation, read-replica, remote-compaction, and Flow comparisons without treating them as implementation equivalence.
- Recast Region overloading and expensive repartitioning as constraints on automatic, query-led placement.
- Added the batch-write path and multidimensional range rules while preserving their latency, failure, cache, and maturity limits.

## Relationships
- [[TimeSeriesDatabase]] - GreptimeDB fits the source's name-label-series definition.
- [[InfluxDB]] - both expose a relationally influenced metric, tag, and field model.
- [[QuestDB]] - both use columnar structures but are classified differently by the source.
- [[EricFu]] - author providing the storage-layout interpretation.
- [[Bigtable]] - comparison system for replicas, background compaction, and materialized-view processing.
- [[StorageArchitectureEvolvability]] - frames whether new capabilities attach to stable mechanisms without rewriting foreground paths.
- [[CiJianDeShanLin]] - affiliated author making the architectural comparison.
- [[DatabasePartitioning]] - GreptimeDB's Regions illustrate the difference between retention boundaries, active-load placement, and overloaded ownership units.
- [[Wayne]] - affiliated practitioner describing the partition implementation history and proposed direction.

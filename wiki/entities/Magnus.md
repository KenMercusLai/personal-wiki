---
title: "Magnus"
type: entity
tags: [software, data-lake, machine-learning, iceberg]
sources:
  - magnus-p4964-song
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Magnus]] is an internal [[ByteDance]] data-management system built on [[ApacheIceberg]] for large-scale machine-learning data, feature engineering, search, updates, and model training.

## Current Profile
Magnus treats [[MachineLearningDataManagement]] as a vertically integrated system rather than a table format alone. Its table layer combines Parquet, a wide-table Krypton format, external Blob storage for media payloads, primary-key and search indexes, snapshots, branches, tags, and statistics. A global service supplies catalog and lifecycle functions, while Java, Python, and C++ SDKs integrate table operations with ingestion, analytics, and training engines.

For mutation-heavy workloads, Magnus writes column-level deltas or bucketed primary-key files and resolves them during reads by sequence number and configurable merge rules. Its Arrow-based native engine reduces the resulting read cost through pruning, predicate-first loading, asynchronous prebuffering, vectorization, and compaction. Training-specific designs deduplicate recommendation sequences across Main and Extra tables and split multimodal scan ranges finely enough to fit worker memory.

## Key Characteristics
- Extends Iceberg's snapshot-and-manifest table model with specialized formats, indexes, metadata caches, and branch workflows.
- Stores large multimodal payloads in Blob files while retaining address metadata in columnar files.
- Supports position updates, equality updates, and primary-key upserts through merge-on-read sequence ordering.
- Integrates ingestion, data engineering, insight, and training through multiple compute engines and SDKs.
- Uses workload-specific physical organization for large recommendation and multimodal model training.

## Evidence
- System boundaries: [[magnus-p4964-song]] diagrams the table, global service, multi-engine layer, storage backends, and ML scenarios.
- Storage and indexing: [[magnus-p4964-song]] describes Krypton, Blob, hash and HFile primary-key indexes, and in-table inverted and vector indexes.
- Metadata and mutation: [[magnus-p4964-song]] presents partition-sorted manifests, sparse offsets, branch merge and rebase, delta files, MOR rules, and compaction.
- Training integration: [[magnus-p4964-song]] documents Main-Extra recommendation tables and row-range planning with compressed scan tasks for multimodal training.
- Production evaluation: [[magnus-p4964-song]] reports wide-table, Blob, planning, update, upsert, LRM, and LMM results from ByteDance workloads.

## Qualifications
The available profile comes from one first-party paper by the system's developers. Magnus is not represented here as a public product or independently benchmarked implementation. Its strongest results depend on selected schemas, ByteDance engines, proprietary formats, tuned compaction, and production infrastructure; update baselines also vary between Iceberg COW and MOR. The paper gives limited operational evidence about correctness under failure, cost, maintenance burden, or long-tail performance.

## What Changed
- Created a source-bounded profile of Magnus's table, metadata, mutation, and training architecture.
- Recorded its production benchmark claims together with comparison and reproducibility limits.

## Relationships
- [[ByteDance]] - develops and operates Magnus for internal ML workloads.
- [[ApacheIceberg]] - supplies the open table and snapshot foundation that Magnus extends.
- [[MachineLearningDataManagement]] - is the workload and systems problem Magnus addresses.
- [[ColumnarStorageTradeoffs]] - motivates Krypton and Blob layout choices.
- [[MultimodalDataPipelines]] - consumes Magnus-managed media datasets and fine-grained shards.
- [[OpenTableFormats]] - broader table-management family containing Magnus's base abstraction.

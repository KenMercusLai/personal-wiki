---
title: "Lake Transactional/Analytical Processing"
type: concept
tags: [databases, transactions, analytics, lakehouse, columnar-storage]
sources:
  - lakebase-ltap-rethinking-database-storage
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[LakeTransactionalAnalyticalProcessing]] (LTAP) is a proposed architecture that gives separate transactional and analytical engines access to one governed durable copy of operational data in open columnar lake storage.

## Current Synthesis
LTAP unifies storage rather than execution. PostgreSQL remains responsible for ACID transactions and its mature interface and extension ecosystem, while Lakehouse engines retain columnar, vectorized analytical execution and independent scaling. A Pageserver materialization path transcodes PostgreSQL row state into Parquet exposed through formats such as Delta or Iceberg, while retaining enough type and version information to reconstruct PostgreSQL pages and history.

Freshness is defined at an LSN. An analytical query obtains that boundary from PostgreSQL, scans data already materialized in object storage, then merges the small recent tail from the Pageserver. This keeps bulk analytical reads away from transactional compute while aiming to expose every table without a selected CDC pipeline or separately governed mirror.

The single-copy description is architectural rather than literal at every tier. Memory buffers, local row-page caches, Pageserver state, Parquet objects, MVCC versions, and transitional verification copies can coexist. The durable-authority and governance claim is that these are coordinated representations of one database history rather than independently replicated application and warehouse datasets.

## Key Claims
- Storage-level unification allows PostgreSQL and analytical engines to specialize without sharing CPU and memory.
- Row-to-columnar materialization must preserve PostgreSQL types, exceptional values, physical tuple identity, MVCC history, and snapshot boundaries.
- LSN-based reads can combine a large materialized prefix with a small recent tail for fresh analytical snapshots.
- Making all tables part of the storage path removes per-table CDC selection and reduces schema, permission, and freshness drift between independent copies.
- Row pages and indexes can become rebuildable performance caches while columnar object storage acts as durable authority.
- Small tables may remain row-oriented when columnar files and table metadata would create more overhead than benefit.

## Evidence
Storage and engine boundary:
- [[lakebase-ltap-rethinking-database-storage]] assigns transactions to PostgreSQL, analytics to Lakehouse engines, and shared durability to Parquet represented through Delta or Iceberg.

Semantic preservation:
- [[lakebase-ltap-rethinking-database-storage]] describes native Parquet mappings, overflow text for exceptional PostgreSQL values, heap addresses for page reconstruction, retained intermediate versions, and invisible garbage-collected history.

Freshness path:
- [[lakebase-ltap-rethinking-database-storage]] diagrams an analytical engine obtaining an LSN, reading most data from object storage, and merging recent Pageserver changes.

CDC comparison:
- [[lakebase-ltap-rethinking-database-storage]] contrasts automatic all-table availability with explicitly selected mirrored tables, a message pipeline, delayed ingestion, and multiple governed copies.

## Counterevidence & Qualifications
The evidence is a first-party architectural article, not an independent systems evaluation. LTAP was still in rollout and temporarily dual-wrote row and columnar representations for verification. The article does not quantify materialization lag, recent-tail size, merge cost, metadata overhead, recovery time, garbage-collection safety, extension compatibility, concurrent analytical performance, or behavior under correlated failures. "One copy" excludes caches and validation replicas and depends on all derived representations sharing one correct authority. CDC may remain preferable when consumers need transformed schemas, independent retention, cross-system delivery, or isolation from changes in the source database.

## What Changed
- Established LTAP as a distinct storage-level alternative to both CDC mirroring and single-engine HTAP.

## Related Concepts
- [[DisaggregatedTransactionalDatabase]] - supplies the independent WAL and page services that make the materialization boundary possible.
- [[ObjectStorageNativeDatabase]] - provides replaceable compute over durable remote state.
- [[OpenTableFormats]] - expose columnar snapshots and metadata to analytical engines.
- [[ColumnarStorageTradeoffs]] - governs compression, scan, metadata, and reconstruction costs in the durable representation.
- [[DataFormatInteroperability]] - defines the semantic burden of sharing PostgreSQL-derived values across engines.
- [[DatabaseBranching]] - reuses the same versioned external storage for isolated histories.
- [[Lakebase]] - product architecture in which LTAP is introduced.

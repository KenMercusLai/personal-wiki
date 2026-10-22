---
title: "Lakebase"
type: entity
tags: [database, postgres, serverless, object-storage, lakehouse]
sources:
  - p4385-pandis
  - lakebase-ltap-rethinking-database-storage
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[Lakebase]] is a [[Databricks]] transactional database service that runs elastic [[PostgreSQL]] compute over disaggregated WAL, page, and cloud-object-storage layers derived from [[Neon]].

## Current Profile
Lakebase separates the lifetime and scaling of PostgreSQL compute from durable database state. A primary broadcasts WAL to three Safekeepers and commits after quorum disk flush; Pageservers ingest committed WAL, compact deltas into page images, and answer versioned page reads; cloud object storage holds WAL and PostgreSQL-format layer files as the durable source of truth.

The architecture supports scale-to-zero, sub-second warm-pool startup, in-place vertical scaling, read replicas, point-in-time static replicas, copy-on-write branches, and multi-zone failure recovery. Its Lakehouse integration also allows Spark to create PostgreSQL page files for bulk ingestion and analytical engines to read committed snapshots outside transactional compute.

The newer LTAP account presents an architectural evolution in the durable representation. As Pageservers materialize database state, they transcode rows into Parquet represented through Delta or Iceberg while preserving PostgreSQL values, physical tuple identity, MVCC history, and reconstruction ability. Analytical engines read the materialized prefix from object storage and merge recent changes from the Pageserver at a PostgreSQL LSN; transactional row pages and indexes remain performance caches. The article describes transitional row-and-column dual writes for verification, so this columnar authority should be treated as a rollout direction rather than a universally deployed replacement for the page-layer system described in the earlier paper.

## Key Characteristics
- Separates PostgreSQL compute, quorum WAL durability, page materialization, and object-store persistence.
- Treats a timeline and LSN as the version boundary for reads, replicas, restore, and branches.
- Uses compute-local SSD caches and Pageserver caches to mask object-store latency.
- Scales compute vertically, to zero when idle, and back from warm virtual machines.
- Supports O(1) copy-on-write branching but not automatic branch merging.
- Allows external compute to ingest or analyze PostgreSQL page files without routing all work through the primary.
- Extends the storage path toward LTAP, where separate transaction and analytical engines consume one PostgreSQL-semantic columnar history at an LSN.

## Evidence
- Architecture and durability: [[p4385-pandis]] diagrams PostgreSQL computes, three-Safekeeper quorum replication, Pageservers, and object storage, with distinct commit, flush, backup, and remote-consistent LSNs.
- Elasticity: [[p4385-pandis]] reports p95 warm-pool startup below 500 ms and shows CPU scaling tracking a production-derived workload surge.
- Branching: [[p4385-pandis]] describes child timelines as metadata references to a parent and branch LSN, with recursive ancestor reads and asynchronous detachment.
- OLTP evaluation: [[p4385-pandis]] reports 23.3K-515.6K peak TPROC-C NOPM across tested tiers under a 20 ms p95 bound.
- Lakehouse integration: [[p4385-pandis]] reports up to 73.3x faster direct-to-storage heap loading at 1 TB and 3x lower geometric-mean TPC-H latency through Direct Access.
- Storage evolution: [[lakebase-ltap-rethinking-database-storage]] describes Pageserver row-to-Parquet transcoding, exact-value overflow handling, heap-address preservation, retained MVCC versions, and rebuildable row-page and index caches.
- Fresh analytical reads: [[lakebase-ltap-rethinking-database-storage]] obtains an LSN from PostgreSQL, scans the materialized majority in object storage, and merges recent Pageserver changes without sending the bulk read through transaction compute.

## Qualifications
The evidence consists of first-party Databricks and Neon material. Comparison systems are anonymized, pricing and statistical uncertainty are incomplete, and production claims are not independently audited. Object-backed storage still requires PostgreSQL-aware readers; deep ancestry and PITR history impose read and space costs; and branch merging, several Direct Access index paths, and some proposed bulk operations are absent or future work. LTAP was still being rolled out, supplies no complete recovery or performance evaluation here, and temporarily keeps verification copies, narrowing claims of one-copy maturity and zero operational risk.

## What Changed
- Reframed the shared-storage path from PostgreSQL page-format direct access toward a PostgreSQL-semantic columnar authority with row pages as caches.
- Added the LSN-bounded object-store-plus-recent-tail read path and its transitional-rollout qualification.

## Relationships
- [[Databricks]] - deploys Lakebase and integrates it with the Lakehouse and Unity Catalog.
- [[Neon]] - supplies the open-source architectural and engineering foundation.
- [[PostgreSQL]] - provides the transactional interface, WAL, page format, and MVCC semantics.
- [[DisaggregatedTransactionalDatabase]] - describes Lakebase's separation of compute and storage responsibilities.
- [[DatabaseBranching]] - is implemented as copy-on-write timeline creation at an LSN.
- [[ObjectStorageNativeDatabase]] - captures its use of object storage as the durable layer.
- [[ServerlessComputing]] - supplies scale-to-zero and warm-pool elasticity.
- [[LakeTransactionalAnalyticalProcessing]] - extends Lakebase toward one durable columnar history read by specialized transaction and analytical engines.

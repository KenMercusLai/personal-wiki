---
title: "Lakebase"
type: entity
tags: [database, postgres, serverless, object-storage, lakehouse]
sources:
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Lakebase]] is a [[Databricks]] transactional database service that runs elastic [[PostgreSQL]] compute over disaggregated WAL, page, and cloud-object-storage layers derived from [[Neon]].

## Current Profile
Lakebase separates the lifetime and scaling of PostgreSQL compute from durable database state. A primary broadcasts WAL to three Safekeepers and commits after quorum disk flush; Pageservers ingest committed WAL, compact deltas into page images, and answer versioned page reads; cloud object storage holds WAL and PostgreSQL-format layer files as the durable source of truth.

The architecture supports scale-to-zero, sub-second warm-pool startup, in-place vertical scaling, read replicas, point-in-time static replicas, copy-on-write branches, and multi-zone failure recovery. Its Lakehouse integration also allows Spark to create PostgreSQL page files for bulk ingestion and analytical engines to read committed snapshots outside transactional compute.

## Key Characteristics
- Separates PostgreSQL compute, quorum WAL durability, page materialization, and object-store persistence.
- Treats a timeline and LSN as the version boundary for reads, replicas, restore, and branches.
- Uses compute-local SSD caches and Pageserver caches to mask object-store latency.
- Scales compute vertically, to zero when idle, and back from warm virtual machines.
- Supports O(1) copy-on-write branching but not automatic branch merging.
- Allows external compute to ingest or analyze PostgreSQL page files without routing all work through the primary.

## Evidence
- Architecture and durability: [[p4385-pandis]] diagrams PostgreSQL computes, three-Safekeeper quorum replication, Pageservers, and object storage, with distinct commit, flush, backup, and remote-consistent LSNs.
- Elasticity: [[p4385-pandis]] reports p95 warm-pool startup below 500 ms and shows CPU scaling tracking a production-derived workload surge.
- Branching: [[p4385-pandis]] describes child timelines as metadata references to a parent and branch LSN, with recursive ancestor reads and asynchronous detachment.
- OLTP evaluation: [[p4385-pandis]] reports 23.3K-515.6K peak TPROC-C NOPM across tested tiers under a 20 ms p95 bound.
- Lakehouse integration: [[p4385-pandis]] reports up to 73.3x faster direct-to-storage heap loading at 1 TB and 3x lower geometric-mean TPC-H latency through Direct Access.

## Qualifications
The evidence is a first-party systems paper from Databricks and Neon authors. Comparison systems are anonymized, pricing and statistical uncertainty are incomplete, and production claims are not independently audited. Object-backed page storage still requires PostgreSQL-aware readers; deep ancestry and PITR history impose read and space costs; and branch merging, several Direct Access index paths, and some proposed bulk operations are absent or future work.

## What Changed
- Established Lakebase as a canonical entity with its storage, compute, branching, availability, and Lakehouse boundaries.

## Relationships
- [[Databricks]] - deploys Lakebase and integrates it with the Lakehouse and Unity Catalog.
- [[Neon]] - supplies the open-source architectural and engineering foundation.
- [[PostgreSQL]] - provides the transactional interface, WAL, page format, and MVCC semantics.
- [[DisaggregatedTransactionalDatabase]] - describes Lakebase's separation of compute and storage responsibilities.
- [[DatabaseBranching]] - is implemented as copy-on-write timeline creation at an LSN.
- [[ObjectStorageNativeDatabase]] - captures its use of object storage as the durable layer.
- [[ServerlessComputing]] - supplies scale-to-zero and warm-pool elasticity.

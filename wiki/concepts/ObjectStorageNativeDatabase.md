---
title: "Object-Storage-Native Database"
type: concept
tags: [databases, object-storage, durability, distributed-systems]
sources:
  - duckdb-on-object-storage
  - slatedb-benchmark
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[ObjectStorageNativeDatabase]] is an architecture that preserves transactional or analytical database semantics while making immutable object storage the durable source of truth and keeping compute replaceable.

## Current Synthesis
The DuckDB implementation shows one way to reconcile mutable database files with immutable objects without introducing an open table format. A filesystem extension translates logical files into path, metadata, and block-aligned content keys over an embedded LSM tree. Atomic write batches make `fsync` durable in the bucket, transactions turn renames into metadata repointing, and committed manifests let readers advance between whole database states.

This choice preserves database-native capabilities such as indexes, enforced constraints, WAL, checkpoints, catalog objects, types, and small writes that a shared Parquet table contract does not necessarily represent. The same choice reduces interoperability: only the owning engine understands the representation, and the bucket no longer contains a directly openable native file.

"Serverless" operation here means eliminating separately operated catalog and compaction services, not eliminating work. Writer processes still compact and garbage-collect data, every durable commit pays object-store latency, caches and manifest polling remain necessary, and a single-writer rule constrains concurrency. The SlateDB benchmark adds that placement is economically material: remote-style persisted-state polling in a colocated process reportedly cost roughly US$40 per month when idle, while in-memory local coordination reduced it below US$5 without excluding remote compactors.

Cache design must also match the intended residency boundary. A coarse 4 MiB object-cache partition makes sense when mirroring most or all of a database locally, but it amplifies small-read misses and produced large p99.9 spikes in SlateDB's balanced workload. Partial caching instead benefits from smaller evictable units; spatial-locality prefetching is a separate optimization rather than a substitute for choosing the right granularity.

Lakebase adds a different point in the design space: object storage holds PostgreSQL-format WAL and page layers, but dedicated Safekeepers establish quorum durability and Pageservers materialize, compact, cache, and reconstruct pages at requested LSNs. Compute-local SSD caches keep common OLTP reads fast, while versioned shared storage supports branches, static replicas, direct Spark ingestion, and analytical readers outside PostgreSQL compute. This increases service complexity but avoids placing every commit and cache miss directly on the bucket path.

“Open” therefore needs a layered definition. PostgreSQL page files let compatible engines share physical state more directly than a proprietary service format, yet readers still need PostgreSQL-version, page, WAL, MVCC, and snapshot knowledge. That is a narrower interoperability contract than a broadly implemented table format, even when it enables a purpose-built analytical engine to bypass the OLTP primary.

## Key Claims
- A virtual filesystem can preserve a database engine and file format while replacing its local-disk durability substrate.
- Block-to-key alignment avoids whole-object rewrites and can make one database block correspond to one point read or write.
- Atomic key-value batches and transactional metadata updates can implement `fsync`, truncation, and rename semantics over immutable objects.
- Manifest checkpoints can give many readers complete committed states while tolerating bounded staleness.
- Native database features and open multi-engine interoperability are competing design goals rather than free complements.
- Eliminating standalone services moves compaction, garbage collection, caching, polling, and fencing into client processes and storage metadata.
- API-call cost and cache-fetch granularity are architectural metrics; intermediate log and page services can trade added complexity for hidden object-store latency, quorum durability, and versioned reads.

## Evidence
Native-semantic preservation:
- [[duckdb-on-object-storage]] demonstrates ordinary DuckDB constraints, indexes, checkpoints, catalog behavior, and read-only attachment over the replacement filesystem.

Mutable-to-immutable mapping:
- [[duckdb-on-object-storage]] diagrams one key per 256 KiB block, separate path and metadata keys, atomic sync batches, transactional rename, and background removal of old versions.

Reader and writer coordination:
- [[duckdb-on-object-storage]] reports one writer, non-fencing readers, manifest takeover, roughly ten-second refresh, and a rewrite test in which no reader sum mixed versions.

Tradeoff boundary:
- [[duckdb-on-object-storage]] contrasts the native database with DuckLake and Iceberg, reports DuckDB-only readability and local-write slowdown, and identifies strong reads, snapshot pinning, fail-fast exclusivity, and single-log durability as future work.

Cost and caching boundary:
- [[slatedb-benchmark]] reports that local in-memory compaction coordination cut idle polling cost from roughly US$40 to below US$5 per month and shows p99.9 spikes when small misses fetch 4 MiB cache partitions.

Disaggregated transactional path:
- [[p4385-pandis]] places Safekeepers and Pageservers between PostgreSQL compute and object storage, reports compute-local cache hit rates above 98.5% in its evaluations, and uses LSN-addressed pages for recovery, branching, replicas, and external analysis.

Interoperability boundary:
- [[p4385-pandis]] lets Spark generate PostgreSQL-compatible pages and Lakehouse//RT read them directly, while still requiring specialized parsing and MVCC handling rather than generic table-format support.

## Counterevidence & Qualifications
This synthesis rests on maintainer- and vendor-authored implementation and benchmark accounts. It does not establish that arbitrary databases can safely use the same translation, because filesystem assumptions, block geometry, WAL ordering, locking, rename semantics, recovery, and extension seams differ. Snapshot-consistent polling is not strong consistency, fencing is not immediate mutual exclusion, and one writer may be unacceptable for collaborative transactional workloads. Lakebase adds quorum and version services but also more distributed components, placement constraints, lag states, and recovery paths. Open table formats remain preferable when broad ecosystem interoperability matters more than preserving native database behavior. SlateDB's cost figures and Lakebase's production performance omit complete pricing assumptions and independent reproduction; cache, branch-depth, and analytical results remain workload- and configuration-specific.

## What Changed
- Added the disaggregated path where quorum WAL and versioned page services mediate between compute and object storage.
- Distinguished PostgreSQL-aware physical interoperability from broad open-table-format interoperability.
- Connected object-backed history to branching, static replicas, and direct analytical reads while preserving its retention and service-complexity costs.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - frames correctness, latency, operability, concurrency, and compatibility as coupled database choices.
- [[StoragePerformanceBenchmarking]] - provides the workload, cache, topology, and cost discipline needed to validate object-backed storage claims.
- [[SystemReliability]] - durability, recovery, fencing, and complete-snapshot reads define system failure behavior.
- [[DataFormatInteroperability]] - explains the cost of choosing an engine-native representation over an open table format.
- [[DuckDBObjectStorage]] - concrete implementation of the architecture for DuckDB.
- [[SlateDB]] - embedded LSM substrate translating mutable blocks into object-storage keys.
- [[DisaggregatedTransactionalDatabase]] - inserts independent WAL and page services between compute and durable object storage.
- [[DatabaseBranching]] - reuses versioned object-backed history through copy-on-write timelines.
- [[Lakebase]] - concrete transactional implementation with Safekeepers, Pageservers, and external engines.

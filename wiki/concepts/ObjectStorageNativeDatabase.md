---
title: "Object-Storage-Native Database"
type: concept
tags: [databases, object-storage, durability, distributed-systems]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[ObjectStorageNativeDatabase]] is an architecture that preserves a database engine's native storage semantics while making immutable object storage the durable source of truth and keeping compute processes replaceable.

## Current Synthesis
The DuckDB implementation shows one way to reconcile mutable database files with immutable objects without introducing an open table format. A filesystem extension translates logical files into path, metadata, and block-aligned content keys over an embedded LSM tree. Atomic write batches make `fsync` durable in the bucket, transactions turn renames into metadata repointing, and committed manifests let readers advance between whole database states.

This choice preserves database-native capabilities—indexes, enforced constraints, WAL, checkpoints, catalog objects, types, and small writes—that a shared Parquet table contract does not necessarily represent. The same choice reduces interoperability: only the owning engine understands the representation, and the bucket no longer contains a directly openable native file.

“Serverless” operation here means eliminating separately operated catalog and compaction services, not eliminating work. Writer processes still compact and garbage-collect data, every durable commit pays object-store latency, caches and manifest polling remain necessary, and a single-writer rule constrains concurrency. The architecture is therefore best understood as moving coordination and maintenance into embedded libraries and bucket metadata.

## Key Claims
- A virtual filesystem can preserve a database engine and file format while replacing its local-disk durability substrate.
- Block-to-key alignment avoids whole-object rewrites and can make one database block correspond to one point read or write.
- Atomic key-value batches and transactional metadata updates can implement `fsync`, truncation, and rename semantics over immutable objects.
- Manifest checkpoints can give many readers complete committed states while tolerating bounded staleness.
- Native database features and open multi-engine interoperability are competing design goals rather than free complements.
- Eliminating standalone services moves compaction, garbage collection, caching, polling, and fencing into client processes and storage metadata.
- Object-store round trips, writer exclusivity, and duplicate durability layers can dominate the remaining performance gap.

## Evidence
Native-semantic preservation:
- [[duckdb-on-object-storage]] demonstrates ordinary DuckDB constraints, indexes, checkpoints, catalog behavior, and read-only attachment over the replacement filesystem.

Mutable-to-immutable mapping:
- [[duckdb-on-object-storage]] diagrams one key per 256 KiB block, separate path and metadata keys, atomic sync batches, transactional rename, and background removal of old versions.

Reader and writer coordination:
- [[duckdb-on-object-storage]] reports one writer, non-fencing readers, manifest takeover, roughly ten-second refresh, and a rewrite test in which no reader sum mixed versions.

Tradeoff boundary:
- [[duckdb-on-object-storage]] contrasts the native database with DuckLake and Iceberg, reports DuckDB-only readability and local-write slowdown, and identifies strong reads, snapshot pinning, fail-fast exclusivity, and single-log durability as future work.

## Counterevidence & Qualifications
This synthesis rests on one maintainer-authored implementation and benchmark. It does not establish that arbitrary databases can safely use the same translation, because filesystem assumptions, block geometry, WAL ordering, locking, rename semantics, recovery, and extension seams differ. Snapshot-consistent polling is not strong consistency, fencing is not immediate mutual exclusion, and one writer may be unacceptable for collaborative transactional workloads. Open table formats remain preferable when Spark, Trino, Flink, or other engines must share the data. Total operating cost must include object requests, compaction, caches, egress, recovery, and process resources even when there is no standalone service.

## What Changed
- Established filesystem translation as one path to a native database over immutable object storage.
- Separated preserved database semantics from multi-engine table-format interoperability.
- Added embedded maintenance, bounded staleness, fencing, and object-store latency as operational qualifications.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - frames correctness, latency, operability, concurrency, and compatibility as coupled database choices.
- [[StoragePerformanceBenchmarking]] - provides the workload and cache discipline needed to validate object-backed storage claims.
- [[SystemReliability]] - durability, recovery, fencing, and complete-snapshot reads define system failure behavior.
- [[DataFormatInteroperability]] - explains the cost of choosing an engine-native representation over an open table format.
- [[DuckDBObjectStorage]] - concrete implementation of the architecture for DuckDB.
- [[SlateDB]] - embedded LSM substrate translating mutable blocks into object-storage keys.

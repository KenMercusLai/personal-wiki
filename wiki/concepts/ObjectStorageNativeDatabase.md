---
title: "Object-Storage-Native Database"
type: concept
tags: [databases, object-storage, durability, distributed-systems]
sources:
  - duckdb-on-object-storage
  - slatedb-benchmark
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[ObjectStorageNativeDatabase]] is an architecture that preserves a database engine's native storage semantics while making immutable object storage the durable source of truth and keeping compute processes replaceable.

## Current Synthesis
The DuckDB implementation shows one way to reconcile mutable database files with immutable objects without introducing an open table format. A filesystem extension translates logical files into path, metadata, and block-aligned content keys over an embedded LSM tree. Atomic write batches make `fsync` durable in the bucket, transactions turn renames into metadata repointing, and committed manifests let readers advance between whole database states.

This choice preserves database-native capabilities such as indexes, enforced constraints, WAL, checkpoints, catalog objects, types, and small writes that a shared Parquet table contract does not necessarily represent. The same choice reduces interoperability: only the owning engine understands the representation, and the bucket no longer contains a directly openable native file.

"Serverless" operation here means eliminating separately operated catalog and compaction services, not eliminating work. Writer processes still compact and garbage-collect data, every durable commit pays object-store latency, caches and manifest polling remain necessary, and a single-writer rule constrains concurrency. The SlateDB benchmark adds that placement is economically material: remote-style persisted-state polling in a colocated process reportedly cost roughly US$40 per month when idle, while in-memory local coordination reduced it below US$5 without excluding remote compactors.

Cache design must also match the intended residency boundary. A coarse 4 MiB object-cache partition makes sense when mirroring most or all of a database locally, but it amplifies small-read misses and produced large p99.9 spikes in SlateDB's balanced workload. Partial caching instead benefits from smaller evictable units; spatial-locality prefetching is a separate optimization rather than a substitute for choosing the right granularity.

## Key Claims
- A virtual filesystem can preserve a database engine and file format while replacing its local-disk durability substrate.
- Block-to-key alignment avoids whole-object rewrites and can make one database block correspond to one point read or write.
- Atomic key-value batches and transactional metadata updates can implement `fsync`, truncation, and rename semantics over immutable objects.
- Manifest checkpoints can give many readers complete committed states while tolerating bounded staleness.
- Native database features and open multi-engine interoperability are competing design goals rather than free complements.
- Eliminating standalone services moves compaction, garbage collection, caching, polling, and fencing into client processes and storage metadata.
- API-call cost and cache-fetch granularity are architectural metrics, not merely deployment tuning details.

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

## Counterevidence & Qualifications
This synthesis rests on maintainer-authored implementation and benchmark accounts. It does not establish that arbitrary databases can safely use the same translation, because filesystem assumptions, block geometry, WAL ordering, locking, rename semantics, recovery, and extension seams differ. Snapshot-consistent polling is not strong consistency, fencing is not immediate mutual exclusion, and one writer may be unacceptable for collaborative transactional workloads. Open table formats remain preferable when Spark, Trino, Flink, or other engines must share the data. The SlateDB cost figures omit full pricing assumptions and total compute, storage, egress, and recovery cost; its cache observations are workload- and configuration-specific.

## What Changed
- Added object-store API cost and cache-fetch granularity as first-class architectural concerns.
- Distinguished colocated in-memory coordination from persisted coordination needed by remote compactors.
- Separated whole-database object mirroring from smaller-unit partial caching.

## Related Concepts
- [[DatabaseEngineeringTradeoffs]] - frames correctness, latency, operability, concurrency, and compatibility as coupled database choices.
- [[StoragePerformanceBenchmarking]] - provides the workload, cache, topology, and cost discipline needed to validate object-backed storage claims.
- [[SystemReliability]] - durability, recovery, fencing, and complete-snapshot reads define system failure behavior.
- [[DataFormatInteroperability]] - explains the cost of choosing an engine-native representation over an open table format.
- [[DuckDBObjectStorage]] - concrete implementation of the architecture for DuckDB.
- [[SlateDB]] - embedded LSM substrate translating mutable blocks into object-storage keys.

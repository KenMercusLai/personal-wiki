---
title: "SlateDB"
type: entity
tags: [storage-engine, lsm-tree, object-storage, rust]
sources:
  - duckdb-on-object-storage
  - slatedb-benchmark
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[SlateDB]] is an embedded Rust LSM-tree storage engine that places durable state in object storage and exposes transactional key-value semantics, caching, compaction, and local or distributed maintenance to embedded applications such as [[DuckDBObjectStorage]].

## Current Profile
SlateDB stores its WAL, memtable flushes, SSTs, and manifest in object storage. In the DuckDB integration, logical paths, file metadata, and 256 KiB content chunks become separate key families, while write batches and transactions implement durable synchronization and atomic renames. Most deployments colocate the writer, compactor, and garbage collector, but distributed compaction can move work to remote machines.

Readers use a non-fencing mode and refresh complete manifest checkpoints, while a read-write opener can take over the manifest and fence an older writer. SlateDB also supplies range scans, point reads, read caching, and an adapter over [[ApacheOpenDAL]] backends. In the current DuckDB stack its WAL duplicates DuckDB's logging.

The public benchmark suite makes application throughput, latency, and object-store API cost observable under roughly 10% cache residency. It has already motivated non-overlap trivial moves, an in-memory local compaction-coordination path that reduced reported idle API cost from roughly US$40 to below US$5 per month, and a clearer cache split: coarse object mirroring for whole-database locality versus smaller evictable Foyer units for partial caching.

## Key Characteristics
- Implements an LSM tree whose persistent structures and manifest reside in object storage.
- Provides atomic write batches and transactions for filesystem sync and rename semantics.
- Supports non-fencing readers that advance among committed manifest states.
- Fences an older writer when a newer writer takes over, but does not reject the second writer immediately.
- Can coordinate compaction locally in memory while preserving persisted state for remote compactors.
- Separates coarse object-store mirroring from smaller-unit block caching according to desired local coverage.

## Evidence
Mutable-object translation:
- [[duckdb-on-object-storage]] contrasts whole-object rewrites with one-key-per-block puts and diagrams path, metadata, and content key families.

Durability and consistency:
- [[duckdb-on-object-storage]] shows dirty chunks and metadata entering one flushed batch, transactional path renames, manifest fencing, and readers observing only complete checkpoints.

Operational and performance boundary:
- [[duckdb-on-object-storage]] states that writer-local compaction and garbage collection consume resources and identifies double logging through both DuckDB and SlateDB WALs.
- [[slatedb-benchmark]] reports routing-induced ingest instability, 4 MiB cache-miss amplification, a non-overlap trivial-move path, and the idle polling-cost reduction from local coordination.

## Qualifications
Both sources are maintainer-authored and supply no independent storage-engine evaluation. The benchmark deliberately compares a roughly 10%-cached remote SlateDB database with a fully local RocksDB database, disables the new trivial-move optimization, and does not provide uncertainty or matched end-to-end cost. It still does not quantify failure recovery, manifest contention, long-running reader consistency, or distributed-compactor failure behavior. Fencing prevents silent divergence but is not immediate mutual exclusion, and bounded reader staleness is not strong read-after-write consistency.

## What Changed
- Added public workload, cost, and tail-latency measurement as part of SlateDB's operating model.
- Added local-versus-remote compaction coordination and quantified the reported idle polling-cost consequence.
- Distinguished coarse whole-database object mirroring from fine-grained partial caching.
- Added non-overlap trivial moves and explicit comparison limits to the performance profile.

## Relationships
- [[DuckDBObjectStorage]] - integration that maps DuckDB files and blocks onto SlateDB keys.
- [[DuckDB]] - supplies the mutable filesystem workload and its own WAL and checkpoints.
- [[ApacheOpenDAL]] - backend interface through which SlateDB reaches storage systems.
- [[ObjectStorageNativeDatabase]] - architecture in which SlateDB reconciles mutable database blocks with immutable objects.
- [[StoragePerformanceBenchmarking]] - public suite used to diagnose routing, compaction, API-cost, and cache-granularity behavior.
- [[SystemReliability]] - durability, fencing, recovery, and garbage collection determine the broader failure model.

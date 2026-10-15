---
title: "SlateDB"
type: entity
tags: [storage-engine, lsm-tree, object-storage, rust]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[SlateDB]] is an embedded Rust LSM-tree storage engine used by [[DuckDBObjectStorage]] to turn immutable object storage into a transactional key-value substrate for mutable DuckDB files.

## Current Profile
SlateDB stores its WAL, memtable flushes, SSTs, and manifest in object storage. The extension maps logical paths, file metadata, and 256 KiB content chunks into separate key families, then uses SlateDB write batches and transactions for durable synchronization and atomic renames. Compaction and garbage collection run inside the writer process rather than as standalone services.

Readers use a non-fencing mode and refresh complete manifest checkpoints, while a read-write opener can take over the manifest and fence an older writer. SlateDB also supplies range scans, point reads, read caching, and an adapter over [[ApacheOpenDAL]] backends. In the current stack its WAL duplicates DuckDB's own logging, which the project identifies as a performance and design issue.

## Key Characteristics
- Implements an LSM tree whose persistent structures and manifest reside in object storage.
- Provides atomic write batches and transactions for filesystem sync and rename semantics.
- Supports non-fencing readers that advance among committed manifest states.
- Fences an older writer when a newer writer takes over, but does not reject the second writer immediately.
- Runs compaction and garbage collection inside the writer process.
- Reaches storage through an OpenDAL operator and supports memory and disk caches above the bucket.

## Evidence
Mutable-object translation:
- [[duckdb-on-object-storage]] contrasts whole-object rewrites with one-key-per-block puts and diagrams path, metadata, and content key families.

Durability and consistency:
- [[duckdb-on-object-storage]] shows dirty chunks and metadata entering one flushed batch, transactional path renames, manifest fencing, and readers observing only complete checkpoints.

Operational and performance boundary:
- [[duckdb-on-object-storage]] states that writer-local compaction and garbage collection consume resources and identifies double logging through both DuckDB and SlateDB WALs.

## Qualifications
The source describes SlateDB only through one integration and supplies no independent storage-engine evaluation. It does not quantify compaction amplification, garbage-collection delay, manifest contention, failure recovery time, request cost, cache effectiveness, or behavior under long-running reader and writer workloads. Fencing prevents silent divergence but is not immediate mutual exclusion, and bounded reader staleness is not strong read-after-write consistency.

## What Changed
- Established SlateDB's role as the transactional object-storage layer beneath DuckDB filesystem semantics.
- Added its manifest-based reader and writer coordination model.
- Recorded writer-local background work and duplicate-WAL cost as material limits.

## Relationships
- [[DuckDBObjectStorage]] - integration that maps DuckDB files and blocks onto SlateDB keys.
- [[DuckDB]] - supplies the mutable filesystem workload and its own WAL and checkpoints.
- [[ApacheOpenDAL]] - backend interface through which SlateDB reaches storage systems.
- [[ObjectStorageNativeDatabase]] - architecture in which SlateDB reconciles mutable database blocks with immutable objects.
- [[SystemReliability]] - durability, fencing, recovery, and garbage collection determine the broader failure model.

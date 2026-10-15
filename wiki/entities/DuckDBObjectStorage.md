---
title: "duckdb_object_storage"
type: entity
tags: [duckdb, object-storage, database-extension, s3]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[DuckDBObjectStorage]] is a DuckDB community extension that exposes bucket-backed storage through the `duckdb_objfs://` filesystem scheme while preserving DuckDB's native database format and behavior.

## Current Profile
The extension substitutes an object-backed filesystem beneath DuckDB rather than defining a new table format or changing the storage engine. Its C++ filesystem implementation forwards calls to a Rust core, which maps paths, metadata, and block-aligned content onto [[SlateDB]] and reaches S3-compatible, local, or memory backends through [[ApacheOpenDAL]]. This keeps DuckDB's indexes, constraints, WAL, checkpoints, catalog, types, `COPY`, and compatible extensions available.

Its concurrency model is one writer and many non-fencing readers. Durable batches and transactional path updates keep readers on complete committed manifest states, but readers can trail the writer by roughly ten seconds. Writer protection is currently eventual fencing: a newer writer can take over before the older writer discovers the conflict on a later flush.

The first-party performance account is close to native for reads but uneven: reported geometric-mean times are 0.92× native for memory-backend TPC-H reads, 1.08× for local-disk reads, and 1.20× for cold S3 reads against HTTPFS. Local writes are reported at only 0.19× native, while writing and delivering to S3 is competitive with a local-write-plus-upload workflow.

## Key Characteristics
- Stores native DuckDB databases through an attached filesystem rather than interoperable Parquet tables.
- Requires no standalone catalog, coordinator, compactor, or metadata database beyond the bucket and client processes.
- Maps each 256 KiB DuckDB block to one SlateDB content key after the 12 KiB database header.
- Flushes dirty chunks, deletes, and metadata as atomic durable write batches and treats checkpoint renames as transactions.
- Supports one fenced writer and multiple snapshot-consistent, potentially stale readers.
- Coalesces adjacent chunks into parallel reads backed by memory and optional disk caches.
- Remains DuckDB-only and lacks immediate writer rejection, directory listing, direct `.duckdb` import, and per-database configuration.

## Evidence
Architecture and feature preservation:
- [[duckdb-on-object-storage]] diagrams the unchanged DuckDB storage engine over `duckdb_objfs`, Rust, SlateDB, and OpenDAL and demonstrates constraints, indexes, checkpoints, and read-only attachment.

Durability and concurrency:
- [[duckdb-on-object-storage]] diagrams atomic `FileSync`, transaction-based rename, manifest fencing, and a reader moving only among complete table rewrites.

Performance and limitations:
- [[duckdb-on-object-storage]] reports TPC-H ratios for memory, local disk, and cold S3; it also reports 0.19× native local-write performance and enumerates staleness, single-writer, compatibility, and configuration limits.

## Qualifications
The evidence is a maintainer-authored launch account rather than independent evaluation. Its benchmarks cover one machine, selected scale factors, a particular remote region, geometric means, and distinct baselines; they do not measure tail latency, request cost, recovery duration, sustained compaction, multi-tenant contention, or broader hardware. “Nothing else to run” excludes separate services but not process-local background work. Snapshot pinning, strong cross-process read-after-write, fail-fast writer exclusion, a single durability log, direct imports, additional backends, and a block-manager integration are roadmap items rather than current guarantees.

## What Changed
- Established the extension's native-database-over-object-storage architecture and operational boundary.
- Recorded its atomic durability, fenced single-writer, snapshot-reader, and caching models.
- Added first-party performance results alongside current compatibility and roadmap limits.

## Relationships
- [[DuckDB]] - host database whose filesystem interface, format, and features the extension preserves.
- [[SlateDB]] - embedded object-storage LSM layer implementing durable mutable-file semantics.
- [[ApacheOpenDAL]] - backend abstraction used to reach S3-compatible, local, and memory stores.
- [[Duckherder]] - distributed execution extension that depends on the shared read-only attachment model.
- [[ObjectStorageNativeDatabase]] - broader architectural pattern exemplified by the extension.
- [[ApacheParquet]] - interoperable representation the extension avoids in order to retain native database features.

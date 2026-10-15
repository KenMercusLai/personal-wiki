---
title: "DuckDB"
type: entity
tags: [database, analytics, embedded, columnar]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[DuckDB]] is an embedded analytical database represented here through its native file format, filesystem and block-manager interfaces, adaptive column compression, database constraints and indexes, WAL and checkpoint behavior, and use as both local and object-backed storage.

## Current Profile
The source treats “a database in a file” as both DuckDB's strength and its distribution boundary. [[DuckDBObjectStorage]] keeps the storage engine and format unchanged while replacing the filesystem underneath, so ordinary SQL, enforced primary, unique, foreign, and check constraints, ART indexes, catalog objects, types, checkpoints, `COPY`, and compatible extensions continue to work when bytes are persisted through object storage.

DuckDB uses a 12 KiB header and 256 KiB blocks in the described version. At checkpoint it measures candidate lightweight compression encodings for each column segment and selects the estimated smallest. Its filesystem API exposes open, read, write, sync, move, and remove operations; a possible future integration at the abstract block-manager layer would avoid converting blocks to byte offsets and back into object keys.

## Key Characteristics
- Operates as an embedded analytical database with a native single-file representation.
- Provides enforced relational constraints, database catalog objects, indexes, WAL, and checkpoints beyond a table format's contract.
- Uses 256 KiB storage blocks after a 12 KiB header in the implementation described by the source.
- Chooses among lightweight column encodings through per-segment analysis at checkpoint.
- Exposes a filesystem interface that extensions can currently replace without modifying the storage engine.
- Has an abstract block-manager seam, but does not yet let this extension inject a custom manager through the direct construction path described.

## Evidence
Database behavior:
- [[duckdb-on-object-storage]] demonstrates tables, primary and foreign keys, unique and check constraints, an ART-backed index, checkpoints, and read-only attachment over the extension.

Storage and compression:
- [[duckdb-on-object-storage]] diagrams the 12 KiB header, 256 KiB blocks, filesystem call chain, and measured selection among compression candidates.

Extension boundary:
- [[duckdb-on-object-storage]] explains that the storage manager currently constructs `SingleFileBlockManager` directly, leaving a custom block manager as future upstream or storage-extension work.

## Qualifications
This profile is derived from one extension maintainer's article and DuckDB 1.5.5-era behavior, not a general or independently validated DuckDB specification. The source's claim that “everything DuckDB does still works” is bounded by redirected SQLLogicTest exclusions, extension compatibility, and operations supported by the virtual filesystem. Native-format preservation also prevents non-DuckDB engines from reading the bucket representation directly.

## What Changed
- Established DuckDB's native-format, constraint, index, WAL, checkpoint, and adaptive-compression profile.
- Added the filesystem extension boundary and proposed block-manager integration path.
- Recorded the file geometry used by the object-storage mapping.

## Relationships
- [[DuckDBObjectStorage]] - extension that replaces DuckDB's filesystem with object-backed mutable storage.
- [[SlateDB]] - maps DuckDB's block-aligned writes onto immutable object storage.
- [[Duckherder]] - distributes queries over shared read-only DuckDB attachments.
- [[ApacheParquet]] - interoperable columnar format contrasted with DuckDB's fuller database semantics.
- [[DatabaseEngineeringTradeoffs]] - frames native features, interoperability, latency, concurrency, and operations as coupled choices.

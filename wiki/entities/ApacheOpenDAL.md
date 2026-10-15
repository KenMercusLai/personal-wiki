---
title: "Apache OpenDAL"
type: entity
tags: [storage, abstraction, object-storage, rust]
sources:
  - duckdb-on-object-storage
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheOpenDAL]] is a storage-access abstraction used beneath SlateDB so [[DuckDBObjectStorage]] can share one code path across S3-compatible object stores, a local filesystem, and memory.

## Current Profile
The integration builds a different OpenDAL `Operator` for each backend while leaving the DuckDB-to-SlateDB layers unchanged. OpenDAL layers also provide backend-neutral request-count, latency, and byte instrumentation exposed through `duckdb_objfs_io_stats()`, while backend implementations preserve relevant semantics such as atomic local writes. The article describes Google Cloud Storage, Azure Blob Storage, and HDFS as near-term feature-flag possibilities rather than current support.

## Key Characteristics
- Presents a common operator interface over multiple storage backends.
- Currently connects the extension to S3 or MinIO, local directories, and memory.
- Supports instrumentation layers used for request, latency, and byte statistics.
- Encapsulates backend-specific semantics below a shared SlateDB code path.
- Makes additional backends plausible but does not itself establish that the integration has tested or shipped them.

## Evidence
Backend abstraction:
- [[duckdb-on-object-storage]] diagrams OpenDAL below SlateDB and names S3-compatible, local-filesystem, and memory operators.

Observability and semantics:
- [[duckdb-on-object-storage]] attributes cross-backend I/O statistics and correct local atomic-write behavior to OpenDAL layers and implementations.

Expansion boundary:
- [[duckdb-on-object-storage]] describes GCS, Azure Blob Storage, and HDFS as mostly a feature flag away while separately listing more backends as roadmap work.

## Qualifications
The source is an account of OpenDAL inside one extension, not a general evaluation of its API, backend coverage, correctness, or performance. Backend-neutral interfaces do not guarantee identical consistency, atomicity, authentication, cost, or failure behavior. Additional backends are prospective until integrated and tested by the extension.

## What Changed
- Established OpenDAL as the backend boundary in the DuckDB object-storage stack.
- Added its role in portable I/O instrumentation and backend-specific semantics.
- Distinguished current backends from proposed feature-flag additions.

## Relationships
- [[SlateDB]] - consumes OpenDAL operators to persist keys, manifests, WAL records, and SSTs.
- [[DuckDBObjectStorage]] - exposes configuration and statistics built on the OpenDAL-backed stack.
- [[DuckDB]] - supplies credentials through its Secret Manager before storage calls reach OpenDAL.
- [[AWS]] - provides the S3 object-store backend used by the article's remote examples.
- [[ObjectStorageNativeDatabase]] - relies on a portable backend layer while retaining native database semantics above it.

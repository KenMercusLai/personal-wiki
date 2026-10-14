---
title: "Database Bypass"
type: concept
tags: [databases, storage, analytics, data-movement]
sources:
  - 2607.07696
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseBypass]] is the controlled extraction of relational data by decoding database-owned storage files directly, avoiding the server query, wire-protocol, row-serialization, and client-conversion path.

## Current Synthesis
The Jailbreak paper treats bulk analytical export as an access-path problem. When a snapshot or replica already exposes PostgreSQL heap segments or MySQL InnoDB tablespaces, a format-specific sequential reader can map stored types into Arrow buffers and hand those buffers to heterogeneous analytical engines without asking the source server to execute and serialize a table scan.

The speed opportunity is real but conditional. It grows when row-oriented connectors dominate end-to-end time and shrinks when engine startup or output encoding dominates. The bypass also moves responsibility outward: the reader must reproduce page traversal, deletion or visibility handling, type decoding, overflow behavior, version compatibility, file consistency, authorization boundaries, and recovery assumptions that the database normally owns.

## Key Claims
- Direct file decoding can eliminate several server and connector stages from snapshot analytics.
- Apache Arrow provides a common zero-copy handoff after database-specific decoding.
- Benefits depend strongly on source connector behavior and downstream engine overhead.
- Correctness requires storage-format, transaction-state, type, version, and snapshot boundaries to be explicit.
- Database bypass complements rather than generally replaces database-managed transactional access.

## Evidence
- Removed stages: [[2607.07696]] contrasts direct sequential file scans with SQL execution, wire transfer, row serialization, and client conversion.
- Interchange: [[2607.07696]] emits Arrow C Data Interface RecordBatches consumed by six analytical engines.
- Performance variation: [[2607.07696]] reports PostgreSQL gains from 1.3x to 5.1x and MySQL gains from 1.4x to 26.9x, with the largest result on a slow row-oriented PyArrow/MySQL path.
- Correctness scope: [[2607.07696]] matches all 22 TPC-H query results in its controlled evaluation while targeting snapshots, read replicas, and offline pipelines.
- Responsibility shift: [[2607.07696]] implements database-specific page traversal, visibility or delete filtering, data-type decoding, BRIN pruning, and Arrow memory ownership in the external reader.

## Counterevidence & Qualifications
One best-of-three TPC-H SF=1 export benchmark on one AWS configuration cannot establish universal throughput or maintenance economics. The experiment includes Parquet writing and framework overhead, and its fastest ratios partly measure weak connector paths. Directly reading changing primary files can violate consistency or safety assumptions; the paper instead targets analytical snapshots. The PostgreSQL reader applies a lightweight visibility heuristic without the complete transaction-status machinery, and both readers map arbitrary-precision numeric or decimal data to float64, so query-result agreement on the tested workload is not proof of universal semantic equivalence. Storage versions, corruption, encryption, compression, overflow cases, access control, and schema evolution also remain part of the operational burden.

## What Changed
- Established database bypass as a conditional snapshot-analytics pattern with an explicit semantic-responsibility transfer.

## Related Concepts
- [[AgenticStorageReaderSynthesis]] - proposes generating the format-specific readers needed for bypass.
- [[PostgreSQLPageArchitecture]] - supplies part of the physical contract a PostgreSQL bypass reader must reproduce.
- [[DatabaseEngineeringTradeoffs]] - bypass exchanges server overhead for format coupling and external correctness obligations.
- [[DatabaseCentricApplicationLogic]] - database-owned behavior may be skipped when data is read below the server boundary.
- [[ColumnarStorageTradeoffs]] - Arrow output changes the downstream scan and interchange representation.
- [[StoragePerformanceBenchmarking]] - end-to-end claims require separating source reads, framework startup, conversion, and output writing.

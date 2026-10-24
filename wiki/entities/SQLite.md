---
title: "SQLite"
type: entity
tags: [database, embedded-database, production]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
  - twelve-years-distributed-sqlite
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[SQLite]] is a single-file relational database that can serve production applications directly or act as the storage engine beneath external replication, recovery, and managed-service layers.

## Current Profile
The source treats SQLite's simplicity as real but conditional. SQLite avoids database servers, ports, user provisioning, connection-pool configuration, and much of the operational overhead of a client-server database. That same single-file design makes remote access, horizontal scaling, multi-machine high availability, and network-filesystem deployment harder.

For production use, SQLite is not mainly limited by database size; Pečar notes its theoretical limit is far beyond ordinary application needs. The more important constraints are configuration defaults, file-system guarantees, one-writer-at-a-time concurrency, serializable transaction behavior, online backup tooling, and limited ALTER TABLE migration support.

The newer history shows that SQLite's local engine can remain useful when a product outgrows a single-node failure model. [[DistributedSQLite]] systems add different machinery around or within it: [[Rqlite]] and dqlite use consensus for ordered cluster writes, Litestream streams the WAL for disaster recovery, and cr-sqlite uses CRDTs for divergent multi-writer convergence. These approaches do not remove tradeoffs; they exchange SQLite's standalone simplicity for specific availability, recovery, consistency, or platform properties.

## Key Characteristics
- Reduces operational complexity by storing the database in a local file instead of running a database service.
- Needs production PRAGMA configuration, especially around foreign keys, WAL mode, durability, mmap, journal size, and cache behavior.
- Supports concurrent reads in WAL mode but allows only one writer per database at a time.
- Is strongest for single-machine, read-heavy web applications with short write transactions.
- Becomes less attractive for multi-machine high availability, heavy parallel writes, long-running transactions, and network or ephemeral file systems.
- Supports external consensus, WAL-streaming, CRDT, filesystem, fork, and managed-platform layers that address different distributed requirements.
- Requires disciplined backup and migration practices because live-file copying is unsafe and ALTER TABLE support is narrower than in PostgreSQL or MySQL.

## Evidence
- Single-file simplicity: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite avoids ports, users, passwords, and connection pools.
- Size qualification: [[anze-pecar-gotchas-with-sqlite-in-production]] says database size is usually not the limiting factor, citing SQLite's very high theoretical limit.
- Configuration: [[anze-pecar-gotchas-with-sqlite-in-production]] recommends PRAGMAs for foreign keys, WAL mode, synchronous behavior, mmap, journal size, and cache size.
- Availability boundary: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite is less appealing when an application must run across multiple machines for high availability.
- Concurrency and transactions: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode allows many readers but only one writer, and recommends short write transactions and `BEGIN IMMEDIATE`.
- Backup and migration limits: [[anze-pecar-gotchas-with-sqlite-in-production]] warns against copying a live SQLite file for backup and notes limited ALTER TABLE support.
- Distributed reuse: [[twelve-years-distributed-sqlite]] traces consensus, WAL-streaming, CRDT, filesystem, forked-engine, and managed-platform systems built around or from SQLite.
- Requirement separation: [[twelve-years-distributed-sqlite]] distinguishes continuous cluster availability, inexpensive restore-oriented recovery, and divergent-writer convergence.

## Qualifications
The sources are practitioner and project-author accounts rather than neutral comparative benchmarks. Workload fit still depends on write rate, transaction duration, availability and recovery targets, file-system guarantees, framework behavior, consistency needs, and tolerance for additional replication or platform machinery. The distributed history supplies no cross-project benchmark or formal equivalence among the systems it groups around SQLite.

## What Changed
- Expanded SQLite from a single-node production profile to an engine reused across consensus, streaming, merge-based, and managed distributed systems.

## Relationships
- [[SQLiteProductionTradeoffs]] - summarizes when SQLite's simplicity helps or hurts production systems.
- [[DatabaseTransactionIsolation]] - SQLite's serializable transactions shape web workload behavior.
- [[DatabaseConsolidation]] - SQLite can simplify a stack even further than a client-server consolidation strategy when one machine is enough.
- [[TechnologyStackComplexity]] - SQLite removes a separate database service but adds file, backup, and concurrency constraints.
- [[ContainerNativePractice]] - ephemeral container file systems can make SQLite unsafe for persistent state.
- [[CloudHighAvailability]] - multi-machine availability pressure weakens SQLite's fit.
- [[DistributedSQLite]] - maps the distinct replication and recovery systems built around SQLite.
- [[Rqlite]] - applies a leader and Raft-replicated log around SQLite for self-operated fault tolerance.

---
title: "SQLite"
type: entity
tags: [database, embedded-database, production]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[SQLite]] is presented as a single-file relational database that can be suitable for production web applications when the application fits a single-machine, read-heavy, low-operations model.

## Current Profile
The source treats SQLite's simplicity as real but conditional. SQLite avoids database servers, ports, user provisioning, connection-pool configuration, and much of the operational overhead of a client-server database. That same single-file design makes remote access, horizontal scaling, multi-machine high availability, and network-filesystem deployment harder.

For production use, SQLite is not mainly limited by database size; Pečar notes its theoretical limit is far beyond ordinary application needs. The more important constraints are configuration defaults, file-system guarantees, one-writer-at-a-time concurrency, serializable transaction behavior, online backup tooling, and limited ALTER TABLE migration support.

## Key Characteristics
- Reduces operational complexity by storing the database in a local file instead of running a database service.
- Needs production PRAGMA configuration, especially around foreign keys, WAL mode, durability, mmap, journal size, and cache behavior.
- Supports concurrent reads in WAL mode but allows only one writer per database at a time.
- Is strongest for single-machine, read-heavy web applications with short write transactions.
- Becomes less attractive for multi-machine high availability, heavy parallel writes, long-running transactions, and network or ephemeral file systems.
- Requires disciplined backups through `VACUUM INTO` or online replication tools rather than copying a live database file.
- Has limited schema-migration ergonomics because ALTER TABLE support is narrower than in PostgreSQL or MySQL.

## Evidence
- Single-file simplicity: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite avoids ports, users, passwords, and connection pools.
- Size qualification: [[anze-pecar-gotchas-with-sqlite-in-production]] says database size is usually not the limiting factor, citing SQLite's very high theoretical limit.
- Configuration: [[anze-pecar-gotchas-with-sqlite-in-production]] recommends PRAGMAs for foreign keys, WAL mode, synchronous behavior, mmap, journal size, and cache size.
- Availability boundary: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite is less appealing when an application must run across multiple machines for high availability.
- Concurrency and transactions: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode allows many readers but only one writer, and recommends short write transactions and `BEGIN IMMEDIATE`.
- Backup and migration limits: [[anze-pecar-gotchas-with-sqlite-in-production]] warns against copying a live SQLite file for backup and notes limited ALTER TABLE support.

## Qualifications
The source is a practitioner article rather than a neutral benchmark suite. It reports one Django and SQLite throughput result and broad operational judgments, but workload fit still depends on write rate, transaction duration, availability targets, file-system guarantees, framework behavior, and team tolerance for SQLite-specific tooling.

## What Changed
- Created SQLite as a production-database entity with its operational fit and limits.

## Relationships
- [[SQLiteProductionTradeoffs]] - summarizes when SQLite's simplicity helps or hurts production systems.
- [[DatabaseTransactionIsolation]] - SQLite's serializable transactions shape web workload behavior.
- [[DatabaseConsolidation]] - SQLite can simplify a stack even further than a client-server consolidation strategy when one machine is enough.
- [[TechnologyStackComplexity]] - SQLite removes a separate database service but adds file, backup, and concurrency constraints.
- [[ContainerNativePractice]] - ephemeral container file systems can make SQLite unsafe for persistent state.
- [[CloudHighAvailability]] - multi-machine availability pressure weakens SQLite's fit.

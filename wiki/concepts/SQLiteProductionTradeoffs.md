---
title: "SQLite Production Tradeoffs"
type: concept
tags: [sqlite, database, operations, architecture]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
  - twelve-years-distributed-sqlite
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[SQLiteProductionTradeoffs]] are the architecture and operations tradeoffs that arise when using SQLite as the primary production database for a web application.

## Current Synthesis
The source's central claim is not that SQLite is only for small projects, but that its production fit depends on the shape of the application. SQLite is compelling when a web app can run on one durable machine, mostly reads data, keeps write transactions short, and values a simpler stack over distributed deployment machinery.

The same design becomes constraining when the application needs multi-machine high availability, remote database access, heavy parallel writes, long-running write transactions, network filesystems, ephemeral container storage, or migration workflows that assume broad ALTER TABLE support. [[DistributedSQLite]] systems can answer narrower versions of these problems, but they do so through different tradeoffs: consensus buys continuous fault-tolerant service, WAL streaming buys inexpensive recovery, and CRDT merging buys leaderless divergent writes. Each adds mechanisms and operational boundaries that the standalone file avoids.

## Key Claims
- SQLite's production ceiling is more often operational shape than raw database size.
- Single-machine deployment can be a strength when vertical scaling and simpler operations meet the product's availability needs.
- Multi-machine availability and horizontal scaling pressure make SQLite less attractive.
- Write concurrency and transaction duration are central workload-fit constraints.
- File-system guarantees, backups, and migrations need SQLite-specific operational discipline.
- Distributed SQLite systems can reduce specific limits, but their consensus, streaming, merge, routing, restore, or platform machinery changes the simplicity advantage rather than preserving it unchanged.

## Evidence
- Size boundary: [[anze-pecar-gotchas-with-sqlite-in-production]] says most applications will not approach SQLite's theoretical size limit.
- Single-machine fit: [[anze-pecar-gotchas-with-sqlite-in-production]] argues many web apps can run on one vertically scaled machine and get enough availability for ordinary needs.
- Multi-machine pressure: [[anze-pecar-gotchas-with-sqlite-in-production]] says higher availability and specialized workloads across machines make SQLite less appealing.
- Write constraints: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode still permits only one writer per database and recommends short write transactions.
- File and backup discipline: [[anze-pecar-gotchas-with-sqlite-in-production]] warns about network filesystems, ephemeral filesystems, unsafe file copying, and the need for VACUUM INTO or online backup tooling.
- Complexity return: [[anze-pecar-gotchas-with-sqlite-in-production]] cautions that libSQL, rqlite, dqlite, and similar projects can become more complex than PostgreSQL or MySQL.
- Mechanism separation: [[twelve-years-distributed-sqlite]] distinguishes leader-and-majority consensus, WAL streaming to object storage, and CRDT-based divergent-writer merging.
- Packaging boundary: [[twelve-years-distributed-sqlite]] contrasts self-operated servers, embedded libraries, filesystem layers, engine forks, and managed edge services.

## Counterevidence & Qualifications
The sources are sympathetic to SQLite but do not establish a universal fit. Read-heavy, single-machine web applications remain good candidates, while write-heavy, multi-machine, long-transaction, or high-durability systems may be better served by PostgreSQL or MySQL. Distributed extensions can satisfy some multi-node or recovery needs, but the historical source provides no comparative performance, failure, cost, or operational evidence showing when their added machinery is preferable to a conventional client-server database.

## What Changed
- Distinguished three distributed responses to SQLite's single-node boundary: consensus availability, streamed recovery, and merge-based multi-writer convergence.
- Reframed extensions as changing the simplicity tradeoff rather than uniformly solving it.

## Related Concepts
- [[SQLite]] - entity whose production use creates these tradeoffs.
- [[DatabaseConsolidation]] - both frames seek simpler data architecture, but SQLite pushes simplification into a local-file model.
- [[TechnologyStackComplexity]] - SQLite can lower service complexity while adding file-system and concurrency constraints.
- [[DatabaseTransactionIsolation]] - transaction behavior is one of SQLite's key production constraints.
- [[CloudHighAvailability]] - high availability requirements determine whether one-machine SQLite remains acceptable.
- [[ContainerNativePractice]] - container file-system behavior can make SQLite persistence unsafe.
- [[DistributedSQLite]] - catalogs replication and recovery approaches that selectively alter these tradeoffs.
- [[Rqlite]] - illustrates the consensus choice for continuous self-operated fault tolerance.

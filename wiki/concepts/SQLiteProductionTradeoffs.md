---
title: "SQLite Production Tradeoffs"
type: concept
tags: [sqlite, database, operations, architecture]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SQLiteProductionTradeoffs]] are the architecture and operations tradeoffs that arise when using SQLite as the primary production database for a web application.

## Current Synthesis
The source's central claim is not that SQLite is only for small projects, but that its production fit depends on the shape of the application. SQLite is compelling when a web app can run on one durable machine, mostly reads data, keeps write transactions short, and values a simpler stack over distributed deployment machinery.

The same design becomes constraining when the application needs multi-machine high availability, remote database access, heavy parallel writes, long-running write transactions, network filesystems, ephemeral container storage, or migration workflows that assume broad ALTER TABLE support. SQLite can still be extended through projects such as LiteFS, Litestream, libSQL, rqlite, or dqlite, but the article warns that these can reintroduce complexity comparable to more traditional databases.

## Key Claims
- SQLite's production ceiling is more often operational shape than raw database size.
- Single-machine deployment can be a strength when vertical scaling and simpler operations meet the product's availability needs.
- Multi-machine availability and horizontal scaling pressure make SQLite less attractive.
- Write concurrency and transaction duration are central workload-fit constraints.
- File-system guarantees, backups, and migrations need SQLite-specific operational discipline.
- Distributed SQLite-adjacent tools can reduce specific limits but may erase the simplicity advantage.

## Evidence
- Size boundary: [[anze-pecar-gotchas-with-sqlite-in-production]] says most applications will not approach SQLite's theoretical size limit.
- Single-machine fit: [[anze-pecar-gotchas-with-sqlite-in-production]] argues many web apps can run on one vertically scaled machine and get enough availability for ordinary needs.
- Multi-machine pressure: [[anze-pecar-gotchas-with-sqlite-in-production]] says higher availability and specialized workloads across machines make SQLite less appealing.
- Write constraints: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode still permits only one writer per database and recommends short write transactions.
- File and backup discipline: [[anze-pecar-gotchas-with-sqlite-in-production]] warns about network filesystems, ephemeral filesystems, unsafe file copying, and the need for VACUUM INTO or online backup tooling.
- Complexity return: [[anze-pecar-gotchas-with-sqlite-in-production]] cautions that libSQL, rqlite, dqlite, and similar projects can become more complex than PostgreSQL or MySQL.

## Counterevidence & Qualifications
The article is sympathetic to SQLite but not universalist. It treats read-heavy, single-machine web applications as good candidates, while write-heavy, multi-machine, long-transaction, or high-durability systems may be better served by PostgreSQL or MySQL.

## What Changed
- Created the concept to capture SQLite's production fit as a conditional simplicity tradeoff.

## Related Concepts
- [[SQLite]] - entity whose production use creates these tradeoffs.
- [[DatabaseConsolidation]] - both frames seek simpler data architecture, but SQLite pushes simplification into a local-file model.
- [[TechnologyStackComplexity]] - SQLite can lower service complexity while adding file-system and concurrency constraints.
- [[DatabaseTransactionIsolation]] - transaction behavior is one of SQLite's key production constraints.
- [[CloudHighAvailability]] - high availability requirements determine whether one-machine SQLite remains acceptable.
- [[ContainerNativePractice]] - container file-system behavior can make SQLite persistence unsafe.

---
title: "Gotchas with SQLite in Production"
type: source
tags: [sqlite, database, production, operations]
date: 2024-07-17
source_file: /mnt/ken_personal_wiki/Articles/Anže Pečar - Gotchas with SQLite in Production.md
---

## Summary
Anže Pečar argues that [[SQLite]] can be a strong production database for many web applications when teams want a simpler single-machine stack, but only if they understand its operational boundaries. The article's core tradeoff is that SQLite reduces database service complexity while making multi-machine deployment, high availability, write concurrency, transaction handling, backups, and schema migrations more constrained than with PostgreSQL or MySQL. The embedded isolation-level table reinforces the transaction section by showing that serializable isolation prevents dirty, non-repeatable, and phantom reads while weaker isolation levels allow more anomalies.

## Key Claims
- [[SQLiteProductionTradeoffs]] center on operational simplicity for single-machine, read-heavy web apps rather than on a small-dataset limit.
- [[SQLite]] needs production-oriented PRAGMA configuration such as foreign keys, WAL mode, synchronous behavior, mmap, journal size, and cache settings.
- SQLite's single-file design removes network database administration but makes horizontal scaling, remote GUI access, and high availability harder than client-server databases.
- Network and ephemeral file systems are risky for SQLite because lock guarantees or persistence may be insufficient; LiteFS and Fly.io are partial answers with write-routing constraints.
- SQLite allows multiple readers in WAL mode but only one writer per database, so write-heavy workloads and long write transactions can become throughput bottlenecks.
- [[DatabaseTransactionIsolation]] matters because SQLite uses serializable transactions, requires short write transactions, and benefits from `BEGIN IMMEDIATE` in web request paths that write.
- SQLite backups and migrations need care: copying the live database file can corrupt backups, online backups need tools such as Litestream, and limited ALTER TABLE support complicates migration tooling.

## Key Quotes
> "The main benefit that you are getting with SQLite is lower operational complexity." - conclusion.

> "As soon as you need multiple machines, have a write-heavy workload, or long-running transactions, SQLite becomes less appealing" - boundary condition.

## Connections
- [[AnzePecar]] - author of the production SQLite article.
- [[SQLite]] - central database being evaluated for production use.
- [[SQLiteProductionTradeoffs]] - the article's main architectural judgment.
- [[DatabaseTransactionIsolation]] - the inspected image and transaction section explain SQLite's serializable behavior and write-lock implications.
- [[DatabaseConsolidation]] - SQLite is another simplification path, but with a narrower deployment envelope than the PostgreSQL-first material.
- [[TechnologyStackComplexity]] - SQLite reduces service and networking surface area when a single-machine architecture is acceptable.
- [[CloudHighAvailability]] - SQLite becomes less appealing when high availability requires multiple machines.
- [[ContainerNativePractice]] - ephemeral container filesystems can erase SQLite changes on restart or redeploy.

## Contradictions
- No direct contradictions found. The source complements the PostgreSQL-first consolidation thread by showing a more radical simplicity option, while qualifying it more sharply around multi-machine availability, write concurrency, and operational tooling.

---
title: "Database Transaction Isolation"
type: concept
tags: [database, transactions, concurrency]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseTransactionIsolation]] is the set of guarantees a database gives concurrent transactions about which intermediate or conflicting changes they can observe.

## Current Synthesis
The SQLite source uses transaction isolation as a practical web-application concern. SQLite transactions are serializable, while many web frameworks commonly operate with read-committed expectations on PostgreSQL or MySQL. The inspected isolation-level table shows the tradeoff: serializable prevents dirty reads, non-repeatable reads, and phantom reads, while weaker levels permit some of those phenomena.

In SQLite, the stronger isolation model interacts with file-level write locking. WAL mode permits multiple concurrent readers, but only one read-write transaction can proceed per database at a time. For web applications, Pečar's operational guidance is to avoid wrapping pure reads in write-capable transactions, keep writes short, and use `BEGIN IMMEDIATE` for write paths so lock contention surfaces predictably instead of failing during a read-to-write upgrade.

## Key Claims
- Isolation level is an application behavior constraint, not only a database-theory category.
- Serializable isolation prevents dirty, non-repeatable, and phantom reads but can reduce write concurrency.
- SQLite's WAL mode allows concurrent read transactions while still limiting writes to one transaction per database.
- Web applications can often approximate read-committed behavior by starting transactions only when writes are needed.
- `BEGIN IMMEDIATE` can make SQLite write-lock acquisition explicit and reduce surprising database-locked failures.

## Evidence
- Isolation table: [[anze-pecar-gotchas-with-sqlite-in-production]] includes a table showing serializable as preventing dirty reads, non-repeatable reads, and phantom reads.
- SQLite default constraint: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite uses serializable transactions while PostgreSQL and MySQL let applications choose isolation levels.
- WAL behavior: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode permits multiple readers but only one read-write transaction.
- Web-application guidance: [[anze-pecar-gotchas-with-sqlite-in-production]] recommends short write transactions and `BEGIN IMMEDIATE` for write transactions.

## Counterevidence & Qualifications
The source discusses transaction isolation mainly through SQLite's production behavior. It does not provide a full comparison of isolation implementation details across PostgreSQL, MySQL, or other databases, and the best isolation choice depends on application invariants rather than framework defaults alone.

## What Changed
- Created the concept from the SQLite transaction section and inspected isolation-level table.

## Related Concepts
- [[SQLite]] - SQLite's serializable transactions and one-writer behavior motivate the concept here.
- [[SQLiteProductionTradeoffs]] - transaction isolation is one of SQLite's key production fit constraints.
- [[SystemReliability]] - transaction boundaries affect correctness and failure behavior under concurrency.
- [[SoftwareVerification]] - concurrent transaction assumptions need tests when application correctness depends on them.

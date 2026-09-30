---
title: "Database Transaction Isolation"
type: concept
tags: [database, transactions, concurrency]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
  - jaana-dogan-things-i-wished-more-developers-knew-about-databases
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseTransactionIsolation]] is the set of guarantees a database gives concurrent transactions about which intermediate or conflicting changes they can observe.

## Current Synthesis
The sources treat transaction isolation as a practical application constraint rather than only a database-theory category. Isolation models form a broader hierarchy than the four SQL-standard names, and database engines can map the same advertised level to different actual guarantees. The inspected cross-engine table is only partial, but it illustrates why applications must test anomaly behavior instead of relying on a label.

In SQLite, the stronger isolation model interacts with file-level write locking. WAL mode permits multiple concurrent readers, but only one read-write transaction can proceed per database at a time. For web applications, Pečar's operational guidance is to avoid wrapping pure reads in write-capable transactions, keep writes short, and use `BEGIN IMMEDIATE` for write paths so lock contention surfaces predictably instead of failing during a read-to-write upgrade.

Dogan extends the concern beyond dirty reads, non-repeatable reads, and phantoms. Write skew can preserve every individual write yet violate a cross-row business invariant when concurrent transactions make decisions from compatible snapshots. Serializable isolation, database constraints, or schema design can prevent some such anomalies; optimistic version checks can also avoid holding an exclusive lock when the application can detect and retry a conflicting row update.

## Key Claims
- Isolation names do not guarantee identical behavior across database engines or implementations.
- Stronger isolation prevents more concurrency anomalies but can increase coordination, contention, and latency.
- SQLite's WAL mode allows concurrent read transactions while still limiting writes to one transaction per database.
- Web applications can often approximate read-committed behavior by starting transactions only when writes are needed.
- `BEGIN IMMEDIATE` can make SQLite write-lock acquisition explicit and reduce surprising database-locked failures.
- Optimistic version checks can detect row-level conflicts without holding a long-lived exclusive lock.
- Write skew shows that correctness can fail even when there is no dirty read or lost write.

## Evidence
- Isolation table: [[anze-pecar-gotchas-with-sqlite-in-production]] includes a table showing serializable as preventing dirty reads, non-repeatable reads, and phantom reads.
- SQLite default constraint: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite uses serializable transactions while PostgreSQL and MySQL let applications choose isolation levels.
- WAL behavior: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode permits multiple readers but only one read-write transaction.
- Web-application guidance: [[anze-pecar-gotchas-with-sqlite-in-production]] recommends short write transactions and `BEGIN IMMEDIATE` for write transactions.
- Model hierarchy: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] includes a diagram ranging from weak read guarantees through serializability, linearizability, and strict serializability.
- Engine variation: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] includes a partial Hermitage table where advertised PostgreSQL and MySQL levels map to different actual isolation behavior.
- Optimistic locking: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] demonstrates an atomic update guarded by an expected version number.
- Invariant anomaly: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] gives a concurrent on-call assignment example where both transactions commit but the intended cardinality rule is violated.

## Counterevidence & Qualifications
The sources provide practitioner explanations, not an exhaustive or current engine conformance study. The cross-engine screenshot is cropped, the article's database details date to 2020, and nominal serializability may be implemented differently. Optimistic locking detects only conflicts represented by its guard, while multi-row invariants may still require constraints, schema changes, or stronger isolation. The best choice depends on actual application invariants, contention, retries, and workload cost rather than framework defaults alone.

## What Changed
- Expanded the concept from SQLite behavior to engine-specific interpretation of isolation labels.
- Added optimistic version checks and write skew as practical concurrency patterns.
- Qualified the partial Hermitage comparison and the limits of row-level conflict detection.

## Related Concepts
- [[SQLite]] - SQLite's serializable transactions and one-writer behavior motivate the concept here.
- [[SQLiteProductionTradeoffs]] - transaction isolation is one of SQLite's key production fit constraints.
- [[SystemReliability]] - transaction boundaries affect correctness and failure behavior under concurrency.
- [[SoftwareVerification]] - concurrent transaction assumptions need tests when application correctness depends on them.
- [[DatabaseEngineeringTradeoffs]] - isolation guarantees trade anomaly prevention against coordination and contention.
- [[DistributedConsensus]] - distributed ordering, partitions, and clocks constrain stronger consistency guarantees.

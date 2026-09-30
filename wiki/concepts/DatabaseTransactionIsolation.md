---
title: "Database Transaction Isolation"
type: concept
tags: [database, transactions, concurrency]
sources:
  - anze-pecar-gotchas-with-sqlite-in-production
  - jaana-dogan-things-i-wished-more-developers-knew-about-databases
  - laisky-reading-notes-on-designing-data-intensive-applications
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DatabaseTransactionIsolation]] is the set of guarantees a database gives concurrent transactions about which intermediate or conflicting changes they can observe.

## Current Synthesis
The sources treat transaction isolation as a practical application constraint rather than only a database-theory category. Isolation models form a broader hierarchy than the four SQL-standard names, and database engines can map the same advertised level to different actual guarantees. The inspected cross-engine table is only partial, but it illustrates why applications must test anomaly behavior instead of relying on a label.

In SQLite, the stronger isolation model interacts with file-level write locking. WAL mode permits multiple concurrent readers, but only one read-write transaction can proceed per database at a time. For web applications, Pečar's operational guidance is to avoid wrapping pure reads in write-capable transactions, keep writes short, and use `BEGIN IMMEDIATE` for write paths so lock contention surfaces predictably instead of failing during a read-to-write upgrade.

Dogan extends the concern beyond dirty reads, non-repeatable reads, and phantoms. Write skew can preserve every individual write yet violate a cross-row business invariant when concurrent transactions make decisions from compatible snapshots. Serializable isolation, database constraints, or schema design can prevent some such anomalies; optimistic version checks can also avoid holding an exclusive lock when the application can detect and retry a conflicting row update.

Laisky's notes add a mechanism-level comparison. MVCC gives transactions a stable versioned view; explicit row locks can prevent lost updates; predicate locks protect matching sets against phantoms; two-phase locking can provide serializability while creating blocking and deadlocks; and serializable snapshot isolation lets work proceed optimistically but may abort transactions when dangerous dependencies appear. Safe retrying and idempotent effects remain part of correctness because stronger isolation does not decide what an application should do after an abort or uncertain outcome.

## Key Claims
- Isolation names do not guarantee identical behavior across database engines or implementations.
- Stronger isolation prevents more concurrency anomalies but can increase coordination, contention, and latency.
- SQLite's WAL mode allows concurrent readers but only one writer, so web applications should keep write-capable transactions short and start them only when needed.
- `BEGIN IMMEDIATE` can make SQLite write-lock acquisition explicit and reduce surprising database-locked failures.
- Optimistic version checks can detect row-level conflicts without holding a long-lived exclusive lock.
- Write skew shows that correctness can fail even when there is no dirty read or lost write.
- MVCC, explicit locks, predicate locks, 2PL, and SSI offer different ways to preserve invariants, with different blocking, abort, and implementation costs.

## Evidence
- Isolation table: [[anze-pecar-gotchas-with-sqlite-in-production]] includes a table showing serializable as preventing dirty reads, non-repeatable reads, and phantom reads.
- SQLite default constraint: [[anze-pecar-gotchas-with-sqlite-in-production]] says SQLite uses serializable transactions while PostgreSQL and MySQL let applications choose isolation levels.
- WAL behavior: [[anze-pecar-gotchas-with-sqlite-in-production]] says WAL mode permits multiple readers but only one read-write transaction.
- Web-application guidance: [[anze-pecar-gotchas-with-sqlite-in-production]] recommends short write transactions and `BEGIN IMMEDIATE` for write transactions.
- Model hierarchy: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] includes a diagram ranging from weak read guarantees through serializability, linearizability, and strict serializability.
- Engine variation: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] includes a partial Hermitage table where advertised PostgreSQL and MySQL levels map to different actual isolation behavior.
- Optimistic locking: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] demonstrates an atomic update guarded by an expected version number.
- Invariant anomaly: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] gives a concurrent on-call assignment example where both transactions commit but the intended cardinality rule is violated.
- Mechanism comparison: [[laisky-reading-notes-on-designing-data-intensive-applications]] relates MVCC and snapshot isolation to version visibility, row and predicate locks to conflicting writes and phantoms, 2PL to blocking, and SSI to optimistic aborts.

## Counterevidence & Qualifications
The sources provide practitioner explanations, not an exhaustive or current engine conformance study. The cross-engine screenshot is cropped, several database details are historical, and nominal serializability may be implemented differently. Optimistic locking detects only conflicts represented by its guard, predicate protection can be expensive, and SSI may trade blocking for aborts. Multi-row invariants may still require constraints or schema changes, so the best choice depends on actual invariants, contention, retries, and workload cost rather than framework defaults alone.

## What Changed
- Added a mechanism-level comparison of MVCC, explicit locking, predicate protection, 2PL, and SSI.
- Added retry safety as an application responsibility after aborts or uncertain outcomes.

## Related Concepts
- [[SQLite]] - SQLite's serializable transactions and one-writer behavior motivate the concept here.
- [[SQLiteProductionTradeoffs]] - transaction isolation is one of SQLite's key production fit constraints.
- [[SystemReliability]] - transaction boundaries affect correctness and failure behavior under concurrency.
- [[SoftwareVerification]] - concurrent transaction assumptions need tests when application correctness depends on them.
- [[DatabaseEngineeringTradeoffs]] - isolation guarantees trade anomaly prevention against coordination and contention.
- [[DistributedConsensus]] - distributed ordering, partitions, and clocks constrain stronger consistency guarantees.
- [[DataIntensiveSystems]] - places transaction isolation among the wider correctness and coordination boundaries of data systems.

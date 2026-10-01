---
title: "Forward-Only Database Migration"
type: concept
tags: [databases, deployment, migrations, compatibility]
sources:
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ForwardOnlyDatabaseMigration]] is a production-change strategy that keeps old and new application versions compatible with staged schema changes, records applied migrations, and repairs mistakes through later migrations instead of assuming schema rollback can restore prior system state.

## Current Synthesis
Stack Overflow's 2016 process combined human coordination, deterministic execution, and compatibility sequencing. Developers reserved a numbered migration, exercised it through the same runner used by higher tiers, and wrote it to tolerate repeat execution. The migrator loaded scripts once, ran pending work across many databases in parallel, and stored each filename, content hash, execution time, and duration. A same-name hash mismatch stopped execution unless explicitly forced.

The safety boundary was mixed-version behavior. Additions were introduced nullable or unused before code depended on them; constraints could follow later. Removals reversed that order: code stopped using an object before a later migration dropped it. API evolution used the same expand-migrate-contract shape. Migration numbers did not guarantee execution order, so individual scripts had to avoid hidden ordering assumptions.

## Key Claims
- Schema and application changes should be sequenced so adjacent deployed versions can coexist.
- Additive changes normally precede their use, while destructive changes follow removal of every caller.
- Idempotent migrations reduce repeat-execution risk but do not make every ordering safe.
- A per-database ledger of filename and content hash makes applied state inspectable and detects edited history.
- Forward repair is often simpler than cross-database rollback when changes are small and frequent.
- Local and preproduction execution should use the real migration runner rather than only ad hoc SQL tests.

## Evidence
- Compatibility sequencing: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] describes nullable additions, later constraints, code-first removals, and a three-deployment API change pattern.
- Execution model: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] says the migrator finds pending scripts from each database's ledger and runs databases in parallel.
- History integrity: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] describes filename-content hashes and aborting when an already recorded migration's hash changes.
- Forward recovery: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] says the tool has no rollback concept and that the team normally fixes mistakes with another migration.

## Counterevidence & Qualifications
This is one team's 2016 process, not proof that rollback is never useful. Idempotence does not remove locking, long-running DDL, replication, data-loss, partial-commit, cross-service, or external-effect risk. The source allows a no-transaction marker and a force option but does not define governance for either escape hatch. Running many databases in parallel improves elapsed time while increasing simultaneous load and blast radius. Some changes require backfills, shadow reads, dual writes, online schema tools, backup restoration, or explicit reversible plans beyond this example.

## What Changed
- Created the concept from Stack Overflow's numbered, hashed, idempotent migration process.
- Distinguished migration execution order from safe application-schema compatibility order.
- Added forward repair as a bounded operating preference rather than a universal prohibition on rollback.

## Related Concepts
- [[DeploymentPipeline]] - database migration is an ordered stage in the path to production.
- [[RollingDeployment]] - mixed application versions require compatible schema and API changes.
- [[ContinuousDelivery]] - small frequent changes make forward correction more practical.
- [[ChangeSafety]] - ledgers, hashes, idempotence, and staged compatibility bound change risk.
- [[DatabaseTransactionIsolation]] - transaction behavior affects what concurrent work can observe during migration.
- [[TrunkBasedDevelopment]] - frequent mainline integration keeps migration and application changes close together.

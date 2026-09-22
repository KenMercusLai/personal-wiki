---
title: "Two-Phase Commit"
type: concept
tags: [distributed-systems, transactions, atomicity, fault-tolerance]
sources:
  - unmesh-joshi-two-phase-commit
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[TwoPhaseCommit]] is a coordinator-led atomic-commit protocol in which every participant first promises that it can complete a transaction, after which all participants are told to commit or roll back as one decision.

## Current Synthesis
Two-phase commit separates readiness from execution. In the prepare phase, each participant acquires the resources it will need, such as locks, and reports whether it can promise to commit. If any participant cannot make that promise, the coordinator aborts the transaction and tells the participants to roll back and release their resources. Only unanimous preparation allows the coordinator to begin the commit phase.

The promise must survive failure rather than exist only in memory. Participants durably record their decisions, for example in a write-ahead log, so a node that crashes and restarts can continue the protocol. The pattern thereby coordinates one atomic outcome across nodes, but its suitability depends on whether the business invariant truly needs to span those nodes. The wiki's microservices evidence argues that teams should usually prefer smaller local transaction boundaries and communicate cross-boundary consistency through immutable events when delayed reconciliation is acceptable.

## Key Claims
- Prepare establishes whether every participant can guarantee a later commit.
- Participants acquire required resources before voting yes and retain enough state to honor that promise.
- Any failed prepare vote causes a global rollback; unanimous preparation permits the commit phase.
- Durable decision records allow a restarted participant to finish the protocol after a crash.
- Two-phase commit should be reserved for invariants that genuinely require cross-resource atomicity rather than used to preserve unnecessarily broad service transactions.

## Evidence
- Phase and decision structure: [[unmesh-joshi-two-phase-commit]] describes prepare as the promise phase and commit as the phase that carries out the update after unanimous agreement.
- Resource acquisition and abort: [[unmesh-joshi-two-phase-commit]] says participants acquire requirements such as locks during prepare, then release them on a coordinator-directed rollback if any node cannot promise.
- Crash recovery: [[unmesh-joshi-two-phase-commit]] requires durable decisions through a mechanism such as a write-ahead log so restarted nodes can complete the protocol.
- Boundary selection: [[christian-posta-the-hardest-part-about-microservices-your-data]] argues that many apparent cross-service invariants can be reduced to smaller aggregate transactions and reconciled with events without two-phase commit.

## Counterevidence & Qualifications
Joshi's source is a concise mechanism overview rather than a complete protocol specification. It does not cover coordinator failure, participants waiting on an unavailable decision, message loss or duplication, recovery-state details, isolation, heuristic outcomes, implementation variants, or performance costs. Posta's microservices guidance does not show that two-phase commit is never appropriate; it asks teams to verify the business invariant and accept the coupling only when atomicity is genuinely required.

## What Changed
- Created a protocol-specific page separating prepare promises from the final commit-or-rollback decision.
- Qualified the mechanism with the existing evidence for smaller aggregate boundaries and event-driven reconciliation.

## Related Concepts
- [[AggregateTransactionBoundary]] - identifies the smallest business invariant that may require atomic commitment.
- [[EventDrivenConsistency]] - offers delayed cross-boundary reconciliation when one distributed transaction is unnecessary.
- [[DistributedProgramming]] - two-phase commit coordinates state changes across independent nodes.
- [[SystemReliability]] - durable protocol state supports recovery after participant crashes.
- [[ReplicatedLog]] - both use durable ordered records, but replicated logs coordinate a shared execution history rather than one transaction's commit decision.

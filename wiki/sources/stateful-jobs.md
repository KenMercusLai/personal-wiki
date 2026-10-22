---
title: "Stateful jobs"
type: source
tags: [distributed-systems, scheduling, state-management, reliability]
date: 2026-09-21
source_file: /mnt/ken_personal_wiki/Articles/stateful-jobs.md
---

## Summary
[[JaanaDogan]] argues that durable state changes job scheduling from short-lived resource placement into lifecycle management. A scheduler for long-running stateful work must coordinate identity, local data, upgrades, application-safe interruption, corruption recovery, and suspension costs because moving or restarting a process can be expensive or unsafe.

The article identifies an underserved layer between general-purpose orchestrators and specialized runtimes, but presents a design argument rather than an implementation or evaluated system.

## Key Claims
- [[StatefulJobScheduling]] cannot treat workers as interchangeable when identity is bound to an embedded store, local checkpoint, in-memory index, stream partition, or warm cache.
- Placement becomes a durable commitment that trades locality and cache warmth against hotspot balancing, temporary node unreachability, and the risk of two workers mutating the same state.
- Every binary upgrade is also a state migration because forward compatibility, rollback after partial mutation, urgent patching, and long-lived mixed-version operation can affect correctness.
- A scheduler needs application-level lifecycle signals because CPU, memory, exit codes, and generic health checks cannot reveal whether a job can be safely preempted, suspended, resumed, or reconnected.
- Restart is not a universal repair strategy for a stateful process: an OOM kill or unclean crash can corrupt write buffers, memtables, caches, connection state, or accumulated progress.
- Zero client traffic does not prove idleness when a job may be compacting, collecting garbage, maintaining peer heartbeats, or preserving leases and connections.
- A general stateful scheduler would need to combine scheduling policy with storage semantics, recovery profiles, migration paths, and application coordination while remaining usable for arbitrary workloads.

## Key Quotes
> "Once jobs carry state, almost every core assumption breaks down." - on the difference between stateless allocation and stateful lifecycle management.

> "You cannot separate scheduling policy from storage semantics." - on why a stateful scheduler is a distributed-systems substrate rather than only a bin-packing layer.

## Connections
- [[JaanaDogan]] - author presenting the stateful-scheduler design argument.
- [[StatefulJobScheduling]] - synthesis of placement, upgrade, recovery, and idleness requirements for state-carrying work.
- [[SystemReliability]] - crashes, corruption, recovery, and long-lived mixed versions turn scheduling decisions into reliability decisions.
- [[ChangeSafety]] - state compatibility and partial mutation make upgrades operational migrations rather than simple binary replacement.
- [[BackupAndRecovery]] - checkpoints and snapshots only help when they are consistent, compatible, and practical to restore.
- [[ServiceHealthChecks]] - application semantics must inform whether a stateful process is safe to interrupt or genuinely idle.
- [[TaskQueueDesign]] - adjacent scheduling domain whose retry and recovery behavior also depends on workload semantics.

## Contradictions
- The source does not say stateless schedulers are useless or that every stateful workload needs one new general-purpose platform. It argues that existing allocation assumptions are insufficient when durable local or application state materially changes movement, restart, and upgrade costs.
- The proposed gap is not supported by a system design, benchmark, failure test, workload survey, or comparison with current orchestrators and specialized operators. Its universality and practical architecture therefore remain open.

---
title: "Data Durability"
type: concept
tags: [distributed-systems, databases, reliability]
sources:
  - distributed-architecture-concepts-i-learned-while-building-a-large-payments-system
  - atc20-rebello
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[DataDurability]] is the guarantee that data acknowledged as successfully stored remains recoverable across subsequent crashes, node loss, or storage corruption within an explicitly defined failure model.

## Current Synthesis
Durability protects the historical fact that an acknowledged operation completed, but the guarantee spans layers. At cluster level, replication can let a surviving node serve or restore a payment record after one storage node fails. At host level, an application still depends on buffers, the page cache, filesystem rules, device writes, and recovery logic agreeing about what an acknowledgement means.

The `fsync` study shows why a successful-path API cannot define the failure contract by itself. After an injected write fault, three tested Linux filesystems marked pages clean even when data was not safely written; some retained newer content in memory than on disk, and one mode reported failure only on a later call. Database recovery could then accept cached state that was not durable or discard logs before stale disk state became visible.

Durability must therefore state acknowledgement conditions, persistent authority, cache treatment, error timing, replication policy, failure independence, repair, backup, and tested recovery behavior. It is distinct from availability, which asks whether the system can respond now, and from consistency, which asks what state concurrent readers and writers observe.

## Key Claims
- Successfully acknowledged payment records should remain recoverable after component failure.
- Durability is an end-to-end property across application, cache, filesystem, device, and replicated storage layers.
- Replication can preserve a record after node loss, but only if the acknowledged local or quorum writes were actually durable within the promised fault model.
- A failed persistence barrier may leave data wholly persisted, partly persisted, or absent; immediate retry is not inherently safe.
- Recovery must establish authoritative persistent state rather than trust clean page-cache contents.
- Durability, availability, and consistency protect different system properties.

## Evidence
- Payment invariant: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] says completed transactions could not be lost and therefore required cluster-level durability.
- Replication mechanism: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] names replication as the usual way to keep data available after node failure.
- Visual failure model: [[distributed-architecture-concepts-i-learned-while-building-a-large-payments-system]] retains a three-step diagram in which one of two record copies survives a storage-node failure and returns the data.
- Persistence ambiguity: [[atc20-rebello]] finds that ext4, XFS, and Btrfs marked pages clean after injected write failures, while memory contents and error timing differed.
- Recovery authority: [[atc20-rebello]] reports application anomalies when recovery consumed page-cache contents that did not match persistent disk state.
- Strategy limits: [[atc20-rebello]] finds no universally sufficient response among ignoring errors, rollback, checksums, crash-restart, and partial direct I/O in its tested workloads.

## Counterevidence & Qualifications
The payments source does not specify write acknowledgement thresholds, replica geography, correlated failures, repair windows, backup and restore, accidental deletion, ransomware, or empirical durability rates. Its database examples show configurable options, not equivalent guarantees, and its retained diagram illustrates one-node survival rather than complete durability. The `fsync` evidence is also bounded: it covers Linux 5.2.11, three filesystems, five application versions, simple insert/update workloads, and single transient write faults. It should shape failure models and tests, not be treated as a permanent claim about current releases or every storage stack.

## What Changed
- Expanded durability from a cluster-replication requirement into an end-to-end acknowledgement and recovery contract.
- Added failed-`fsync`, page-cache divergence, delayed error reporting, and persistent-authority constraints.
- Qualified the new storage findings by kernel, version, workload, and fault model.

## Related Concepts
- [[DurableMessaging]] - applies persistence and replication to in-flight work rather than database records.
- [[IdempotentPaymentProcessing]] - depends on retained operation state to recognize retries after failures.
- [[DistributedPaymentArchitecture]] - combines durable state with selective consistency and delivery guarantees.
- [[CloudHighAvailability]] - focuses on continued service through infrastructure failure rather than preservation alone.
- [[FsyncFailureSemantics]] - defines what can and cannot be inferred when a local persistence barrier fails.
- [[BackupAndRecovery]] - restores durable state after primary-path guarantees or live copies fail.

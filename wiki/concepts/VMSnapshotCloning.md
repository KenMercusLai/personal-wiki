---
title: "VM Snapshot Cloning"
type: concept
tags: [virtualization, snapshots, memory, startup]
sources:
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[VMSnapshotCloning]] creates multiple virtual machines by repeatedly restoring a prepared snapshot of memory, registers, and device state rather than booting and initializing each VM independently.

## Current Synthesis
In the Aurora DSQL case, the system boots Linux, starts PostgreSQL and supporting agents, loads database-specific metadata, and captures that prepared state once. New query processors restore the snapshot, avoiding repeated initialization. The clones can share unchanged clean pages while receiving private copies when they write, so the technique improves both startup work and memory density. Correct cloning must also regenerate state that is supposed to be unique, such as random-number generator state.

## Key Claims
- Prepared snapshots move repeated boot and application initialization out of the critical creation path.
- One snapshot can be restored many times for equivalent workers.
- Clean memory pages can be physically shared across clones without sharing writable state.
- Copy-on-write dirty pages preserve per-VM modification boundaries.
- Clone correctness requires deliberate restoration of per-instance uniqueness.

## Evidence
- Snapshot contents: [[seven-years-of-firecracker-marcs-blog]] describes Firecracker writing VM memory, registers, and device state to a file.
- Prepared processor: [[seven-years-of-firecracker-marcs-blog]] snapshots Linux, PostgreSQL, support agents, customization, and loaded metadata before query-processor demand arrives.
- Startup effect: [[seven-years-of-firecracker-marcs-blog]] says restoration is orders of magnitude faster than repeating the full startup path.
- Page categories: [[seven-years-of-firecracker-marcs-blog]] diagrams exclusive dirty pages, shared clean pages, and empty per-microVM capacity.
- Uniqueness requirement: [[seven-years-of-firecracker-marcs-blog]] notes extra plumbing for correct random numbers in cloned VMs.

## Counterevidence & Qualifications
The article gives no timings, memory quantities, cache measurements, concurrency results, or comparison with alternative process and container initialization. Snapshot preparation can introduce staleness, secret duplication, identity collisions, device-state assumptions, and patch-distribution concerns that the source does not analyze. Page sharing remains safe only while shared pages are clean and write isolation is correctly enforced.

## What Changed
- Created the concept from Aurora DSQL's prepared query-processor clones.

## Related Concepts
- [[Firecracker]] - provides the snapshot-and-restore mechanism described by the source.
- [[AuroraDSQL]] - uses snapshot clones for PostgreSQL-derived query processors.
- [[BackupAndRecovery]] - snapshot cloning reuses initialized runtime state, whereas recovery snapshots preserve or restore durable service state after failure.
- [[ImmutableInfrastructure]] - prepared snapshots similarly shift initialization into a versioned artifact, but include live machine state beyond an image.
- [[CostConstrainedInfrastructure]] - clean-page sharing reduces the physical memory cost of equivalent workers.

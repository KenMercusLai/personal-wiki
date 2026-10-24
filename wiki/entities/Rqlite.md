---
title: "rqlite"
type: entity
tags: [database, sqlite, raft, open-source]
sources:
  - twelve-years-distributed-sqlite
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[Rqlite]] is a standalone open-source relational database server that adds Raft-based replication and fault tolerance around [[SQLite]].

## Current Profile
Rqlite serializes writes through a leader, records them in a Raft log, and requires acknowledgement from a majority. A partitioned minority refuses writes, making the system a CP design that prioritizes consistent replicated state over accepting writes in every partition.

The project began in 2014, moved from goraft to HashiCorp Raft in 2016, and retained its core architecture while adding read-consistency levels, snapshots, and WAL-related improvements. Its packaging distinguishes it from dqlite: rqlite is a server deployed beside an application rather than a library embedded within one.

## Key Characteristics
- Uses SQLite as its relational storage engine and Raft as its write-replication mechanism.
- Routes writes through one leader and commits them through a majority.
- Refuses minority-partition writes to preserve consistency.
- Runs as a standalone server exposed through an HTTP API.
- Targets self-operated fault tolerance when waiting for backup restoration is unacceptable.
- Has kept its central design stable since 2014 while changing Raft implementation and improving surrounding capabilities.

## Evidence
- Architecture: [[twelve-years-distributed-sqlite]] describes a Raft log in front of SQLite and includes a three-node diagram with one distinguished leader.
- Consistency: [[twelve-years-distributed-sqlite]] states that writes go through the leader, require majority acknowledgement, and are refused by a partitioned minority.
- History: [[twelve-years-distributed-sqlite]] dates the public release to 2014 and the move to HashiCorp Raft to 2016.
- Packaging: [[twelve-years-distributed-sqlite]] contrasts rqlite's server model with dqlite's embedded-library model.
- Operational purpose: [[twelve-years-distributed-sqlite]] distinguishes rqlite's continuous fault tolerance from Litestream's restore-oriented disaster recovery.

## Qualifications
The source is a first-party project history, not a benchmark or independent reliability evaluation. It supplies no measured failover time, throughput, latency, recovery-point objective, recovery-time objective, partition experiment, operational-cost comparison, or proof of the claimed open-source priority.

## What Changed
- Created a current profile of rqlite's architecture, consistency choice, packaging, and operational purpose.

## Relationships
- [[PhilipOToole]] - creator and long-term maintainer of rqlite.
- [[SQLite]] - storage engine wrapped by rqlite.
- [[DistributedSQLite]] - design category in which rqlite occupies the consensus corner.
- [[DistributedConsensus]] - agreement mechanism used to commit writes across the cluster.
- [[ReplicatedLog]] - ordered Raft history through which replicas apply writes.
- [[CloudHighAvailability]] - availability requirement that motivates replicated operation across nodes.

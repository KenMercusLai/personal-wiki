---
title: "Philip O'Toole"
type: entity
tags: [software-engineer, databases, distributed-systems]
sources:
  - twelve-years-distributed-sqlite
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[PhilipOToole]] is the creator and long-term maintainer of [[Rqlite]], represented here through his first-person history of distributed SQLite from 2014 to 2026.

## Current Profile
O'Toole built rqlite after encountering a need for small relational storage that did not belong to only one node. He released the source in 2014, initially used goraft, replaced it with HashiCorp Raft in 2016, and continued developing the project while the wider distributed-SQLite category expanded.

His retrospective frames architecture by user need rather than declaring one universal solution: rqlite targets self-operated fault tolerance without restore delay, Litestream targets inexpensive recovery, and CRDT-based systems target divergent multi-writer operation.

## Key Characteristics
- Created rqlite as a standalone open-source server combining SQLite with Raft replication.
- Treats majority-backed leader writes and minority write refusal as a durable design commitment.
- Distinguishes continuous availability from backup-and-restore recovery.
- Places rqlite within a broader history that includes earlier internal systems and later open-source and managed products.
- Continues to position rqlite as understandable, self-hosted infrastructure rather than a paid platform.

## Evidence
- Project origin: [[twelve-years-distributed-sqlite]] says O'Toole released rqlite in September 2014 after encountering a clustered relational-storage problem at jut.io.
- Protocol evolution: [[twelve-years-distributed-sqlite]] says rqlite moved from goraft to HashiCorp Raft in 2016.
- Design judgment: [[twelve-years-distributed-sqlite]] contrasts consensus, WAL streaming, and merge-based replication by the operational questions each answers.
- Project positioning: [[twelve-years-distributed-sqlite]] presents rqlite as a free, self-operated fault-tolerant relational database.

## Qualifications
The profile rests on one first-party retrospective. Its priority claims, category history, project comparisons, adoption judgments, and commercial interpretation are not independently verified here.

## What Changed
- Created a profile of rqlite's creator and his requirements-centered account of distributed SQLite.

## Relationships
- [[Rqlite]] - project O'Toole created and maintains.
- [[SQLite]] - embedded database engine underlying rqlite.
- [[DistributedSQLite]] - category whose history and architecture O'Toole interprets.
- [[DistributedConsensus]] - protocol problem addressed by rqlite's Raft layer.

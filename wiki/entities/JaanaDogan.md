---
title: "Jaana Dogan"
type: entity
tags: [person, software-engineering, databases, distributed-systems]
sources:
  - jaana-dogan-things-i-wished-more-developers-knew-about-databases
  - stateful-jobs
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[JaanaDogan]] appears in the wiki as a software practitioner writing about database behavior and the lifecycle requirements of stateful jobs.

## Current Profile
The database source presents Dogan as a practitioner translating accumulated storage experience for developers who are not specialists. She says design mistakes encountered over time caused data loss and outages, then uses those experiences to organize seventeen less-obvious database concerns.

The newer source carries the same systems orientation into job scheduling. It argues that state binds process identity to data and history, turning placement, upgrade, restart, and idleness into application-aware lifecycle problems. Across both articles, Dogan's teaching style connects infrastructure abstractions to concrete failure and migration paths rather than accepting labels such as ACID, healthy, idle, or schedulable at face value.

## Key Characteristics
- Writes practitioner guidance about databases and stateful distributed systems.
- Grounds the article's lessons in reported design mistakes, data loss, and outages.
- Emphasizes concrete failure modes and tradeoffs over database feature labels.
- Connects transaction and scheduling semantics with networking, clocks, identity, storage, observability, migration, and recovery.
- Treats persistent state as a cross-layer constraint on application and infrastructure decisions.

## Evidence
- Author role: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] identifies Jaana Dogan as the article's author.
- Experience basis: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] says her database knowledge accumulated while design mistakes caused data loss and outages.
- Teaching scope: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] organizes seventeen lessons for developers who are not database specialists.
- Systems orientation: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] links database guarantees with network faults, clock uncertainty, transaction behavior, operation-level performance, and growth.
- Stateful scheduling thesis: [[stateful-jobs]] argues that durable identity and application state change placement, upgrade, recovery, and suspension semantics.
- Cross-layer reasoning: [[stateful-jobs]] connects scheduler policy with storage compatibility, fencing, checkpoints, background work, and connection lifecycle.

## Qualifications
This profile is based on two practitioner articles and does not attempt to reconstruct Dogan's complete biography, employment history, or views outside them. The database examples support the stated teaching orientation but do not independently establish the prevalence of their failure modes. The stateful-jobs essay is a design argument without an implementation, benchmark, workload survey, or comparison demonstrating that one general scheduler can cover the proposed gap.

## What Changed
- Broadened the profile from database guidance to stateful scheduling and distributed-systems lifecycle design.
- Added persistent state as the common constraint connecting her transaction, migration, placement, and recovery arguments.

## Relationships
- [[DatabaseEngineeringTradeoffs]] - Dogan's database article is the founding source for this concept.
- [[DatabaseTransactionIsolation]] - Dogan explains isolation levels, optimistic locking, and write-skew risk.
- [[DistributedConsensus]] - her database guidance highlights partitions, ordering, and clock uncertainty.
- [[StatefulJobScheduling]] - her newer essay frames stateful scheduling as application-aware lifecycle management.
- [[SystemReliability]] - both sources connect infrastructure abstractions to failure and recovery behavior.

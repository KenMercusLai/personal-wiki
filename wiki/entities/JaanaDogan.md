---
title: "Jaana Dogan"
type: entity
tags: [person, software-engineering, databases]
sources:
  - jaana-dogan-things-i-wished-more-developers-knew-about-databases
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[JaanaDogan]] appears in the wiki as the author of "Things I Wished More Developers Knew About Databases."

## Current Profile
The source presents Dogan as a software practitioner translating accumulated database experience for developers who are not storage specialists. Her authority in this page is source-bounded: she says design mistakes encountered over time caused data loss and outages, then uses those experiences to organize seventeen less-obvious database concerns.

Her teaching style connects database internals to application decisions. Rather than treating ACID, latency, ordering, or scale as generic labels, she uses failure timelines, consistency hierarchies, transaction examples, and migration sequences to show what a developer must verify in a particular system.

## Key Characteristics
- Writes practitioner guidance for application developers working with databases.
- Grounds the article's lessons in reported design mistakes, data loss, and outages.
- Emphasizes concrete failure modes and tradeoffs over database feature labels.
- Connects transaction semantics with networking, clocks, observability, migration, and growth.

## Evidence
- Author role: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] identifies Jaana Dogan as the article's author.
- Experience basis: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] says her database knowledge accumulated while design mistakes caused data loss and outages.
- Teaching scope: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] organizes seventeen lessons for developers who are not database specialists.
- Systems orientation: [[jaana-dogan-things-i-wished-more-developers-knew-about-databases]] links database guarantees with network faults, clock uncertainty, transaction behavior, operation-level performance, and growth.

## Qualifications
This profile is based on one 2020 practitioner article and does not attempt to reconstruct Dogan's complete biography, employment history, or later views. The article's examples support the stated teaching orientation but do not independently establish the prevalence of the reported failure modes.

## What Changed
- Created a source-bounded profile of Dogan's database engineering guidance.

## Relationships
- [[DatabaseEngineeringTradeoffs]] - Dogan's article is the founding source for this concept.
- [[DatabaseTransactionIsolation]] - Dogan explains isolation levels, optimistic locking, and write-skew risk.
- [[DistributedConsensus]] - her database guidance highlights partitions, ordering, and clock uncertainty.

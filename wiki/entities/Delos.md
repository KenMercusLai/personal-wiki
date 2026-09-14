---
title: "Delos"
type: entity
tags: [database, storage-system, distributed-systems, infrastructure]
sources:
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Delos]] is presented as a Facebook production storage system created under [[MaheshBalakrishnan]]'s leadership and compared to Facebook's version of [[ZooKeeper]].

## Current Profile
The source describes Delos as a critical storage-system project at the bottom of Facebook's infrastructure stack. It reached production with a three-person team in less than a year, later grew to more than thirty engineers across sub-teams, avoided severe outages above SEV3 during Balakrishnan's four-year leadership period, and was replacing all Facebook uses of ZooKeeper as of the 2021 essay.

Delos is also used as the case behind Balakrishnan's production-infrastructure advice. The system's lessons emphasize conservative APIs, careful implementation migration, consistency and durability before availability, multiple implementations in test, implementation-independent observability, internal strategy against adjacent systems, and research-backed design communication.

## Key Characteristics
- Critical production storage system at the bottom of Facebook's infrastructure stack.
- Built quickly by a small initial team, then scaled to a large multi-subteam engineering effort.
- Framed as Facebook's replacement path for [[ZooKeeper]] usage.
- Used conservative API and migration guidance as a central design lesson.
- Treated consistency, durability, and correctness checks as first-order production priorities.
- Documented through academic papers in OSDI 2020 and SOSP 2021.

## Evidence
- System role: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Delos was a storage system at the bottom of the Facebook stack.
- Team growth: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says the team reached production with three people in less than a year and later scaled beyond thirty engineers.
- Reliability outcome: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Delos had no severe outage above SEV3 during Balakrishnan's four years leading the team.
- Replacement role: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Delos was replacing all uses of ZooKeeper at Facebook.
- Design lessons: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] connects the system to conservative APIs, staged rollout, migration support, and multiple tested implementations.
- Research record: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says the design is documented in OSDI 2020 and SOSP 2021 papers.

## Qualifications
This page reflects Balakrishnan's 2021 article rather than the Delos papers themselves. The source does not provide a full architecture description, later production status, or independent outage history beyond the author's leadership-period account.

## What Changed
- Created the Delos entity from Balakrishnan's production database essay.

## Relationships
- [[MaheshBalakrishnan]] - created and led the Delos team.
- [[Facebook]] - operating environment and production infrastructure stack for Delos.
- [[ZooKeeper]] - Delos is described as replacing Facebook uses of ZooKeeper.
- [[ProductionInfrastructureLeadership]] - Delos supplies the article's case evidence.
- [[SystemReliability]] - Delos' outage history and rollout discipline are reliability evidence in the source.
- [[ServiceObservability]] - Delos lessons include measuring above APIs and outside implementations.

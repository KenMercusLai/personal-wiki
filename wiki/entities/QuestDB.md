---
title: "QuestDB"
type: entity
tags: [database, columnar, append-mostly, time-series]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[QuestDB]] is presented as a simplified relational, columnar database optimized for append-mostly workloads and high ingestion throughput.

## Current Profile
The source excludes QuestDB from its narrow vector-native definition while recognizing its strong temporal workload orientation. New records append to the latest chunk in a direct columnar layout; updates require versioning and background vacuum work, making frequent mutation a poorer fit than ingestion-heavy workloads.

## Key Characteristics
- Uses a simplified relational model with indexes and joins.
- Optimizes for append-mostly ingestion.
- Stores newly arriving data in the latest columnar chunk.
- Handles updates through versioning and background vacuuming.

## Evidence
- Workload identity: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes QuestDB as append-mostly with high ingestion performance.
- Relational scope: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] notes indexes and joins in its simplified relational model.
- Storage path: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says data appends into the newest chunk.
- Update cost: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] links updates to versioning and vacuum mechanisms.

## Qualifications
The source's category exclusion is a modeling judgment rather than an assertion that QuestDB is not marketed or useful as a time-series database. No current benchmark or version-specific measurement is supplied.

## What Changed
- Established QuestDB's append-mostly relational profile and update-path qualification.

## Relationships
- [[TimeSeriesDatabase]] - QuestDB serves temporal workloads but falls outside the source's narrow model-based definition.
- [[GreptimeDB]] - both use columnar storage but have different reported write and model orientations.
- [[DatabaseConsolidation]] - QuestDB's specialization should be weighed against adding a separate datastore.
- [[TechnologyStackComplexity]] - adopting QuestDB introduces another operational and data-flow boundary.

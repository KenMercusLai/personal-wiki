---
title: "TimescaleDB"
type: entity
tags: [database, postgresql, time-series, extension]
sources:
  - eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[TimescaleDB]] is presented as a PostgreSQL extension optimized for temporal workloads while retaining a relational data model.

## Current Profile
The source deliberately excludes TimescaleDB from its narrow vector-native definition of a time-series database. It characterizes the product as reorganizing cooled PostgreSQL data into array-like columnar structures to improve scans and compression at the cost of update performance, while preserving access to PostgreSQL indexes, transactions, foreign keys, and general relational modeling.

## Key Characteristics
- Extends PostgreSQL rather than replacing its relational model.
- Can store a broad range of timestamped relational data.
- Reorganizes cooled data for scan performance and compression.
- Retains PostgreSQL capabilities such as indexes, transactions, and foreign keys.

## Evidence
- Category placement: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] calls TimescaleDB closer to a relational database optimized for cold temporal data.
- Storage transformation: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] describes cooled rows being reorganized into array-like structures.
- Tradeoff: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] says the change trades update performance for scans and compression.
- Relational breadth: [[eric-fu-dao-di-shi-yao-shi-xu-shu-ju-ku]] emphasizes PostgreSQL indexes, transactions, and foreign keys.

## Qualifications
Exclusion from the source's category is definitional, not a finding that TimescaleDB cannot handle time-series workloads. The article provides no comparative benchmark, and product internals can change across versions.

## What Changed
- Established TimescaleDB's relational-model profile and the source's vector-native taxonomy boundary.

## Relationships
- [[PostgreSQL]] - TimescaleDB extends PostgreSQL and retains its relational capabilities.
- [[Timescale]] - company associated with the TimescaleDB product and PostgreSQL-centered systems.
- [[TimeSeriesDatabase]] - TimescaleDB supports temporal workloads but falls outside the source's narrow model-based definition.
- [[DatabaseConsolidation]] - extending PostgreSQL can preserve consolidation while adding temporal optimization.

---
title: "Databricks"
type: entity
tags: [company, data-platform, lakehouse, databases]
sources:
  - p4385-pandis
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[Databricks]] is represented as the company deploying [[Lakebase]], a serverless PostgreSQL-compatible transactional service integrated with its Lakehouse platform.

## Current Profile
In the systems paper, Databricks operates Lakebase at a reported scale above 10 million database creations and management operations daily. Its platform joins transactional compute to Spark, Delta, Lakehouse//RT, Unity Catalog, and cloud object storage so operational and analytical engines can exchange data or share consistent snapshots without forcing analytical work through the OLTP primary.

## Key Characteristics
- Operates the production Lakebase service described in the source.
- Integrates PostgreSQL identities and grants with Unity Catalog.
- Uses Spark for streaming and direct-to-storage ingestion into Lakebase.
- Uses Lakehouse//RT for vectorized direct analysis of PostgreSQL page snapshots.
- Frames agents as a driver of short-lived compute and deep database-branch hierarchies.

## Evidence
- Service scale: [[p4385-pandis]] reports more than 10 million databases managed daily and roughly four times more database creation by agents than human users.
- Unified governance: [[p4385-pandis]] describes OAuth identity propagation, PostgreSQL-role mapping, delegated grants, and live catalog metadata.
- Data movement: [[p4385-pandis]] describes Delta change-feed streaming, parallel Spark page generation, logical decoding into Delta, and direct analytical reads.
- Production telemetry: [[p4385-pandis]] supplies compute-lifetime, branch-depth, startup, and autoscaling measurements from the service.

## Qualifications
This profile comes from one first-party paper authored by company and Neon engineers. Scale, adoption, reliability, and performance figures are not independently audited, and the evidence describes one product architecture rather than Databricks's full company, business, or platform history.

## What Changed
- Established Databricks as the operator and integration boundary for Lakebase.

## Relationships
- [[Lakebase]] - transactional database service deployed and evaluated by Databricks.
- [[Neon]] - engineering and open-source foundation acknowledged by the paper.
- [[PostgreSQL]] - transactional engine and compatibility surface used by Lakebase.
- [[DisaggregatedTransactionalDatabase]] - architecture Databricks applies to transactional workloads.
- [[ObjectStorageNativeDatabase]] - durable storage pattern joining Lakebase to lake infrastructure.

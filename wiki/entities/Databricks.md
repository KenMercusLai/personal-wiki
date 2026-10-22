---
title: "Databricks"
type: entity
tags: [company, data-platform, lakehouse, databases]
sources:
  - p4385-pandis
  - lakebase-ltap-rethinking-database-storage
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Overview
[[Databricks]] is represented as the company deploying [[Lakebase]], a serverless PostgreSQL-compatible transactional service integrated with its Lakehouse platform.

## Current Profile
In the systems paper, Databricks operates Lakebase at a reported scale above 10 million database creations and management operations daily. Its platform joins transactional compute to Spark, Delta, Lakehouse//RT, Unity Catalog, and cloud object storage so operational and analytical engines can exchange data or share consistent snapshots without forcing analytical work through the OLTP primary.

The LTAP article sharpens that integration into a storage-level program. Databricks proposes materializing PostgreSQL state as Parquet exposed through Delta or Iceberg, then letting Lakehouse//RT read the object-store prefix plus recent Pageserver changes at an LSN. This preserves separate engines and resource pools while aiming to remove selected-table CDC, duplicated governance, and replica drift. The account describes an active rollout with dual representations used for validation rather than a completed platform-wide state.

## Key Characteristics
- Operates the production Lakebase service described in the source.
- Integrates PostgreSQL identities and grants with Unity Catalog.
- Uses Spark for streaming and direct-to-storage ingestion into Lakebase.
- Uses Lakehouse//RT for vectorized direct analysis of PostgreSQL page snapshots.
- Frames agents as a driver of short-lived compute and deep database-branch hierarchies.
- Develops LTAP as a storage-level bridge between PostgreSQL transactions and independently scaled Lakehouse analytics.

## Evidence
- Service scale: [[p4385-pandis]] reports more than 10 million databases managed daily and roughly four times more database creation by agents than human users.
- Unified governance: [[p4385-pandis]] describes OAuth identity propagation, PostgreSQL-role mapping, delegated grants, and live catalog metadata.
- Data movement: [[p4385-pandis]] describes Delta change-feed streaming, parallel Spark page generation, logical decoding into Delta, and direct analytical reads.
- Production telemetry: [[p4385-pandis]] supplies compute-lifetime, branch-depth, startup, and autoscaling measurements from the service.
- LTAP design: [[lakebase-ltap-rethinking-database-storage]] describes Parquet materialization, Delta or Iceberg exposure, LSN-bounded recent-change merging, and automatic analytical availability for all tables.
- Rollout state: [[lakebase-ltap-rethinking-database-storage]] says Databricks was dual-writing row and columnar forms for verification and still ironing out LTAP behavior.

## Qualifications
This profile comes from two first-party publications by Databricks and Neon participants. Scale, adoption, reliability, compression, and performance claims are not independently audited, and the evidence describes one product architecture rather than Databricks's full company, business, or platform history. The newer article mixes available Lakebase behavior with LTAP mechanisms still in rollout and does not provide a reproducible end-to-end evaluation.

## What Changed
- Added LTAP as Databricks's proposed storage-level integration of PostgreSQL transactions with Lakehouse analytics.
- Qualified the shared-columnar-store description as transitional rather than fully deployed evidence.

## Relationships
- [[Lakebase]] - transactional database service deployed and evaluated by Databricks.
- [[Neon]] - engineering and open-source foundation acknowledged by the paper.
- [[PostgreSQL]] - transactional engine and compatibility surface used by Lakebase.
- [[DisaggregatedTransactionalDatabase]] - architecture Databricks applies to transactional workloads.
- [[ObjectStorageNativeDatabase]] - durable storage pattern joining Lakebase to lake infrastructure.
- [[LakeTransactionalAnalyticalProcessing]] - announced architecture for fresh analytics over Lakebase's governed operational history.
- [[ReynoldXin]] - Databricks cofounder presenting the design and rollout argument.

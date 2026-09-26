---
title: "Apache Airflow"
type: entity
tags: [software, workflow-orchestration, data-engineering]
sources:
  - building-a-data-informed-culture-an-introduction-to-data-at-gusto
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheAirflow]] is the open-source workflow orchestrator used in Gusto's 2016 data platform for ingestion, transformation, testing, and quality alerts.

## Current Profile
The source places Airflow between raw warehouse inputs and more usable analytical data. It coordinated vendor-API ingestion, SQL that created higher-level views, and tests intended to detect faulty logic or downstream production changes before bad data reached users.

Airflow also formed part of Gusto's controlled self-service model: analysts could author SQL-based ETL tasks and expose resulting BI tables in Looker without handing every transformation to a data engineer.

## Key Characteristics
- Open-source workflow orchestration tool in the described platform.
- Coordinated third-party ingestion and SQL transformations.
- Ran testing and QA tasks that alerted on logic and upstream-production changes.
- Enabled analyst-authored ETL while infrastructure access remained controlled.

## Evidence
- Orchestration scope: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] names API ingestion, higher-level SQL views, and testing as Airflow tasks.
- Quality role: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] says alerts were intended to stop faulty logic or application changes from propagating bad data.
- Self-service role: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] says analysts could write Airflow tasks to create BI tables and expose them through Looker.

## Qualifications
The source describes one company's use in 2016, not Airflow's complete feature set or current project state. It gives no workflow volume, reliability, scheduler performance, access-control design, deployment details, failure-recovery behavior, or comparative evaluation.

## What Changed
- Created the entity from Gusto's orchestration and analyst-self-service case.

## Relationships
- [[Gusto]] - company using Airflow in the source.
- [[LayeredDataWarehouse]] - Airflow moves and validates data between warehouse layers.
- [[AmazonRedshift]] - analytical database against which the described SQL transformations run.
- [[Looker]] - downstream interface receiving Airflow-produced BI tables.
- [[DataScienceEngineeringPractice]] - testing and centralized automation are engineering disciplines applied to analytical work.

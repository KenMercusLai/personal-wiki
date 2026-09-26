---
title: "Amazon Redshift"
type: entity
tags: [software, analytical-database, data-warehouse, aws]
sources:
  - building-a-data-informed-culture-an-introduction-to-data-at-gusto
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[AmazonRedshift]] is the analytical database at the center of Gusto's described 2016 warehouse, with Amazon S3 as the underlying data lake.

## Current Profile
The source presents Redshift as the common destination for replicas of production application databases, event data, and third-party integrations. Within it, Gusto separated raw schemas, reusable denormalized BI tables, team-specific views, and more tightly controlled PII.

This central role made Redshift both a consistency mechanism and a governed work surface: approved analysts could inspect raw tables through the ETL environment, create higher-level tables, and publish them to Looker.

## Key Characteristics
- Central analytical warehouse in the described Gusto platform.
- Received replicated production data alongside events and vendor data.
- Hosted raw, BI, team-view, and access-controlled PII structures.
- Supported SQL transformations orchestrated by Apache Airflow.

## Evidence
- Platform role: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] identifies Redshift as the analytical database and S3 as the underlying data lake.
- Replication: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] says Amazon Database Migration Service copied production databases into individual Redshift schemas.
- Warehouse structure: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] describes raw sources, denormalized BI tables, team views, and separated PII access.
- Transformation access: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] says analysts could use available raw tables to author SQL ETL tasks and publish new BI tables.

## Qualifications
This is a narrow 2016 deployment account, not a current or comparative assessment of Redshift. The source reports no data volume, query latency, concurrency, cost, backup and recovery design, encryption details beyond selected application fields, or measured improvement from centralization.

## What Changed
- Created the entity from Gusto's layered analytical-warehouse case.

## Relationships
- [[Gusto]] - company operating the warehouse described in the source.
- [[LayeredDataWarehouse]] - organizational structure implemented inside Redshift.
- [[ApacheAirflow]] - orchestrates SQL transformations and quality work over warehouse data.
- [[Looker]] - explores BI tables and presents team dashboards downstream.
- [[AWS]] - cloud platform family containing Redshift, S3, and Database Migration Service.

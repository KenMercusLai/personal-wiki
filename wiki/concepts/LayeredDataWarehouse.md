---
title: "Layered Data Warehouse"
type: concept
tags: [data-warehouse, data-engineering, governance, analytics]
sources:
  - building-a-data-informed-culture-an-introduction-to-data-at-gusto
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
A [[LayeredDataWarehouse]] organizes analytical data into progressively more usable and audience-specific representations while preserving controlled access to sensitive source data.

## Current Synthesis
Gusto's 2016 design used three logical levels. Raw production replicas, events, and third-party integrations formed the lowest layer. Denormalized BI tables provided reusable, analyst-friendly representations in the middle. Team-specific joins and rollups supported dashboards and daily work at the highest level.

The layers divided responsibilities rather than merely copying data. Raw access supported new transformations but remained restricted because source schemas contained PII. The BI layer standardized reusable data, including separate controls for PII. Team views optimized recurring consumption. Airflow transformations and checks connected the layers, while Looker exposed the resulting tables and views.

## Key Claims
- Preserve raw source fidelity separately from reusable analytical representations.
- Use a middle BI layer to denormalize operational data into definitions that are easier to analyze and reuse.
- Build team-facing views from shared BI tables instead of repeatedly joining raw sources in each dashboard.
- Separate and tightly control PII rather than treating warehouse centralization as universal access.
- Let analysts extend shared layers when scale and controls make the ownership model practical.

## Evidence
- Raw layer: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] places production tables, events, and third-party integrations at the lowest level.
- BI layer: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] describes denormalized, user-friendly tables and a separately controlled PII schema.
- Team layer: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] describes joined and aggregated views used for core dashboards and daily work.
- Transformation path: [[building-a-data-informed-culture-an-introduction-to-data-at-gusto]] says analysts could build BI tables from approved raw data through Airflow and expose them in Looker.

## Counterevidence & Qualifications
The source supplies no schema examples, lineage model, semantic-definition process, freshness target, ownership matrix, query-performance evidence, deletion workflow, or incident history. The article says Gusto had not yet encountered major scaling problems, so analyst-authored ETL may not transfer directly to larger or more regulated environments. The referenced architecture diagram is missing, leaving the prose as the only inspectable evidence for exact boundaries and flows.

## What Changed
- Created the concept from Gusto's raw-to-BI-to-team-view warehouse structure and access model.

## Related Concepts
- [[DataInformedCulture]] - warehouse layers make consistent evidence usable across an organization.
- [[DataScienceEngineeringPractice]] - transformations need testing, versioning, automation, and maintainability.
- [[EventAnalyticsPipeline]] - event ingestion supplies one raw input that can feed analytical warehouse layers.
- [[DatabaseConsolidation]] - centralization reduces cross-system fragmentation but creates shared-platform responsibilities.
- [[ProductionAccessControl]] - raw and PII schemas require stricter authorization than general analytical views.

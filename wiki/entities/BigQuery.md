---
title: "BigQuery"
type: entity
tags: [google-cloud, analytics, data-warehouse]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[BigQuery]] is the analytical storage and query destination in [[JellyButtonGames]]'s custom event pipeline.

## Current Profile
The source positions BigQuery as the durable analysis layer after streaming transformations. Structured fields are promoted into columns while remaining payload data is retained as JSON in a string column, balancing query access with schema flexibility.

## Key Characteristics
- Stores high-volume event data for later analysis.
- Receives near-real-time output from [[GoogleCloudDataflow]].
- Supports a mixed schema of selected columns plus retained JSON payload.
- Appears as a comparatively small part of the reported July 2017 service bill.

## Evidence
- Pipeline role: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] and its inspected diagrams place BigQuery after streaming Dataflow processing.
- Data model: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] describes mapping selected fields to columns and preserving the rest as JSON text.
- Historical cost: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about $100 in BigQuery cost for July 2017.

## Qualifications
The source's performance, ingestion-limit, and cost statements date to 2017 and describe one workload. They do not establish current service limits, prices, or fit for other analytical designs.

## What Changed
- Created BigQuery as the storage and query layer in the Jelly Button pipeline.

## Relationships
- [[GoogleCloudDataflow]] - streaming processor that writes transformed events into BigQuery.
- [[EventAnalyticsPipeline]] - architecture in which BigQuery supplies analytical storage.
- [[JellyButtonGames]] - operator of the described workload.

---
title: "Jelly Button Games"
type: entity
tags: [games, mobile, analytics]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[JellyButtonGames]] is the mobile and web game company whose replacement of [[Mixpanel]] with a Google Cloud analytics pipeline is described in the source.

## Current Profile
The 2017 article identifies Pirate Kings as Jelly Button's flagship title and reports roughly 70 million downloads across iOS, Android, and Facebook. The company's analytics workload collected game events for research, marketing, and product analysis, with low latency, no tolerated data loss, and rapid query availability as design requirements.

## Key Characteristics
- Develops and publishes mobile and web games.
- Operated a high-volume, multi-client event stream for game analytics.
- Required geographically responsive ingestion and near-real-time analytical access.
- Chose a custom Google Cloud pipeline to reduce analytics cost and increase flexibility.

## Evidence
- Product scale: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about 70 million Pirate Kings downloads.
- Workload requirements: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] requires low client latency, high throughput, loss avoidance, and quickly queryable data.
- Operating result: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about 500 events per second in July 2017 and a production deployment operating for several months.

## Qualifications
The company and workload figures are historical and company-reported. The source provides no independent validation, current company profile, or full reliability and cost accounting.

## What Changed
- Created Jelly Button Games as the client and workload context for the analytics migration.

## Relationships
- [[DoiTInternational]] - consultancy that designed and built the pipeline with Jelly Button.
- [[Mixpanel]] - analytics service Jelly Button replaced.
- [[EventAnalyticsPipeline]] - custom infrastructure built for Jelly Button's event workload.
- [[BigQuery]] - analytical destination used by the replacement system.

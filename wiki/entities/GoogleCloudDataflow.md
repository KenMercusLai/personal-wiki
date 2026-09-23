---
title: "Google Cloud Dataflow"
type: entity
tags: [google-cloud, streaming, etl]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[GoogleCloudDataflow]] is the managed streaming ETL service used between [[GoogleCloudPubSub]] and [[BigQuery]] in the source's event-analytics architecture.

## Current Profile
The pipeline delegates filtering, field mapping, transformation, and aggregation to Dataflow so synchronous ingestion remains fast. Streaming mode keeps the job running and processing Pub/Sub messages as they arrive, making transformed data available for analysis near real time.

## Key Characteristics
- Runs distributed data processing on managed workers.
- Consumes messages asynchronously from Pub/Sub.
- Performs filtering, mapping, transformation, and aggregation.
- Writes structured and retained raw payload data into BigQuery.

## Evidence
- ETL boundary: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] assigns transformation and aggregation to Dataflow rather than the request path.
- Streaming behavior: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] identifies streaming mode as continuous processing of arriving Pub/Sub messages.
- Historical cost: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about $500 in Dataflow cost for July 2017.

## Qualifications
The source does not provide latency distributions, worker counts, failure behavior, replay tests, or a comparison with alternative stream processors. Service behavior and pricing are historical.

## What Changed
- Created Dataflow as the pipeline's asynchronous transformation layer.

## Relationships
- [[GoogleCloudPubSub]] - upstream message source for the streaming job.
- [[BigQuery]] - downstream analytical store receiving transformed events.
- [[EventAnalyticsPipeline]] - architecture whose ETL work Dataflow performs.

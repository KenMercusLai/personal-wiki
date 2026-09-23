---
title: "Event Analytics Pipeline"
type: concept
tags: [analytics, streaming, data-engineering]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
An [[EventAnalyticsPipeline]] is a system that receives product or behavioral events, buffers them, transforms or aggregates them, stores them for analytical queries, and exposes the results with a bounded delay.

## Current Synthesis
The Jelly Button case divides the pipeline by latency and responsibility. A globally distributed Kubernetes tier handles client requests and performs only metadata enrichment plus message publication. Pub/Sub absorbs events across the synchronous boundary, Dataflow continuously parses and transforms them, and BigQuery stores selected structured fields alongside retained JSON for analysis. This design trades a managed analytics product for lower reported direct cost and greater pipeline control, but it also makes the operator responsible for several interacting cloud services.

## Key Claims
- Keep synchronous event ingestion thin when client latency and burst handling matter.
- Use a persistent asynchronous boundary to decouple acceptance from transformation and analytical storage.
- Perform filtering, mapping, and aggregation in a scalable streaming layer rather than on the request path.
- Preserve both query-friendly structured fields and sufficiently rich raw payload data for later analysis.
- Evaluate build-versus-buy choices with total ownership cost, not only the replacement services' monthly bill.

## Evidence
- Thin ingestion: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] says the Node.js backend only adds metadata and publishes the payload.
- Decoupled flow: the inspected diagrams in [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] show clients flowing through GKE to Pub/Sub, Dataflow, and BigQuery.
- Continuous ETL: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] runs Dataflow in streaming mode for near-real-time transformation.
- Flexible storage: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] maps some fields into BigQuery columns and retains the rest as JSON text.
- Cost case: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports roughly $1,300 in listed monthly cloud-service costs at about 500 events per second.

## Counterevidence & Qualifications
The architecture is one 2017 vendor-authored case. It does not compare data quality, analyst experience, feature parity, maintenance labor, on-call burden, schema evolution, deletion and privacy requirements, or failure recovery with Mixpanel. Its direct-cost result therefore supports a feasible architecture, not a universal case for replacing managed analytics.

## What Changed
- Created the concept from the Jelly Button GKE-to-BigQuery production pipeline.

## Related Concepts
- [[CloudCostOptimization]] - cost pressure can motivate replacing managed analytics with owned infrastructure.
- [[TechnologyStackComplexity]] - a custom pipeline adds service boundaries and operational responsibility.
- [[GoogleCloudPubSub]] - persistent asynchronous boundary between ingestion and processing.
- [[GoogleCloudDataflow]] - streaming transformation and aggregation layer.
- [[BigQuery]] - analytical storage and query layer.
- [[Kubernetes]] - orchestration layer for the latency-sensitive ingestion service.

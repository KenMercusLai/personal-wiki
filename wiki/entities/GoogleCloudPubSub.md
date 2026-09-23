---
title: "Google Cloud Pub/Sub"
type: entity
tags: [google-cloud, messaging, streaming]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[GoogleCloudPubSub]] is the asynchronous messaging boundary between the low-latency ingestion service and streaming transformation in the Jelly Button analytics pipeline.

## Current Profile
The Node.js backend adds metadata and publishes each event to Pub/Sub without doing transformation work. The inspected delivery diagram shows publishers writing messages to a topic, message storage buffering them, and subscribers consuming them through subscriptions; the solution diagram then shows Dataflow as the downstream consumer.

## Key Characteristics
- Decouples client-facing event receipt from downstream processing.
- Uses topics, subscriptions, and subscribers as the delivery model shown in the source.
- Buffers events so transformation can proceed asynchronously.
- Feeds the continuously running Dataflow pipeline.

## Evidence
- Latency boundary: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] says the backend only adds metadata and publishes the payload.
- Delivery model: the inspected Pub/Sub diagram in [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] shows publisher-to-topic-to-subscription-to-subscriber flow with a message store.
- Historical cost: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about $200 in Pub/Sub cost for July 2017.

## Qualifications
The source claims unlimited rate, worldwide guaranteed delivery, and up to seven days of persistence without documenting tests or failure semantics. These are historical vendor-era statements, not current guarantees established by the wiki.

## What Changed
- Created Pub/Sub as the durable asynchronous boundary in the analytics pipeline.

## Relationships
- [[GoogleKubernetesEngine]] - hosts the ingestion service that publishes events.
- [[GoogleCloudDataflow]] - downstream subscriber and stream processor.
- [[EventAnalyticsPipeline]] - architecture whose synchronous and asynchronous stages Pub/Sub separates.

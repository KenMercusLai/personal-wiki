---
title: "Google Kubernetes Engine"
type: entity
tags: [google-cloud, kubernetes, containers]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[GoogleKubernetesEngine]] is the managed [[Kubernetes]] service, then called Google Container Engine in the source, that hosted Jelly Button's client-facing event-ingestion tier.

## Current Profile
The case uses federated clusters in the United States and Europe behind one geo-aware global HTTP/S load balancer. Each pod contains Nginx and a Node.js backend, with Horizontal Pod Autoscaler adjusting pods and the Container Engine node autoscaler adjusting cluster nodes.

## Key Characteristics
- Provides managed Kubernetes clusters on Google Cloud.
- Supports the source's multi-region ingestion deployment.
- Runs two-container pods containing Nginx and Node.js.
- Scales both pod count and cluster node count for variable traffic.

## Evidence
- Geographic topology: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] describes US and European clusters behind a geo-aware global load balancer.
- Runtime composition: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] says every pod contains Nginx and Node.js containers.
- Elasticity: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] uses both Horizontal Pod Autoscaler and node autoscaling.
- Historical cost: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about $500 in Container Engine cost for July 2017.

## Qualifications
The source does not report cluster size, utilization, failover tests, tail latency, incident history, or maintenance labor. The old Google Container Engine name and cost figures are historical.

## What Changed
- Created GKE as the managed Kubernetes ingestion tier in the Jelly Button case.

## Relationships
- [[Kubernetes]] - orchestration system managed by GKE.
- [[GoogleCloudPubSub]] - messaging service to which the hosted backend publishes events.
- [[EventAnalyticsPipeline]] - architecture whose latency-sensitive front door runs on GKE.
- [[JellyButtonGames]] - operator of the workload described in the source.

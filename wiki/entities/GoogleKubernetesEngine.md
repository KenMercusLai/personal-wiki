---
title: "Google Kubernetes Engine"
type: entity
tags: [google-cloud, kubernetes, containers]
sources:
  - vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes
  - rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[GoogleKubernetesEngine]] is Google Cloud's managed [[Kubernetes]] service, represented through Jelly Button's geo-distributed event-ingestion tier and Rainforest QA's application-platform migration.

## Current Profile
Jelly Button's 2017 case uses US and European clusters behind one geo-aware global HTTP/S load balancer. Each pod contains Nginx and a Node.js backend, with autoscalers adjusting pods and cluster nodes.

Rainforest QA's 2018 evaluation chose GKE for a broader estate because its small operations team valued managed control-plane and node concerns, cluster scaling, and application scaling from custom metrics. Its staged topology used us-east4 as a temporary low-latency bridge to Heroku Postgres and us-east1 as the final GKE and Cloud SQL home. The case also exposes configuration risk inside a managed service: CPU limits throttled Rails startup, slow liveness responses caused restarts, and rollback to Heroku was needed before limits were removed.

## Key Characteristics
- Provides managed Kubernetes clusters on Google Cloud.
- Supports the source's multi-region ingestion deployment.
- Runs two-container pods containing Nginx and Node.js.
- Scales both pod count and cluster node count for variable traffic.
- Supported custom-metric autoscaling for Rainforest QA's queue-backed workers.
- Enabled a staged regional topology that separated application migration from database cutover.

## Evidence
- Geographic topology: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] describes US and European clusters behind a geo-aware global load balancer.
- Runtime composition: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] says every pod contains Nginx and Node.js containers.
- Elasticity: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] uses both Horizontal Pod Autoscaler and node autoscaling.
- Historical cost: [[vadim-solovey-how-we-saved-over-240k-per-year-by-replacing-mixpanel-with-bigquery-dataflow-and-kubernetes]] reports about $500 in Container Engine cost for July 2017.
- Managed-service selection: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] says GKE's management of nodes and autoscaling distinguished it from EKS during the 2018 evaluation.
- Custom metrics: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] describes queue-depth metrics exported through Prometheus and a Stackdriver adapter for worker autoscaling.
- Staged topology: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] shows a temporary us-east4 cluster using Heroku Postgres before final traffic and data moved to us-east1.
- Configuration failure: [[rainforest-qa-how-and-why-we-migrated-from-heroku-to-kubernetes]] reports CPU throttling, slow startup requests, failed liveness probes, and a rollback before the limits were removed.

## Qualifications
Both cases are historical first-party reports without controlled comparisons. The old Google Container Engine name, costs, service maturity, regional availability, and GKE-versus-EKS feature claims date to 2017-2018. Rainforest QA's CPU-limit experience is valuable incident evidence but may depend on its Rails workload, settings, and the Kubernetes and Linux behavior of that period. Neither case establishes current cluster economics or universal platform fit.

## What Changed
- Expanded GKE from an ingestion-tier example into a broader managed application-platform and migration case.
- Added custom-metric autoscaling, staged regional cutover, and CPU-limit failure evidence.

## Relationships
- [[Kubernetes]] - orchestration system managed by GKE.
- [[GoogleCloudPubSub]] - messaging service to which the hosted backend publishes events.
- [[EventAnalyticsPipeline]] - architecture whose latency-sensitive front door runs on GKE.
- [[JellyButtonGames]] - operator of the workload described in the source.
- [[RainforestQA]] - operator that used GKE as the target for a staged Heroku migration.
- [[Heroku]] - source platform and temporary database dependency during the staged cutover.
- [[ServiceHealthChecks]] - liveness behavior amplified slow pod startup into an availability incident.

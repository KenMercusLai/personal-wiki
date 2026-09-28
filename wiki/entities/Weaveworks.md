---
title: "Weaveworks"
type: entity
tags: [company, gitops, cloud-native]
sources:
  - gitops-operations-by-pull-request
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Weaveworks]] is the company whose developer-operated cloud service provides the source's early [[GitOps]] case.

## Current Profile
In the source, Weaveworks runs multiple Kubernetes clusters, AWS resources, applications, and a Prometheus-based observability stack through version-controlled declarative configuration. Pull requests and pipelines govern operational change, environment-specific diff tools report divergence, and [[WeaveFlux]] synchronizes Git and cluster state. The company also commercialized related tooling through Weave Cloud, creating a product interest that qualifies the account.

## Key Characteristics
- Uses developer ownership of production operations as the organizational setting for GitOps.
- Stores infrastructure and application intent in version control.
- Uses diff alerts and synchronization to connect repository intent with live environments.
- Presents reconstructibility and fast recovery as benefits of the operating model.

## Evidence
- Operating scope: [[gitops-operations-by-pull-request]] says Weaveworks managed AWS provisioning, Kubernetes, applications, and cloud-native monitoring through GitOps practices.
- Change path: [[gitops-operations-by-pull-request]] says operational changes flowed through pull requests plus build and release pipelines.
- Drift loop: [[gitops-operations-by-pull-request]] describes kubediff, ansiblediff, terradiff, Prometheus metrics, and alerts across development and production.
- Recovery: [[gitops-operations-by-pull-request]] reports reconstruction of the deleted AWS-hosted system in under 45 minutes.

## Qualifications
The evidence is a company-authored case and product introduction. It does not independently verify the recovery time, compare alternative practices, or quantify routine delivery and reliability outcomes.

## What Changed
- Created a source-bounded company profile centered on the early GitOps operating case.

## Relationships
- [[AlexisRichardson]] - author describing the company's practice.
- [[GitOps]] - operating model named for the company's repository-driven workflow.
- [[WeaveFlux]] - open-source synchronization component in the workflow.
- [[Kubernetes]] - principal application platform managed in the case.
- [[Prometheus]] - monitoring system used to expose persistent environment drift.

---
title: "I Didn't Need Kubernetes"
type: source
tags: [kubernetes, cloud-run, infrastructure, devops]
date: 2024-11-05
source_file: /mnt/ken_personal_wiki/Articles/Ben Houston - I Didn't Need Kubernetes.md
---

## Summary
[[BenHouston]] argues that [[Kubernetes]] was useful when moving beyond bare-metal operations for [[ClaraIO]] and [[Threekit]], but later became too costly and complex for his containerized service and job workloads. The article presents [[GoogleCloudRun]] as a simpler managed platform for Docker containers, autoscaling services, and async tasks, especially where low idle cost, fast scaling, and reduced cluster-management overhead matter more than Kubernetes extensibility.

## Key Claims
- [[Kubernetes]] can reduce hardware-management burden while still adding cluster cost, operational staffing needs, and ecosystem-specific complexity.
- Slow Kubernetes autoscaling can force over-provisioning, turning unused capacity into a standing cost.
- [[GoogleCloudRun]] fits Docker-based services and long-running jobs when the desired abstraction is a simple managed PaaS rather than a full orchestration platform.
- [[CloudCostOptimization]] can come from scale-to-zero billing and per-request CPU/memory use, not only from cheaper servers.
- [[TaskQueueDesign]] can be simplified when the platform supplies task execution, result tracking, and retries instead of requiring custom worker infrastructure.
- [[TechnologyStackComplexity]] includes abstraction lock-in: Kubernetes-specific service naming, cluster resources, and integration assumptions can make outside resources harder to use.

## Key Quotes
> "Kubernetes proved difficult to provision, expensive to maintain, and time-consuming to manage." - on the author's experience after adopting it.

> "The key is that I am not using Kubernetes or Borg, I am using a simplified PaaS system" - on Cloud Run's abstraction value.

## Connections
- [[BenHouston]] - author describing the migration away from Kubernetes.
- [[Kubernetes]] - orchestration system the article critiques for this workload.
- [[GoogleCloudRun]] - target platform for managed container services and tasks.
- [[Docker]] - packaging layer retained across the migration.
- [[ClaraIO]] - earlier 3D editor platform operated on bare metal before the managed-compute shift.
- [[Threekit]] - enterprise 3D platform context for the original Kubernetes adoption.
- [[CloudCostOptimization]] - central reason for preferring Cloud Run for the author's current projects.
- [[ContainerNativePractice]] - Cloud Run keeps containers but changes the operational contract around deployment, scaling, and jobs.
- [[TaskQueueDesign]] - Cloud Run Tasks are presented as a simpler way to run large batches of asynchronous work.
- [[TechnologyStackComplexity]] - Kubernetes-specific abstractions are treated as added cognitive and migration burden.
- [[DistributedSystemRestraint]] - the article argues for choosing less orchestration machinery when project needs do not justify it.

## Contradictions
- No direct contradiction identified. The source qualifies earlier positive Kubernetes material by distinguishing Kubernetes as a powerful extensible platform from Kubernetes as an unnecessary operating burden for smaller or PaaS-suited workloads. The inspected image reinforces the article's thesis by showing tangled Kubernetes/server/container complexity migrating to a single Cloud Run container.

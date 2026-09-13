---
title: "Container-Native Practice"
type: concept
tags: [containers, operations, reliability]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
  - ben-houston-i-didnt-need-kubernetes
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ContainerNativePractice]] is the operational discipline of designing applications to behave correctly inside containers rather than merely packaging existing programs in container images.

## Current Synthesis
Wang Ziting's retrospective distinguishes long-term container use from actually becoming container native. A team can run programs in containers for years while still depending on local storage, lacking meaningful health checks, or failing to handle process signals for graceful shutdown. Ben Houston's Cloud Run essay adds that container-native practice also includes choosing the right platform abstraction: the workload may remain Docker-based while orchestration, scaling, retries, and task execution move from self-managed Kubernetes primitives into a narrower managed service.

## Key Claims
- Container adoption is incomplete when teams only run existing programs inside containers.
- Local-storage assumptions can keep containerized workloads tied to fragile host state.
- Effective health checks are part of container-native operation, not optional decoration.
- Signal handling and graceful shutdown are necessary for safe lifecycle management.
- Tooling around Dockerfiles can improve repeatability and cache behavior, but it does not by itself make services container native.
- A managed container platform can preserve container packaging while reducing how much orchestration machinery the application team must operate.

## Evidence
- Adoption gap: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the company had used containers in production for years but often only ran existing programs in containers.
- Local storage: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] names local-storage dependency as a remaining non-container-native behavior.
- Health checks: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says many containers lacked effective health checks.
- Graceful shutdown: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says many containers could not correctly handle signals.
- Dockerfile DSL: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] describes a Node.js DSL that structured Dockerfile instructions to improve formatting and cross-language caching.
- Managed container operations: [[ben-houston-i-didnt-need-kubernetes]] says [[GoogleCloudRun]] handles container deployment, scaling, downtime management, and job running for the author's Docker-based stack.
- Platform fit: [[ben-houston-i-didnt-need-kubernetes]] keeps Docker containers while rejecting direct Kubernetes operation for this workload.

## Counterevidence & Qualifications
The sources do not imply that managed container services remove the need for container discipline. Local development, service naming, task emulation, storage, health, and graceful shutdown still matter. Houston's Cloud Run experience is workload-specific, while Wang Ziting's retrospective reflects 2018 container practice in one organization.

## What Changed
- Added Cloud Run as a managed-container case where the deployment unit stays containerized but orchestration burden shifts to the platform.

## Related Concepts
- [[ContainerApplicationStartup]] - startup design is one part of broader container-native behavior.
- [[DeclarativeInfrastructure]] - declarative container platforms still require well-behaved workloads.
- [[GameServerCloudNativeDelivery]] - container-native practice supports delivery, rollback, and operations goals.
- [[SystemReliability]] - health checks and graceful shutdown are reliability mechanisms.
- [[GoogleCloudRun]] - managed platform that can handle some container operation concerns.
- [[Kubernetes]] - orchestration platform whose value still depends on well-behaved workloads.

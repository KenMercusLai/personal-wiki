---
title: "Game Server SLA"
type: concept
tags: [game-server, sla, reliability, observability]
sources:
  - you-shang-xian-chan-sheng-de-si-kao
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[GameServerSLA]] is the service-level reliability target a game server team commits to users and internal functions, built above cloud-provider guarantees through application-level governance, recovery, and observability.

## Current Synthesis
The source treats cloud-provider SLA as a lower bound, not the full reliability goal. A game server team should pursue higher standards by controlling its own service governance, recovery automation, and application observability. Service governance includes discovery, health checks, load balancing, degradation, rate limiting, circuit breaking, and self-recovery; the source also stresses that health decisions should avoid depending on one fragile component.

Disaster recovery is framed as a correctness problem. Multi-availability-zone deployment, partitioned external dependencies, VM failure, planned restarts, network glitches, external IO instability, core-service reconnects, and service/data recovery paths all need process, state, and logic correctness. Observability should cover metrics, monitoring, alerts, logs, tracing, inspection, debugging, REPL-style access, and business-level signals instead of only machine metrics.

## Key Claims
- Cloud-provider SLA is only a baseline for a game server team's user-facing reliability promise.
- Service governance should be configurable, layered, and resilient to component failure.
- Disaster recovery must cover infrastructure, network, external IO, service, data, and emergency-process failures.
- Recovery quality depends on process correctness, state correctness, automation, and decentralized offline detection.
- Observability should saturate the application and business layers, not stop at host-level metrics.

## Evidence
- SLA framing: [[you-shang-xian-chan-sheng-de-si-kao]] defines SLA as both user-facing service level and the backend team's commitment to other functions.
- Service governance: [[you-shang-xian-chan-sheng-de-si-kao]] names discovery, liveness detection, load balancing, degradation, rate limits, circuit breaking, self-recovery, native-layer governance, and business-framework governance.
- Recovery surface: [[you-shang-xian-chan-sheng-de-si-kao]] lists multi-AZ deployment, external dependency partitioning, VM faults, network and ACL instability, external IO instability, core-service reconnection, service recovery, data recovery, drills, plans, and SOPs.
- Observability surface: [[you-shang-xian-chan-sheng-de-si-kao]] calls for monitoring, statistics, instrumentation, alerts, logs, tracing, business metrics, latency, traffic, congestion, error, load, inspect, debug, and REPL capabilities.

## Counterevidence & Qualifications
The source provides an engineering agenda rather than measured SLA outcomes. It assumes enough organizational control to modify frameworks, service roles, observability, and recovery workflows.

## What Changed
- Created the concept page for SLA as an application-level game-server reliability target.

## Related Concepts
- [[GameServerScaleAndStability]] - SLA pursuit operationalizes the stability side of game-server launch experience.
- [[LowOpsGameServer]] - low-operations design reduces the manual burden of meeting reliability goals.
- [[HarnessEngineering]] - both concepts use surrounding systems to make execution more reliable.
- [[SoftwareVerification]] - correctness checks and drills support the SLA target.

---
title: "Dependency Degradation"
type: concept
tags: [software-engineering, reliability, architecture]
sources:
  - wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[DependencyDegradation]] is the reliability practice of identifying which dependencies are strong or weak and designing fallback, degradation, or fail-fast behavior so dependency trouble does not unnecessarily take down the whole service.

## Current Synthesis
The source presents dependency recognition as a design-level reliability control. Strong dependencies determine whether the service can function at all; weak dependencies should be surrounded with degradation strategies so their failure reduces capability without causing full system failure. This sits beside capacity protection: a service must know its own throughput ceiling and fail quickly once it exceeds safe capacity rather than accumulating unsafe online backlog.

The article frames disaster recovery as the broader version of this design thinking. Clustered deployment, same-city multi-active setups, and geo-distributed multi-active systems are mature options, but the real architectural decision is how much reliability investment a business context justifies.

The health-check source extends degradation from dependency classification into continuous workload control. Partial failure includes features or capacity becoming unavailable while the process remains alive. Preserving the rest of the service then depends on detecting degraded quality, refusing work before saturation, bounding queues, and propagating backpressure so failure does not migrate to the next component.

## Key Claims
- Reliability design starts by distinguishing strong dependencies from weak dependencies.
- Weak dependencies should have degradation strategies.
- Services need an explicit understanding of their own capacity limits.
- Online services should avoid unbounded accumulation when request volume exceeds capacity.
- Partial failure can exist while a process remains alive, so graceful degradation needs quality-of-service and capacity signals.
- Backpressure, bounded queues, and explicit rejection keep overload from spreading invisibly through dependencies.
- Disaster recovery and degradation architecture require business-level investment tradeoffs.

## Evidence
- Dependency classification: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says weak dependencies need degradation strategies and cites a key Alibaba system whose stability improved after doing this well.
- Capacity protection: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says online services should understand request-per-second capacity and fail fast beyond it.
- Backlog warning: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] warns that accumulation in online systems can create problems unless bounded.
- Disaster recovery: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] names clustering, same-city multi-active, and geo-distributed multi-active patterns as mature reliability options.
- Investment tradeoff: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says architecture-level reliability investment can be large and therefore becomes a bigger decision than individual code robustness.
- Partial failure: [[health-checks-and-graceful-degradation-in-distributed-systems]] distinguishes service features or capacity being degraded from a process being fully down.
- Overload containment: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes request refusal, alternate routing, bounded queues, rejection, and retry backoff in the Spillway case.

## Counterevidence & Qualifications
The sources give principles and one historical design rather than a general implementation recipe. They do not specify how to classify dependencies, choose degradation semantics, size thresholds and queues, protect fairness, prevent retry amplification, or decide when multi-active disaster recovery is worth its cost.

## What Changed
- Broadened degradation from dependency classification to continuous partial-capacity and overload handling.
- Added bounded admission and end-to-end backpressure as mechanisms for keeping local degradation local.

## Related Concepts
- [[SystemReliability]] - dependency degradation is a design-level reliability mechanism.
- [[ChangeSafety]] - degradation and capacity limits reduce the impact of faulty changes.
- [[ReliabilityInvestment]] - dependency and disaster-recovery work often requires explicit business investment.
- [[GameServerScaleAndStability]] - both emphasize capacity, failure, and recovery under real load.
- [[ServiceHealthChecks]] - quality-of-service signals reveal degraded capacity before total failure.
- [[AdaptiveBackpressure]] - upstream admission control prevents a weak dependency from accumulating unlimited work.

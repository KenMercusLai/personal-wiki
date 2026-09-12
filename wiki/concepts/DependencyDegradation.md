---
title: "Dependency Degradation"
type: concept
tags: [software-engineering, reliability, architecture]
sources:
  - wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[DependencyDegradation]] is the reliability practice of identifying which dependencies are strong or weak and designing fallback, degradation, or fail-fast behavior so dependency trouble does not unnecessarily take down the whole service.

## Current Synthesis
The source presents dependency recognition as a design-level reliability control. Strong dependencies determine whether the service can function at all; weak dependencies should be surrounded with degradation strategies so their failure reduces capability without causing full system failure. This sits beside capacity protection: a service must know its own throughput ceiling and fail quickly once it exceeds safe capacity rather than accumulating unsafe online backlog.

The article frames disaster recovery as the broader version of this design thinking. Clustered deployment, same-city multi-active setups, and geo-distributed multi-active systems are mature options, but the real architectural decision is how much reliability investment a business context justifies.

## Key Claims
- Reliability design starts by distinguishing strong dependencies from weak dependencies.
- Weak dependencies should have degradation strategies.
- Services need an explicit understanding of their own capacity limits.
- Online services should avoid unbounded accumulation when request volume exceeds capacity.
- Disaster recovery can be designed through increasingly resilient deployment patterns.
- Architectural reliability choices require business-level investment tradeoffs.

## Evidence
- Dependency classification: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says weak dependencies need degradation strategies and cites a key Alibaba system whose stability improved after doing this well.
- Capacity protection: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says online services should understand request-per-second capacity and fail fast beyond it.
- Backlog warning: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] warns that accumulation in online systems can create problems unless bounded.
- Disaster recovery: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] names clustering, same-city multi-active, and geo-distributed multi-active patterns as mature reliability options.
- Investment tradeoff: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] says architecture-level reliability investment can be large and therefore becomes a bigger decision than individual code robustness.

## Counterevidence & Qualifications
The source gives principles rather than implementation recipes. It does not specify how to classify dependencies, choose degradation semantics, size capacity thresholds, or decide when multi-active disaster recovery is worth its cost.

## What Changed
- Created the concept page for dependency-aware reliability design and capacity protection.

## Related Concepts
- [[SystemReliability]] - dependency degradation is a design-level reliability mechanism.
- [[ChangeSafety]] - degradation and capacity limits reduce the impact of faulty changes.
- [[ReliabilityInvestment]] - dependency and disaster-recovery work often requires explicit business investment.
- [[GameServerScaleAndStability]] - both emphasize capacity, failure, and recovery under real load.

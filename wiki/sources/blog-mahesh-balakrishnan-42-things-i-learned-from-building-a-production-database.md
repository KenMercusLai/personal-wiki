---
title: "42 Things I Learned from Building a Production Database"
type: source
tags: [database, distributed-systems, production-infrastructure, engineering-leadership]
date: 2021-10-19
source_file: /mnt/ken_personal_wiki/Articles/Blog - Mahesh Balakrishnan - 42 Things I Learned from Building a Production Database.md
---

## Summary
[[MaheshBalakrishnan]] distills lessons from leading [[Delos]], a Facebook storage system built by a three-person team, scaled to 30+ engineers, and run without severe outages during his four-year leadership period. The article frames [[ProductionInfrastructureLeadership]] as a combined customer, design, review, strategy, observability, and research practice: production database work succeeds when teams stay close to real users, preserve conservative APIs, prioritize consistency and durability, review critical changes carefully, and detect problems before customers do.

## Key Claims
- [[ProductionInfrastructureLeadership]] starts with customer selection and direct contact: early infrastructure teams should serve the right first customers, talk to customer ICs, and read their code instead of accepting requirements at face value.
- Infrastructure leads should keep the mission simple, socialize realistic task estimates, match work to IC strengths, and make projects robust to management re-orgs.
- Production storage APIs should be conservative and migration-friendly while implementations remain swappable through staged rollout, shadowing, multiple tested implementations, and CLI-driven migration paths.
- Storage systems should initially bias toward consistency and durability because these properties are harder to measure and repair than availability.
- Critical code review should slow down when correctness matters: multiple accepts, high-quality critique, and willingness to throw away wrong code are more important than fast landing time.
- [[ServiceObservability]] should sit above APIs and outside implementations where possible, with consistency checks pushed into deployment so implementation swaps do not corrupt measurement.
- Production infrastructure teams need technical strategy and research literacy: they should understand adjacent internal systems, compete on fundamental design properties, track research, try novel feasible designs, and write papers to clarify assumptions.

## Key Quotes
> "Keep your customers happy; else the rest of this document doesn't matter." - customer priority.

> "Design as a team; implement as individuals." - design-process rule.

> "Measurement is a means, not an end." - observability caveat.

## Connections
- [[MaheshBalakrishnan]] - author and Delos tech lead.
- [[Delos]] - production storage system whose development and operation supply the article's evidence.
- [[Facebook]] - company context for Delos and large-scale infrastructure replacement.
- [[ZooKeeper]] - system Delos was replacing within Facebook.
- [[ProductionInfrastructureLeadership]] - source's central synthesis across customers, design, review, observability, strategy, and research.
- [[SystemReliability]] - Delos' no-severe-outage record and rollout practices connect reliability to design, process, and monitoring.
- [[ServiceObservability]] - the source argues for observability above APIs and implementation-independent measurement.
- [[CodeReviewPractice]] - the source qualifies fast-flow review norms for critical components.
- [[SoftwareVerification]] - multiple implementations in test and consistency checks in deployment are verification mechanisms.
- [[ChangeSafety]] - shadowing, staged rollout, and single-command implementation switches reduce migration and rollout risk.
- [[DistributedSystemRestraint]] - the article is not anti-distribution, but it stresses careful abstraction count, single source of truth, and clock-bound awareness.

## Contradictions
- Partly qualifies [[CodeReviewPractice]]: the Asana review source says reviewers should usually approve unless they can prove a bug, while this source argues critical infrastructure components may need stricter gates, slower landing, and even unanimous approval from selected ICs.

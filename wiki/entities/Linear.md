---
title: "Linear"
type: entity
tags: [software, product, quality, growth]
sources:
  - everyone-can-build-almost-no-one-can-judge
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[Linear]] is a software company represented as both a product-led operating example for [[QualityGrowth]] and a customer case for permission-aware delta synchronization over a large action history.

## Current Profile
[[MaiYang]] presents Linear as translating product quality into routines rather than treating it as branding. The article reports a zero-bugs policy with 48-hour handling for high-priority defects and seven-day handling for other defects, plus “Quality Wednesdays” aimed at small experience flaws. It also says the company relied relatively little on an early sales organization and sought growth through product demand, but supplies no underlying company metrics or independent comparison.

Linear also appears in the evidence as a delta-sync systems case. Its clients retain local data and request actions after a checkpoint when returning online. As workspace history grew, the old PostgreSQL path reportedly scanned an expanding ID range and evaluated permission groups and subscriptions, producing unstable tail latency. Linear moved compact sync metadata into [[Turbopuffer]], represented permission groups and subscriptions as sorted ID sets, and intersected them with the post-checkpoint range before fetching complete actions. A deliberately overlapping recent PostgreSQL window, action-ID deduplication, PostgreSQL fallback, and prelaunch shadow comparison bounded synchronization risk.

## Key Characteristics
- Uses time-bounded defect handling instead of an indefinitely accumulating bug backlog.
- Treats small product-experience defects as recurring operating work.
- Favors focused user workflows over feature-checklist breadth.
- Is presented as pursuing product-driven, capital-efficient growth.
- Uses local client state and checkpointed delta synchronization.
- Reportedly narrows sync actions through indexed permission, subscription, and checkpoint set intersections.
- Keeps an overlapping PostgreSQL read path for freshness, fallback, and result comparison.

## Evidence
- Defect discipline: [[everyone-can-build-almost-no-one-can-judge]] reports 48-hour handling for high-priority defects and seven-day handling for other bugs under Linear's public policy.
- Quality routine: [[everyone-can-build-almost-no-one-can-judge]] describes “Quality Wednesdays” as regular attention to small experience problems.
- Product focus: [[everyone-can-build-almost-no-one-can-judge]] says Linear designs around users' principal work rather than positioning itself as an unbounded platform.
- Growth posture: [[everyone-can-build-almost-no-one-can-judge]] says the early company had little sales capacity and depended more heavily on product recognition.
- Delta-sync workload: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes clients requesting authorized and subscribed actions after their last checkpoint.
- Indexed narrowing: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] relays sorted-ID unions and intersections in Turbopuffer before complete records are fetched.
- Freshness and fallback: [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes overlapping recent PostgreSQL reads, action-ID deduplication, fallback, and shadow comparison of old and new paths.

## Qualifications
The profile comes from one favorable secondary essay drawing on company posts and interviews plus a practitioner retelling of a first-party customer case. It gives no defect-volume denominator, compliance rate, customer cohorts, retention, revenue, or causal proof that quality practices drove growth. The sync account gives no action volume, query distribution, latency percentiles, error rate, authorization audit, infrastructure cost, failure-test result, or independent reproduction. It demonstrates a reported architecture and migration discipline, not universal superiority over PostgreSQL or another index.

## What Changed
- Created a source-scoped profile of Linear's reported defect discipline, workflow focus, and product-led growth posture.
- Added the permission- and subscription-aware delta-sync read path.
- Added overlap, deduplication, shadow comparison, and PostgreSQL fallback as migration safeguards.

## Relationships
- [[KarriSaarinen]] - co-founder and CEO in the supplied source.
- [[MaiYang]] - author presenting Linear as the article's central company case.
- [[QualityGrowth]] - Linear is the principal operating example used to explain this framework.
- [[ZeroBugsPolicy]] - reported defect-disposition practice with time targets.
- [[FeatureCreep]] - Linear's workflow focus is positioned against checklist-driven breadth.
- [[ProductLedRetention]] - recurring product desire is the implied mechanism behind durable product-led growth.
- [[Turbopuffer]] - supplies the reported historical set-intersection path for delta sync.
- [[PostgreSQL]] - retains recent authoritative actions and the fallback path.
- [[PersonalAgentRetrieval]] - shares the need to combine indexed candidates with authorization and authoritative source records.

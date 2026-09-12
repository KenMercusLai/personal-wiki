---
title: "稳定性，难的不是技术，而是"
type: source
tags: [software-engineering, reliability, operations, change-management]
date: 2026-09-12
source_file: /mnt/ken_personal_wiki/Articles/稳定性，难的不是技术，而是.md
---

## Summary
[[Bixuan]] argues that [[SystemReliability]] is difficult less because teams lack technical principles than because those principles require sustained organizational investment. The article organizes reliability work across [[RobustProgramming]], dependency-aware design, capacity protection, disaster recovery, and [[ChangeSafety]], then argues that reliability must be budgeted like product functionality rather than treated as an occasional campaign.

## Key Claims
- [[RobustProgramming]] depends on controlling input boundaries, deeply understanding APIs, and failing fast before unexpected conditions exhaust resources or crash services.
- [[DependencyDegradation]] and capacity protection are design-level reliability practices: teams need to distinguish strong from weak dependencies, degrade weak dependencies, and fail fast when load exceeds service capacity.
- [[ChangeSafety]] is central because many incidents are change-related; mandatory canary release, monitoring, rollback, and blast-radius control matter most for core systems.
- Incident handling should prioritize rapid service restoration over root-cause analysis during the outage, while preserving enough evidence for later investigation.
- [[ReliabilityInvestment]] is the hard part: reliability has no silver bullet, earns little credit when it works, and requires continuous staffing, process, and attention.

## Key Quotes
> "并没有银弹级产品" - the author rejects tool-based guarantees for reliability.

> "很多公司都是运动式的做稳定性" - the author describes episodic reliability campaigns.

> "有些时候慢才是快" - the article justifies mandatory change controls for critical systems.

## Connections
- [[Bixuan]] - practitioner-author reflecting on reliability from serious incident experience.
- [[SystemReliability]] - the article's central umbrella concept.
- [[RobustProgramming]] - code-level reliability discipline.
- [[DependencyDegradation]] - design-level handling of weak dependencies and overload.
- [[ChangeSafety]] - operational-change controls for canarying, rollback, monitoring, blast radius, and recovery.
- [[ReliabilityInvestment]] - the article's main explanation for why reliability remains difficult.
- [[SoftwareVerification]] - adjacent quality practice; this source broadens reliability beyond tests into design, change, and operations.
- [[HarnessEngineering]] - related through the use of process, monitoring, rollback, and constraints to make work reliable.
- [[GameServerScaleAndStability]] - domain-specific reliability page that this source complements with general software-system principles.

## Contradictions
- None identified. The article qualifies existing verification and game-server stability pages by emphasizing that known technical practices still fail without continuous investment and organizational enforcement.

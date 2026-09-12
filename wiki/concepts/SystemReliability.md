---
title: "System Reliability"
type: concept
tags: [software-engineering, reliability, operations]
sources:
  - wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[SystemReliability]] is the practice of keeping software services dependable across code behavior, architecture, dependencies, capacity limits, operational change, disaster recovery, and incident response.

## Current Synthesis
The source presents reliability as a system of many small practices rather than a product or silver-bullet tool. Code must reject bad input, handle boundary conditions, understand API behavior, and fail fast before resources are exhausted. Design must identify strong and weak dependencies, degrade weak dependencies, protect system capacity, and build disaster-recovery paths. Change management must constrain blast radius through canarying, monitoring, rollback, and recovery-first incident handling.

The harder claim is organizational: the technical playbook is widely available, and many postmortems repeat the same improvement themes. What breaks reliability work is the difficulty of keeping enough people, time, enforcement, and business priority attached to it when success is invisible.

## Key Claims
- Reliability spans code, design, change, operations, and recovery rather than one technical layer.
- Known principles are necessary but insufficient without concrete implementation details.
- Fail-fast behavior protects online services from resource exhaustion and uncontrolled backlog.
- Dependency classification, degradation, capacity protection, and disaster recovery are design-level reliability controls.
- Change-related incidents require canarying, monitoring, rollback, and blast-radius reduction.
- Reliability is difficult because it requires sustained investment even when avoided failures are hard to see.

## Evidence
- Code layer: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] names input-boundary control, API understanding, and fail-fast behavior as core code-level reliability practices.
- Design layer: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] names strong/weak dependency recognition, degradation, capacity protection, and disaster recovery as design responsibilities.
- Change layer: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] names mandatory canarying, monitoring, rollback, and restoration-first incident response.
- Organizational layer: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] argues that postmortem recommendations repeat known principles, but teams struggle to sustain the investment needed to implement them.
- Business priority: [[wen-ding-xing-nan-de-bu-shi-ji-shu-er-shi]] uses Taobao and high-stakes businesses as examples where making reliability a top business target changed outcomes.

## Counterevidence & Qualifications
The source argues from practitioner experience and named examples rather than comparative measurement. Its fail-fast emphasis is explicitly strongest for online services; queueing, batch, streaming, or safety-critical systems may require different overload behavior and recovery semantics.

## What Changed
- Created the general reliability concept to complement existing AI-harness and game-server-specific reliability pages.

## Related Concepts
- [[RobustProgramming]] - code-level reliability is one layer of system reliability.
- [[DependencyDegradation]] - dependency classification and degradation are design-level reliability controls.
- [[ChangeSafety]] - safe operational change is a major reliability layer.
- [[ReliabilityInvestment]] - sustained investment is the source's main explanation for reliability difficulty.
- [[SoftwareVerification]] - verification checks behavior, while system reliability also includes capacity, change, recovery, and investment.
- [[HarnessEngineering]] - both rely on scaffolds, feedback signals, and constraints to make technical work dependable.
- [[GameServerScaleAndStability]] - game-server stability is a domain-specific instance of broader system reliability.

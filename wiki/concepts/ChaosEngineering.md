---
title: "Chaos Engineering"
type: concept
tags: [software-engineering, reliability, operations, testing]
sources:
  - 7-reasons-why-your-staging-environment-sucks-loadmill
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ChaosEngineering]] is the practice of deliberately introducing controlled failure or surprise into a system so teams can verify resilience before uncontrolled production failure occurs.

## Current Synthesis
The source introduces chaos engineering through staging rather than through production experimentation. Its argument is that real systems face crashes, abusive traffic, denial-of-service attempts, hosting outages, and network failures, so a serious test cycle should include some element of surprise before release.

In this framing, chaos engineering is not random breakage for its own sake. It is a reliability exercise performed against a representative [[StagingEnvironment]] so teams can discover whether recovery paths, dependencies, monitoring, and operational assumptions hold under conditions they did not explicitly script.

## Key Claims
- Real operational environments include surprise, so pre-release testing should not cover only expected happy paths.
- Injected failures can reveal resilience gaps that ordinary automated tests miss.
- Staging is a lower-risk venue for practicing chaos when teams are trying to improve reliability before release.
- Chaos experiments are most meaningful when the surrounding environment resembles production.

## Evidence
- Surprise requirement: [[7-reasons-why-your-staging-environment-sucks-loadmill]] argues that servers crash, abuse and denial-of-service attacks happen, hosting services fail, and networks go down.
- Staging application: [[7-reasons-why-your-staging-environment-sucks-loadmill]] recommends adding chaos while running the test cycle in staging.
- Tool examples: [[7-reasons-why-your-staging-environment-sucks-loadmill]] cites Chaos Monkey, Simian Army, and Gremlin as examples of open-source or commercial chaos tooling.
- Production resemblance: [[7-reasons-why-your-staging-environment-sucks-loadmill]] places chaos alongside architecture, monitoring, data, traffic, and internet exposure as part of realistic staging.

## Counterevidence & Qualifications
The source does not provide a full chaos-engineering methodology, safety model, or production-experiment design. Its recommendation is scoped to staging-based resilience practice, where the goal is to reveal pre-release weakness without exposing users first.

## What Changed
- Created the concept page for controlled surprise and failure injection in staging.

## Related Concepts
- [[StagingEnvironment]] - staging is the source's recommended venue for chaos experiments.
- [[SystemReliability]] - chaos experiments test whether reliability mechanisms survive realistic failure.
- [[DependencyDegradation]] - injected dependency failures can validate degradation behavior.
- [[ChangeSafety]] - chaos testing can reduce release risk before production changes.
- [[SoftwareVerification]] - chaos experiments provide behavioral evidence beyond deterministic tests.

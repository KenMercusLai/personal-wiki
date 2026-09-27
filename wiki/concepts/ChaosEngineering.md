---
title: "Chaos Engineering"
type: concept
tags: [software-engineering, reliability, operations, testing]
sources:
  - 7-reasons-why-your-staging-environment-sucks-loadmill
  - emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[ChaosEngineering]] is the practice of deliberately introducing controlled failure or surprise into a system so teams can verify resilience before uncontrolled production failure occurs.

## Current Synthesis
The source introduces chaos engineering through staging rather than through production experimentation. Its argument is that real systems face crashes, abusive traffic, denial-of-service attempts, hosting outages, and network failures, so a serious test cycle should include some element of surprise before release.

In this framing, chaos engineering is not random breakage for its own sake. It is a reliability exercise performed against a representative [[StagingEnvironment]] so teams can discover whether recovery paths, dependencies, monitoring, and operational assumptions hold under conditions they did not explicitly script.

Uber's uDestroy account adds a recurring service-operations case: controlled disruption was used to prepare for outages and network-connectivity failures, and periodic experiments were intended to expose new vulnerabilities as systems evolved. This broadens the practice beyond a one-time pre-release surprise while leaving the environment and safety controls unspecified.

## Key Claims
- Real operational environments include surprise, so pre-release testing should not cover only expected happy paths.
- Injected failures can reveal resilience gaps that ordinary automated tests miss.
- Staging is a lower-risk venue for practicing chaos when teams are trying to improve reliability before release.
- Chaos experiments are most meaningful when the surrounding environment resembles production.
- Repeating controlled disruption can reveal resilience regressions as services and dependencies change.

## Evidence
- Surprise requirement: [[7-reasons-why-your-staging-environment-sucks-loadmill]] argues that servers crash, abuse and denial-of-service attacks happen, hosting services fail, and networks go down.
- Staging application: [[7-reasons-why-your-staging-environment-sucks-loadmill]] recommends adding chaos while running the test cycle in staging.
- Tool examples: [[7-reasons-why-your-staging-environment-sucks-loadmill]] cites Chaos Monkey, Simian Army, and Gremlin as examples of open-source or commercial chaos tooling.
- Production resemblance: [[7-reasons-why-your-staging-environment-sucks-loadmill]] places chaos alongside architecture, monitoring, data, traffic, and internet exposure as part of realistic staging.
- Recurring disruption: [[emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering]] says Uber's uDestroy simulated outages and network problems periodically so teams could identify vulnerabilities and improve durability.

## Counterevidence & Qualifications
Neither source provides a full chaos-engineering methodology, hypothesis design, abort condition, blast-radius control, or outcome measurement. The Loadmill recommendation is scoped to staging-based practice. Uber does not specify where uDestroy experiments ran, which failures were injected, how experiments were contained, or whether measured resilience improved, so its account should not be read as permission for uncontrolled production disruption.

## What Changed
- Extended the concept from staging surprise to periodic disruption as systems evolve.
- Added an explicit qualification around unspecified environment, containment, and measured outcomes.

## Related Concepts
- [[StagingEnvironment]] - staging is the source's recommended venue for chaos experiments.
- [[SystemReliability]] - chaos experiments test whether reliability mechanisms survive realistic failure.
- [[DependencyDegradation]] - injected dependency failures can validate degradation behavior.
- [[ChangeSafety]] - chaos testing can reduce release risk before production changes.
- [[SoftwareVerification]] - chaos experiments provide behavioral evidence beyond deterministic tests.
- [[MicroservicePlatformEngineering]] - a shared disruption tool can make resilience testing reusable across service teams.

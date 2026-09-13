---
title: "Continuous Delivery"
type: concept
tags: [continuous-delivery, release-engineering, software-architecture]
sources:
  - architecting-for-continuous-delivery-thoughtworks
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ContinuousDelivery]] is the capability to release software frequently, reliably, and with low friction through compatible architecture, fast feedback, automated deployment, and visible release flow.

## Current Synthesis
The Thoughtworks source frames continuous delivery as broader than tool selection. Version control, CI servers, infrastructure configuration, monitoring, and deployment automation matter, but they do not produce CD if developers avoid small frequent commits, lack automated tests, or cannot see and improve the release path.

The durable synthesis is that CD is a system property. Slow monolithic builds, brittle acceptance-test suites, and disconnected deployment jobs each reduce release confidence. Architecture, test design, and pipeline design therefore become delivery concerns, not secondary implementation details.

## Key Claims
- Continuous delivery is a release capability, not a list of tools.
- CD depends on frequent small integration, automated tests, and repeated deployment practice.
- Architectural choices can improve or damage delivery throughput.
- Feedback speed matters at both developer and CI levels.
- Pipeline visibility helps teams identify bottlenecks and improve the production flow over time.

## Evidence
- Tooling limit: [[architecting-for-continuous-delivery-thoughtworks]] says a CI server and version-control tool do not create CI when commits are large or automated tests are missing.
- Release goal: [[architecting-for-continuous-delivery-thoughtworks]] defines the CD goal as frequent, reliable, low-friction release.
- Architecture role: [[architecting-for-continuous-delivery-thoughtworks]] presents monolith decomposition, test-suite design, and deployment pipelines as recurring CD-enablement themes.
- Improvement loop: [[architecting-for-continuous-delivery-thoughtworks]] says teams should identify deployment bottlenecks and streamline the process over time.

## Counterevidence & Qualifications
The source is practitioner guidance from 2016, not a universal CD taxonomy. Its examples focus on codebase decomposition, test feedback, and pipeline tooling; later practices such as feature flags, canary rollout, progressive delivery, and production observability can extend the same release-confidence frame.

## What Changed
- Created the concept from Thoughtworks' architecture-centered CD article.

## Related Concepts
- [[DeploymentPipeline]] - pipeline visibility is the article's core mechanism for CD release confidence.
- [[DeploymentAutomation]] - automation is necessary but insufficient for CD.
- [[CDComponentization]] - component boundaries can improve CD feedback and ownership.
- [[TestPyramid]] - test design keeps CD feedback fast enough to trust.
- [[MicroserviceOperationalOverhead]] - service-based CD gains must be weighed against operational cost.
- [[DistributedSystemRestraint]] - decomposition should match organizational maturity and capacity.

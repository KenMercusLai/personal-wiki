---
title: "Continuous Delivery"
type: concept
tags: [continuous-delivery, release-engineering, software-architecture]
sources:
  - architecting-for-continuous-delivery-thoughtworks
  - blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ContinuousDelivery]] is the capability to release software frequently, reliably, and with low friction through compatible architecture, fast feedback, automated deployment, and visible release flow.

## Current Synthesis
The Thoughtworks source frames continuous delivery as broader than tool selection. Version control, CI servers, infrastructure configuration, monitoring, and deployment automation matter, but they do not produce CD if developers avoid small frequent commits, lack automated tests, or cannot see and improve the release path.

The durable synthesis is that CD is a system property. Slow monolithic builds, brittle acceptance-test suites, and disconnected deployment jobs each reduce release confidence. Architecture, test design, and pipeline design therefore become delivery concerns, not secondary implementation details.

Nygard's compliance source adds the regulated-environment constraint: CD in a DevOps culture must preserve team autonomy, frequent small releases, and low MTTR while still producing objective compliance evidence and auditability. Compliance architecture can either support CD by moving checks left and to the point of change, or inhibit CD by adding central queues, manual gates, and large approval batches.

## Key Claims
- Continuous delivery is a release capability, not a list of tools.
- CD depends on frequent small integration, automated tests, and repeated deployment practice.
- Architectural choices can improve or damage delivery throughput.
- Feedback speed matters at both developer and CI levels.
- Pipeline visibility helps teams identify bottlenecks and improve the production flow over time.
- Regulated delivery needs compliance evidence and auditability without turning approval into a batch-size driver.

## Evidence
- Tooling limit: [[architecting-for-continuous-delivery-thoughtworks]] says a CI server and version-control tool do not create CI when commits are large or automated tests are missing.
- Release goal: [[architecting-for-continuous-delivery-thoughtworks]] defines the CD goal as frequent, reliable, low-friction release.
- Architecture role: [[architecting-for-continuous-delivery-thoughtworks]] presents monolith decomposition, test-suite design, and deployment pipelines as recurring CD-enablement themes.
- Improvement loop: [[architecting-for-continuous-delivery-thoughtworks]] says teams should identify deployment bottlenecks and streamline the process over time.
- DevOps compliance fit: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] says DevOps culture stresses autonomy, frequent small releases, and low MTTR while still needing compliance controls and audit.
- Batch pressure: [[blog-carl-nygard-martinfowler-com-compliance-in-a-devops-culture]] says slow compliance approvals can force larger deployment batches because approval capacity limits release count.

## Counterevidence & Qualifications
The sources are practitioner guidance rather than a universal CD taxonomy. Naik's examples focus on codebase decomposition, test feedback, and pipeline tooling; Nygard's regulated-delivery examples add compliance controls, auditability, and organizational ownership. Later practices such as feature flags, canary rollout, progressive delivery, and production observability can extend the same release-confidence frame.

## What Changed
- Created the concept from Thoughtworks' architecture-centered CD article.
- Added regulated-delivery constraints from Nygard's compliance article.

## Related Concepts
- [[DeploymentPipeline]] - pipeline visibility is the article's core mechanism for CD release confidence.
- [[DeploymentAutomation]] - automation is necessary but insufficient for CD.
- [[CDComponentization]] - component boundaries can improve CD feedback and ownership.
- [[TestPyramid]] - test design keeps CD feedback fast enough to trust.
- [[MicroserviceOperationalOverhead]] - service-based CD gains must be weighed against operational cost.
- [[DistributedSystemRestraint]] - decomposition should match organizational maturity and capacity.
- [[ComplianceArchitecture]] - compliance design can either support or inhibit CD flow.

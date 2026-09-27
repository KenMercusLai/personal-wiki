---
title: "Production Ownership"
type: concept
tags: [software-engineering, devops, operations, observability]
sources:
  - etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[ProductionOwnership]] is the assignment of continuing operational responsibility to the people who build and deploy software, including responsibility for knowing whether it works, detecting failure, participating in recovery, and improving the system afterward.

## Current Synthesis
The Etsy interview connects authority and feedback. When an engineer can deploy their own change, responsibility becomes concrete: the next questions are how they will know it is broken, whether it can fail invisibly, and what monitoring, alerting, and metrics are required. Ownership therefore extends beyond code authorship into operation and learning.

This does not mean every engineer must independently master every layer or that infrastructure abstractions are useless. [[JohnAllspaw]] distinguishes focus from disinterest: engineers can use an abstraction while understanding that lower layers still matter and seeking specialists when an application, database, network, or platform boundary becomes relevant. Production ownership is strongest when shared tools and expertise make responsibility actionable, rather than using “you own it” as permission for blame or unsupported on-call burden.

## Key Claims
- Deploy authority should be paired with responsibility for the production behavior of the change.
- Ownership creates demand for monitoring, alerting, metrics, and failure-detection paths.
- Abstraction should let engineers focus temporarily without declaring lower layers irrelevant.
- Multidisciplinary ownership depends on shared understanding and access to specialists, not universal individual expertise.
- Simple, confidence-producing deployment and onboarding make ownership more reachable for new engineers.
- Operational responsibility must remain supported and psychologically safe or it can degrade into blame and overload.

## Evidence
- Authority and accountability: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] states “you build it, you own it” and links pressing the production deploy button with personal responsibility for the result.
- Observability consequence: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] says deploy responsibility leads engineers to ask how breakage will be detected and to care about monitoring, alerting, and metrics.
- Abstraction boundary: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] distinguishes focused use of an abstraction from treating the underlying system as “not my job.”
- Shared expertise: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] describes application and network engineers learning across boundaries while still seeking domain experts.
- Accessible path: [[etsy-cto-q-a-we-need-software-engineers-not-developers-the-new-stack]] treats inability to deploy during the first day or week as evidence that deployment or onboarding is too difficult.

## Counterevidence & Qualifications
The evidence is one 2016 executive interview without incident, workload, retention, or delivery comparisons. Code authors may not control shared infrastructure, staffing, access, legacy architecture, vendor failures, or organizational priorities, so responsibility must follow real authority and support. Strict individual ownership can discourage reporting, intensify on-call load, or personalize systemic failure; regulated or high-risk systems may also require separation of duties, independent review, and specialized operators. The durable principle is closed-loop responsibility with shared systems and expertise, not solitary ownership of every dependency.

## What Changed
- Created the concept around the link between deployment authority, observability, operation, and supported cross-domain learning.

## Related Concepts
- [[DevOpsCulture]] - broadens production responsibility into an organization-wide collaboration and incentive model.
- [[ServiceObservability]] - supplies the signals by which owners learn whether production behavior matches intent.
- [[DeploymentAutomation]] - makes the path into production repeatable enough for ownership to be exercised safely.
- [[SystemReliability]] - production owners contribute to prevention, detection, response, and recovery.
- [[PsychologicalSafety]] - ownership requires candid failure reporting without humiliation or scapegoating.
- [[FailureOwnership]] - converts acknowledged failure into learning, while production ownership adds continuing operational authority and duty.
- [[InternalDeveloperPlatform]] - can package safe deployment, monitoring, rollback, and support defaults for service owners.

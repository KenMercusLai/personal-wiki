---
title: "Deployment-Release Separation"
type: concept
tags: [deployment, release-engineering, reliability, continuous-delivery]
sources:
  - deploy-release-part-1-turbine-labs
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DeploymentReleaseSeparation]] is the practice of installing and validating a software version on production infrastructure before independently deciding whether, when, and how much production traffic it should serve.

## Current Synthesis
The distinction divides one production change into two risk boundaries. Deployment establishes that a version can start, pass health checks, and remain ready on production infrastructure. Release then changes customer exposure by routing traffic to it. When these phases are independently controlled, startup failure can be detected without putting user requests on the new version, while traffic can be shifted progressively and reversed through the release mechanism.

Release-in-place collapses both boundaries: replacing and restarting the version on a traffic-serving instance immediately exposes customers to missing configuration, dependencies, startup failure, and application defects. Canarying reduces the share exposed, but does not remove either class of risk for the canary traffic. Rollback also remains conditional because it is another deployment and release performed under pressure into an environment that may no longer match the old version's assumptions.

## Key Claims
- A version can be deployed in production without being released to production traffic.
- Deployment risk concerns installation, startup, configuration, dependencies, and health readiness; release risk concerns behavior under real user traffic.
- Separating traffic activation from installation can make deployment nearly customer-neutral when the inactive version is isolated from shared production effects.
- Release-in-place exposes customers to both deployment and release risk at the moment each instance restarts.
- Canarying bounds exposure by instance or traffic share but does not eliminate risk for exposed requests.
- Rollback is a fallible deploy-and-release path, not proof that the whole system returns to its former state.

## Evidence
- Process boundary: [[deploy-release-part-1-turbine-labs]] defines shipping as build, test, deploy, and release, with deployment ending before traffic activation.
- Inactive production version: [[deploy-release-part-1-turbine-labs]] depicts v1.2 running beside v1.1 while traffic continues to reach v1.1.
- Traffic activation: [[deploy-release-part-1-turbine-labs]] defines release as moving production traffic to a new version and locates user-visible risk in that exposure.
- Collapsed boundary: [[deploy-release-part-1-turbine-labs]] says release-in-place makes deployment and release simultaneous and leaves no old version to receive traffic when startup fails.
- Bounded exposure: [[deploy-release-part-1-turbine-labs]] says canary exposure is proportional to the number of new-version instances divided by total cluster instances.
- Recovery boundary: [[deploy-release-part-1-turbine-labs]] says rollback re-releases a known version under time pressure into a possibly changed environment.

## Counterevidence & Qualifications
The source presents a conceptual practitioner model rather than comparative reliability measurements. A supposedly inactive deployment may still affect shared databases, migrations, queues, caches, capacity, or control planes, so deployment is not inherently zero-risk. Instance share also need not equal traffic or customer exposure when load balancing, tenancy, request cost, or cohort assignment is uneven. Separating phases requires routing, compatibility, health, and observability mechanisms that can themselves fail, and rollback cannot reverse persistent or client-visible effects already produced.

## What Changed
- Created the concept with separate installation and traffic-activation boundaries.
- Distinguished deploy risk from behavior-under-traffic release risk.
- Preserved canarying and rollback as bounded controls rather than guarantees.

## Related Concepts
- [[DeploymentAutomation]] - automation implements separate install, validation, traffic-shift, and recovery controls.
- [[ChangeSafety]] - phase separation keeps startup failures away from users and enables bounded exposure.
- [[ContinuousDelivery]] - frequent delivery becomes safer when deployment does not automatically activate a change.
- [[DeploymentPipeline]] - a pipeline can model deployment and release as distinct stages with separate evidence.
- [[ServiceObservability]] - traffic expansion and reversal depend on signals that distinguish readiness from user-facing health.
- [[ImmutableInfrastructure]] - parallel versioned capacity makes traffic activation separable from artifact installation.

---
title: "Trunk-Based Development"
type: concept
tags: [software-engineering, continuous-delivery, branching]
sources:
  - architecting-for-continuous-delivery-thoughtworks
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[TrunkBasedDevelopment]] is a development practice where teams integrate small changes frequently on a shared mainline so continuous integration and delivery pipelines can validate current product state quickly.

## Current Synthesis
The Thoughtworks source mentions trunk-based development as a practice that deployment pipelines can support. In context, the connection is release-flow visibility: when each commit moves through staged validation toward production, long-lived hidden work becomes less compatible with the feedback model.

The source does not explain trunk-based development in detail, but it places it inside the continuous-delivery system: small frequent integration, automated tests, and deployment-pipeline confidence reinforce one another.

## Key Claims
- Trunk-based development fits continuous delivery because it keeps integration frequent and visible.
- Deployment pipelines can support trunk-based development by validating each revision through staged checks.
- The practice depends on automated feedback that makes small changes cheaper to verify.

## Evidence
- Pipeline fit: [[architecting-for-continuous-delivery-thoughtworks]] says deployment pipelines can support best practices such as trunk-based development.
- Integration context: [[architecting-for-continuous-delivery-thoughtworks]] says a team is not really practicing CI if it lacks small frequent check-ins or automated tests.

## Counterevidence & Qualifications
The source only mentions trunk-based development briefly, so this page should be expanded with more direct sources before making stronger claims about branch lifetime, feature flags, release branching, or review policy.

## What Changed
- Created the concept from Thoughtworks' pipeline and CI context.

## Related Concepts
- [[ContinuousDelivery]] - trunk-based development is one practice that supports frequent reliable release.
- [[DeploymentPipeline]] - the pipeline validates mainline revisions through staged checks.
- [[DeploymentAutomation]] - automated deployment gives integrated changes a path toward production.
- [[SoftwareVerification]] - small frequent integration depends on fast automated validation.

---
title: "Infrastructure as Code"
type: concept
tags: [infrastructure, automation, cloud, operations]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[InfrastructureAsCode]] is the practice of describing infrastructure provisioning and configuration in versioned, repeatable automation so environments can be created, changed, replaced, and scaled with less manual coordination.

## Current Synthesis
The Auth0 source presents infrastructure as code as a scaling constraint for both traffic and engineering teams. After converging on AWS, Auth0 stopped trying to keep automation platform-independent and instead used Terraform and SaltStack to provision new environments and replace existing ones. That helped the company move from partially automated environments at roughly 300 logins per second to more fully automated environments above 3,400 logins per second.

Infrastructure as code does not remove the need for playbooks or operational judgment. The source pairs automation with incident-response documentation, annual failover exercises, and platform work because reproducible infrastructure still needs humans to understand procedures, consequences, and service-specific maturity.

## Key Claims
- Infrastructure as code becomes more valuable as cloud resource count, service count, and regional footprint grow.
- Provider-specific automation can move faster than platform-independent automation when a company has standardized on one cloud.
- Reproducible provisioning supports regional expansion, environment replacement, and scaling up or down.
- Automation must be paired with playbooks because incidents still require understanding, coordination, and practiced response.
- Infrastructure automation can become a productized internal platform when many teams need the same operational defaults.

## Evidence
- Scale pressure: [[a-look-at-auth0-cloud-architecture-5-years-in]] reports growth to more than a thousand cloud resources and four environments.
- AWS standardization: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Auth0 stopped platform-independent automation work after choosing AWS for public cloud.
- Tooling: [[a-look-at-auth0-cloud-architecture-5-years-in]] names Terraform and SaltStack as the revamped provisioning approach.
- Throughput change: [[a-look-at-auth0-cloud-architecture-5-years-in]] links better automation to growth from about 300 to more than 3,400 logins per second.
- Playbooks: [[a-look-at-auth0-cloud-architecture-5-years-in]] says playbooks helped engineers understand, manage, and respond to incidents in a growing service mesh.

## Counterevidence & Qualifications
The source is not a controlled comparison of Terraform, SaltStack, or alternative infrastructure tools. It also shows that infrastructure as code can remain incomplete: Auth0 describes its automation as not perfect and still needing broader platform and deployment unification.

## What Changed
- Created the infrastructure-as-code concept from Auth0's AWS provisioning and environment-replacement story.

## Related Concepts
- [[DeclarativeInfrastructure]] - both use declared desired state, but infrastructure as code here emphasizes provisioning and configuration automation rather than controller reconciliation.
- [[CloudHighAvailability]] - reproducible environments support regional failover and expansion.
- [[DeploymentAutomation]] - provisioning automation and release automation are adjacent operational layers.
- [[InternalDeveloperPlatform]] - internal platforms can package infrastructure as code behind simpler developer interfaces.
- [[ReliabilityInvestment]] - sustained automation work is a reliability investment.

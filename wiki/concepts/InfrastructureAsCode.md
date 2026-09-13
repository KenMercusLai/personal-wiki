---
title: "Infrastructure as Code"
type: concept
tags: [infrastructure, automation, cloud, operations]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
  - an-infrastructure-guide-for-founders-starting-up-security-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[InfrastructureAsCode]] is the practice of describing infrastructure provisioning and configuration in versioned, repeatable automation so environments can be created, changed, replaced, and scaled with less manual coordination.

## Current Synthesis
The Auth0 source presents infrastructure as code as a scaling constraint for both traffic and engineering teams. After converging on AWS, Auth0 stopped trying to keep automation platform-independent and instead used Terraform and SaltStack to provision new environments and replace existing ones. That helped the company move from partially automated environments at roughly 300 logins per second to more fully automated environments above 3,400 logins per second.

The Startup Security source shifts the same practice earlier in the company lifecycle. It argues that founding teams should make cloud infrastructure subject to normal engineering standards: repository-backed definitions, review, tests, build-server or CI/CD execution, and limited console access. That discipline reduces malicious or accidental drift, especially around network rules, production systems, and security-sensitive configuration.

Infrastructure as code does not remove the need for playbooks or operational judgment. The sources pair automation with incident-response documentation, failover exercises, platform work, and access constraints because reproducible infrastructure still needs humans to understand procedures, consequences, and service-specific maturity.

## Key Claims
- Infrastructure as code becomes more valuable as cloud resource count, service count, and regional footprint grow.
- Provider-specific automation can move faster than platform-independent automation when a company has standardized on one cloud.
- Reproducible provisioning supports regional expansion, environment replacement, and scaling up or down.
- Repository-backed infrastructure lets teams apply code review, tests, and CI/CD standards to cloud changes.
- Limiting console writes and manual changes helps prevent drift, malicious modification, and forgotten temporary exposure.
- Automation must be paired with playbooks because incidents still require understanding, coordination, and practiced response.

## Evidence
- Scale pressure: [[a-look-at-auth0-cloud-architecture-5-years-in]] reports growth to more than a thousand cloud resources and four environments.
- AWS standardization: [[a-look-at-auth0-cloud-architecture-5-years-in]] says Auth0 stopped platform-independent automation work after choosing AWS for public cloud.
- Tooling: [[a-look-at-auth0-cloud-architecture-5-years-in]] names Terraform and SaltStack as the revamped provisioning approach.
- Throughput change: [[a-look-at-auth0-cloud-architecture-5-years-in]] links better automation to growth from about 300 to more than 3,400 logins per second.
- Playbooks: [[a-look-at-auth0-cloud-architecture-5-years-in]] says playbooks helped engineers understand, manage, and respond to incidents in a growing service mesh.
- Early discipline: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] argues that Terraform or CloudFormation can make infrastructure part of the same deploy pipeline as application code.
- Change control: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] links limited console access, required reviews, tests, and CI/CD execution to lower drift and stronger resistance to erroneous or malicious changes.

## Counterevidence & Qualifications
The sources are not controlled comparisons of Terraform, SaltStack, CloudFormation, or alternative infrastructure tools. They also show that infrastructure as code can remain incomplete: Auth0 describes its automation as not perfect and still needing broader platform and deployment unification, while the startup guide notes that disciplined infrastructure workflows have to balance security with developer velocity.

## What Changed
- Added the startup security guide's argument that infrastructure as code should start early to apply review, tests, CI/CD, and drift resistance to cloud changes.

## Related Concepts
- [[DeclarativeInfrastructure]] - both use declared desired state, but infrastructure as code here emphasizes provisioning and configuration automation rather than controller reconciliation.
- [[CloudHighAvailability]] - reproducible environments support regional failover and expansion.
- [[DeploymentAutomation]] - provisioning automation and release automation are adjacent operational layers.
- [[InternalDeveloperPlatform]] - internal platforms can package infrastructure as code behind simpler developer interfaces.
- [[ReliabilityInvestment]] - sustained automation work is a reliability investment.
- [[StartupSecurityDebt]] - early IaC adoption prevents unreviewed cloud changes from becoming security debt.

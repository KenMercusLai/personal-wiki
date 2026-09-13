---
title: "Network Segmentation"
type: concept
tags: [networking, security, cloud, infrastructure]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkSegmentation]] is the design of network boundaries, routing, subnets, security groups, and access rules so only intended services are reachable from the internet or other trust zones.

## Current Synthesis
The source presents segmentation as a standard but security-critical part of cloud infrastructure planning. Teams should understand VPC concepts, public and private placement, subnet counts, peering, security groups, and network ACLs before temporary fixes or lazy rules expose internal services.

The practical concern is drift. A load balancer may need public exposure, but internal Jenkins, caches, and databases generally should not. Once a layout is chosen, teams need disciplined change controls so troubleshooting does not leave broad protocol allowances or `0.0.0.0/0` rules attached to sensitive systems.

## Key Claims
- Public exposure should be intentional rather than an accidental byproduct of cloud defaults or troubleshooting.
- Public and private segmentation is especially important for internal tools, caches, and databases.
- Security groups and network ACLs require disciplined standards because small rule changes can create large exposure.
- Network design and infrastructure engineering standards are mutually dependent.
- Segmentation can reduce damage when network-based attacks or service-specific vulnerabilities spread.

## Evidence
- Planning scope: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] names VPC concepts, peering, subnet allocation, public/private segmentation, security groups, and network ACLs.
- Intentional exposure: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] contrasts exposing a load balancer with avoiding public exposure of internal-only Jenkins.
- Sensitive services: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] warns about accidentally exposing caches or databases.
- Broad rules: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] flags allowing any protocol from `0.0.0.0/0` as a lazy and risky security-group pattern.

## Counterevidence & Qualifications
The source gives high-level AWS network guidance rather than detailed subnet topology, zero-trust architecture, service mesh policy, or private connectivity design. Segmentation also depends on operational discipline; a design can degrade if ad hoc changes bypass review.

## What Changed
- Created the concept from the source's VPC, public/private, security-group, and drift-prevention discussion.

## Related Concepts
- [[NetworkLoadBalancing]] - load balancers are often the intentionally public entry point in segmented designs.
- [[DatabaseServiceExposure]] - databases are a sensitive service category segmentation should protect.
- [[UnauthenticatedServiceExposure]] - segmentation limits reachability even when service authentication is weak or absent.
- [[StartupSecurityDebt]] - network drift is an early infrastructure shortcut with later incident risk.
- [[InfrastructureAsCode]] - versioned infrastructure changes help keep network layout from drifting.

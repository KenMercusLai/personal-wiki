---
title: "Cloud High Availability"
type: concept
tags: [cloud, reliability, availability, architecture]
sources:
  - a-look-at-auth0-cloud-architecture-5-years-in
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[CloudHighAvailability]] is the design of cloud services so they can continue serving critical functionality across instance, availability-zone, regional, routing, and data-layer failures.

## Current Synthesis
Auth0's architecture frames cloud high availability as a layered design problem. Running application and database services in every availability zone keeps one data-center failure from becoming a full outage, while regional failover through Route53 provides a recovery path when the primary region is unavailable or unhealthy. Data-layer strategy has to match each datastore: MongoDB can use a cross-region cluster, PostgreSQL can use RDS replication, and Elasticsearch may need regular snapshots and restore automation when cross-region clustering is not available.

The source also shows that high availability has maturity levels. Some services can fail over with stale caches or reduced feature availability, while core authentication paths receive the strongest continuity guarantees. Annual failover exercises, playbooks, and automation turn the architecture from a diagram into practiced operational capacity.

## Key Claims
- Multi-AZ deployment keeps a single availability-zone failure from taking down the service.
- Cross-region failover provides a recovery path for regional failure but depends on routing, automation, data replication, and practiced procedures.
- Different datastores require different replication or restoration strategies.
- High availability can be feature-tiered: core paths may continue while less mature support services degrade.
- Failover exercises and playbooks are part of the availability design, not after-the-fact documentation.

## Evidence
- Multi-AZ layout: [[a-look-at-auth0-cloud-architecture-5-years-in]] says all services, including databases, run instances in every AWS availability zone for an environment.
- Regional failover: [[a-look-at-auth0-cloud-architecture-5-years-in]] describes us-west-2 as primary and us-west-1 as failover, with Route53 updates used to resume operation if the primary region fails.
- Data-layer strategy: [[a-look-at-auth0-cloud-architecture-5-years-in]] names cross-region MongoDB, RDS PostgreSQL replication, and Elasticsearch snapshots/restores.
- Maturity levels: [[a-look-at-auth0-cloud-architecture-5-years-in]] says some services may operate with stale data while core functionality continues.
- Operational rehearsal: [[a-look-at-auth0-cloud-architecture-5-years-in]] says failover is exercised at least annually with playbooks and automation.

## Counterevidence & Qualifications
The source explains one AWS-centered SaaS architecture rather than a general benchmark. It also shows that cloud high availability involves tradeoffs: feature parity, cross-region data behavior, operational complexity, and provider-specific services can make multi-cloud or cross-region designs expensive to sustain.

## What Changed
- Created the concept from Auth0's multi-AZ and cross-region availability strategy.

## Related Concepts
- [[SystemReliability]] - cloud high availability is one architecture layer of system reliability.
- [[ReliabilityInvestment]] - availability requires ongoing automation, exercises, and operational staffing.
- [[AuthenticationInfrastructure]] - Auth0's identity service uses cloud HA to protect customer login paths.
- [[InfrastructureAsCode]] - reproducible environments support failover and regional expansion.
- [[ServiceObservability]] - monitoring and alerts reveal whether availability mechanisms are working.

---
title: "Nick Craver"
type: entity
tags: [infrastructure, web-performance, stack-overflow]
sources:
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
  - nick-craver-stack-overflow-the-architecture-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[NickCraver]] is represented as a [[StackOverflow]] infrastructure engineer documenting the platform's architecture, rapid deployment path, and four-year transition to HTTPS by default.

## Current Profile
Craver's accounts join architecture, application performance, measurement, and rollout detail. The architecture overview describes a modest server fleet handling large traffic through multi-tenancy, specialized service tiers, layered caches, redundant network and power paths, and derived Redis and Elasticsearch stores over a SQL source of truth. Spare capacity is presented as support for deployment, headroom, and failure tolerance rather than proof that normal traffic needs every machine.

The deployment article follows a push through GitLab, TeamCity, database migration, localization, tier promotion, and an HAProxy-coordinated rolling update. The HTTPS retrospective expands the boundary to certificates, DNS, CDNs, cookies, login, mixed content, APIs, redirects, search traffic, and operational testing. Across all three, Craver favors simple mechanisms, direct measurement, compatible change, and explicit disclosure of local compromises and failure modes.

## Key Characteristics
- Writes from direct operational involvement in Stack Overflow infrastructure.
- Explains architecture through component relationships, workload placement, capacity, and failure boundaries.
- Uses request metrics, real-user timings, dashboards, and utilization data to evaluate systems.
- Treats security and deployment changes as cross-layer compatibility and rollout problems.
- Distinguishes technical feasibility from operational prudence, especially around redundancy and spare capacity.
- Documents failures, constraints, and rejected designs alongside deployed mechanisms.
- Presents simple technology choices as context-dependent rather than universally transferable.

## Evidence
- Architecture and capacity: [[nick-craver-stack-overflow-the-architecture-2016-edition]] connects edge routing, HAProxy, IIS, specialized services, Redis, websockets, Elasticsearch, and SQL Server while showing traffic distribution and tier utilization.
- Redundancy boundary: [[nick-craver-stack-overflow-the-architecture-2016-edition]] describes paired racks, power and network paths, alternate inter-site routes, and asynchronous Colorado replicas while acknowledging that not every path is intrinsically redundant.
- Migration scope: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes four years of certificate, domain, edge, application, and content work before final activation.
- Measurement practice: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes browser timing collection from about 5% of traffic and billions of stored measurements; [[nick-craver-stack-overflow-the-architecture-2016-edition]] adds per-request HAProxy timing capture and infrastructure dashboards.
- Failure disclosure: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] details Railgun instability, protocol-relative URL problems, an infinite redirect, and a faulty backfill.
- Deployment and compatibility: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] traces a reported sub-nine-minute push through development, Meta, and production using staged schema change, HAProxy drainage, readiness polls, and static-assets-first rollout.

## Qualifications
The profile is based on three first-person 2016-2017 accounts and does not establish Craver's complete role, later work, or the independent contributions of other engineers. Traffic, timing, utilization, topology, software-version, and reliability figures are historical operational snapshots without independent datasets. Direct-to-main work, forward-only migration, on-premises redundancy, and the particular tier design are local practices rather than universal recommendations.

## What Changed
- Added the 2016 whole-system architecture account and its emphasis on workload placement and bounded redundancy.
- Identified capacity headroom and component-level measurement as recurring parts of Craver's operational reasoning.
- Strengthened the profile's distinction between demonstrated feasibility and recommended production practice.

## Relationships
- [[StackOverflow]] - platform whose architecture, deployment, and HTTPS transition Craver documents.
- [[HAProxy]] - traffic, TLS, measurement, and deployment-control layer in all three operational accounts.
- [[Redis]] - cache and pub/sub layer described in the architecture overview.
- [[MultiSiteHighAvailability]] - failure-boundary design illustrated by New York and Colorado infrastructure.
- [[DynamicContentCaching]] - L1/L2 cache and invalidation pattern described in the architecture.
- [[HTTPSMigration]] - cross-layer security program described in the later retrospective.
- [[DeploymentPipeline]] - staged source-to-production process documented in the deployment account.
- [[RollingDeployment]] - HAProxy-coordinated server rollout used by Stack Overflow.

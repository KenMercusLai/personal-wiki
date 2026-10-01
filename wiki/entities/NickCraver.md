---
title: "Nick Craver"
type: entity
tags: [infrastructure, web-performance, stack-overflow]
sources:
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[NickCraver]] is represented as a [[StackOverflow]] infrastructure engineer who documented both the network's rapid deployment path and its four-year transition to HTTPS by default.

## Current Profile
Craver's accounts combine architecture, application, measurement, and rollout detail. The 2016 deployment article follows a developer push through GitLab, TeamCity, database migration, localization, tier promotion, and an HAProxy-coordinated rolling update. It connects short lead time to small changes, fast local checkout, automated builds, compatible schema evolution, and explicit handling of mixed server and static-asset versions.

The 2017 HTTPS retrospective presents security migration as a cross-team dependency program involving certificates, DNS, CDNs, load balancers, cookies, login, mixed content, internal APIs, redirects, search traffic, and operational testing rather than as a single endpoint configuration. Both accounts disclose local compromises and failure modes instead of presenting tooling as universally transferable.

## Key Characteristics
- Writes from direct operational involvement in Stack Overflow infrastructure.
- Treats security migrations as cross-layer dependency and rollout problems.
- Uses real-user performance measurements to compare infrastructure choices.
- Connects HTTPS adoption to HTTP/2 performance, DDoS protection, and user privacy.
- Documents failures and rejected designs alongside the deployed architecture.
- Explains high-frequency deployment through concrete human, build, database, traffic, and compatibility steps.
- Treats simple mechanisms as valuable only when their failure direction and operating context are explicit.

## Evidence
- Migration scope: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes four years of certificate, domain, edge, application, and content work before the final feature-flag activation.
- Measurement practice: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes browser timing collection from about 5% of traffic and more than five billion stored measurements.
- Failure disclosure: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] details Railgun's retirement, protocol-relative URL problems, an infinite redirect, and a faulty Help Center backfill.
- Deployment path: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] traces a push through development, Meta, and production in under nine reported minutes.
- Compatibility practice: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] describes staged database and API evolution, HAProxy drainage, readiness polls, and static-assets-first rollout.

## Qualifications
The profile is based on two first-person 2016-2017 retrospectives and does not establish Craver's complete role, later work, or the independent contribution of other engineers. Technical choices, operating figures, and product capabilities are historical to the deployment periods. Direct-to-main work, forward-only migration, and the particular deployment topology are presented as local practice rather than universal recommendations.

## What Changed
- Created the profile around Craver's operational account of Stack Overflow's HTTPS migration.
- Identified measurement-led infrastructure selection and candid failure reporting as recurring characteristics of the source.
- Added the end-to-end deployment account and its emphasis on small batches, compatibility, and explicit traffic state.

## Relationships
- [[StackOverflow]] - platform whose HTTPS migration Craver documents.
- [[HTTPSMigration]] - principal systems program described in his account.
- [[Fastly]] - edge provider selected during the migration.
- [[Cloudflare]] - earlier edge provider evaluated and operated during the migration.
- [[HAProxy]] - local load-balancing and TLS-termination layer in the architecture.
- [[HTTP2]] - performance driver that strengthened the case for HTTPS.
- [[DeploymentPipeline]] - staged source-to-production process Craver documents.
- [[RollingDeployment]] - HAProxy-coordinated web-server rollout in the deployment account.
- [[ForwardOnlyDatabaseMigration]] - schema-change strategy described in the deployment account.

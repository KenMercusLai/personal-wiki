---
title: "Nick Craver"
type: entity
tags: [infrastructure, web-performance, stack-overflow]
sources:
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[NickCraver]] is represented as a [[StackOverflow]] infrastructure engineer who documented the network's four-year transition to HTTPS by default.

## Current Profile
Craver's account combines architecture, application, measurement, and rollout detail. He presents HTTPS as a cross-team dependency program involving certificates, DNS, CDNs, load balancers, cookies, login, mixed content, internal APIs, redirects, search traffic, and operational testing rather than as a single endpoint configuration. The retrospective is unusually open about discarded approaches and public mistakes, including Railgun instability, protocol-relative URLs, a cached-redirect loop, and a Help Center backfill bug.

## Key Characteristics
- Writes from direct operational involvement in Stack Overflow infrastructure.
- Treats security migrations as cross-layer dependency and rollout problems.
- Uses real-user performance measurements to compare infrastructure choices.
- Connects HTTPS adoption to HTTP/2 performance, DDoS protection, and user privacy.
- Documents failures and rejected designs alongside the deployed architecture.

## Evidence
- Migration scope: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes four years of certificate, domain, edge, application, and content work before the final feature-flag activation.
- Measurement practice: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes browser timing collection from about 5% of traffic and more than five billion stored measurements.
- Failure disclosure: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] details Railgun's retirement, protocol-relative URL problems, an infinite redirect, and a faulty Help Center backfill.

## Qualifications
The profile is based on one first-person 2017 retrospective and does not establish Craver's complete role, later work, or the independent contribution of other engineers. Technical choices and product capabilities are historical to the deployment period.

## What Changed
- Created the profile around Craver's operational account of Stack Overflow's HTTPS migration.
- Identified measurement-led infrastructure selection and candid failure reporting as recurring characteristics of the source.

## Relationships
- [[StackOverflow]] - platform whose HTTPS migration Craver documents.
- [[HTTPSMigration]] - principal systems program described in his account.
- [[Fastly]] - edge provider selected during the migration.
- [[Cloudflare]] - earlier edge provider evaluated and operated during the migration.
- [[HAProxy]] - local load-balancing and TLS-termination layer in the architecture.
- [[HTTP2]] - performance driver that strengthened the case for HTTPS.

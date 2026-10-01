---
title: "Fastly"
type: entity
tags: [cdn, web-performance]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
  - improve-cache-performance-with-optimized-api-design
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Fastly]] appears as an edge cloud and CDN provider used by [[Thinks]] and [[StackOverflow]], and as the publisher of guidance on cache-friendly API design.

## Current Profile
The Thinks case places Fastly in front of Baqend application infrastructure, where nearby CDN cache nodes reduce round trips and absorb most requests during a television-driven traffic spike. Fastly's API-design article adds the operational model behind broader edge reuse: choose shared response boundaries, bound cache variants, tag representations with the objects they contain, purge those tags after changes, and optionally serve stale content during origin failure.

The [[StackOverflow]] HTTPS retrospective adds a different selection case. After earlier Cloudflare use, Stack Overflow chose Fastly for programmable VCL, faster configuration propagation, automation, customer-controlled certificates, and local TLS termination. That flexibility also created configuration responsibilities: a protocol-blind default cache key caused an infinite HTTPS redirect until the scheme signal was included in variation logic.

The combined profile is therefore broader than a named CDN dependency. Fastly is represented as an edge delivery and TLS platform whose value depends on application cache design, programmable edge behavior, configuration automation, and correct request variation.

## Key Characteristics
- Provides edge caching in the Thinks/Baqend performance architecture.
- Reduces origin work and user-to-content round trips when responses are reusable.
- Advocates cache-friendly API design through HTTP-aligned reads and shared response boundaries.
- Supports event-driven invalidation with surrogate-key tagging across overlapping representations.
- Supports stale serving as an availability mechanism during origin failure or for freshness-tolerant clients.
- Exposes programmable VCL and rapid configuration propagation suited to application-specific edge controls.

## Evidence
- Delivery role: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] names Fastly as the CDN and places it before Baqend application servers, MongoDB, and Redis.
- Production reuse: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports a 98.5% CDN cache-hit rate during the Thinks DHDL traffic spike.
- API cache design: [[improve-cache-performance-with-optimized-api-design]] recommends reusable resource boundaries, `GET` reads, bounded pagination, and normalization of equivalent request variants.
- Invalidation and resilience: [[improve-cache-performance-with-optimized-api-design]] demonstrates surrogate-key purging and recommends stale responses when an origin is down.
- Stack Overflow selection: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] says VCL flexibility, faster propagation, and automated configuration were decisive reasons to move from Cloudflare to Fastly.
- TLS and redirect behavior: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] places Fastly at the local-to-user TLS edge and documents an infinite redirect caused when the default cache key did not distinguish protocol.

## Qualifications
The Thinks metrics are vendor-authored case-study results, while the API article is Fastly guidance without comparative benchmarks. The Stack Overflow source compares providers from one customer's 2017 requirements and deployment experience, not a neutral or current market evaluation. Authentication headers, purges, and stale policies do not automatically make a response safe to share; applications still need correct cache keys, protocol variation, authorization boundaries, and data-specific freshness limits.

## What Changed
- Added Stack Overflow's provider-selection criteria: programmable VCL, rapid propagation, automation, certificate control, and edge TLS.
- Added the redirect-loop incident as evidence that configurable edge caching requires correct protocol-aware keys.

## Relationships
- [[Baqend]] - uses Fastly as the CDN component in the source architecture.
- [[Thinks]] - webshop that used Fastly during the TV traffic spike.
- [[WebPerformanceOptimization]] - CDN placement is one network-latency lever.
- [[DynamicContentCaching]] - CDN caching works with Baqend's browser-cache freshness checks.
- [[APIResponseCaching]] - Fastly's guidance connects interface boundaries to edge reuse and targeted invalidation.
- [[StackOverflow]] - selected Fastly as its CDN, proxy, and TLS edge in the historical migration account.
- [[HTTPSMigration]] - edge termination and cache behavior are part of the migration's performance and correctness boundary.
- [[Cloudflare]] - earlier Stack Overflow provider contrasted with Fastly's programmable configuration model.

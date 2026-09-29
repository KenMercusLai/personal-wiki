---
title: "Fastly"
type: entity
tags: [cdn, web-performance]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
  - improve-cache-performance-with-optimized-api-design
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Fastly]] appears in the wiki as an edge cloud and CDN provider used in the [[Thinks]] webshop case study and as the publisher of guidance on cache-friendly API design.

## Current Profile
The Thinks case places Fastly in front of Baqend application infrastructure, where nearby CDN cache nodes reduce round trips and absorb most requests during a television-driven traffic spike. Fastly's API-design article adds the operational model behind broader edge reuse: choose shared response boundaries, bound cache variants, tag representations with the objects they contain, purge those tags after changes, and optionally serve stale content during origin failure.

The combined profile is therefore broader than a named CDN dependency. Fastly is represented as both an edge delivery platform and a practitioner source advocating that API method, URL, representation, and invalidation design determine how much traffic the edge can safely reuse.

## Key Characteristics
- Provides edge caching in the Thinks/Baqend performance architecture.
- Reduces origin work and user-to-content round trips when responses are reusable.
- Advocates cache-friendly API design through HTTP-aligned reads and shared response boundaries.
- Supports event-driven invalidation with surrogate-key tagging across overlapping representations.
- Supports stale serving as an availability mechanism during origin failure or for freshness-tolerant clients.

## Evidence
- Delivery role: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] names Fastly as the CDN and places it before Baqend application servers, MongoDB, and Redis.
- Production reuse: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports a 98.5% CDN cache-hit rate during the Thinks DHDL traffic spike.
- API cache design: [[improve-cache-performance-with-optimized-api-design]] recommends reusable resource boundaries, `GET` reads, bounded pagination, and normalization of equivalent request variants.
- Invalidation and resilience: [[improve-cache-performance-with-optimized-api-design]] demonstrates surrogate-key purging and recommends stale responses when an origin is down.

## Qualifications
Neither source compares Fastly with other CDN or edge platforms. The Thinks metrics are vendor-authored case-study results, while the API article is Fastly guidance without comparative benchmarks. Authentication headers, purges, and stale policies do not automatically make a response safe to share; applications still need correct cache keys, authorization boundaries, and data-specific freshness limits.

## What Changed
- Expanded Fastly from a named CDN component into an edge-cache platform and API-caching guidance source.
- Added surrogate-key invalidation and stale-serving capabilities with explicit correctness qualifications.

## Relationships
- [[Baqend]] - uses Fastly as the CDN component in the source architecture.
- [[Thinks]] - webshop that used Fastly during the TV traffic spike.
- [[WebPerformanceOptimization]] - CDN placement is one network-latency lever.
- [[DynamicContentCaching]] - CDN caching works with Baqend's browser-cache freshness checks.
- [[APIResponseCaching]] - Fastly's guidance connects interface boundaries to edge reuse and targeted invalidation.

---
title: "Baqend"
type: entity
tags: [backend-as-a-service, web-performance, caching]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Baqend]] is presented as a backend-as-a-service and web-performance platform whose central promise is accelerating application requests through the full HTTP caching hierarchy while preserving correctness for dynamic data.

## Current Profile
The source frames Baqend as both the platform behind the [[Thinks]] webshop and the research context for a cache-sketch approach to [[DynamicContentCaching]]. Its stack combines stateless Orestes application servers, a JavaScript SDK, REST API access, file and data storage, real-time queries, push notifications, access control, CDN integration, browser caching, and cache-coherence logic for dynamic data.

The article's strongest claim is that Baqend can make dynamic web applications behave more like static cached sites without delivering stale data. It does this by purging invalidation-based caches when resources change, then giving clients a small Bloom filter that identifies resources that might be stale; definitely-fresh resources can be served from the browser cache.

## Key Characteristics
- Positions web performance as a managed backend and caching problem rather than only frontend optimization.
- Uses CDN and browser caching aggressively, including for dynamic resources.
- Maintains dynamic-data correctness with Bloom-filter freshness checks and cache purging.
- Provides backend features through a JavaScript SDK and REST API.
- Uses MongoDB for primary data and Redis for expiring Bloom-filter maintenance in the Thinks example.
- Claims sub-second page loads and high cache-hit rates in both benchmarks and the Thinks TV-traffic case.

## Evidence
- Platform role: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says the Thinks webshop was built on Baqend and used its JS SDK, REST API, CDN, Orestes servers, MongoDB, Redis, and cache-coherence features.
- Cache sketch: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] explains Baqend's Bloom-filter approach for checking URL staleness before bypassing or using the browser cache.
- Load spike: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports Thinks stayed below one-second page loads during DHDL traffic with 98.5% CDN cache hit rate and 3% average server CPU load.
- Benchmark claim: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says Baqend loaded below one second and averaged 6.8 times faster than competitors in its BaaS comparison.

## Qualifications
The source is Baqend-authored and therefore promotional. The reported benchmark and Thinks metrics are useful evidence, but they should be treated as vendor case-study claims rather than an independently audited performance study.

## What Changed
- Created the Baqend entity page from the Thinks performance case study.

## Relationships
- [[Thinks]] - flagship ecommerce case study in the source.
- [[DynamicContentCaching]] - Baqend's cache-sketch approach is the source's distinctive technical mechanism.
- [[WebPerformanceOptimization]] - Baqend's product promise spans frontend, network, backend, and cache hierarchy work.
- [[Redis]] - used to maintain the expiring Bloom filter.
- [[MongoDB]] - primary database in the Thinks backend stack.
- [[Fastly]] - CDN used by the Thinks implementation.

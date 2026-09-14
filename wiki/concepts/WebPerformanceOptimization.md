---
title: "Web Performance Optimization"
type: concept
tags: [web, performance, ecommerce, latency]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[WebPerformanceOptimization]] is the practice of reducing user-visible page-load time by coordinating frontend rendering, network latency, backend processing, caching, and capacity planning.

## Current Synthesis
The Baqend source frames web performance as a whole-system problem rather than a single tooling checklist. Frontend work reduces the critical rendering path by shrinking critical resources, minifying and compressing bytes, loading JavaScript and CSS carefully, and relying on browser caching. Network work reduces round trips through persistent connections, redirect avoidance, [[HTTP2]], explicit cache headers, CDNs, and content closer to users. Backend work keeps request processing fast and scalable through load balancing, autoscaling, failover, stateless sessions, efficient application servers, and scalable databases.

The source's distinctive contribution is the link between performance and ecommerce economics under bursty demand. A webshop can technically stay available while still losing revenue if latency harms conversion, and a successful TV appearance can create a short traffic spike that punishes any uncached, stateful, or round-trip-heavy design. The Thinks case study treats caching and load testing as product infrastructure because speed protects conversion during moments of high purchase intent.

## Key Claims
- Page-load time depends on frontend rendering, network latency, and backend processing together.
- Availability alone is insufficient for ecommerce because latency directly affects user satisfaction and conversion.
- Browser and CDN caching are the highest-leverage network optimizations when they safely reduce round trips.
- Backend scalability has to be designed before the spike, using load balancing, statelessness, autoscaling, failover, and database choices.
- Load testing should simulate expected traffic shape and payment behavior, not only homepage availability.
- Dynamic content requires cache-coherence mechanisms if teams want browser-cache speed without stale data.

## Evidence
- Three-bottleneck diagram: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] shows backend processing, network latency, and frontend processing as the three page-load drivers.
- Conversion framing: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] cites one extra second of latency as associated with 7% lower conversions, 11% fewer page views, and 16% lower customer satisfaction.
- Frontend guidance: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] recommends CRP reduction, minification, compression, async loading, concatenation, and browser caching.
- Network guidance: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] recommends persistent connections, redirect avoidance, HTTP/2, cache headers, CDNs, and SPA-style asynchronous loading where appropriate.
- Backend guidance: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] recommends load balancing, automatic scaling, failover, stateless sessions, efficient IO, and scalable databases.
- Production case: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] reports Thinks handled a TV spike with sub-second page loads, 98.5% CDN cache hit rate, and 7.8% conversion.

## Counterevidence & Qualifications
The source is a vendor case study and uses Baqend's own benchmark and production reporting. Its general principles are broadly plausible and consistent with web-performance practice, but the specific benchmark ratios and production metrics should be treated as reported case-study evidence.

## What Changed
- Created the concept from the Baqend/Thinks source.

## Related Concepts
- [[CriticalRenderingPath]] - frontend rendering path optimized as part of web performance.
- [[DynamicContentCaching]] - cache-coherence technique for serving dynamic data quickly.
- [[LatencyHierarchy]] - network round trips sit high enough in the latency hierarchy to dominate page loads.
- [[HTTP2]] - network protocol feature set that reduces request overhead and improves parallelism.
- [[ProductPageOptimization]] - ecommerce product pages need speed to preserve purchase intent.
- [[ConversionRateOptimization]] - performance improvements are treated as conversion levers.

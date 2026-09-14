---
title: "Building a Shop with Sub-Second Page Loads: Lessons Learned"
type: source
tags: [web-performance, ecommerce, caching, scalability]
date: 2016-10-13
source_file: "/mnt/ken_personal_wiki/Articles/Building a Shop with Sub-Second Page Loads- Lessons Learned.md"
---

## Summary
This Baqend case study argues that ecommerce performance under TV-scale traffic depends on jointly optimizing frontend rendering, network round trips, backend scalability, and cache coherence for dynamic data. The [[Thinks]] webshop used [[Baqend]], [[Fastly]], aggressive browser caching, CDN caching, stateless application servers, [[MongoDB]], and [[Redis]] to stay below one-second page loads during a German TV traffic spike. The inspected diagrams and screenshots support the article's three-bottleneck model, dynamic-cache architecture, load-test topology, and episode comparison.

## Key Claims
- [[WebPerformanceOptimization]] has three major bottlenecks: frontend rendering, network round trips, and backend processing.
- Page-load latency is a conversion problem, not only an availability problem; the source cites one extra second as associated with 7% lower conversions, 11% fewer page views, and 16% lower customer satisfaction.
- Frontend performance depends heavily on the [[CriticalRenderingPath]], especially render-blocking CSS, parser-blocking JavaScript, critical-resource count, byte size, and CRP round trips.
- Network performance is often dominated by latency and round-trip count rather than raw bandwidth, making persistent connections, redirect avoidance, [[HTTP2]], caching headers, CDNs, and nearby cache nodes important.
- Backend performance under spikes requires load balancing, autoscaling, failover, stateless application servers, efficient IO, and scalable databases.
- [[DynamicContentCaching]] is hard because browser caches are expiration-based, but Baqend's Bloom-filter cache-sketch approach can avoid stale browser-cache reads while still serving definitely-fresh dynamic resources locally.
- In the [[Thinks]] DHDL episode, the article reports 3.4 million requests, 300,000 visitors, about 50,000 concurrent visitors, up to 20,000 requests per second, a 98.5% CDN cache-hit rate, 3% average server CPU load, sub-second page loads, and 7.8% conversion.

## Key Quotes
> "Availability is not enough - latency is key!" - framing performance as revenue-critical rather than merely operational.

> "Network performance is the most important factor when it comes to page load time" - on latency and round-trip count as the hard bottleneck.

## Connections
- [[Baqend]] - platform and source author context for the caching infrastructure, JS SDK, Orestes servers, and dynamic cache-sketch approach.
- [[Thinks]] - webshop case study that handled the DHDL traffic spike.
- [[WebPerformanceOptimization]] - central concept connecting frontend, network, backend, caching, and load testing.
- [[CriticalRenderingPath]] - frontend bottleneck model used to explain CSS, JavaScript, and above-the-fold optimization.
- [[DynamicContentCaching]] - Baqend's Bloom-filter freshness-check approach for browser-cached dynamic data.
- [[ConversionRateOptimization]] - latency is tied directly to page views, satisfaction, and ecommerce conversion.
- [[ProductPageOptimization]] - fast product pages are framed as a purchase-path requirement during demand spikes.
- [[HTTP2]] - recommended network-performance tool through multiplexing, header compression, and server push.
- [[Redis]] - high-write-throughput store for Baqend's expiring Bloom filter.
- [[MongoDB]] - primary database for the Thinks webshop in the Baqend stack.
- [[Fastly]] - CDN used by the Thinks implementation.
- [[LatencyHierarchy]] - the article strengthens the hierarchy by showing global request latency, handshakes, and round trips dominating page load time.

## Contradictions
- No direct contradiction found. The source complements existing product-page and conversion material by treating speed as a measurable conversion lever, and it complements the existing HTTP/2 and latency pages by grounding protocol and network claims in ecommerce page-load behavior.

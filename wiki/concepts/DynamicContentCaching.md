---
title: "Dynamic Content Caching"
type: concept
tags: [caching, web-performance, distributed-systems]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[DynamicContentCaching]] is the practice of caching application data that can change at runtime while preserving freshness guarantees strong enough for user-facing correctness.

## Current Synthesis
The Baqend source frames dynamic content as the unresolved gap in ordinary web caching. Static assets can use long TTLs and filename hashes, but runtime data such as profiles, posts, comments, stock counts, and product data can change unpredictably. Invalidation-based caches such as CDNs and Varnish can be purged proactively, but expiration-based browser caches cannot be directly invalidated by the server after a response has been cached.

Baqend's cache-sketch approach tries to keep browser-cache speed without serving stale dynamic data. At the start of a session, the client fetches a small Bloom filter representing stale resources. If a URL is definitely absent from the filter, the browser cache can serve it as fresh. If the URL might be present, the client bypasses the browser cache and fetches from the CDN, whose stale entries are proactively purged. False positives may cause unnecessary revalidation, but false negatives are avoided, so the design trades a small amount of extra network work for correctness.

## Key Claims
- Static-resource caching is easier than dynamic-resource caching because deploy-time hashes and long TTLs work when content changes only on release.
- Browser caches are hard to use for dynamic data because expiration-based caches cannot be proactively invalidated by the server.
- CDN and Varnish-style invalidation caches can be purged when resources become stale.
- Bloom-filter cache sketches let clients distinguish definitely-fresh resources from potentially-stale resources.
- False positives are acceptable because they only cause extra revalidation, while false negatives would serve stale data.
- Dynamic caching requires backend machinery for query matching, TTL estimation, distributed coordination, and scalable freshness metadata.

## Evidence
- Caching taxonomy: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] distinguishes invalidation-based caches from expiration-based browser caches.
- Static contrast: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says static assets can use hashed filenames and long cache lifetimes because they mostly change on deployment.
- Cache-sketch mechanism: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says Baqend fetches a small Bloom filter at session start so clients can check whether a resource might be stale before using the browser cache.
- Correctness property: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says the Bloom filter may revalidate fresh resources because of false positives but will not drop a stale item that was added.
- Size example: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] says about 11KB can represent 20,000 distinct updates at a low false-positive rate.
- Architecture diagram: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] shows Baqend purging CDN/Varnish while clients use Bloom-filter checks before browser-cache reads.

## Counterevidence & Qualifications
The approach comes from a Baqend-authored source and is not compared against all modern alternatives such as service workers, stale-while-revalidate policies, edge compute, or framework-level data caches. It is most useful as a concrete design pattern for combining browser-cache speed with dynamic-data freshness.

## What Changed
- Created the concept from Baqend's cache-sketch discussion.

## Related Concepts
- [[WebPerformanceOptimization]] - dynamic caching reduces user-visible page-load latency.
- [[LatencyHierarchy]] - using browser cache avoids high-cost network round trips.
- [[HTTP2]] - protocol improvements reduce overhead but do not by themselves solve freshness for dynamic browser caches.
- [[Redis]] - stores Baqend's expiring Bloom filter in the source architecture.
- [[Baqend]] - platform that implements the cache-sketch approach.

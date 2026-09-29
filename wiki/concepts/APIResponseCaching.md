---
title: "API Response Caching"
type: concept
tags: [api, caching, http, cdn, web-performance]
sources:
  - improve-cache-performance-with-optimized-api-design
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[APIResponseCaching]] is the design and operation of application interfaces so intermediaries can reuse read responses across compatible requests while invalidating or qualifying them when the underlying data changes.

## Current Synthesis
API cacheability begins with representation boundaries, not with a CDN switch. A reusable response should describe a resource or cohort shared by many callers, use ordinary [[HTTP]] read semantics, and keep caller-specific credentials or quota details outside the body. Batch wrappers, read operations sent as `POST`, personalized echoes, and success-wrapped errors make it harder for an intermediary to identify equivalent safe reads.

Freshness then becomes an invalidation problem. Stable and volatile fields can be separated into endpoints with different change rates; filter and page shapes can be bounded so the cache-key space does not grow without limit; and equivalent requests such as an omitted page number and explicit page one can be normalized. Because one object may appear in many list responses, surrogate-key tags let a mutation purge every representation containing that object without discarding unrelated cached data. Stale serving adds a separate resilience choice when temporary age is preferable to origin failure.

## Key Claims
- Cacheable API reads need shared response units, explicit `GET` semantics, and no unnecessary requester-specific body data.
- Resource boundaries should separate data by audience and change rate, such as personal bookings from flight-wide seat availability.
- Batching reduces request count but can reduce response reuse and make invalidation coarse; newer transports weaken request-count overhead without eliminating all latency.
- Filter and pagination design should bound and normalize cache variants rather than allow arbitrary equivalent key combinations.
- Surrogate-key tagging maps one changed entity to every cached representation that embeds it.
- Event-driven purge preserves long cache lifetimes by invalidating content when mutations occur instead of relying only on short expiration.
- Stale serving can trade bounded freshness for availability during origin failure or for clients that do not require the latest data.

## Evidence
- Cache-safe request contract: [[improve-cache-performance-with-optimized-api-design]] recommends `GET` for reads, credentials in an authorization header, meaningful error statuses, and responses without requester-specific echoes.
- Boundary design: [[improve-cache-performance-with-optimized-api-design]] separates booking data from flight seats and product lists from faster-changing review aggregates.
- Variant control: [[improve-cache-performance-with-optimized-api-design]] recommends key filter endpoints, fixed page sizes, finite page numbers, and normalization of implicit versus explicit page one.
- Targeted invalidation: [[improve-cache-performance-with-optimized-api-design]] shows responses tagged with category and product surrogate keys so mutations can purge affected representations.
- Resilience: [[improve-cache-performance-with-optimized-api-design]] recommends serving stale cached content when the origin is unavailable or the requester can tolerate older data.

## Counterevidence & Qualifications
The source is platform-vendor guidance and provides no benchmark comparing the proposed designs with batch, GraphQL, private-cache, or uncached alternatives. Splitting responses may increase client coordination, and HTTP/2 or QUIC reduces transport overhead rather than making every extra request free. Authentication in a header does not itself make private or authorization-dependent data safe to share; cache policy and key construction must still separate incompatible callers. Purging and stale serving also require application-specific correctness limits because booking, price, inventory, and entitlement data tolerate different ages.

## What Changed
- Created a synthesis of cache-key reuse, resource-boundary design, bounded variants, surrogate-key invalidation, and stale serving for APIs.

## Related Concepts
- [[RESTAPI]] - HTTP-aligned resource and method semantics make cacheable reads easier to identify.
- [[DynamicContentCaching]] - broader freshness problem that API invalidation and stale policies address at intermediary caches.
- [[HTTP]] - supplies methods, headers, status codes, cache directives, and representation semantics.
- [[HTTP2]] - reduces multi-request transport overhead while leaving response reuse and invalidation as separate concerns.
- [[WebPerformanceOptimization]] - avoiding origin work and network round trips can reduce user-visible latency.
- [[CloudHighAvailability]] - stale cache can preserve degraded read availability during origin failure.

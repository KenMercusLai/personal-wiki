---
title: "Dynamic Content Caching"
type: concept
tags: [caching, web-performance, distributed-systems]
sources:
  - building-a-shop-with-sub-second-page-loads-lessons-learned
  - improve-cache-performance-with-optimized-api-design
  - nick-craver-stack-overflow-the-architecture-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[DynamicContentCaching]] is the practice of reusing application data that changes at runtime while keeping freshness, invalidation, tenant isolation, and source-of-truth recovery explicit.

## Current Synthesis
The sources show three complementary cache layers. Baqend addresses the browser boundary: static assets can use hashes and long TTLs, but runtime data changes unpredictably and browser caches cannot be directly purged. Its Bloom-filter cache sketch lets the client use definitely-fresh local objects and revalidate objects that might be stale, accepting false-positive network work while avoiding false-negative stale reads.

Fastly addresses shared edge representations. Cache-friendly resource boundaries and surrogate-key tags let one mutation purge every list or detail response containing an entity without flushing unrelated objects. Serving stale content during origin failure then becomes an explicit availability-versus-freshness policy.

Stack Overflow supplies an application-tier hierarchy. Each server kept an L1 cache and fell back to shared Redis L2; a miss at both layers fetched from the source and filled both. Redis pub/sub propagated invalidation so other servers could evict local entries, while site prefixes and database IDs separated tenants. SQL remained the source of truth, making Redis a fast derived layer rather than the canonical record.

## Key Claims
- Cache design must state which layer is authoritative and how derived entries are refilled or invalidated.
- Local L1 caches reduce process latency, while a shared L2 cache can prevent repeated source work across servers.
- Multi-layer caches need cross-node invalidation or bounded staleness because local entries diverge after mutation.
- Browser-cache freshness is harder than server or CDN invalidation because the origin cannot directly purge every client.
- Surrogate tags can invalidate all representations containing one changed entity while keeping unrelated objects warm.
- Tenant or site namespaces must prevent cache-key collisions and cross-tenant reuse.
- Stale serving is an availability policy, not a universally safe fallback.

## Evidence
- Application hierarchy: [[nick-craver-stack-overflow-the-architecture-2016-edition]] describes local L1 caches, shared Redis L2, source refill after a double miss, and per-site namespaces.
- Cross-server invalidation: [[nick-craver-stack-overflow-the-architecture-2016-edition]] uses Redis pub/sub to clear L1 entries on other servers after removal.
- Source boundary: [[nick-craver-stack-overflow-the-architecture-2016-edition]] treats SQL Server as canonical while Redis and Elasticsearch remain derived.
- Browser boundary: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] distinguishes invalidation-based shared caches from expiration-based browser caches.
- Cache-sketch correctness: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] uses a Bloom filter whose false positives cause revalidation while avoiding false negatives for inserted stale objects.
- Entity tagging: [[improve-cache-performance-with-optimized-api-design]] attaches surrogate keys to composite responses so one mutation can purge every affected representation.
- Availability policy: [[improve-cache-performance-with-optimized-api-design]] recommends stale cached responses during origin failure only where the requester can tolerate age.

## Counterevidence & Qualifications
The three sources are first-party practitioner or vendor accounts rather than controlled comparisons. Stack Overflow's 2016 utilization and operation counts do not establish current Redis performance or prove that pub/sub invalidation cannot be missed; restart, message loss, eviction, stampede, and versioning behavior are not detailed. Surrogate tagging requires complete dependency metadata, while Bloom filters and stale serving preserve correctness only within their stated assumptions. Inventory, entitlement, price, and safety-critical data may need stronger read-after-write or transactional guarantees than these patterns provide.

## What Changed
- Added the application-tier L1/L2 hierarchy, source refill, tenant namespacing, and Redis pub/sub invalidation.
- Made source-of-truth placement explicit across browser, edge, local-process, and shared-cache layers.

## Related Concepts
- [[WebPerformanceOptimization]] - caching removes network, serialization, and origin work from user-visible paths.
- [[LatencyHierarchy]] - local and shared caches trade freshness machinery for lower access cost.
- [[APIResponseCaching]] - applies reuse and invalidation rules to HTTP representations.
- [[Redis]] - shared L2 and invalidation channel in the Stack Overflow design.
- [[BrowserCaching]] - client-side layer with expiration and validation constraints.
- [[Fastly]] - edge platform associated with surrogate-key purging and stale responses.
- [[MultiTenantArchitecture]] - requires namespaced cache ownership and isolation across sites.

---
title: "Latency Hierarchy"
type: concept
tags: [systems, performance, latency]
sources:
  - back-of-the-envelope-calculation-better-programmer
  - building-a-shop-with-sub-second-page-loads-lessons-learned
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[LatencyHierarchy]] is the ordered scale of time costs across computer-system operations, from CPU cache access through memory, synchronization, compression, network round trips, disk, and long-distance communication.

## Current Synthesis
The Better Programmer source uses Jeff Dean's "numbers everyone should know" table to teach relative latency. L1 cache access is treated as sub-nanosecond, L2 cache and branch misprediction as single-digit nanoseconds, mutex and main-memory operations as roughly hundreds of nanoseconds, compression and local network transfer as microseconds, same-datacenter round trips as sub-millisecond, disk seek and network/disk megabyte reads as milliseconds, and intercontinental packet round trips as hundreds of milliseconds.

The source's main judgment is architectural rather than numerical. When operations differ by orders of magnitude, system design should avoid accidental movement into slower tiers. Caching thumbnails in memory, avoiding disk seeks, considering datacenter round trips in distributed key-value access, and treating global networks as non-free all follow from the same hierarchy.

Browser page loads are a user-facing version of the same hierarchy. DNS lookup, TCP handshake, TLS handshake, time to first byte, slow-start downloads, and many small resource requests can dominate user experience. Increasing bandwidth beyond a modest threshold may not help as much as reducing latency and round trips, so browser caches, CDNs, persistent connections, redirect avoidance, and HTTP/2 matter because they move work closer to the user or remove requests entirely.

## Key Claims
- Cache, memory, disk, and network operations differ enough that relative scale shapes architecture.
- Disk seeks and long-distance network round trips can dominate user-visible latency.
- Same-datacenter communication still has measurable cost and should be counted in distributed designs.
- In-memory caching can be justified when the working set is small enough and latency matters.
- Browser and CDN caches can be justified because they avoid high-cost network round trips.
- Request count and connection setup can dominate page-load latency even when backend processing is fast.
- Reference tables need periodic updating, but their order-of-magnitude lessons remain useful.

## Evidence
- Relative operation costs: [[back-of-the-envelope-calculation-better-programmer]] reproduces a table ranging from L1 cache reference at 0.5ns to a California-Netherlands-California packet round trip at 150,000,000ns.
- Disk impact: [[back-of-the-envelope-calculation-better-programmer]] estimates serial thumbnail reads at about 560ms because thirty disk seeks dominate the design.
- Datacenter communication: [[back-of-the-envelope-calculation-better-programmer]] calls out same-datacenter round trips as a real latency term for distributed in-memory key-value stores.
- Caching tradeoff: [[back-of-the-envelope-calculation-better-programmer]] argues that thirty 256KB thumbnails fit in roughly 6-7MB, making memory caching plausible on modern machines.
- Browser-network path: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] decomposes an initial request into DNS lookup, TCP connection, TLS handshake, time to first byte, and resource download.
- Bandwidth qualification: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] argues that after about 5 Mbps, lowering latency helps page-load time more than increasing bandwidth.
- Cache locality: [[building-a-shop-with-sub-second-page-loads-lessons-learned]] presents browser caching and CDNs as ways to reduce round trips and physical distance to users.
- Staleness caution: [[back-of-the-envelope-calculation-better-programmer]] notes that the cited talk was seven years old at the time of writing and based on a 2009 mid-range PC.

## Counterevidence & Qualifications
The hierarchy is a thinking aid, not a universal benchmark. Actual latency depends on CPU generation, cache behavior, SSD and disk characteristics, network topology, contention, serialization, compression data shape, software stack overhead, cloud/provider placement, browser behavior, and last-mile network conditions.

## What Changed
- Created the concept to capture the latency reference model behind the article's performance-estimation examples.
- Added browser page-load latency as a user-facing instance of the same hierarchy.

## Related Concepts
- [[BackOfEnvelopeEstimation]] - uses latency hierarchy numbers as inputs for rough design arithmetic.
- [[SystemReliability]] - latency and capacity failures often begin as ignored system costs.
- [[CloudCostOptimization]] - cost hierarchies and latency hierarchies both guide architecture through rough unit comparisons.
- [[TechnologyStackComplexity]] - crossing more tiers and services can introduce hidden latency terms.
- [[WebPerformanceOptimization]] - page-load work applies latency hierarchy to browser, network, cache, and backend design.
- [[DynamicContentCaching]] - browser-cache hits avoid expensive network tiers while preserving freshness.

---
title: "Redis"
type: entity
tags: [database, cache, server-side, task-queue]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
  - blog-antirez-dont-fall-into-the-anti-ai-hype
  - blog-wulc-pa-chong-zhua-qu-dai-li-ip
  - building-a-shop-with-sub-second-page-loads-lessons-learned
  - kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian
  - nick-craver-stack-overflow-the-architecture-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Redis]] is an in-memory data system used across the sources for layered caching, pub/sub invalidation, queue coordination, Lua-scripted atomic transitions, proxy-pool persistence, cache-freshness metadata, and latency-critical inventory snapshots.

## Current Profile
The sources show Redis in bounded high-speed roles. Wang Ziting stores task-queue state in Redis and uses Lua for atomic coordination; Wulc uses a set as a reusable proxy pool; Baqend stores an expiring Bloom filter for dynamic browser-cache freshness. Stack Overflow adds a large-scale application cache: local L1 entries fall back to shared Redis L2, double misses refill both from the source, and pub/sub clears L1 entries across servers. SQL remains canonical, tenant identifiers namespace cache entries, and the 2016 dashboard shows instance CPU mostly below 2% despite a reported 160 billion monthly operations.

Kikcat places more correctness pressure on Redis by using it as the synchronous inventory-admission snapshot while database records and events reconcile durable state. That design fails closed on stale snapshots, checks Sentinel epochs, consults a Sentinel majority, and rebuilds Redis only after draining pending events. Sentinel failover can still leave old and new masters writable during a partition because ordinary writes lack quorum confirmation. Redis therefore provides speed and atomic local primitives, while durability, freshness, fencing, recovery, and business correctness remain responsibilities of the surrounding protocol.

Antirez's essay presents Redis as a mature systems-code project where AI reproduced transient test failures and internal Streams changes under expert direction; this concerns maintenance practice rather than runtime guarantees.

## Key Characteristics
- Provides low-latency shared state and atomic multi-step transitions through Lua scripts.
- Supports local/shared cache hierarchies, cross-server invalidation, queues, proxy pools, freshness sketches, and inventory snapshots.
- Can remove repeated source work from hot paths while remaining a derived layer over canonical storage.
- Uses pub/sub to distribute invalidation or events, but delivery and recovery guarantees must be designed explicitly.
- Requires stale-state, failover-generation, and reconciliation controls when business correctness depends on an in-memory snapshot.
- Sentinel improves failover availability but cannot alone prevent split-brain writes or guarantee zero inconsistency.
- Its narrow primitives are adaptable, while correctness comes from the surrounding architecture.

## Evidence
- Layered caching: [[nick-craver-stack-overflow-the-architecture-2016-edition]] uses Redis as shared L2 beneath local L1 caches, refills both after a double miss, and namespaces site data.
- Invalidation and scale: [[nick-craver-stack-overflow-the-architecture-2016-edition]] uses Redis pub/sub to clear remote L1 caches and reports about 160 billion monthly operations with instances mostly under 2% CPU in the retained chart.
- Atomic queue coordination: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] uses Redis state and Lua so Node.js workers can coordinate and recover interrupted work.
- Bounded high-change storage: [[blog-wulc-pa-chong-zhua-qu-dai-li-ip]] persists proxy candidates in a set, while [[building-a-shop-with-sub-second-page-loads-lessons-learned]] stores Baqend's expiring Bloom filter.
- Inventory and recovery: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] conditionally deducts inventory with Lua, rejects stale snapshots, and rebuilds only after draining pending events.
- Failover boundary: [[kikcat-dian-shang-xi-tong-de-gao-bing-fa-ku-cun-kou-jian]] shows Sentinel partitions leaving two writable masters and treats epoch, majority, timeout, and replica-health controls as mitigation rather than proof.
- Project maintenance: [[blog-antirez-dont-fall-into-the-anti-ai-hype]] describes expert-supervised AI reproduction of Redis test and internal-change work.

## Qualifications
The sources are practitioner narratives and vendor cases rather than a complete Redis evaluation. Stack Overflow's operations and utilization are 2016 first-party snapshots without workload distribution, latency percentiles, persistence configuration, eviction behavior, or independent verification. Pub/sub invalidation is described functionally but the source does not specify missed-message recovery, cold-start refill, stampede control, or version skew. Kikcat's inventory throughput is expected rather than independently benchmarked and explicitly retains overselling and underselling risk. Modern Redis modes and guarantees require current documentation.

## What Changed
- Added Stack Overflow's local-L1/shared-L2 cache hierarchy and cross-server invalidation pattern.
- Added large-scale but historical operations and CPU-utilization evidence.
- Clarified the distinction between Redis as a derived performance layer and canonical durable state.

## Relationships
- [[DynamicContentCaching]] - uses Redis as shared cache, freshness metadata, and invalidation infrastructure.
- [[StackOverflow]] - platform using Redis for L2 caching, pub/sub, and machine-learning data.
- [[TaskQueueDesign]] - uses Redis state and Lua for atomic worker coordination.
- [[HighConcurrencyInventoryDeduction]] - places Redis on the synchronous stock-admission path.
- [[EventDrivenConsistency]] - reconciles Redis snapshots with durable database state.
- [[WebScrapingProxyPool]] - stores and samples reusable proxies in a Redis set.
- [[Baqend]] - stores an expiring cache-sketch Bloom filter in Redis.
- [[Antirez]] - Redis creator discussing project maintenance and AI coding.

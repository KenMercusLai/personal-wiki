---
title: "Crawler Architecture"
type: concept
tags: [web-crawling, queues, concurrency, distributed-systems]
sources:
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Definition
[[CrawlerArchitecture]] organizes recursive discovery around a mutable frontier whose workers fetch and parse items that can add further work, together with explicit admission, deduplication, capacity, policy, and completion controls.

## Current Synthesis
The comparison of four link checkers identifies a stable core across languages and runtimes. Seed URLs and discovered URLs enter the same frontier. Admission atomically checks and marks URL identity before work is queued, workers fetch and extract new links, and completion is declared only when no item is queued or active and no active item can still create a descendant.

The frontier answers what may run next; a worker pool, semaphore, socket cap, delay cache, or per-host throttler answers how quickly it may run. Keeping these roles separate prevents a recursive producer-consumer cycle from filling the very bounded channel whose consumer must continue draining work to release capacity. Policy is another layer: depth, domain, robots rules, tag support, `nofollow`, body availability, cancellation, and memory limits determine what should be admitted without changing the core worklist invariant.

## Key Claims
- Recursive crawling requires a feedback edge from fetched content to the same logical frontier that supplied the fetch.
- URL identity must be claimed atomically during admission, before network work, to prevent duplicate submissions from concurrent parents.
- Quiescence requires both an empty frontier and no active work capable of creating descendants.
- Frontier storage must be separated from concurrency, rate, and per-host politeness controls.
- Crawl policy and resource bounds constrain admission without replacing deduplication or termination invariants.
- Runtime primitives alter coordination cost but do not remove the underlying worklist, identity, capacity, and completion obligations.

## Evidence
- Feedback topology: [[link-checkers-recurse]] contrasts lychee's one-way input-to-result DAG with crawlers that return discovered links to the frontier.
- Admission identity: [[link-checkers-recurse]] finds enqueue-time visited marking in muffet, LinkChecker, linkinator, and broken-link-checker.
- Completion: [[link-checkers-recurse]] maps `sync.WaitGroup`, `join()`, `queue.onIdle()`, and nested drain events to the same quiescence requirement.
- Capacity separation: [[link-checkers-recurse]] shows frontier structures paired with distinct semaphores, fixed thread counts, queue concurrency, socket caps, or per-host throttlers.
- Policy and scale: [[link-checkers-recurse]] describes robots and tag filters, GET-versus-HEAD body needs, in-memory growth, URL caps, and industrial disk-backed frontiers and probabilistic duplicate filters.

## Counterevidence & Qualifications
The evidence is one maintainer's source-code comparison at a point in time, not a formal taxonomy or cross-tool benchmark. The common pattern does not prescribe one queue representation, fairness policy, retry model, durability level, cancellation protocol, URL-canonicalization rule, or memory bound. Enqueue-time deduplication can also suppress intentional revisits unless freshness and retry states are modeled separately. An unbounded frontier avoids a particular cyclic deadlock by accepting memory risk rather than eliminating resource constraints.

## What Changed
- Created a cross-runtime model of recursive crawler topology and coordination.
- Separated frontier storage, admission identity, execution capacity, crawl policy, and quiescence into distinct obligations.
- Added enqueue-time URL claiming as the shared defense against duplicate admission.

## Related Concepts
- [[DistributedTerminationDetection]] - determines when the dynamic frontier and all descendant-producing work are quiescent.
- [[AdaptiveBackpressure]] - bounds execution and request rate without making the recursive frontier depend on its own blocked consumer.
- [[ConcurrencyFailureModes]] - duplicate admission, premature completion, and cyclic queue blocking are crawler coordination hazards.
- [[TaskQueueDesign]] - supplies queue capacity, ordering, retry, and worker-allocation choices beneath the frontier.
- [[LargeScaleWebScraping]] - extends crawler structure with extraction, anti-bot operations, maintenance, and data-quality controls.
- [[Lychee]] - illustrates the cost of adding a crawler feedback edge to a performance-oriented one-way stream.

---
title: "Hybrid Timeline Fan-out"
type: concept
tags: [system-design, social-feeds, caching, event-driven-architecture]
sources:
  - how-i-made-twitter-back-end
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[HybridTimelineFanout]] is a feed-generation strategy that precomputes delivery for lower-fan-out publishers while merging posts from exceptionally high-fan-out publishers when a reader requests a timeline.

## Current Synthesis
The source presents hybrid fan-out as a workload placement decision. A Timeline consumer reads new-tweet events from RabbitMQ, pushes posts from authors below a follower threshold into each follower's Redis timeline, and avoids that write amplification for authors above the threshold. At read time, the service identifies high-follower accounts a user follows, fetches their recent posts, and merges them with the precomputed timeline.

This split trades one uniform cost for two bounded costs: ordinary posts incur asynchronous write-time duplication, while celebrity posts incur active-user read-time fetch and merge work. The design is plausible but incomplete because follower count is only a proxy for actual fan-out cost and the source provides no benchmark, threshold method, consistency protocol, or recovery path.

## Key Claims
- Push fan-out can make ordinary home-timeline reads cheap by storing ready-to-read per-user timelines.
- Pull fan-out avoids writing a high-follower author's post into very large numbers of active and inactive timelines.
- A hybrid threshold can isolate exceptional publishers instead of forcing one delivery mode on every post.
- Queue-based propagation decouples tweet acceptance from timeline materialization but makes home-feed visibility eventually consistent.
- Correctness requires ordering, deduplication, retry, idempotency, cache-recovery, and merge rules that the source does not specify.

## Evidence
- Write-time path: [[how-i-made-twitter-back-end]] shows the Timeline consumer copying an ordinary tweet into follower keys shaped like `users:${username}:timeline` in Redis.
- Exceptional-publisher path: [[how-i-made-twitter-back-end]] says authors above follower threshold `x` are pulled and merged when an active follower loads the home timeline.
- Event boundary: [[how-i-made-twitter-back-end]] diagrams Tweet publishing through a message queue to Timeline after writing PostgreSQL and Redis.
- Cost rationale: [[how-i-made-twitter-back-end]] uses a one-million-follower author to illustrate write amplification and notes that push also spends work on inactive followers.

## Counterevidence & Qualifications
The source is an educational design narrative, not a production trace, controlled comparison, or verified account of Twitter's internals. It supplies no value for `x`, workload distribution, latency target, cache-retention policy, or measurements showing where push becomes slower or more expensive than pull. A static follower threshold can misclassify dormant large accounts, highly active smaller accounts, or audiences with unusual read behavior. The design also leaves celebrity-list freshness, pagination, ranking, ordering, duplicates, deletes, unfollows, retweets, broker failure, poison messages, backpressure, Redis loss, and durable replay unresolved.

## What Changed
- Created the concept around the source's threshold-based push/pull timeline strategy.
- Separated the cost-placement insight from unsupported claims about Twitter's production implementation.
- Made the unaddressed consistency, recovery, and threshold-calibration requirements explicit.

## Related Concepts
- [[EventDrivenConsistency]] - queued timeline materialization exchanges immediate visibility for asynchronous propagation.
- [[TaskQueueDesign]] - broker delivery, retries, idempotency, and backpressure govern the fan-out worker path.
- [[NetworkLoadBalancing]] - request routing sits upstream of the Tweet and Timeline services.
- [[AuthenticationInfrastructure]] - distributed feed services verify tokens without needing token-signing authority.
- [[ServiceHealthChecks]] - endpoint reachability alone is weaker than workload-sensitive health for the fan-out path.

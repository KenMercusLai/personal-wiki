---
title: "KV-Cache-Aware Routing"
type: concept
tags: [ai-inference, routing, kv-cache]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

KV-cache-aware routing assigns an inference request partly according to which worker can reuse cached key-value blocks for the request's token prefix.

## Current Synthesis

Cache reuse is prefix-based because a token's KV representation depends on the preceding sequence. Implementations therefore need both accurate tokenization and a view of cached blocks. The current source contrasts exact event consumption with inferred cache state and presents Dynamo's cost function as an explicit way to trade reduced prefill work against decode load.

## Key Claims

- Reusable KV blocks correspond to a shared prefix, not arbitrary matching token subsequences.
- Cache-aware routing needs a mechanism to learn block creation and eviction.
- Maximizing overlap alone can overload a popular worker, so reuse and active load must be combined.
- Event-driven cache state reduces polling but introduces replica-consistency concerns.

## Evidence

### Prefix reuse and cache knowledge

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] explains AIBrix's token-prefix tree and KV-event consumption, and contrasts them with GAIE's assumption that routed requests create blocks and its LRU eviction simulation.

### Reuse-load tradeoff

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] describes Dynamo's cost as weighted prefill blocks plus estimated decode blocks, using active-block events and router history to evaluate workers.

## Counterevidence & Qualifications

- The source does not report comparative hit rate, latency, or throughput measurements.
- Simulated state may be less accurate than engine events, but the practical error is not quantified.
- Replica synchronization is eventually consistent, so concurrent routers can still make decisions from divergent millisecond-scale state.

## What Changed

- Added the prefix-dependency rationale for KV-cache reuse.
- Distinguished event-observed cache state from router-simulated state.
- Framed cache affinity as a cost balanced against worker load.

## Related Concepts

- [[InferenceLoadBalancing]] - uses cache affinity as one input to request placement.

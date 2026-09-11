---
title: "KV-Cache-Aware Routing"
type: concept
tags: [ai, inference, routing, caching]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Definition
[[KVCacheAwareRouting]] routes inference requests by considering which workers already hold reusable key-value cache blocks for a prompt prefix, reducing prefill work when cached prefixes can be reused.

## Current Synthesis
The source explains KV-cache-aware routing as a block-prefix problem. Inference engines share cached key-value state at configurable block granularity, and a request can avoid recomputing the portion of its prefix already cached on a worker. Prefix matching matters because later token computations depend on earlier tokens; arbitrary matching in the middle of a sequence is not equivalent.

Implementations differ in how they know cache state. AIBrix consumes KV events and performs prefix-tree matching. Gateway API Inference Extension infers cache creation from routing decisions and simulates deletion with LRU behavior. Dynamo combines KV-event active-block state with router-maintained routing history and a cost function that balances prefill blocks against decode blocks.

## Key Claims
- KV-cache reuse can materially change the true cost of serving an inference request.
- Prefix matching is required because cached later-token state depends on the preceding token sequence.
- KV-event streams give routers a lower-overhead view of cache state than repeated metric polling.
- Simulating cache state can enable cache-aware routing but may diverge from actual engine state.
- Cost functions can combine cache overlap and current worker load into a routing decision.

## Evidence
- Prefix-cache mechanics: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] explains why shared KV-cache blocks are reusable for prompt prefixes rather than arbitrary matching subsequences.
- AIBrix design: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] says AIBrix uses KV events with tokenizer-backed prefix-tree matching.
- GAIE design: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] says GAIE infers created blocks from routed requests and simulates deletion with LRU.
- Dynamo design: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] describes a cost function using prefill blocks, decode blocks, active-block KV events, and router history.

## Counterevidence & Qualifications
The source does not compare cache-hit rates or route quality empirically. Its assessment of simulated cache state is architectural, and real-world accuracy would depend on engine behavior, event fidelity, and synchronization delays.

## What Changed
- Created the concept page for cache-aware inference routing.

## Related Concepts
- [[InferenceLoadBalancing]] - KV-cache state is one of the load signals used for routing.
- [[InferenceTokenization]] - tokenized prefixes and block boundaries determine what cache can be reused.

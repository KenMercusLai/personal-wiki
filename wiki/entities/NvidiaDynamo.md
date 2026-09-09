---
title: "NVIDIA Dynamo"
type: entity
tags: [ai-inference, open-source, nvidia]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Overview

NVIDIA Dynamo is an open-source inference platform with local tokenizers and event-driven, KV-cache-aware routing.

## Current Profile

The current source regards Dynamo as the strongest of the compared metric architectures because it combines engine-emitted active-block events with router-owned placement history instead of polling every backend. Its cost function balances prefill reuse against decode load, while replica synchronization and routing temperature address distributed coordination.

## Key Characteristics

- Supports local Hugging Face, forked tiktoken, and fast tokenizer implementations.
- Scores workers using weighted prefill blocks plus estimated decode blocks.
- Uses KV active-block events and local routing history as its primary load state.
- Offers router-replica synchronization and randomized selection temperature.

## Evidence

### Local estimation and cost-based routing

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] lists Dynamo's three local tokenizer options and describes its prefill-plus-decode cost function.

### Distributed state

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] explains how KV events and route history avoid backend polling, with replica synchronization for shared state and temperature to reduce herd behavior.

## Qualifications

- The favorable assessment is architectural and lacks cross-project benchmark evidence.
- Network delay leaves brief state divergence even with replica synchronization.
- Active blocks are a proxy for compute and memory load rather than a complete measurement of all bottlenecks.

## What Changed

- Added Dynamo as an event-driven inference-platform entity.
- Recorded its explicit balance between cache overlap and decode load.
- Preserved eventual-consistency limits alongside the source's positive judgment.

## Relationships

- [[InferenceLoadBalancing]] - implements event-driven load estimation and cost-based placement.
- [[KVCacheAwareRouting]] - balances reusable prefill blocks against decode work.
- [[AIBrix]] - contrasts event consumption with high-frequency backend polling.

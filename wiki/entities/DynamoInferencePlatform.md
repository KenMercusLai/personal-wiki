---
title: "Dynamo Inference Platform"
type: entity
tags: [ai, inference, infrastructure, routing]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Overview
[[DynamoInferencePlatform]] is an inference platform whose router is presented in the source as a comparatively efficient design for [[InferenceLoadBalancing]].

## Current Profile
The source treats Dynamo as the strongest surveyed implementation for metric collection overhead. Dynamo uses local tokenizer options, routes through configurable strategies, and centers one strategy on a worker cost function that combines cache-overlap effects with active decode load. Its main architectural advantage is avoiding repeated backend polling by relying on KV events, router-maintained history, router replica synchronization, and controlled randomness.

## Key Characteristics
- Supports local HuggingFace, tiktoken-derived, and fast tokenizer paths.
- Uses a cost function balancing prefill blocks and decode blocks.
- Derives worker load from KV-event active-block state and router history.
- Avoids high-frequency polling of every inference engine.
- Supports router replica synchronization and temperature-based randomness.

## Evidence
- Tokenizers: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] lists Dynamo's local tokenizer options.
- Cost routing: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] describes Dynamo's cost formula using prefill blocks, decode blocks, and an overlap weight.
- Metric efficiency: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] argues that Dynamo has the lowest metric-collection overhead because it consumes KV events instead of polling engines.
- Replica behavior: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] notes router replica synchronization and temperature options to reduce stale-state and herd effects.

## Qualifications
The source still acknowledges millisecond-level state inconsistency between router replicas. Dynamo's design is presented as eventually consistent rather than perfectly synchronized.

## What Changed
- Created the entity page for Dynamo as an inference routing platform.

## Relationships
- [[InferenceLoadBalancing]] - Dynamo is presented as an efficient inference load-balancing implementation.
- [[KVCacheAwareRouting]] - Dynamo's cost function depends on cache overlap and active-block state.
- [[InferenceTokenization]] - Dynamo relies on local tokenizer implementations.

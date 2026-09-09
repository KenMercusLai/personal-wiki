---
title: "Inference Load Balancing"
type: concept
tags: [ai-inference, load-balancing]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Definition

Inference load balancing is the routing and admission-control layer that estimates the work represented by AI inference requests, observes serving-engine state, and assigns requests to keep latency and resource use acceptably distributed.

## Current Synthesis

An inference load balancer needs a model-aware estimate of incoming work, sufficiently fresh backend state, and a routing rule that converts both into a placement decision. The current source favors local, model-matched tokenization and event-driven state over generic token estimates, remote tokenization calls, or every-router-to-every-engine polling. [[KVCacheAwareRouting]] adds reuse potential to the decision but must be balanced against current worker load.

## Key Claims

- Token counts are useful only when the tokenizer matches the served model closely enough.
- Metric freshness can improve balance, but polling cost grows with both router and engine counts.
- Event-driven KV state plus router-owned request history can replace much backend polling.
- A routing architecture must account for request and response paths, not only picker logic.

## Evidence

### Model-aware load estimation

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] compares byte estimates, tiktoken encodings, remote APIs, and local Hugging Face tokenizers, arguing that model mismatch is especially visible for text without word separators.

### State collection and routing architecture

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] estimates that AIBrix-style router-to-engine polling has multiplicative scaling cost and contrasts it with Dynamo's KV-event and routing-history design.
- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] also notes that sidecar and centralized-picker designs can limit response-side measurement or create an additional request-path bottleneck.

## Counterevidence & Qualifications

- The source is an expert architectural critique, not a controlled performance comparison.
- Its large-cluster request-rate calculation depends on assumed engine, gateway, and refresh counts.
- Event-driven designs still face delayed or inconsistent state across router replicas.
- The article does not quantify when simpler estimates are accurate enough to justify lower implementation complexity.

## What Changed

- Established the wiki's first comparison framework for inference load balancers.
- Added model-matched tokenization and metric topology as primary design criteria.
- Identified event-driven state as a promising scaling alternative with consistency limits.

## Related Concepts

- [[KVCacheAwareRouting]] - supplies cache-reuse information to inference placement decisions.

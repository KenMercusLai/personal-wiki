---
title: "锐评主流AI推理负载均衡开源实现"
type: source
tags: [ai, inference, load-balancing, infrastructure]
date: 2026-03-29
source_file: /mnt/ken_personal_wiki/Articles/锐评主流AI推理负载均衡开源实现.md
---

## Summary
This article compares open-source implementations of [[InferenceLoadBalancing]] across standalone components and inference-platform gateways. It evaluates [[AIBrix]], [[Kthena]], [[GatewayAPIInferenceExtension]], and [[DynamoInferencePlatform]] through three core questions: how requests are tokenized, how balancing metrics are collected, and how routing decisions use those metrics. The author argues that tokenizer correctness, metric freshness, distributed collection cost, and [[KVCacheAwareRouting]] design are the main differentiators.

## Key Claims
- [[InferenceLoadBalancing]] should be evaluated by tokenizer accuracy, metric collection freshness, metric-to-routing logic, and quota enforcement.
- Tokenizer choice matters for routing and accounting, especially for Chinese and other text without clear word separators.
- [[AIBrix]] exposes flexible tokenization and KV-cache-aware routing, but its high-frequency polling and Prometheus path can become costly at large cluster scale.
- [[Kthena]] improves routing composition and deployment simplicity over AIBrix, but inherits a questionable tiktoken encoding choice.
- [[GatewayAPIInferenceExtension]] centralizes endpoint selection, but its EPP design may become a bottleneck when request and response paths must traverse it.
- [[DynamoInferencePlatform]] uses local tokenizers, KV-event-derived state, cost-based routing, and router replica synchronization to reduce backend polling.

## Key Quotes
> "负载均衡一向是业务架构里不可或缺的一部分" - on why inference workloads still require load balancing.

> "我个人推崇的想法是采用 hf tokenizer" - on preferring local HuggingFace tokenization at the gateway.

## Connections
- [[InferenceLoadBalancing]] - the article's central evaluation frame for inference gateways and routers.
- [[InferenceTokenization]] - tokenizer strategy is treated as a core routing and accounting concern.
- [[KVCacheAwareRouting]] - multiple implementations are compared by how they reuse or infer KV-cache state.
- [[AIBrix]] - critiqued for tokenizer choices, polling-based metric collection, and architecture.
- [[Kthena]] - compared with AIBrix on routing composition and router architecture.
- [[GatewayAPIInferenceExtension]] - evaluated as a centralized endpoint-picker design.
- [[DynamoInferencePlatform]] - presented as the strongest design for low-overhead metric collection.

## Contradictions
- No direct contradictions with existing wiki content. This source extends the AI thread from personal knowledge tooling into inference infrastructure.

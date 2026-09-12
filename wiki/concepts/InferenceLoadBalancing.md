---
title: "Inference Load Balancing"
type: concept
tags: [ai, inference, infrastructure, load-balancing]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[InferenceLoadBalancing]] is the routing, quota, and scheduling layer that distributes AI inference requests across model-serving workers while accounting for tokenized workload, live system state, and cache reuse opportunities.

## Current Synthesis
The source frames inference load balancing as a specialized form of load balancing whose unit of work is not just a request count. A capable implementation needs to understand prompt size through tokenization, collect timely metrics that approximate worker load, and choose routing policies that balance fairness, throughput, and cache reuse. The article treats quota enforcement as comparatively straightforward once workload accounting is reliable.

The strongest architectural distinction is how implementations obtain live state. Polling every inference engine from every gateway can create large fan-out costs, while event-driven designs that consume KV-cache events reduce collection overhead. Centralized endpoint-picking avoids some duplicate collection but may move the bottleneck into the picker if request and response paths pass through it.

Application-layer cache protocols can change the apparent cost of a request before it reaches routing. If a provider accepts cache edits that logically remove selected tool-result blocks while preserving a stable prefix, routers and serving systems may still reason in prefix-cache terms, but they need semantics rich enough to account for the edited cached view.

## Key Claims
- Inference load balancers need workload-aware tokenization rather than request-count-only routing.
- Metric freshness matters because routing quality depends on how current the load picture is.
- Distributed high-frequency polling can become expensive as gateway and engine counts both grow.
- KV-cache state is a first-class routing signal because prefix reuse changes the true cost of a request.
- Quota enforcement is easier once token-level workload estimates are already available.
- Application-layer prompt-cache edits can affect prefill cost and therefore the load signal a router should ideally understand.

## Evidence
- Evaluation criteria: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] defines tokenizer choice, balancing metrics, and metric-driven routing as the basic questions for judging an inference load balancer.
- Freshness and scale: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] argues that more timely metrics produce more even upstream load, while every-gateway-to-every-engine polling can approach O(n^2) behavior.
- KV-cache routing: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] explains that block-prefix cache reuse can avoid recomputing already cached token blocks.
- Quotas: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] treats quotas as policies over already-known load counters.
- Cache-edited request shape: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] argues that Claude Code's microcompact keeps a stable cached prefix plus replayed edit script, which can change the effective prefill work.

## Counterevidence & Qualifications
The sources are implementation and code-behavior analyses rather than benchmark studies. Their judgments are grounded in architectural reasoning and source-code behavior, but they do not provide measured latency, throughput, cache-hit, or failure-mode data across comparable deployments.

## What Changed
- Created the concept page for inference-specific load balancing.
- Added the core evaluation frame of tokenization, metric collection, routing, and quota enforcement.
- Added application-layer prompt-cache edits as a serving-cost signal that may affect routing.

## Related Concepts
- [[InferenceTokenization]] - token accounting is the first step in estimating request load.
- [[KVCacheAwareRouting]] - cache-aware routing is one way inference load balancers reduce work.
- [[AIKnowledgeAssistant]] - both concern AI systems, but this page focuses on serving infrastructure rather than personal knowledge workflows.
- [[PromptCaching]] - prompt-cache reuse can change how expensive a request is to serve.

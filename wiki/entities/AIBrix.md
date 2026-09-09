---
title: "AIBrix"
type: entity
tags: [ai-inference, open-source]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Overview

AIBrix is an open-source inference platform whose gateway provides tokenization, metrics collection, rate limiting, and multiple routing algorithms.

## Current Profile

In the current source, AIBrix is a feature-rich baseline whose architecture combines Envoy with a Go sidecar. Its KV-aware routing consumes engine events, but its tokenizer defaults and high-frequency distributed polling are criticized as poor fits for heterogeneous models and large clusters.

## Key Characteristics

- Supports byte, tiktoken, and remote-API tokenization.
- Polls engine metrics and Prometheus while also consuming KV events.
- Offers multiple routing algorithms, including prefix-based KV-cache-aware routing.
- Uses an Envoy-plus-sidecar data path.

## Evidence

### Load estimation and observation

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] reports the three tokenizer modes and three metric paths, while criticizing `cl100k_base`, redundant Prometheus queries, and multiplicative polling cost.

### Routing and data path

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] describes KV-event-backed prefix matching and notes that a response path bypassing the sidecar forces some output-token estimates.

## Qualifications

- The profile reflects one author's code and architecture review rather than benchmark results.
- Polling intervals and worker counts are configurable, so the default-cost critique is not universal.
- AIBrix can disable its own gateway and use another load-balancing component.

## What Changed

- Added AIBrix as an inference-platform entity.
- Recorded both its broad routing feature set and the source's scalability critique.

## Relationships

- [[InferenceLoadBalancing]] - implements inference routing and admission functions.
- [[KVCacheAwareRouting]] - consumes KV events and matches token prefixes for reuse.
- [[Kthena]] - serves as the architectural baseline for the source's comparison of Kthena.

---
title: "Kthena"
type: entity
tags: [ai-inference, open-source]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-09
knowledge_schema: synthesis-v1
---

## Overview

Kthena is an open-source inference router implemented as a single Go binary.

## Current Profile

The source presents Kthena as architecturally similar to AIBrix's gateway but simpler in its data plane and able to combine routing algorithms by weight. It nevertheless receives the same criticism for using the `cl100k_base` tiktoken encoding without ensuring model compatibility.

## Key Characteristics

- Runs as a single Go router binary.
- Supports weighted composition of multiple routing algorithms.
- Avoids an Envoy-plus-sidecar data plane.
- Uses `cl100k_base` for its tiktoken option in the reviewed version.

## Evidence

### Simplicity and composition

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] credits Kthena with weighted algorithm composition and a simpler single-binary data path.

### Tokenizer limitation

- [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] argues that its fixed GPT-oriented encoding may misestimate work for other models.

## Qualifications

- This profile is limited to the router behavior reviewed by one author.
- The source provides no comparative latency or throughput measurements.
- Simpler deployment does not by itself establish better reliability or performance.

## What Changed

- Added Kthena as an inference-router entity.
- Recorded weighted strategy composition as its principal differentiator.

## Relationships

- [[InferenceLoadBalancing]] - provides a single-binary implementation of inference routing.
- [[AIBrix]] - shares a similar broad architecture while simplifying the data path.
- [[GatewayAPIInferenceExtension]] - also supports weighted routing-strategy composition.

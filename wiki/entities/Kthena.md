---
title: "Kthena"
type: entity
tags: [ai, inference, infrastructure, router]
sources:
  - rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Overview
[[Kthena]] is an inference router discussed as a simpler alternative to AIBrix-style gateway architecture.

## Current Profile
The source presents Kthena as architecturally similar to AIBrix but improved in two ways: it can compose multiple routing algorithms by weight, and it is implemented as a single Go router binary rather than an Envoy plus sidecar data-plane arrangement. The article still criticizes Kthena for copying a tiktoken encoding choice that may not match modern or non-GPT models.

## Key Characteristics
- Supports weighted composition of multiple routing algorithms.
- Uses a single Go binary router design.
- Is compared favorably against AIBrix's more complex data-plane structure.
- Still uses cl100k_base in the discussed tiktoken path.
- Serves as a case where simpler architecture does not automatically solve tokenizer correctness.

## Evidence
- Routing composition: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] identifies weighted routing-algorithm composition as a Kthena improvement.
- Deployment simplicity: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] favors Kthena's single-binary router over an Envoy plus sidecar design.
- Tokenizer critique: [[rui-ping-zhu-liu-ai-tui-li-fu-zai-jun-heng-kai-yuan-shi-xian]] criticizes Kthena for using cl100k_base in 2025-era code.

## Qualifications
The source covers Kthena through the lens of routing architecture and tokenizer choices. It does not provide a full feature audit, production benchmark, or operational comparison.

## What Changed
- Created the entity page for Kthena as an inference router.

## Relationships
- [[AIBrix]] - Kthena is presented as architecturally similar but simpler.
- [[InferenceLoadBalancing]] - Kthena is evaluated as an inference routing implementation.
- [[InferenceTokenization]] - tokenizer encoding choice is the main critique.

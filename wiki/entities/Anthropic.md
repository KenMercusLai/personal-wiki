---
title: "Anthropic"
type: entity
tags: [ai, llm, company]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Anthropic]] appears in the source as an example LLM provider using prompt caching with segmented cache controls.

## Current Profile
The source mentions Anthropic while discussing the engineering tension between dynamic context compression and KV/prompt caching. Anthropic's prompt caching is used as an example of caching stable prompt segments such as tools, system messages, and conversation messages, with a limited number of cache breakpoints.

## Key Characteristics
- Represents a mainstream provider using prefix or prompt caching for LLM inference.
- Is used to illustrate why stable prompt prefixes matter for latency and cost.
- Provides a segmented caching example involving tools, system prompts, and messages.
- Shows the engineering tension between dynamic context edits and cache reuse.

## Evidence
- Provider example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] names Anthropic among providers doing prefix caching.
- Segment structure: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Anthropic's prompt caching handles tools, system, and messages in a fixed order.
- Cache breakpoints: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says the mechanism supports multiple cache-control points.
- Compression tension: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] uses this caching model to explain why modifying earlier context can invalidate later cache reuse.

## Qualifications
This profile reflects the source's caching discussion and should not be read as current Anthropic product documentation, limits, pricing, or API guidance.

## What Changed
- Created an entity profile for Anthropic as an example in prompt-caching architecture.

## Relationships
- [[DynamicContextCompression]] - Anthropic's caching model illustrates compression/cache tension.
- [[LLMContextManagement]] - prompt caching rewards stable context organization.
- [[KVCacheAwareRouting]] - both pages concern reuse of KV-derived computation, though at different layers.

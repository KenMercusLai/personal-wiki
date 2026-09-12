---
title: "Anthropic"
type: entity
tags: [ai, llm, company]
sources:
  - yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Anthropic]] appears in the sources as an LLM provider associated with prompt caching architecture and with Claude Code's product, model, and usage-limit context.

## Current Profile
One source mentions Anthropic while discussing the engineering tension between dynamic context compression and KV/prompt caching: Anthropic's prompt caching is used as an example of caching stable prompt segments such as tools, system messages, and conversation messages, with a limited number of cache breakpoints. The Claude Code retrospective presents Anthropic as both model provider and tool builder, arguing that this vertical integration helps Claude Code feel more coherent than combinations of other models and agent shells, while also noting weekly limits as a resource and pricing constraint.

## Key Characteristics
- Represents a mainstream provider using prefix or prompt caching for LLM inference.
- Is used to illustrate why stable prompt prefixes matter for latency and cost.
- Provides a segmented caching example involving tools, system prompts, and messages.
- Shows the engineering tension between dynamic context edits and cache reuse.
- Builds or provides the Claude Code context in the source's account, combining model quality with tool workflow design.
- Imposes usage limits that the source interprets as evidence of compute and pricing pressure.

## Evidence
- Provider example: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] names Anthropic among providers doing prefix caching.
- Segment structure: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says Anthropic's prompt caching handles tools, system, and messages in a fixed order.
- Cache breakpoints: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] says the mechanism supports multiple cache-control points.
- Compression tension: [[yi-kou-qi-ba-suo-you-rang-ni-mu-xuan-de-llm-ming-ci-quan-dou-guo-yi-bian]] uses this caching model to explain why modifying earlier context can invalidate later cache reuse.
- Vertical integration: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] argues that Anthropic benefits from being both model provider and Claude Code tool developer.
- Usage limits: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] discusses new weekly limits and speculates that heavy usage, compute scarcity, and pricing pressure are part of the background.

## Qualifications
This profile reflects source-scoped caching and Claude Code usage discussion and should not be read as current Anthropic product documentation, current limits, pricing, financing status, or API guidance.

## What Changed
- Created an entity profile for Anthropic as an example in prompt-caching architecture.
- Added the Claude Code source's view of Anthropic as a vertically integrated model/tool provider with usage-limit pressure.

## Relationships
- [[DynamicContextCompression]] - Anthropic's caching model illustrates compression/cache tension.
- [[LLMContextManagement]] - prompt caching rewards stable context organization.
- [[KVCacheAwareRouting]] - both pages concern reuse of KV-derived computation, though at different layers.
- [[ClaudeCode]] - Anthropic is the provider context for the tool in the source.
- [[VibeCoding]] - Anthropic's tool and model integration shapes the source's vibe-coding experience.

---
title: "如何像 Claude Code 一样使用私有 API 管理 prompt cache"
type: source
tags: [ai, llm, prompt-caching, context-management, infrastructure]
date: 2026-04-03
source_file: /mnt/ken_personal_wiki/Articles/如何像 Claude Code 一样使用私有 API 管理 prompt cache.md
---

## Summary
This article analyzes how [[ClaudeCode]] manages [[PromptCaching]] when calling [[Anthropic]] models, especially how stable request shape, cache breakpoints, and private cache-edit markers can preserve cache reuse while changing the effective provider-side context. It argues that Claude Code's microcompact path is not ordinary local summarization: it marks large tool results with cache references, appends cache-edit deletion instructions in later requests, and logically removes low-value cached blocks from the server's view without changing the user's visible conversation history.

## Key Claims
- [[PromptCaching]] in Anthropic-style APIs depends on stable system, tool, model, message-prefix, thinking-config, and beta-header inputs rather than an explicit user-supplied cache key.
- [[ClaudeCode]] improves cache-hit rates by avoiding unnecessary changes to cache-covered structures, including using system reminder messages instead of regenerating tool definitions when tools are enabled or disabled.
- Anthropic's public cache controls support breakpoint-style caching over system and content blocks, while Claude Code usually relies on a small number of breakpoints.
- Claude Code's private microcompact path uses `cache_reference` on old content blocks and later `cache_edits` blocks to delete those references from the provider-side cached view.
- Microcompact performs logical deletion during request serialization rather than rewriting local message history, so UI-visible history and local records remain intact.
- Replaying pinned cache edits in later requests suggests a "cached prefix plus persistent edit script" model rather than a permanently mutated server-side cache object.
- This design links product behavior, agent context management, and inference infrastructure: [[DynamicContextCompression]] becomes more useful when the provider can preserve cache reuse while evicting low-value tool results.

## Key Quotes
> "本地历史没删" - on microcompact preserving local conversation history while changing the cached server view.

> "cached prefix + edit script" - on the inferred model behind Claude Code's private cache-edit mechanism.

## Connections
- [[ClaudeCode]] - central product whose request serialization and microcompact behavior are analyzed.
- [[Anthropic]] - model provider whose prompt-cache pricing, cache controls, and private API behavior frame the article.
- [[PromptCaching]] - central mechanism for stable-prefix reuse, cache breakpoints, and cache edits.
- [[LLMContextManagement]] - the article treats prompt shape and tool-result history as active context-management concerns.
- [[DynamicContextCompression]] - microcompact is a cache-preserving form of removing low-value context from the provider-side view.
- [[KVCacheAwareRouting]] - the article connects cache edits back to prefix-oriented KV-cache reuse and routing assumptions.
- [[InferenceLoadBalancing]] - prompt-cache state changes can affect serving cost and routing strategy.

## Contradictions
- No direct contradiction with existing wiki pages. The source qualifies earlier [[DynamicContextCompression]] material by showing one provider-specific design that can reduce the usual conflict between context edits and prompt-cache reuse.

---
title: "Prompt Caching"
type: concept
tags: [ai, llm, caching, inference]
sources:
  - ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache
  - context-engineering-from-the-inside-out
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[PromptCaching]] is an LLM serving mechanism that reuses previously processed prompt prefixes or marked prompt segments so repeated system prompts, tools, message history, and other stable inputs do not need to be fully recomputed on every request.

## Current Synthesis
The source presents prompt caching as both an infrastructure optimization and a product-design constraint. Anthropic-style prompt caching does not expose a user-defined cache key; instead, the effective key is inferred to include stable request parts such as system text, tools, model, message prefix, thinking configuration, and beta headers. Because tools and message prefixes are part of that reusable shape, clients that want good cache-hit rates must avoid gratuitously changing them.

[[ClaudeCode]] is the main case study. It improves cache reuse by keeping cache-covered structures stable and moving some changing control information into appended messages. Its private microcompact path extends this idea: large, low-value tool results can be assigned `cache_reference` names, then later `cache_edits` can delete those references from the provider-side cached view. The local conversation is not rewritten; instead, request serialization sends a persistent edit script that changes the effective cached prefix while preserving stable surrounding content.

The newer source broadens the design surface from one provider's cache controls to the whole agent trajectory. Tool definitions are part of the prefix, so adding, removing, or reordering tools can invalidate reuse. Across repeated workflows, nondeterministic tool fields such as timestamps, UUIDs, unstable result ordering, and irrelevant changing metadata can also prevent otherwise similar prefixes from matching. This makes response normalization a cache concern as well as a context-quality concern.

## Key Claims
- Prompt-cache keys are shaped by stable request content rather than by a separate application-provided key.
- Cache breakpoints let a client choose which prompt prefix or segment should be cacheable.
- Cache efficiency depends on keeping system prompts, tool definitions, and reusable message prefixes stable.
- Claude Code's microcompact mechanism treats selected large tool results as logically deletable from the provider-side cached view.
- Replayed cache edits suggest a persistent "cached prefix plus edit script" model rather than a permanently rewritten cache object.
- Prompt caching links context-management quality with inference cost, latency, and routing concerns.
- Stable tool catalogs and deterministic tool-result serialization can increase reuse across repeated sessions, while compaction deliberately accepts a one-time prefix reset.

## Evidence
- Cache-key shape: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] infers that Anthropic cache matching covers system, tools, model, message prefix, thinking config, and beta headers.
- Breakpoint behavior: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] describes public cache-control breakpoints and notes that Claude Code commonly uses a small number of them.
- Stability tactics: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] says Claude Code preserves tool definitions and appends system-reminder messages when tool availability changes.
- Microcompact semantics: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] describes `cache_reference` and `cache_edits` as a logical deletion mechanism for old tool results.
- Edit replay: [[ru-he-xiang-claude-code-yi-yang-shi-yong-si-you-api-guan-li-prompt-cache]] argues that pinned cache edits being resent in later requests points to a stable request shape containing the edit script.
- Tool-schema stability: [[context-engineering-from-the-inside-out]] notes that complete tool schemas occupy the system prefix and that changing their membership or order forces prefix recomputation.
- Deterministic responses: [[context-engineering-from-the-inside-out]] recommends stripping irrelevant timestamps and UUIDs, sorting by stable keys, and removing changing metadata where repeated workflows can otherwise share prefixes.
- Compaction trade-off: [[context-engineering-from-the-inside-out]] says reactive compaction causes a one-time cache miss when the summary becomes a new prefix, after which that prefix can remain stable again.

## Counterevidence & Qualifications
The sources combine code reading, inference about private provider behavior, and a practitioner design essay rather than controlled serving benchmarks. Private cache-edit fields are not documented public API, and the claimed cross-session benefit of deterministic tool results depends on provider caching scope, retention, routing, and exact serialization. Within one append-only conversation, a new tool result extends rather than invalidates the preceding prefix.

## What Changed
- Added tool-schema stability and deterministic tool-result serialization as cross-request cache-design concerns.
- Clarified that compaction trades a one-time prefix reset for a new stable cacheable trajectory.

## Related Concepts
- [[LLMContextManagement]] - prompt caching rewards stable organization of instructions, tools, and history.
- [[DynamicContextCompression]] - cache edits make one form of compression compatible with cache reuse.
- [[KVCacheAwareRouting]] - both depend on reuse of cached prefix computation.
- [[InferenceLoadBalancing]] - cache reuse changes the true serving cost that routers may need to consider.
- [[InferenceTokenization]] - tokenized prompt structure determines the units of cached computation.

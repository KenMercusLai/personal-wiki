---
title: "DeepSeek Harness"
type: entity
tags: [ai, agents, coding-agent, runtime, open-source]
sources:
  - deepseek-harness-source-analysis
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[DeepSeekHarness]] is a local-first coding agent and composable agent development runtime whose analyzed architecture combines models with tool execution, context policy, sessions, persistence, permissions, and application entry points.

## Current Profile
The analyzed version uses Cordis to manage plugin dependencies and lifecycle. Profiles select application shapes such as Web, desktop, headless, or SDK; Bundles distribute reusable plugin combinations; and ordered Patches replace configuration for matching plugin entries. The SDK drives a runtime subprocess over JSON-RPC, while the agent loop advances Turns through model-and-tool Steps.

Its session design separates an append-only event Log from a derived Surface used as model history. Persistence plugins buffer events to compressed or plain JSONL, checkpoint before model requests and top-level tool calls, and repair interrupted executions without claiming that a missing tool result proves the external action did not happen. The runtime also exposes Skills, dynamic plugins, and [[ProgrammaticToolCalling]], while documented examples connect generated UI, GitHub review triggers, Lark messaging, and scheduled task cards.

## Key Characteristics
- Cordis plugins make model adapters, tools, sessions, context policy, storage, and execution environments separately composable.
- Profile, Bundle, and Patch layers describe application composition, with later configuration layers modifying earlier entries.
- The loop preserves explicit Turn and Step boundaries while tool scheduling respects declared concurrency safety.
- Session Log retains execution events while Surface derives the smaller message history used for the next model request.
- Buffered persistence and checkpoints narrow data-loss windows without providing exactly-once external effects.
- Skills supply operating guidance over capabilities, while plugins can add capabilities and register Skills.
- Web, desktop, headless, and SDK entry points reuse the same runtime composition model.

## Evidence
- Composition model: [[deepseek-harness-source-analysis]] and its retained architecture diagram show Profiles, Bundles, and Patches feeding Cordis-managed plugins for models, loop, tools, sessions, context, and execution.
- Execution model: [[deepseek-harness-source-analysis]] describes multi-Step Turns, concurrency-safe tool batches, ordered results, and stale-file-version rejection.
- Session and recovery: [[deepseek-harness-source-analysis]] distinguishes Log from Surface and documents buffered persistence, checkpoints, interrupted-run repair, and uncertainty after an unrecorded outcome.
- Extension surface: [[deepseek-harness-source-analysis]] documents Skills, dynamic tool plugins, PTC, generated UI, event-triggered review, messaging, and scheduled task examples.

## Qualifications
The profile rests on one detailed source-reading article, not direct installation or independent benchmarking. It reflects commit `c291e7961a` and a developer-preview release, so interfaces and defaults may change. The author did not run the whole application or validate the community plugins. DSH's SDK could continue a session in one live runtime but did not restore an uncached persisted session in a new SDK process through the shown API. Checkpointed logging improves recoverability but does not make external effects atomic, idempotent, or exactly once.

## What Changed
- Created a product profile separating DSH's composable runtime from the broader [[HarnessEngineering]] practice.

## Relationships
- [[HarnessEngineering]] - DSH exposes harness responsibilities as configurable runtime components.
- [[TapeAndAnchors]] - both separate durable execution history from the context view assembled for a model request.
- [[AgentResumability]] - DSH checkpoints persistence and repairs interrupted session records before continuation.
- [[ProgrammaticToolCalling]] - DSH offers `run_code` as a model-generated composition layer over governed tools.
- [[LLMToolingSkills]] - DSH discovers and loads task instructions that guide use of installed capabilities.
- [[GenerativeUI]] - a community plugin demonstrates generated interfaces whose saved state can inform a later turn.

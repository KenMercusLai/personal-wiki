---
title: "Qwen Code"
type: entity
tags: [ai, coding-agent, developer-tools, open-source]
sources:
  - using-local-coding-agents
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[QwenCode]] is an open-source command-line coding-agent harness from the Qwen ecosystem, used in the source as the primary client for locally served models.

## Current Profile
Qwen Code supplies the agent layer around an LLM: provider configuration, file and shell tools, approval controls, model switching, project context, and extensibility. It can connect to an Ollama endpoint through a custom OpenAI-compatible provider and is optimized with Qwen models in mind, but it can also serve other local models. The source's audit finds ordinary coding-agent authority and prompt-injection surfaces plus optional telemetry and update paths that must be configured explicitly for a stricter local-only posture.

## Key Characteristics
- Open-source harness whose installation artifacts can be compared with or built from reviewed source.
- Accepts custom OpenAI-compatible providers and multiple locally installed model identifiers.
- Exposes approval-gated shell execution and workspace file access typical of coding agents.
- Supports thinking mode, model switching, hooks, MCP servers, telemetry, usage statistics, updates, and artifact settings.
- Does not automatically outperform other harnesses when paired with a Qwen model in the source's small task pack.

## Evidence
- Model-harness optimization: [[using-local-coding-agents]] cites Qwen3.5-4B SWE-bench results favoring Qwen Code before Polar training.
- Local provider setup: [[using-local-coding-agents]] walks through Qwen Code's custom-provider protocol, Ollama base URL, placeholder API key, model IDs, and thinking mode.
- Security audit: [[using-local-coding-agents]] identifies command execution, file and secret scope, telemetry, network egress, hooks, MCP, prompt injection, and updates as review targets.
- Small benchmark: [[using-local-coding-agents]] reports 4/5 for Qwen3.6, North Mini Code, and Nemotron 3 Nano, and 1/5 for Gemma 4 E2B in Qwen Code.

## Qualifications
The audit is a practitioner review rather than an independent security assessment, and software behavior may change after the cited version. Disabling automatic updates reduces uncontrolled code change but also requires disciplined manual patching. The five-task benchmark is too small to establish a durable harness ranking, and its pass rate does not cover code quality, maintainability, or adversarial behavior.

## What Changed
- Added Qwen Code as an open-source local-model harness with configurable providers and privacy controls.
- Recorded the tension between model-specific optimization claims and the source's small cross-harness results.

## Relationships
- [[QwenTeam]] - research and model ecosystem associated with the harness.
- [[Ollama]] - local inference provider connected through an OpenAI-compatible endpoint.
- [[LocalCodingAgents]] - operating context in which Qwen Code supplies the agent layer.
- [[HarnessEngineering]] - Qwen Code's tools, prompts, context, and approvals shape end-to-end behavior.
- [[AgentPermissionModel]] - shell and file access are mediated through approval and configuration.
- [[Codex]] - open-source alternative harness that scored better and used fewer tokens in the source's small comparison.
- [[ClaudeCode]] - proprietary comparison harness with higher token use in the source's experiments.
- [[SebastianRaschka]] - practitioner who configured, audited, and benchmarked Qwen Code.

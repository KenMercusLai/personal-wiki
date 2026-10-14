---
title: "Sebastian Raschka"
type: entity
tags: [ai, machine-learning, technical-writing, evaluation]
sources:
  - using-local-coding-agents
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[SebastianRaschka]] is a machine-learning author and practitioner represented here through a tutorial and first-party evaluation of local open-weight coding-agent stacks.

## Current Profile
Raschka treats local coding agents as an engineering system rather than a model download. He combines hardware and runtime measurement, model and harness comparisons, a focused security audit, reproducible configuration, and a small personal task pack. He continues to use proprietary Codex and Claude Code as daily tools while presenting local models as controlled, inspectable, private, offline-capable alternatives and backups.

## Key Characteristics
- Explains machine-learning systems through implementation-oriented tutorials and visual comparisons.
- Evaluates local agent workflows across model, runtime, harness, hardware, security, and task-fit layers.
- Prefers hands-on personal benchmarks as a supplement to standardized leaderboards.
- Treats open-source inspectability and explicit configuration as practical trust mechanisms.
- States important limits around small samples, memory measurement, code quality, and proprietary-model advantages.

## Evidence
- Layered tutorial: [[using-local-coding-agents]] connects open-weight models, Ollama, and three coding harnesses into a complete local workflow.
- Measurement practice: [[using-local-coding-agents]] publishes scripts and charts for long-context speed, memory, tool reasoning, task success, and token use.
- Security practice: [[using-local-coding-agents]] audits Qwen Code before installation and proposes privacy-oriented settings plus isolated execution.
- Comparative restraint: [[using-local-coding-agents]] calls the five-task harness results small and explicitly separates correctness from code quality and readability.

## Qualifications
The profile is based on one tutorial and its self-run experiments. It does not independently validate the benchmark implementation, security audit, model claims, or hardware measurements, and it should not be generalized to all of Raschka's work.

## What Changed
- Added Raschka as the author and evaluator of the local coding-agent workflow.
- Recorded his combined emphasis on implementation, measurement, security review, and explicit limitations.

## Relationships
- [[LocalCodingAgents]] - subject of Raschka's tutorial and experiments.
- [[Ollama]] - runtime used to serve the tested local models.
- [[QwenCode]] - primary harness configured and audited in the tutorial.
- [[Codex]] - proprietary-model daily driver and open-source CLI used as a local-model harness.
- [[ClaudeCode]] - proprietary daily driver and comparison harness in the local experiments.

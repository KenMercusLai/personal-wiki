---
title: "Kuafu"
type: entity
tags: [ai, agents, runtime, personal-software]
sources:
  - xiang-zuo-xiang-you-leetao
last_updated: 2026-10-10
knowledge_schema: synthesis-v1
---

## Overview
[[Kuafu]] is [[Leetao]]'s experimental, channel-independent personal-agent runtime, named in tribute to agent projects and writing that influenced its design.

## Current Profile
Kuafu concentrates framework responsibility in a fixed perceive-think-decide-act-reflect state machine. Perception assembles context and routes Skills; the model produces structured output; decision logic applies stop or loop policy and guardrails; action invokes built-in tools or Skills; optional reflection records experience. A SQLite-plus-vector store holds tasks, messages, executions, lessons, and embeddings.

The project moved from a sandboxed Telegram setup with model routing toward a bridge that can invoke local coding CLI tools. Leetao then experimented with multiple agents by assigning implementation to one and review to another, while [[ToastPlan]] exposed tasks and AI activity for human observation.

## Key Characteristics
- Separates messaging channels from a compact execution, tool, and persistence kernel.
- Uses an explicit five-stage state machine with a policy and guardrail decision point.
- Records positive and negative task lessons alongside execution history and vectors.
- Bridges selected host CLI capabilities into an otherwise sandbox-oriented setup.
- Supports small multi-agent coding and review arrangements plus external task tracking.

## Evidence
- Runtime structure: [[xiang-zuo-xiang-you-leetao]] describes and diagrams the perceive-think-decide-act-reflect kernel and its store.
- Learning loop: [[xiang-zuo-xiang-you-leetao]] says failed and successful experience is preserved for later attempts.
- Host integration: [[xiang-zuo-xiang-you-leetao]] reports adding a bridge for Codex and other local CLI tools after earlier sandboxed experiments.
- Collaboration and oversight: [[xiang-zuo-xiang-you-leetao]] shows coding/review agents and ToastPlan task and audit interfaces.

## Qualifications
The available evidence is a first-person design reflection, not a repository audit or controlled evaluation. It does not quantify reliability, lesson-retrieval quality, security isolation, token cost, improvement across iterations, or comparative performance against one stronger model. The author explicitly questions whether framework changes transcend model limits and acknowledges that the branch metaphor may still describe linear execution.

## What Changed
- Created Kuafu's profile from Leetao's architecture, workflow, and product screenshots.

## Relationships
- [[Leetao]] - creator and operator of Kuafu.
- [[OpenClaw]] - product inspiration and comparison point for the experiment.
- [[Bub]] - studied agent project that influenced the design direction.
- [[GenerativeAIAgentArchitecture]] - supplies the broader model-runtime-tools-state frame Kuafu instantiates.
- [[AgentMemory]] - Kuafu's store persists executions and reusable lessons.
- [[AgentTeam]] - Kuafu can coordinate separate coding and review agents.
- [[ToastPlan]] - provides task integration and an operator-visible audit surface.

---
title: "Peter Steinberger"
type: entity
tags: [software-engineering, ai, developer-tools]
sources:
  - blog-peter-steinberger-shipping-at-inference-speed
  - openclaw-architecture-explained-how-it-works
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[PeterSteinberger]] is a software developer and the creator of [[OpenClaw]], represented in the wiki through both his high-throughput solo coding-agent workflow and a secondary account of OpenClaw's rapid early adoption.

## Current Profile
In the source, Steinberger presents himself as an experienced builder whose role has shifted away from typing and exhaustive code reading toward product direction, architecture, ecosystem and dependency choices, task dispatch, executable feedback, and deciding when an agent's result feels suspicious. He prefers [[Codex]] for large codebase changes, uses Claude Opus for much of his general computer automation, and builds many small command-line tools that expose services and devices to agents.

His workflow is deliberately personal: one main project and several satellite projects, queued ideas, short conversational prompts, durable documentation, reuse of patterns from neighboring repositories, long-running sessions, ad hoc refactoring, and usually direct commits to main. The source also shows a boundary to the speed narrative: concentrated context switching is tiring, system design and dependency selection still require thought, and more agent concurrency would not remove his own attention bottleneck.

The OpenClaw architecture article identifies Steinberger as the project's creator and describes him as the focal figure at an early February 2026 ClawCon event that reportedly drew more than 700 people. In that account, his contribution was not merely an agent loop but the product scaffolding around it: channel adapters, a Gateway control plane, persistent sessions, tool execution, memory, plugins, security policy, and deployment options. The event and adoption narrative is promotional, secondary, and not independently measured.

## Key Characteristics
- Treats coding agents as primary implementation workers while retaining a system-level map of each project.
- Optimizes projects and tools for agent legibility, direct execution, and fast feedback.
- Uses CLI-first development to make behavior easy for agents to invoke and verify.
- Iterates from hands-on product feel rather than expecting a complete specification upfront.
- Prefers a simple solo workflow over orchestration, worktrees, issue tracking, and pull-request overhead unless a task requires them.
- Created OpenClaw as a deployable personal-agent platform around model, channel, state, tool, and policy layers.

## Evidence
- Role shift: [[blog-peter-steinberger-shipping-at-inference-speed]] says Steinberger reads little generated code but tracks component structure, architecture, and system design.
- Agent preference: [[blog-peter-steinberger-shipping-at-inference-speed]] contrasts Codex's extended repository reading with Opus's faster, more eager editing style.
- Workflow design: [[blog-peter-steinberger-shipping-at-inference-speed]] describes queues, multiple concurrent projects, short prompts, cross-project references, durable docs, long sessions, and ad hoc cleanup.
- CLI-first loop: [[blog-peter-steinberger-shipping-at-inference-speed]] argues that agents can call text interfaces directly and verify their outputs.
- Remaining constraints: [[blog-peter-steinberger-shipping-at-inference-speed]] identifies architecture, dependencies, system boundaries, attention, and inference time as continuing bottlenecks.
- OpenClaw role: [[openclaw-architecture-explained-how-it-works]] identifies Steinberger as creator and attributes the platform's productization and early community momentum to his work.

## Qualifications
The coding-workflow profile comes from Steinberger's own retrospective rather than independent observation, while the OpenClaw account is an enthusiastic secondary article. Model comparisons, productivity outcomes, event attendance, adoption speed, and causal claims about productization are time-bound or anecdotal. The sources do not establish the long-term maintainability, security, defect rate, or team suitability of routinely reading little generated code, nor do they independently audit OpenClaw's implementation.

## What Changed
- Added Steinberger's role as OpenClaw creator and connected his product judgment to the platform's runtime scaffolding.
- Preserved a distinction between his first-person workflow evidence and the secondary article's event and adoption narrative.

## Relationships
- [[Codex]] - Steinberger's preferred coding agent for broad, long-running implementation and refactoring work.
- [[OpenAI]] - provider of the GPT and Codex systems central to the source.
- [[ClaudeCode]] - comparison point and part of the broader workflow history discussed in the source.
- [[VibeCoding]] - names the conversational, low-code-reading development mode Steinberger practices.
- [[AICodingPractice]] - frames the task design, context, verification, and ownership questions raised by his workflow.
- [[AutomationFriendlyCLI]] - supports his preference for agent-callable, text-first product surfaces.
- [[OpenClaw]] - personal-agent platform he created.

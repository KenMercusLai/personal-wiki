---
title: "Peter Steinberger"
type: entity
tags: [software-engineering, ai, developer-tools]
sources:
  - blog-peter-steinberger-shipping-at-inference-speed
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[PeterSteinberger]] is represented in the wiki as a software developer who uses coding agents to run a high-throughput, solo product-development workflow.

## Current Profile
In the source, Steinberger presents himself as an experienced builder whose role has shifted away from typing and exhaustive code reading toward product direction, architecture, ecosystem and dependency choices, task dispatch, executable feedback, and deciding when an agent's result feels suspicious. He prefers [[Codex]] for large codebase changes, uses Claude Opus for much of his general computer automation, and builds many small command-line tools that expose services and devices to agents.

His workflow is deliberately personal: one main project and several satellite projects, queued ideas, short conversational prompts, durable documentation, reuse of patterns from neighboring repositories, long-running sessions, ad hoc refactoring, and usually direct commits to main. The source also shows a boundary to the speed narrative: concentrated context switching is tiring, system design and dependency selection still require thought, and more agent concurrency would not remove his own attention bottleneck.

## Key Characteristics
- Treats coding agents as primary implementation workers while retaining a system-level map of each project.
- Optimizes projects and tools for agent legibility, direct execution, and fast feedback.
- Uses CLI-first development to make behavior easy for agents to invoke and verify.
- Iterates from hands-on product feel rather than expecting a complete specification upfront.
- Prefers a simple solo workflow over orchestration, worktrees, issue tracking, and pull-request overhead unless a task requires them.

## Evidence
- Role shift: [[blog-peter-steinberger-shipping-at-inference-speed]] says Steinberger reads little generated code but tracks component structure, architecture, and system design.
- Agent preference: [[blog-peter-steinberger-shipping-at-inference-speed]] contrasts Codex's extended repository reading with Opus's faster, more eager editing style.
- Workflow design: [[blog-peter-steinberger-shipping-at-inference-speed]] describes queues, multiple concurrent projects, short prompts, cross-project references, durable docs, long sessions, and ad hoc cleanup.
- CLI-first loop: [[blog-peter-steinberger-shipping-at-inference-speed]] argues that agents can call text interfaces directly and verify their outputs.
- Remaining constraints: [[blog-peter-steinberger-shipping-at-inference-speed]] identifies architecture, dependencies, system boundaries, attention, and inference time as continuing bottlenecks.

## Qualifications
The profile comes from Steinberger's own retrospective rather than independent observation. Its model comparisons and productivity outcomes are time-bound, anecdotal, and shaped by an expert solo developer's projects, risk tolerance, infrastructure, and ability to diagnose failures. The source does not establish the long-term maintainability, security, defect rate, or team suitability of routinely reading little generated code.

## What Changed
- Created a profile of Steinberger's agent-centered software-development practice.
- Established the tension between extreme implementation leverage and the continuing bottlenecks of judgment, attention, architecture, and verification.

## Relationships
- [[Codex]] - Steinberger's preferred coding agent for broad, long-running implementation and refactoring work.
- [[OpenAI]] - provider of the GPT and Codex systems central to the source.
- [[ClaudeCode]] - comparison point and part of the broader workflow history discussed in the source.
- [[VibeCoding]] - names the conversational, low-code-reading development mode Steinberger practices.
- [[AICodingPractice]] - frames the task design, context, verification, and ownership questions raised by his workflow.
- [[AutomationFriendlyCLI]] - supports his preference for agent-callable, text-first product surfaces.

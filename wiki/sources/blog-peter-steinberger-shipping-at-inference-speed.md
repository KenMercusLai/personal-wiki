---
title: "Shipping at Inference-Speed"
type: source
tags: [ai, software-engineering, codex, workflow, vibe-coding]
date: 2025-12-28
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Peter Steinberger - Shipping at Inference-Speed.md"
---

## Summary
[[PeterSteinberger]] describes a solo, expert [[VibeCoding]] workflow in which coding-agent capability has moved his bottleneck from typing toward inference time, product judgment, architecture, dependencies, and human attention. He favors [[Codex]] for long codebase-scale work, starts products with a model-accessible CLI, iterates conversationally, keeps durable project documentation, queues work across several projects, and relies increasingly on agent execution rather than line-by-line code reading. The account is strong evidence about one prolific practitioner's operating style, but its one-shot success, speed, and model-comparison claims are anecdotal and do not establish defect rates, maintainability, team suitability, or general productivity gains.

## Key Claims
- Mature coding agents can make inference time and hard design decisions more limiting than code production for an experienced solo developer.
- [[Codex]] is described as slower but more willing than Claude Opus to inspect a large codebase before editing, which can reduce corrective rework on broad features and refactors.
- Conversational exploration can replace a separate restricted planning mode when the agent can research, inspect code, propose a plan, and wait for an explicit build instruction.
- A text-first CLI closes the agent verification loop because the agent can invoke the product directly and inspect its output before a richer interface exists.
- Steinberger's workflow combines queued tasks, one main project plus satellite projects, cross-project examples, durable `docs/` context, long sessions with compaction, short prompts, and ad hoc cleanup.
- Agent-friendly codebase design shifts important human choices toward language, ecosystem, dependency quality, system boundaries, data flow, and verification rather than routine implementation.
- Parallel work and direct-to-main iteration fit Steinberger's solo practice, but he explicitly says the same approach would not work unchanged in a larger team.

## Key Quotes
> "The amount of software I can create is now mostly limited by inference time and hard thinking." - on the bottleneck shift in the author's workflow.

> "whatever you build, start with the model and a CLI first" - on making the first product surface directly usable by an agent.

> "usually I'm the bottleneck" - on why more elaborate multi-agent orchestration does not solve his main constraint.

## Connections
- [[PeterSteinberger]] - author and practitioner whose workflow the article documents.
- [[Codex]] - preferred coding agent for long-running, repository-scale implementation and refactoring.
- [[VibeCoding]] - the article presents an expert, low-code-reading form of fast conversational software creation.
- [[AICodingPractice]] - architecture, dependencies, documentation, verification, task shape, and cleanup remain human operating concerns.
- [[AutomationFriendlyCLI]] - CLI-first products give agents a directly callable and inspectable interface.
- [[LLMContextManagement]] - long sessions, codebase reading, durable docs, and compaction shape the workflow.
- [[SoftwareVerification]] - executable CLI output and agent-run checks are used to close implementation loops.
- [[OpenAI]] - provider of the GPT and Codex systems praised in the article.
- [[ClaudeCode]] - comparison point whose Opus-based workflow the author still values for smaller edits and general computer automation.

## Contradictions
- The routine of reading little generated code tensions [[HumanCodeResponsibility]] and review-centered accounts of [[AICodingPractice]]; architecture awareness and executable checks are not evidence that security, maintainability, or subtle behavior has been adequately reviewed.
- The preference for long conversations and successful compaction qualifies sources that recommend frequent session resets, but it is explicitly model- and version-dependent rather than a universal context-management rule.
- Direct commits to main, minimal checkpointing, and three-to-eight concurrent projects are framed as a solo-developer choice; the author says this workflow would not transfer unchanged to a larger team.
- The article reports striking one-shot outcomes, including a five-hour TypeScript-to-Zig conversion, without comparative task definitions, defect measurements, long-term maintenance evidence, or independent verification.

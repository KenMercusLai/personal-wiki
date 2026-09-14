---
title: "Vibe Coding"
type: concept
tags: [ai, software-engineering, developer-tools]
sources:
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - blog-guangzhengli-vibe-coding-and-context-coding
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[VibeCoding]] is an AI-assisted software work mode whose original Karpathy sense meant steering code almost entirely by conversation and visible results while barely reading or hand-editing the code; in broader wiki usage it also covers speed-amplified coding-agent workflows that need planning, context, review, and verification.

## Current Synthesis
The sources frame vibe coding as a real shift in software iteration speed and human role. The developer spends less time hand-writing boilerplate and more time setting direction, choosing task boundaries, managing context, reviewing generated changes, and verifying behavior. That speed is double-edged: it can make product iteration dramatically faster, but it can also create competitive pressure, overlarge diffs, shallow understanding, context failure, unhealthy pace, and delayed project risk unless paired with small steps, tests, planning, and explicit human judgment. The independent-developer example adds a concrete positive pattern: natural-language instructions can behave like code when they are precise enough about files, interfaces, data flow, UI behavior, and acceptance criteria.

The mihomo-rust source shows a heavier version of vibe coding for large systems. Instead of one fast conversation, agent acceleration is organized through role separation, specs, ADRs, memories, milestone resets, and full CI. In this mode, "vibe" is not improvisation; it is high-throughput implementation inside a deliberately designed harness.

Guangzhengli adds a naming correction. The article argues that many debates confuse Karpathy's original no-review, throwaway-project vibe coding with broader AI-assisted programming. For maintainable software, the better label is [[ContextCoding]]: developers still use AI heavily, but the important work is managing context, rules, retrieval, tools, debugging signals, and verification rather than surrendering code ownership.

## Key Claims
- Vibe coding's most visible effect is faster product iteration rather than only smarter models.
- Command-line agents can produce a deeper vibe-coding experience than editor-bound AI when they understand and modify whole projects.
- Planning is useful for existing systems and architecture-sensitive work, while exploratory prototypes may benefit from faster implementation-first loops.
- Small, reviewable iterations and fine-grained natural-language implementation instructions usually beat large uncontrolled generations because they preserve understanding and rollback ability.
- Context windows, compaction, and session boundaries become workflow constraints that must be actively managed.
- Verification, human pace, and reviewability matter: accelerated tools should not eliminate compilation, tests, linting, thinking time, formal roles, specs, CI, or production responsibility.
- Pure no-review vibe coding is especially risky for non-programmers deploying maintained products because security, subscription, API-key, database, and maintenance failures can arrive faster than the builder can understand them.

## Evidence
- Iteration speed: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] says AI-assisted development can compress product work from days to hours and intensify competition.
- Tool shape: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] argues that editor AI keeps attention near a file or selected lines, while command-line agents can build project-level understanding.
- Planning fit: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends Plan Mode for existing architecture and maintenance work, but allows faster prototyping when code quality and long-term maintenance matter less.
- Iteration control: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] reports that huge one-shot changes can become hard to inspect, debug, and salvage, while small steps aid control and learning.
- Risk postponement: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] argues that broad AI coding can leave developers with late-stage failures in code they cannot understand.
- Precise steering: [[du-li-kai-fa-zhe-fen-xiang-ai-coding-de-mi-jue-yi-huo-de-shou-quan]] shows prompts that name exact files, functions, callbacks, localization files, and reviewable change summaries.
- Context constraints: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] highlights context-window pressure, auto-compaction risk, subagents, task decomposition, plan documents, and new sessions as practical context-management tactics.
- Verification: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends compile-test-lint loops, TDD, cross-review, version control, and modular work.
- Human boundary: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] warns that tools should serve people rather than force unsustainable acceleration.
- Structured acceleration: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] uses Agent Team roles, spec documents, memory rules, milestone respawn, and layered tests for a large Rust port.
- Original meaning: [[blog-guangzhengli-vibe-coding-and-context-coding]] uses the inspected Karpathy screenshot to ground vibe coding in a no-review, conversational, result-steered workflow suitable mostly for throwaway weekend projects.
- Naming distinction: [[blog-guangzhengli-vibe-coding-and-context-coding]] argues that disciplined AI-assisted programming is better understood as [[ContextCoding]] than as vibe coding.
- Non-programmer risk: [[blog-guangzhengli-vibe-coding-and-context-coding]] uses Leo's March 2025 screenshots to show how a Cursor-built SaaS with no hand-written code quickly ran into API-key exhaustion, subscription bypass, database abuse, and shutdown.
- Expert leverage: [[blog-guangzhengli-vibe-coding-and-context-coding]] contrasts the Leo case with @levelsio's AI-built flight-simulator example, where the builder's prior programming experience made takeover and repair more plausible.

## Counterevidence & Qualifications
The sources are personal practitioner accounts rather than comparative studies. They also treat specific models and tools as strong in their moment, so some conclusions may depend on model quality, token allowances, pricing, language/domain coverage, and tool design. The term itself is unstable: some sources use vibe coding broadly for AI-assisted development, while Guangzhengli reserves it for a narrower no-review style and recommends [[ContextCoding]] for serious practice. Vibe coding is not presented as a replacement for exact IDE refactors, domain expertise, or human responsibility.

## What Changed
- Created the concept page for vibe coding as an agent-driven, speed-amplified software work mode with practical guardrails.
- Added the independent-developer source's risk-postponement warning and "Chinese as code" task-slicing pattern.
- Added a large-system variant where vibe-coding acceleration is structured through Agent Team and harness design.
- Added Guangzhengli's distinction between original no-review vibe coding and disciplined context coding.

## Related Concepts
- [[AICodingPractice]] - vibe coding needs disciplined norms for human judgment, review, and maintainability.
- [[AIAgentCollaboration]] - developers steer agents through planning, questioning, and feedback.
- [[SoftwareVerification]] - tests and execution checks make generated code accountable.
- [[LLMContextManagement]] - task splitting, subagents, session resets, and compaction timing protect agent reliability.
- [[AIFirstEngineering]] - both describe AI-centered software work, but vibe coding focuses on individual workflow experience.
- [[HarnessEngineering]] - harnesses formalize the checks and scaffolds that make fast agent work safer.
- [[AgentTeam]] - role separation is one way to scale vibe coding beyond a single agent conversation.
- [[ContextCoding]] - proposed label for serious AI-assisted programming where context, review, and verification remain central.

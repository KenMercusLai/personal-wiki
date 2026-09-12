---
title: "一个半月高强度 Claude Code 使用后感受"
type: source
tags: [ai, software-engineering, developer-tools, vibe-coding]
date: 2025-08-03
source_file: /mnt/ken_personal_wiki/Articles/一个半月高强度 Claude Code 使用后感受.md
---

## Summary
Onevcat reflects on a month and a half of intensive [[ClaudeCode]] use, arguing that command-line coding agents make [[VibeCoding]] feel qualitatively different from editor-bound AI tools because they can reason from project context, execute tasks, and support fast iteration. The article is enthusiastic about speed and broad utility, but repeatedly qualifies that speed with [[AICodingPractice]], [[AIAgentCollaboration]], [[SoftwareVerification]], and [[LLMContextManagement]] constraints: plan when useful, iterate in small steps, test constantly, manage context, and avoid letting the tool's acceleration consume human judgment or life.

## Key Claims
- [[VibeCoding]] primarily changes product iteration speed, but faster development also intensifies competition and can pressure developers into unhealthy pace.
- [[ClaudeCode]] differs from editor AI by operating from the command line, reading and changing whole projects, and reducing mid-task human micromanagement.
- [[AIAgentCollaboration]] should adapt to task uncertainty: use planning for existing codebases and architecture-sensitive work, but prototypes can benefit from faster exploratory implementation.
- [[AICodingPractice]] works best in small, reviewable iterations; large uncontrolled agent changes can become hard to understand, debug, or recover.
- [[LLMContextManagement]] is a practical constraint for coding agents because long sessions, auto-compaction, and large tasks can destabilize agent behavior.
- [[SoftwareVerification]] is non-negotiable: compile, test, lint, and use TDD or agent-verifiable checks wherever possible.
- [[ModelContextProtocol]], commands, hooks, subagents, worktrees, speech input, and project documentation can extend or discipline the coding-agent workflow.

## Key Quotes
> "千万别让工具把自己逼死" - on keeping human pace and judgment above tool speed.

> "小步迭代往往总是更好的选择" - on keeping AI-generated changes understandable and recoverable.

> "AI 生成的代码，未经测试都是废品" - on verification as a hard workflow boundary.

## Connections
- [[Onevcat]] - author/source account for the reflection.
- [[ClaudeCode]] - central tool being evaluated.
- [[VibeCoding]] - central working mode shaped by coding agents.
- [[AICodingPractice]] - the article gives practical norms for agent-assisted coding.
- [[AIAgentCollaboration]] - planning, questioning, and feedback are treated as part of agent work.
- [[SoftwareVerification]] - compilation, tests, linting, and TDD are presented as essential.
- [[LLMContextManagement]] - context windows, compaction, subagents, and task splitting shape reliability.
- [[ModelContextProtocol]] - MCP is recommended for adding external knowledge and tool integration.
- [[Anthropic]] - provider behind Claude Code and the usage-limit discussion.
- [[Claude]] - model family and assistant context for Claude Code.

## Contradictions
- No direct contradiction with existing wiki pages. The source qualifies optimistic [[AIFirstEngineering]] and [[AICodingPractice]] material by emphasizing small steps, human pace, context limits, and verification rather than pure acceleration.

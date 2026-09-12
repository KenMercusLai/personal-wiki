---
title: "用 Claude Code 将三万行 Go 项目移植到 Rust：Agent Team 实践与 Harness 效率优化"
type: source
tags: [ai, software-engineering, claude-code, rust, agent-team]
date: 2026-04-12
source_file: /mnt/ken_personal_wiki/Articles/用 Claude Code 将三万行 Go 项目移植到 Rust：Agent Team 实践与 Harness 效率优化.md
---

## Summary
This engineering case study describes using [[ClaudeCode]] and a four-role [[AgentTeam]] to port [[MihomoRust]] from a 30,000-line Go proxy core into a Rust workspace. It argues that large-scale AI coding becomes useful when surrounded by [[HarnessEngineering]]: dense `CLAUDE.md` guidance, file-system state, specs, ADRs, targeted memory, milestone resets, and a layered [[SoftwareVerification]] pipeline.

## Key Claims
- [[AgentTeam]] can split large coding-agent work into PM, Architect, Engineer, and QA roles with different model assignments and explicit file ownership.
- [[SpecDrivenAgentDevelopment]] turns documents into agent interfaces: ADRs settle architecture, specs define schemas and structs, and test plans verify implementation.
- [[HarnessEngineering]] for coding agents depends on concise project instructions, precise documentation references, explicit status fields, and file-system state rather than long inherited context.
- [[AgentMemory]] should store compact behavioral feedback such as "do not add CatchPanic" or `tokio::time::pause()` limits, not code conventions, git history, or temporary tasks.
- [[UpstreamDivergencePolicy]] helps a port decide whether upstream-compatible behavior should be preserved, warned about, or rejected as a hard error.
- [[SoftwareVerification]] is the only reliable quality gate for agent-produced code; the project used 619 test functions, 24 integration suites, Dockerized TProxy E2E tests, MSRV checks, and five CI jobs.
- The embedded diagrams add evidence about project scale and workflow: 31,178 Rust LOC across 11 crates, a four-role information-flow graph, a spec pipeline for the transport layer, a commit-velocity spike during the Agent Team sprint, a two-class divergence policy, and a five-layer testing pyramid.

## Key Quotes
> "ADR 决定架构（不可协商），spec 填充细节（可讨论），测试计划验证 spec" - on the document hierarchy used to coordinate agents.

> "上下文窗口是最稀缺的资源" - on why state is pushed into concise files and milestone resets.

> "看起来正确" 不等于 "运行正确" - on why tests, not appearance, decide whether agent work can merge.

## Connections
- [[ClaudeCode]] - central coding-agent tool used to coordinate the port.
- [[MihomoRust]] - Rust port and case-study project produced through the workflow.
- [[AgentTeam]] - central collaboration pattern in the source.
- [[SpecDrivenAgentDevelopment]] - document-driven pipeline used to coordinate PM, Architect, Engineer, and QA agents.
- [[HarnessEngineering]] - the source gives concrete harness levers for making agents useful in a large codebase.
- [[AICodingPractice]] - the source extends prior AI coding norms into multi-agent project operations.
- [[AIAgentCollaboration]] - collaboration occurs through roles, file-owned state, and handoffs rather than one engineer-agent pair.
- [[VibeCoding]] - the source shows a more structured, milestone-driven version of coding-agent acceleration.
- [[LLMContextManagement]] - the source treats context windows, stale state, and milestone respawns as core reliability constraints.
- [[AgentMemory]] - the source gives a narrow feedback-memory pattern for cross-session correction.
- [[UpstreamDivergencePolicy]] - ADR-0002's two-class policy structures porting decisions.
- [[SoftwareVerification]] - the source treats layered tests and CI as the merge boundary for agent work.
- [[MaxLv]] - author/site associated with the case study.
- [[Anthropic]] - provider context for Claude Code and its Opus/Sonnet/Haiku model roles in the source.

## Contradictions
- No direct contradiction with existing wiki content. The source qualifies earlier [[VibeCoding]] material by showing that very large AI coding work may need heavier role separation, documentation, and verification than a single-agent exploratory loop.

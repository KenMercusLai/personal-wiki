---
title: "谈谈 AI 编程工具的进化与 Vibe Coding"
type: source
tags: [ai, programming, vibe-coding, context-engineering, ai-tools]
date: 2025-08-28
source_file: "/mnt/ken_personal_wiki/Articles/Blog - guangzhengli - 谈谈 AI 编程工具的进化与 Vibe Coding.md"
---

## Summary
[[Guangzhengli]] argues that current arguments about [[VibeCoding]] blur two different practices: Karpathy-style no-review conversational coding for throwaway projects, and disciplined [[ContextCoding]] where AI tools are steered through codebase context, rules, retrieval, command-line search, MCP, and verification. The article traces [[GitHubCopilot]], [[Cursor]], and [[ClaudeCode]] as milestones in context engineering, then warns that production systems built by non-programmers through pure vibe coding can accumulate security flaws, maintainability failures, and hidden technical debt.

## Key Claims
- [[VibeCoding]] originally meant forgetting the code exists, accepting generated changes without review, and steering by result, which may fit throwaway projects but is a poor name for all AI-assisted programming.
- [[ContextCoding]] is a better frame for serious AI-assisted programming because improvements come from giving the LLM better context through open files, RAG indexes, rules, command-line search, MCP tools, documentation, and debugging signals.
- [[GitHubCopilot]] was a milestone because it first made IDE code context and cursor-local completion feel practical, but early versions were constrained by weaker models, small context, and limited editing ability.
- [[Cursor]] advanced AI coding through fast Tab completion, stronger models, direct code editing, project RAG, file and folder references, Git history indexing, documentation indexing, and rules.
- [[ClaudeCode]] can outperform editor-bound AI on larger multi-file work because it spends tokens more freely, inspects the project through Unix tools, and works from a more global command-line view.
- For coding agents, RAG and grep/search are complementary: semantic retrieval can help, but code association and business context often require precise live search over the current repository.
- Pure vibe coding can expose non-technical builders to production security, subscription-bypass, API-key, maintenance, and comprehension failures, while experienced developers can use AI leverage more safely because they can take over, review, and repair.

## Key Quotes
> "一种叫做 vibe coding，另外一种不管是叫 AI 辅助编程，AI Coding、Agents Coding 还是 Context Coding 都会更好一点。" - on separating no-review vibe coding from disciplined AI-assisted coding.

> "AI 辅助编程的所有提升都是基于给 LLM 传递更合适的上下文这个基本原理展开的" - on context as the core mechanism behind AI coding tools.

> "未来完整的 AI IDE 一定会提供 RAG + Grep 两种能力。" - on combining semantic retrieval with live code search.

## Connections
- [[Guangzhengli]] - author of the article and practitioner voice comparing AI coding tools.
- [[VibeCoding]] - central term the article narrows and critiques.
- [[ContextCoding]] - proposed alternative label for disciplined context-driven AI programming.
- [[GitHubCopilot]] - early milestone for IDE code context and cursor-local completion.
- [[Cursor]] - AI IDE milestone for Tab completion, codebase RAG, rules, and direct editing.
- [[ClaudeCode]] - command-line coding agent presented as especially strong for large multi-file tasks.
- [[AICodingPractice]] - the article gives practical norms for context files, small changes, debugging, and verification.
- [[LLMContextManagement]] - context engineering is the article's organizing explanation for AI coding progress.
- [[AgenticRAG]] - grep/read loops are defended as a current-code retrieval pattern.
- [[CodingAgentMinimalTooling]] - Unix search, file reading, and command-line tools are treated as a strong coding-agent substrate.
- [[HumanCodeResponsibility]] - production responsibility remains with the human, especially around security and maintainability.
- [[SoftwareVerification]] - tests, logs, debugging, and review are implied safeguards against fluent but unsafe output.
- [[AndrejKarpathy]] - source of the original vibe-coding post discussed by the article.

## Contradictions
- Qualifies broad [[VibeCoding]] usage by distinguishing Karpathy's original no-review, throwaway-project meaning from more disciplined AI-assisted coding.
- Partly tensions pure RAG-heavy [[Cursor]] framing by arguing that codebase semantic similarity is not enough for business-context retrieval, while still expecting future tools to combine RAG and grep/search.
- Reinforces existing [[AICodingPractice]] and [[HumanCodeResponsibility]] warnings: non-programmers can ship insecure systems faster than they can understand, debug, or maintain them.

## Image Evidence
- The Karpathy screenshot anchors the original February 2, 2025 meaning of vibe coding as fully giving in to conversational coding, forgetting the code exists, using Cursor Composer with Sonnet and voice input, accepting all changes, and treating it as amusing for throwaway weekend projects.
- The Claude Code `/context` screenshot shows a concrete context-budget view for `claude-sonnet-4-20250514`: 121k of 200k tokens used, with system prompt, system tools, MCP tools, messages, and free space broken out.
- The Leo screenshots show a short failure arc: on March 15, 2025 he claimed a paid SaaS was built with Cursor and no hand-written code; on March 17 he reported attacks, API-key exhaustion, subscription bypass, and database abuse; on March 20 he shut the app down and admitted he had deployed unsecured code.
- The @levelsio screenshots show a contrasting expert-leverage case: a multiplayer flight simulator built almost entirely with AI, Cursor, and Grok 3 using Python websockets and Three.js, later reported as reaching $87,000 MRR or $1 million ARR in 17 days with 320,000 players.

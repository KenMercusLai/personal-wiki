---
title: "Software Verification"
type: concept
tags: [software-engineering, testing, quality]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
  - 7-reasons-why-your-staging-environment-sucks-loadmill
  - 7-best-practices-for-doing-code-reviews
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SoftwareVerification]] is the practice of checking that software behavior actually works through tests, self-testing, execution, production-like environments, and repeatable validation loops.

## Current Synthesis
The sources introduce software verification through the specific risk of AI-generated code. Piglei focuses on the developer workflow: code review cannot expose every behavior issue, so engineers need automated tests and self-checks before asking others to review. The AI-first source raises the bar from local testing to production-speed verification: deterministic CI/CD, AI review, end-to-end tests, feature flags, staged rollout, monitoring, rollback, and post-deploy triage must make validation as fast as implementation. Onevcat adds the day-to-day coding-agent routine: compile after small features, run relevant tests, lint and format, use TDD when possible, and split work or use worktrees when verification latency becomes the bottleneck.

The mihomo-rust case study shows verification as the hard boundary that makes multi-agent code generation acceptable. Its layered test infrastructure spans unit, async, integration, protocol, E2E, and CI jobs, and the author treats full test-suite execution as non-negotiable before merging agent work.

The staging source broadens verification beyond code-level and CI feedback. Some bugs depend on production-like architecture, long runtimes, monitoring agents, realistic data, traffic, internet paths, and failure conditions, so a representative [[StagingEnvironment]] becomes a verification layer between localized tests and production exposure.

The same principle applies inside human code review: code reading is a weak substitute for actual execution. Running the app, using breakpoints, pulling the change into a realistic development environment, and seeing compile, warning, and test feedback all turn review from textual inspection into behavioral verification.

## Key Claims
- AI-generated code should be accompanied by automated tests and self-testing.
- Unverified code should not be handed to review as if review were the final safety net.
- Some bugs only appear through execution, so reviewers should run changes and inspect local compiler, warning, test, and runtime feedback instead of relying on diff reading alone.
- Later bug discovery raises repair cost.
- Agent-verifiable tests support a validation-fix loop that can improve iteration quality.
- Verification pipelines should continue through deployment, monitoring, rollback, and ticket closure, while staying close to each small change in coding-agent workflows.
- Production-like staging verifies behavior that depends on architecture, data, traffic, monitoring, internet exposure, and operational surprise.

## Evidence
- Testing expectation: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests and self-testing for AI-implemented code.
- Review limit: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says code review cannot find all problems.
- Execution evidence: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] notes that some issues only trigger when code actually runs.
- Cost timing: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] argues that bugs discovered later cost more to fix.
- Validation loop: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] encourages tests that allow agents to enter a verify-and-fix cycle.
- Pipeline verification: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes validation CI, environment deployment, development and production tests, release gates, and monitoring-backed rollback.
- Operational verification: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes production-health summaries, error triage, regression reopening, and automatic ticket closure after metrics confirm a fix.
- Local loop: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends recording build/test/lint commands in project instructions, compiling after each small feature, running relevant tests, and using TDD or worktrees when helpful.
- Layered test stack: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] reports 619 test functions, 24 integration suites, Dockerized TProxy E2E tests, MSRV checks, and CI jobs for lint, test, TProxy, MSRV, and macOS.
- Staging realism: [[7-reasons-why-your-staging-environment-sucks-loadmill]] argues that representative staging catches bugs missed by empty, short-lived, unmonitored, isolated, or inactive test environments.
- Review execution: [[7-best-practices-for-doing-code-reviews]] argues that reviewers should run the app, use breakpoints for complicated lifecycles, pull changes locally, and use compiler, warning, test, navigation, and whole-file context.

## Counterevidence & Qualifications
No source defines a universal testing strategy. The appropriate mix of unit tests, API tests, integration checks, end-to-end tests, static analysis, manual self-test, staging realism, staged rollout, and production monitoring depends on product risk, language, architecture, available observability, build latency, environment cost, and the cost of false positives or false negatives.

## What Changed
- Expanded software verification from pre-review tests and self-checks into a full AI-first delivery, observability, and rollback loop.
- Added the Claude Code source's local compile-test-lint habit loop for agent-generated changes.
- Added a large-port case where layered CI and E2E testing are the merge boundary for Agent Team output.
- Added representative staging as a verification layer for production-like conditions.
- Added code-review execution habits as a reviewer-side verification practice.

## Related Concepts
- [[CodeReviewPractice]] - code review can include execution-backed behavioral checks.
- [[AICodingPractice]] - verification is required to make AI-assisted changes trustworthy.
- [[HumanCodeResponsibility]] - tests help engineers demonstrate ownership of behavior.
- [[PRReviewHygiene]] - verification reduces the burden placed on later review.
- [[HarnessEngineering]] - verification infrastructure is a major part of the agent harness.
- [[AIFirstEngineering]] - AI-first work depends on verification moving as quickly as implementation.
- [[WorkHabits]] - repeatable validation loops are a disciplined work habit.
- [[VibeCoding]] - fast agent iteration raises the cost of weak verification.
- [[AgentTeam]] - QA role and CI state make verification a first-class agent-team responsibility.
- [[SpecDrivenAgentDevelopment]] - test plans verify whether specs were implemented.
- [[StagingEnvironment]] - realistic staging validates behavior that local tests may not exercise.
- [[ChaosEngineering]] - controlled failure injection verifies resilience under surprise.

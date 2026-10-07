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
  - duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
  - wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de
  - dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[SoftwareVerification]] is the practice of checking that software behavior actually works through tests, self-testing, execution, production-like environments, and repeatable validation loops.

## Current Synthesis
The sources introduce software verification through the specific risk of AI-generated code. Piglei focuses on the developer workflow: code review cannot expose every behavior issue, so engineers need automated tests and self-checks before asking others to review. The AI-first source raises the bar from local testing to production-speed verification: deterministic CI/CD, AI review, end-to-end tests, feature flags, staged rollout, monitoring, rollback, and post-deploy triage must make validation as fast as implementation. Onevcat adds the day-to-day coding-agent routine: compile after small features, run relevant tests, lint and format, use TDD when possible, and split work or use worktrees when verification latency becomes the bottleneck.

The mihomo-rust case study shows verification as the hard boundary that makes multi-agent code generation acceptable. Its layered test infrastructure spans unit, async, integration, protocol, E2E, and CI jobs, and the author treats full test-suite execution as non-negotiable before merging agent work.

The staging source broadens verification beyond code-level and CI feedback. Some bugs depend on production-like architecture, long runtimes, monitoring agents, realistic data, traffic, internet paths, and failure conditions, so a representative [[StagingEnvironment]] becomes a verification layer between localized tests and production exposure.

The same principle applies inside human code review: code reading is a weak substitute for actual execution. Running the app, using breakpoints, pulling the change into a realistic development environment, and seeing compile, warning, and test feedback all turn review from textual inspection into behavioral verification.

For multi-agent pipelines, verification topology becomes a reliability architecture. Deterministic checks such as tests, lint, type checks, and schemas create a low-cost floor, while LLM reviewers cover semantic gaps probabilistically and humans resolve intent or architectural ambiguity. The point is not that verification proves all correctness; it converts some misunderstanding failures into detectable stops, keeps downstream work from amplifying bad upstream artifacts, and lets recurring failures migrate into cheaper deterministic checks.

Software verification also has a behavioral-continuity layer. Verification is cheapest when the system has a fixed point: in one phase only tests move, in the next only implementation moves. [[DeterministicTesting]] and [[SnapshotTesting]] make the residual visible, while [[CoreRegressionTestSeparation]] keeps human attention on correctness-critical core cases and diff decisions rather than exhaustive review of every generated regression baseline.

For AI coding, verification can act like an "andon cord" that lets the workflow stop itself when generated code fails checks. Trust is therefore layered defense rather than belief in the generator. Lint, tests, E2E checks, logs, code review, and QA each have holes, but together they reduce the chance that a fluent near-miss travels downstream.

Ci Jian De Shan Lin moves the same bottleneck to infrastructure scale. When code generation becomes cheap and agent output volume exceeds human attention, sampled trust gives way to industrialized verification. The verification portfolio must also be heterogeneous: another related model may share the generator's blind spots, whereas compilers, theorem checkers, rules, databases, and real-world feedback provide differently sourced judgment. Complete traces then make residual errors auditable and attributable rather than merely observable.

## Key Claims
- AI-generated code should be accompanied by automated tests and self-testing.
- Unverified code should not be handed to review as if review were the final safety net.
- Some bugs only appear through execution, so reviewers should run changes and inspect local compiler, warning, test, and runtime feedback instead of relying on diff reading alone.
- Agent-verifiable tests support a validation-fix loop that can improve iteration quality.
- Verification pipelines should continue through deployment, monitoring, rollback, and ticket closure, while staying close to each small change in coding-agent workflows.
- Production-like staging verifies behavior that depends on architecture, data, traffic, monitoring, internet exposure, and operational surprise.
- Agent verification should combine deterministic and reality-anchored judges, probabilistic semantic review, layered human review, human oracle routing, residual-focused behavior baselines, and auditable traces rather than relying on one repeated check.

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
- Verification topology: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] summarizes Rothrock's gates across planning, design, file-level code review, and global code review.
- Deterministic ceiling: [[duo-agent-xie-zuo-ben-zhi-shi-fen-bu-shi-xi-tong-wen-ti-mo-xing-duo-qiang-ye-mei-yong]] says deterministic checks give hard guarantees only within their structural coverage, while semantic correctness still needs probabilistic review or human judgment.
- Residual loop: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends test-only and implementation-only phases so each failure has a clear likely cause.
- Behavior continuity: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] argues that broad regression tests need not prove correctness if they reliably expose behavior changes from the previous usable version.
- Test split: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] separates human-confirmed core tests from agent-generated snapshot-heavy regression tests.
- Andon loop: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] describes generate, verify, fix/log as the automatic stop-and-repair loop for AI-generated code.
- Layered trust: [[wei-shen-me-ai-xie-dai-ma-geng-kuai-dan-jiao-fu-mei-bian-yi-ji-wo-zen-me-ba-ta-ban-hui-lai-de]] uses the Swiss-cheese model to argue that lint, review, unit tests, E2E tests, QA, and human design judgment cover different failure classes.
- Verification bottleneck: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] argues that cheap machine-scale code generation shifts complexity and delivery capacity into build, test, validation, deployment, and operation.
- Correlated-review limit: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] warns that model-on-model self-review can pass averages while sharing systematic blind spots and failing in the tail.
- External judges: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] treats compilers, rules, theorem checkers, databases, and reality feedback as epistemic anchors outside model reasoning.
- Accountability: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] says high-volume verification needs complete auditability so errors can be proved, attributed, and reviewed after people leave the per-action loop.

## Counterevidence & Qualifications
No source defines a universal testing strategy. The appropriate mix of unit tests, API tests, integration checks, end-to-end tests, static analysis, manual self-test, LLM review, staging realism, staged rollout, production monitoring, residual snapshots, and human escalation depends on product risk, language, architecture, available observability, build latency, environment cost, semantic ambiguity, and the cost of false positives or false negatives. Multi-agent verification can harm liveness through retry storms, while snapshot-heavy regression can preserve wrong behavior unless paired with core tests and human judgment. “Heterogeneous” judges can still share specifications, training data, or upstream assumptions, and real-world feedback may arrive only after harm. Layered checks and audit trails reduce risk but do not decide acceptable error rates or remove human responsibility for architecture, intent, security, performance, and redress.

## What Changed
- Verification now spans local tests, execution-backed review, realistic staging, deployment gates, monitoring, rollback, and post-deploy confirmation.
- Agent workflows need cheap deterministic floors, probabilistic semantic review, and human oracle routing rather than repeated versions of one judge.
- Residual-focused tests and andon loops make behavioral changes visible and stop bad output before it accumulates downstream.
- Added external non-model judges and reality feedback as epistemic anchors against correlated model-review errors.
- Added complete auditability as the accountability layer required when agent volume exceeds per-action human review.

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
- [[TrustTopology]] - verification gates become an arrangement for agent reliability.
- [[OracleRouting]] - human escalation handles intent questions that checks cannot decide.
- [[AgentTDDResidual]] - alternates stable tests and stable implementation to make verification residuals reviewable.
- [[CoreRegressionTestSeparation]] - separates correctness-confirming tests from continuity-preserving regression coverage.
- [[DeterministicTesting]] - keeps test output stable enough for reliable residual review.
- [[SnapshotTesting]] - captures behavior baselines that expose unintended changes.
- [[BottleneckAwareAICoding]] - verification determines whether faster or parallel agent work can improve delivery throughput.
- [[AccountabilityInfrastructure]] - preserves verification evidence so autonomous actions and residual failures can be reconstructed and attributed.

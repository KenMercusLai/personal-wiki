---
title: "Software Verification"
type: concept
tags: [software-engineering, testing, quality]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[SoftwareVerification]] is the practice of checking that software behavior actually works through tests, self-testing, execution, and repeatable validation loops.

## Current Synthesis
The sources introduce software verification through the specific risk of AI-generated code. Piglei focuses on the developer workflow: code review cannot expose every behavior issue, so engineers need automated tests and self-checks before asking others to review. The AI-first source raises the bar from local testing to production-speed verification: deterministic CI/CD, AI review, end-to-end tests, feature flags, staged rollout, monitoring, rollback, and post-deploy triage must make validation as fast as implementation.

## Key Claims
- AI-generated code should be accompanied by automated tests and self-testing.
- Unverified code should not be handed to review as if review were the final safety net.
- Some bugs only appear through execution, so review alone is insufficient.
- Later bug discovery raises repair cost.
- Agent-verifiable tests support a validation-fix loop that can improve iteration quality.
- AI-first workflows need verification pipelines that continue through deployment, monitoring, rollback, and ticket closure.

## Evidence
- Testing expectation: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests and self-testing for AI-implemented code.
- Review limit: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says code review cannot find all problems.
- Execution evidence: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] notes that some issues only trigger when code actually runs.
- Cost timing: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] argues that bugs discovered later cost more to fix.
- Validation loop: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] encourages tests that allow agents to enter a verify-and-fix cycle.
- Pipeline verification: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes validation CI, environment deployment, development and production tests, release gates, and monitoring-backed rollback.
- Operational verification: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] describes production-health summaries, error triage, regression reopening, and automatic ticket closure after metrics confirm a fix.

## Counterevidence & Qualifications
Neither source defines a universal testing strategy. The appropriate mix of unit tests, API tests, integration checks, end-to-end tests, static analysis, manual self-test, staged rollout, and production monitoring depends on product risk, language, architecture, available observability, and the cost of false positives or false negatives.

## What Changed
- Expanded software verification from pre-review tests and self-checks into a full AI-first delivery, observability, and rollback loop.

## Related Concepts
- [[AICodingPractice]] - verification is required to make AI-assisted changes trustworthy.
- [[HumanCodeResponsibility]] - tests help engineers demonstrate ownership of behavior.
- [[PRReviewHygiene]] - verification reduces the burden placed on later review.
- [[HarnessEngineering]] - verification infrastructure is a major part of the agent harness.
- [[AIFirstEngineering]] - AI-first work depends on verification moving as quickly as implementation.
- [[WorkHabits]] - repeatable validation loops are a disciplined work habit.

---
title: "Software Verification"
type: concept
tags: [software-engineering, testing, quality]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[SoftwareVerification]] is the practice of checking that software behavior actually works through tests, self-testing, execution, and repeatable validation loops.

## Current Synthesis
The source introduces software verification through the specific risk of AI-generated code. Since code review cannot expose every behavior issue, engineers should build enough automated tests and self-checks for the agent and the human to verify results before review. Verification becomes a loop: run checks, inspect failures, fix, and rerun until the change has concrete behavioral evidence behind it.

## Key Claims
- AI-generated code should be accompanied by automated tests and self-testing.
- Unverified code should not be handed to review as if review were the final safety net.
- Some bugs only appear through execution, so review alone is insufficient.
- Later bug discovery raises repair cost.
- Agent-verifiable tests support a validation-fix loop that can improve iteration quality.

## Evidence
- Testing expectation: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests and self-testing for AI-implemented code.
- Review limit: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says code review cannot find all problems.
- Execution evidence: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] notes that some issues only trigger when code actually runs.
- Cost timing: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] argues that bugs discovered later cost more to fix.
- Validation loop: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] encourages tests that allow agents to enter a verify-and-fix cycle.

## Counterevidence & Qualifications
The source does not define a complete testing strategy for every project. The appropriate mix of unit tests, API tests, integration checks, manual self-test, and static analysis depends on risk, language, system design, and team conventions.

## What Changed
- Created the concept page for software verification as a necessary companion to AI-generated implementation.

## Related Concepts
- [[AICodingPractice]] - verification is required to make AI-assisted changes trustworthy.
- [[HumanCodeResponsibility]] - tests help engineers demonstrate ownership of behavior.
- [[PRReviewHygiene]] - verification reduces the burden placed on later review.
- [[WorkHabits]] - repeatable validation loops are a disciplined work habit.

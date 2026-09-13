---
title: "Core Regression Test Separation"
type: concept
tags: [software-engineering, testing, ai]
sources:
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[CoreRegressionTestSeparation]] is the practice of separating correctness-focused core tests from continuity-focused regression tests so human attention and agent-generated coverage serve different roles.

## Current Synthesis
The source distinguishes two kinds of tests in agent-heavy development. Core tests protect correctness: humans choose key paths, keep outputs small and clear, and confirm expected behavior. Regression tests protect continuity: agents can generate many cases, capture broad outputs or summaries, and preserve the behavior of the last usable version.

This separation makes snapshot-heavy regression testing less dangerous. Regression tests do not claim that every baseline is semantically correct; they claim that unexpected behavior changes should become visible as diffs. Human attention is then spent where it has leverage: reviewing core expected outputs, deciding whether a regression diff is acceptable, and promoting repeated regression diffs into stricter core tests.

## Key Claims
- Core tests are responsible for correctness because humans confirm their expected behavior.
- Regression tests are responsible for behavior continuity because they preserve the previous version's outputs or output summaries.
- Agent-generated regression tests can be valuable even when humans do not review every baseline line.
- Snapshot diffs route human attention to behavior changes rather than complete test suites.
- Repeated regression diffs are signals that a behavior deserves promotion into a stricter core test.
- A simple directory split such as `tests/core/` and `tests/regression/` can make review expectations executable.

## Evidence
- Core-test role: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says core tests cover key paths with clear outputs and human-confirmed expected results.
- Regression-test role: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says regression tests can be generated in bulk to freeze current behavior and expose later drift.
- Attention split: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] argues that core tests consume attention while regression tests mainly consume tokens.
- Diff-driven review: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says humans intervene when snapshot diffs appear and decide whether the change is intended.
- Promotion path: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends upgrading repeatedly changing regression cases into core tests with semantic assertions.

## Counterevidence & Qualifications
The source does not say regression tests replace correctness tests. Snapshot-heavy baselines can preserve wrong behavior, hide semantic errors behind shallow summaries, or create noisy review burden if outputs are not deterministic. The separation works only when teams keep the human-confirmed core suite strong and treat regression diffs as prompts for judgment rather than automatic truth.

## What Changed
- Created the concept page from the agent-era TDD source.

## Related Concepts
- [[AgentTDDResidual]] - residual-focused TDD uses this split to keep correctness and continuity distinct.
- [[SoftwareVerification]] - core and regression tests are complementary verification layers.
- [[SnapshotTesting]] - snapshots are the source's favored regression-test mechanism.
- [[DeterministicTesting]] - deterministic behavior keeps regression diffs actionable.
- [[CodeReviewPractice]] - review effort shifts from reading all baselines to evaluating important diffs and core assertions.
- [[HarnessEngineering]] - test separation is part of the harness around coding-agent work.

---
title: "Agent TDD Residual"
type: concept
tags: [ai, software-engineering, testing, tdd]
sources:
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[AgentTDDResidual]] is a coding-agent workflow that alternates test-only and implementation-only phases so humans inspect the residual behavior change instead of reviewing all generated code at once.

## Current Synthesis
The source presents residual-focused TDD as a response to the "homework submission" pattern of agent coding. If a developer gives an agent a large spec, receives a large implementation, then tries to review, replay, and repair it, the saved coding time can be lost in verification and rework.

The proposed alternative is to preserve one stable side of the system in each phase. In test-building mode, the implementation stays fixed and the agent adjusts tests until they accurately reflect the current working behavior. In implementation mode, the test harness stays fixed and the agent changes code until the behavior passes. The developer's scarce attention moves from full-code review to the changed residual: new requirements, test intent, key implementation spots, and snapshot diffs.

## Key Claims
- Agent-era development is limited less by code generation speed than by the cost of trustworthy verification.
- Alternating test-only and implementation-only phases creates a fixed point from the last usable version.
- When tests fail during test-building mode, the default diagnosis is that the test failed to describe current behavior.
- When tests fail during implementation mode, the default diagnosis is that the new implementation failed to preserve or extend required behavior.
- The human review target becomes the residual behavior change rather than all generated tests and code.
- The workflow depends on stable, deterministic feedback loops so the agent can self-correct cheaply.

## Evidence
- Bottleneck diagnosis: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says agent code generation can shift the bottleneck to code review, replay comparison, and confidence before release.
- Alternating rule: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] describes Mode A as test-only and Mode B as implementation-only, with the agent fixing the side allowed to move.
- Fixed point: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says the workflow reuses the fact that the previous version was usable as the continuity baseline.
- Review shift: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says developers still review key test examples and key implementation code, but avoid reviewing every generated line.
- Self-correction: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] treats failing tests as feedback the agent should use to revise either tests or implementation depending on phase.

## Counterevidence & Qualifications
The source is a practitioner workflow proposal rather than a controlled comparison with traditional TDD or other AI-coding processes. It assumes a codebase where deterministic tests and snapshot baselines can be built. It also does not remove the need for human correctness judgment: it reduces attention spent on broad generated artifacts, then concentrates that attention on residual diffs, core tests, and acceptance decisions.

## What Changed
- Created the concept page from the agent-era TDD source.

## Related Concepts
- [[SoftwareVerification]] - residual-focused TDD is a verification workflow for agent-generated code.
- [[AICodingPractice]] - the practice changes how engineers bound and review coding-agent work.
- [[HarnessEngineering]] - fixed tests, snapshots, and deterministic execution form the harness around the agent.
- [[CoreRegressionTestSeparation]] - core and regression tests divide correctness attention from continuity coverage.
- [[DeterministicTesting]] - deterministic outputs keep residual diffs meaningful.
- [[SnapshotTesting]] - snapshots provide the continuity baseline for many regression tests.
- [[CodeReviewPractice]] - residual review shifts attention away from full textual diff inspection.

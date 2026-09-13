---
title: "Agent 时代的 TDD：只关注行为的残差"
type: source
tags: [ai, software-engineering, testing, tdd]
date: 2026-01-12
source_file: /mnt/ken_personal_wiki/Articles/Agent 时代的 TDD：只关注行为的残差.md
---

## Summary
This article argues that coding agents move the software bottleneck from implementation speed to verification cost. It proposes [[AgentTDDResidual]]: alternate between test-only and implementation-only phases so the developer reviews behavioral residuals rather than the full generated code. The article separates [[CoreRegressionTestSeparation|core tests and regression tests]] so human attention remains on correctness-critical behavior while cheap agent-generated snapshots preserve behavior continuity.

## Key Claims
- Agent-generated code can make "submit homework" workflows slower overall because review, replay comparison, and rework become the bottleneck.
- [[AgentTDDResidual]] keeps test changes and implementation changes separate so each phase has a stable reference point and the agent can self-correct against it.
- The fixed point for agent-era TDD does not require perfect test correctness; it requires behavior continuity from the last usable version.
- [[DeterministicTesting]] is a prerequisite for residual-focused workflows because noisy outputs make snapshot diffs unusable.
- [[SnapshotTesting]] can turn large outputs, API contracts, schemas, edge cases, and logs into regression baselines that surface unintended behavior changes.
- [[CoreRegressionTestSeparation]] lets core tests consume human attention for correctness while regression tests consume tokens to preserve continuity and highlight diffs.

## Key Quotes
> "测试和实现，永远只改一边。" - on the central workflow rule.

> "验得起才是真的快" - on verification cost as the real speed limit.

## Connections
- [[AICodingPractice]] - the article adds a testing-centered workflow for keeping agent implementation reviewable.
- [[SoftwareVerification]] - verification cost, not code generation speed, is treated as the main agent-era bottleneck.
- [[HarnessEngineering]] - deterministic tests, snapshots, and residual review form a harness around coding-agent output.
- [[AgentTDDResidual]] - central workflow proposed by the source.
- [[CoreRegressionTestSeparation]] - the source's division between correctness-focused and continuity-focused tests.
- [[DeterministicTesting]] - needed so snapshot diffs reflect behavior rather than noise.
- [[SnapshotTesting]] - used as the low-attention mechanism for regression baselines.
- [[CodeReviewPractice]] - the article shifts human review from full diffs toward behavioral residuals.

## Contradictions
- No direct contradictions identified. The source qualifies broad AI-coding acceleration claims by arguing that code generation is only useful when verification feedback is cheap, stable, and reviewable.

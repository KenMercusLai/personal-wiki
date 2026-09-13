---
title: "Snapshot Testing"
type: concept
tags: [software-engineering, testing, regression]
sources:
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[SnapshotTesting]] is a testing technique that captures outputs or output summaries as versioned baselines, then fails when later runs differ from those baselines.

## Current Synthesis
The source uses snapshot testing as the practical mechanism for agent-generated regression coverage. Instead of requiring humans to hand-author and review every assertion over large outputs, the agent can dump stable outputs, API schemas, statistics, error types, log summaries, and edge-case behavior into snapshots. Later diffs reveal behavioral residuals that humans can inspect.

The technique is framed as continuity-oriented rather than correctness-complete. A snapshot can preserve imperfect behavior, but if the last version was usable, a changed snapshot still tells the team something important: behavior moved. Core tests and human judgment then decide whether that movement is intended, acceptable, or evidence of a regression.

## Key Claims
- Snapshot testing is useful when outputs are large, structured, or hard to review exhaustively.
- Snapshots can preserve behavior continuity even when they do not prove semantic correctness.
- Snapshot diffs make residual behavior changes visible to humans.
- Good snapshot targets include statistical summaries, API contracts, schemas, edge cases, error types, logs, shapes, dtypes, and boundary values.
- Snapshot testing works best when output determinism has already been controlled.
- In agent-heavy workflows, snapshots let tokens create broad regression coverage while humans judge only meaningful diffs.

## Evidence
- Large-output baselines: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] gives examples such as server-log aggregation, API response streams, and recommendation rankings.
- Python practice: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] mentions syrupy as a simple way to add Python snapshot tests.
- Statistical snapshots: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends snapshots of dataframe shape, dtypes, descriptions, quantiles, and index ranges.
- Contract snapshots: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends snapshotting API fields, types, null constraints, and error codes.
- Edge-case snapshots: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends agent-generated cases such as empty data, extreme ranges, disorder, duplicate keys, missing fields, and invalid encodings.

## Counterevidence & Qualifications
Snapshots can become noisy or misleading when outputs are nondeterministic, overly broad, or semantically shallow. The source therefore pairs snapshots with deterministic testing and core tests: snapshots expose continuity changes, but humans still decide correctness and should promote repeatedly important diffs into semantic assertions.

## What Changed
- Created the concept page from the agent-era TDD source.

## Related Concepts
- [[DeterministicTesting]] - stable output is the prerequisite for meaningful snapshot diffs.
- [[CoreRegressionTestSeparation]] - snapshots are mainly used for regression continuity rather than core correctness.
- [[AgentTDDResidual]] - snapshot diffs expose the residual behavior changes to review.
- [[SoftwareVerification]] - snapshots are one verification technique among tests, execution, staging, and review.
- [[HarnessEngineering]] - snapshots are a cheap feedback surface for coding agents.

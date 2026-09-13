---
title: "Deterministic Testing"
type: concept
tags: [software-engineering, testing, reliability]
sources:
  - agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[DeterministicTesting]] is the practice of making test runs produce stable outputs for the same relevant inputs so failures and diffs reflect real behavior changes rather than noise.

## Current Synthesis
The source treats deterministic testing as the foundation for residual-focused agent development. If outputs vary because of random seeds, unordered traversal, time access, concurrency, or environmental noise, snapshot diffs stop pointing to meaningful residuals and start consuming human attention.

For single-threaded programs, the source's practical advice is to fix random seeds, control unordered data iteration, and move system time behind explicit inputs or outer hooks. For concurrent systems, it notes that determinism is much harder and points toward specialized simulation or runtime tools, but the key claim remains the same: cheap agent verification requires stable feedback.

## Key Claims
- Deterministic output is required before snapshot diffs can serve as useful review artifacts.
- Test noise turns residual-focused workflows into attention sinks.
- Single-threaded determinism often depends on random seeds, ordered iteration, and explicit time inputs.
- Multi-threaded determinism is harder because scheduling and interleavings can create nondeterministic behavior.
- Deterministic testing supports agent self-correction because failures become repeatable.

## Evidence
- Snapshot prerequisite: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] says unstable outputs make snapshot diffs unmanageable.
- Randomness control: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends fixing random seeds.
- Ordering control: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] warns about unordered structures such as hash maps.
- Time control: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] recommends hooking timestamp access at the boundary and passing it as input.
- Concurrency qualification: [[agent-shi-dai-de-tdd-zhi-guan-zhu-xing-wei-de-can-cha]] notes that multi-threaded determinism requires more specialized techniques.

## Counterevidence & Qualifications
The source gives workflow advice, not a full taxonomy of deterministic testing techniques. Some systems deliberately include nondeterministic or probabilistic behavior; those systems may need statistical assertions, simulation, replay, seed capture, or narrower snapshot summaries rather than full output equality.

## What Changed
- Created the concept page from the agent-era TDD source.

## Related Concepts
- [[SnapshotTesting]] - snapshot tests depend on deterministic output.
- [[AgentTDDResidual]] - deterministic feedback makes residual review usable.
- [[CoreRegressionTestSeparation]] - regression tests need stable baselines to preserve continuity.
- [[SoftwareVerification]] - determinism improves the signal quality of verification.
- [[HarnessEngineering]] - deterministic execution is part of the agent test harness.

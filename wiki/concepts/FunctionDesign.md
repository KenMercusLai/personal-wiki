---
title: "Function Design"
type: concept
tags: [software-quality, python, programming]
sources:
  - bob-belderbos-10-tips-to-write-better-functions-in-python
  - do-one-thing
  - john-carmack-on-inlined-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[FunctionDesign]] is the practice of choosing function boundaries, names, inputs, outputs, state effects, and reuse surfaces so code remains understandable, testable, and safe in its actual execution context.

## Current Synthesis
Good function design begins with interface discipline: descriptive names, small argument surfaces, early validation, predictable returns, close variable placement, useful type information, and minimal hidden state. Small isolated functions often improve reuse and [[SoftwareVerification]], but neither size nor operation count establishes a good boundary.

“Do one thing” is an interpretive question about abstraction and change. Batchelder shows how a cohesive unit can later yield a better reusable abstraction; Carmack supplies the inverse pressure. In sequential, mutation-heavy real-time code, a single-use helper can hide execution order, skipped updates, latency, and global dependencies. Keeping that work visible in the controlling path may improve system-level reasoning even when it produces a long function.

The strongest reconciliation is to separate pure computation from orchestration. Extract work that can accept explicit inputs and return a value without permanent-state mutation; keep essential ordering and mutation visible enough that readers can see when state changes and whether expected work runs. Function boundaries should therefore be selected by coherence, reuse, testing, state visibility, execution order, and change isolation rather than a universal line limit.

## Key Claims
- Function names and explicit input-output contracts are major readability and tooling surfaces.
- Hidden global state and mutable defaults make behavior depend on context and prior execution.
- Small pure functions usually improve reuse, testing, and local reasoning.
- “One thing” has no objective operation-count or line-count test; boundaries can change as reuse and understanding evolve.
- Single-use stateful helpers can reduce [[ExecutionPathTransparency]] by hiding ordering, latency, and skipped updates.
- Pure computation and stateful orchestration often deserve different decomposition strategies.

## Evidence
- Interface discipline: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] recommends descriptive names, small argument lists, early validation, clear calling conventions, type hints, and consistent returns.
- State hazards and testability: [[bob-belderbos-10-tips-to-write-better-functions-in-python]] warns against globals and mutable defaults while connecting isolated functions to easier testing.
- Boundary ambiguity: [[do-one-thing]] shows that operation count, stakeholder count, and reasons to change do not mechanically define one responsibility.
- Evolutionary extraction: [[do-one-thing]] uses Zellij's `PointMap`-to-`Defuzzer` refactoring to show how new reuse needs can reveal a smaller abstraction.
- Stateful counterpressure: [[john-carmack-on-inlined-code]] argues that single-use helpers in a frame loop can conceal sequence, mutation, conditional skipping, and latency.
- Pure-function reconciliation: [[john-carmack-on-inlined-code]] recommends explicit parameters, `const`, and complete purity for work that can avoid permanent state.

## Counterevidence & Qualifications
All three sources provide practitioner heuristics rather than comparative defect or maintenance studies. Inlining can create very long functions, weaken modularity, complicate shared work and rebuilds, and make large conditional blocks harder to scan. Conversely, aggressive decomposition can scatter one stateful sequence across call layers. Performance, API stability, framework conventions, code ownership, power use, testing strategy, and team familiarity can all change the preferred boundary.

## What Changed
- Added the counterpressure that single-use stateful helpers may hide important execution order and mutation.
- Reconciled small-function advice with long sequential orchestration by favoring pure extraction and visible state transitions.
- Removed any implication that function length alone determines design quality.

## Related Concepts
- [[InternalSoftwareQuality]] - function boundaries affect readability, maintenance cost, and defect localization.
- [[SoftwareVerification]] - explicit, isolated computations are easier to test and reason about.
- [[SingleResponsibilityPrinciple]] - supplies a useful but interpretation-dependent boundary heuristic.
- [[ExecutionPathTransparency]] - stateful orchestration benefits when ordering and mutations remain inspectable.
- [[FunctionalProgramming]] - purity provides a safer reusable boundary than stateful helper extraction.
- [[DeveloperTooling]] - type hints and explicit interfaces give tools more structure to inspect.

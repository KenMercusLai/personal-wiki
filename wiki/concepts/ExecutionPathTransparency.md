---
title: "Execution Path Transparency"
type: concept
tags: [software-quality, control-flow, reliability, real-time-systems]
sources:
  - john-carmack-on-inlined-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ExecutionPathTransparency]] is the degree to which a reader can see what work executes, in what order, under which conditions, and with which state changes along a consequential control path.

## Current Synthesis
Carmack argues that transparency matters especially in recurring real-time loops, where deeply nested helpers and conditional execution can hide work, skip required state updates, add a frame of latency, or make average timing look better while worsening variance. Source-level inlining of a single-use stateful helper is one way to expose sequence and mutation, but it is not the goal by itself and is not a function-call performance optimization.

The broader design pattern is to make orchestration visible while extracting pure computation. Work expected every frame can be placed near the outer loop; mutations can be consolidated at controlled points; large sections can use comments and lexical scopes; and reusable calculations can become pure functions with explicit inputs. Consistent execution followed by inhibiting or ignoring results can further simplify paths, though its time, energy, and thermal costs make it conditional.

## Key Claims
- Visible execution order helps expose repeated assignments, skipped work, and latency-producing sequence errors.
- Deep helper chains and implicit C++ behavior can conceal performance and stability costs even when local functions appear readable.
- Doing expected work consistently can reduce timing variance and conditional-state bugs.
- Centralizing a mutation decision can be safer than exposing one stateful operation to many callers.
- Pure functions preserve modularity without hiding permanent-state changes.
- Code duplication remains a greater risk than most call-context problems, so inlining should not create copied implementations.

## Evidence
- Ordering and latency: [[john-carmack-on-inlined-code]] connects nested frame operations to barely perceptible input lag and visibly trailing attachments, then reports a later near-ship one-frame input-latency bug.
- Conditional state risk: [[john-carmack-on-inlined-code]] says skipped expensive operations often also skipped state updates required elsewhere.
- Controlled mutation: [[john-carmack-on-inlined-code]] contrasts one health-state check with a stateful `KillPlayer()` call exposed across many sites.
- Inlining experiment: [[john-carmack-on-inlined-code]] reports that flattening Armadillo Aerospace's main tick exposed repeated assignments and questionable control flow while reducing code.
- Pure extraction: [[john-carmack-on-inlined-code]] identifies functions that read explicit inputs and return values without permanent-state mutation as safe reusable units.

## Counterevidence & Qualifications
The evidence is one experienced practitioner's account rather than a controlled comparison. Long functions can overwhelm readers, large conditionals and loops can remain clearer as named helpers, and modularity protects ownership and abstraction boundaries. Always-execute strategies consume more absolute time and can be inappropriate on mobile or other power- and thermal-constrained systems. The Saab Gripen defect claim is secondhand and should not be treated as verified proof that forward-only code eliminates bugs.

## What Changed
- Created the concept from Carmack's reliability rationale for visible sequential execution.

## Related Concepts
- [[FunctionDesign]] - choosing a function boundary changes how much ordering and mutation remain visible.
- [[FunctionalProgramming]] - pure extraction removes hidden dependencies without obscuring state changes.
- [[InternalSoftwareQuality]] - execution awareness can improve debugging and reduce surprise during change.
- [[SoftwareVerification]] - explicit control and data flow can make testing and review more tractable.
- [[ProgrammerInterruptionRecovery]] - visible orchestration can reduce the context needed to reconstruct a running path.

---
title: "Functional Programming"
type: concept
tags: [programming, software-quality, state-management]
sources:
  - john-carmack-on-inlined-code
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[FunctionalProgramming]] is represented here as structuring computation around explicit inputs and returned values while minimizing hidden dependencies and mutation of persistent state.

## Current Synthesis
Carmack's 2014 commentary presents purity as the more direct and complete answer to the problem his 2007 inlining advice targeted: unexpected dependency and state mutation. A function that reads only its arguments and returns a value can be reused without relying on an assumed global execution environment, while stateful orchestration remains visible at the call site.

The source supports a pragmatic rather than absolute boundary. Code that references only a small amount of global state should consider receiving it as an argument; `const` can expose unexpected mutation paths; and lightweight helpers should be made purely functional where reasonable. Carmack's earlier concern that whole-program purity could become obscure or inefficient remains part of the historical record, but his later note says he became much more favorable to functional programming even in C and C++.

## Key Claims
- Purity directly removes hidden global dependencies and permanent-state mutation from a function.
- Explicit parameters make a function's operating context more visible to callers and reviewers.
- Reusable computation is safer when separated from stateful orchestration.
- `const` can reveal mutation paths, although casts and global access can weaken the guarantee.
- Carmack's 2014 position is more favorable to functional techniques than the 2007 email it annotates.

## Evidence
- Direct remedy: [[john-carmack-on-inlined-code]] says functional programming solves unexpected dependency and state mutation more directly than inlining.
- Safe reuse: [[john-carmack-on-inlined-code]] describes argument-only, value-returning functions without permanent-state mutation as safe from call-context state errors.
- Explicit dependencies: [[john-carmack-on-inlined-code]] recommends passing limited global state as parameters and using `const` where functions must be shared.
- Position change: [[john-carmack-on-inlined-code]] preserves Carmack's 2007 skepticism while adding his 2014 statement that he had become much more bullish on pure functional programming.

## Counterevidence & Qualifications
This is one programmer's conceptual and experiential account, not evidence comparing functional and imperative systems. The source does not define observational purity rigorously, benchmark the claimed inefficiencies, or cover effects, immutable data structures, functional languages, concurrency, or large-scale architecture. C and C++ `const` do not by themselves prevent global reads or all external effects.

## What Changed
- Created the concept from Carmack's revised judgment that purity better addresses hidden dependency and mutation than inlining alone.

## Related Concepts
- [[FunctionDesign]] - pure inputs and outputs provide a strong reusable function boundary.
- [[ExecutionPathTransparency]] - pure extraction can simplify orchestration while leaving state changes visible.
- [[InternalSoftwareQuality]] - reduced hidden state can make behavior easier to reason about and test.
- [[SoftwareVerification]] - explicit dependencies and deterministic value computation support focused checks.

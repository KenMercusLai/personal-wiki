---
title: "John Carmack on Inlined Code"
type: source
tags: [programming, code-style, inlining, game-development]
date: 2007-03-13
source_file: "/mnt/ken_personal_wiki/Articles/John Carmack on Inlined Code.md"
---

## Summary
[[JohnCarmack]] argues that sequential, stateful work can be easier to reason about when its execution order and mutations remain visible in one controlling function rather than being hidden behind layers of helpers. His 2014 preface narrows the 2007 advice: [[FunctionalProgramming]] addresses unexpected dependencies and mutation more directly, while inlining remains a situational technique for state-heavy real-time loops. The article connects visible control flow, consistent per-frame execution, copy-paste avoidance, and pure-function extraction to reliability rather than to function-call performance.

## Key Claims
- [[ExecutionPathTransparency]] can reduce hidden ordering, skipped-update, latency, and state-assumption bugs in sequential real-time code.
- A function called from only one place is a candidate for source-level inlining, but modularity, repeated use, large conditionals, build effects, and object boundaries can justify keeping it separate.
- Work expected every frame may be safer in an outer loop; executing consistently and inhibiting or ignoring results can reduce control-flow bugs and timing variance, though it consumes more power and time.
- [[FunctionalProgramming]] and explicit inputs are safer extraction boundaries because pure functions avoid hidden global dependencies and permanent-state mutation.
- Consolidating mutation at one controlled point can be safer than exposing an operation such as `KillPlayer()` to many callers with different state assumptions.
- Explicit loops can be less error-prone than copy-paste-modify sequences, which Carmack says repeatedly produced subtle indexing mistakes.

## Key Quotes
> "The function that is least likely to cause a problem is one that doesn't exist" - on eliminating a single-use stateful helper by inlining it.

> "If the work is close to purely functional, with few references to global state, try to make it completely functional." - on the preferred boundary for reusable functions.

## Connections
- [[JohnCarmack]] - author of the 2007 email and 2014 qualifying commentary.
- [[IdSoftware]] - game-development setting for the frame-loop, latency, and state-management examples.
- [[FunctionDesign]] - the source challenges small-function rules when decomposition hides sequential stateful behavior.
- [[ExecutionPathTransparency]] - central reliability rationale for exposing execution order and mutations.
- [[FunctionalProgramming]] - later-preferred way to remove unexpected dependencies and state mutation.
- [[InternalSoftwareQuality]] - the proposed style targets debugging awareness, reliability, and change safety.
- [[SoftwareVerification]] - the Saab Gripen anecdote and Carmack's testing concerns motivate inspectable control and data flow.

## Contradictions
- Qualifies [[bob-belderbos-10-tips-to-write-better-functions-in-python]]: small isolated functions improve reuse and testing, but Carmack argues that stateful single-use helpers can hide ordering and mutation that matter more than local size.
- Carmack's 2014 preference for functional techniques qualifies his own 2007 skepticism about functional programming and narrows inlining to code that still performs substantial mutation.
- The Saab Gripen flight-software claim is explicitly recalled secondhand through Henry Spencer, and the article supplies no primary program record or comparative defect data.
- The execute-and-inhibit strategy can improve reliability and timing consistency but is less suitable for power- and thermal-constrained systems such as mobile devices.
- The supplied Markdown contains no effective image references.

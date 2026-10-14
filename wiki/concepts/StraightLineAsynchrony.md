---
title: "Straight-Line Asynchrony"
type: concept
tags: [async-await, concurrency, programming-languages, semantics]
sources:
  - 2608.20677
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[StraightLineAsynchrony]] is asynchronous programming expressed in direct, sequential-looking control flow through constructs such as asynchronous functions and `await`, with the language or runtime managing the underlying continuations and scheduling.

## Current Synthesis
Shared `async`/`await` vocabulary does not define a portable semantic contract. A computation may begin lazily, execute immediately on the calling thread, or merely be scheduled; an `await` may always yield or only yield when its operand is incomplete. Task lifetime then depends separately on scope, reachability, runtime reference strength, scope-exit cleanup, and failure propagation.

Cancellation is likewise not one operation. A runtime may let the cancelled task observe the request or simply stop rescheduling it, propagate cancellation top-down, bottom-up, or simultaneously through a dependency graph, and treat the request as transient or persistent. These choices determine whether cleanup can run, whether child work survives a parent, and whether an apparently handled cancellation reappears at later suspension points.

## Key Claims
- Surface similarity across `async`/`await` languages conceals distinct execution-order and operation-presence guarantees.
- Start-of-life semantics comprise both function-call eagerness and whether `await` is guaranteed to suspend.
- End-of-life semantics comprise task extent, runtime reference strength, destruction policy, and propagation of unawaited failures.
- Cancellation must be described through awareness, direction, and persistence rather than as a single binary feature.
- Structured task lifetime does not by itself determine whether children are awaited or cancelled or whether their failures propagate.
- Formal comparison can expose different semantic paths that happen to produce the same visible output.

## Evidence
- Cross-runtime divergence: [[2608.20677]] reports distinct combined output profiles for seven runtime combinations on three small programs.
- Nine-axis taxonomy: [[2608.20677]] separates eagerness and suspension; extent, reference strength, destruction, and propagation; and cancellation awareness, direction, and persistence.
- Cancellation safety: [[2608.20677]] shows that an aware task can restore an invariant in cleanup code, whereas unaware cancellation can leave it broken.
- Formal correspondence: [[2608.20677]] provides executable Redex models, example suites, and differential fuzzing against real runtimes.

## Counterevidence & Qualifications
The taxonomy emphasizes semantic functionality rather than syntax, ergonomics, or runtime implementation performance. Its principal table covers JavaScript, C#, Swift, Python with Asyncio or Trio, and Rust with Tokio or Smol; configurable C++20, Kotlin's implicit suspension style, and Zig's evolving I/O-parametric design are not assigned complete profiles. The work establishes differences and design rationales, not which alternatives minimize defects or best match developer intuition.

## What Changed
- Established a nine-dimension vocabulary for comparing the full lifecycle of direct-style asynchronous computations.
- Separated structured task extent from destruction and failure-propagation policy.
- Added cancellation awareness, graph direction, and persistence as independent safety and liveness choices.

## Related Concepts
- [[StructuredConcurrency]] - imposes explicit lifetime structure on tasks but leaves other async design dimensions open.
- [[ConcurrentProgramming]] - straight-line asynchrony is a cooperative form of concurrent execution.
- [[ConcurrencyFailureModes]] - starvation, leaked work, ignored failures, and broken invariants arise from particular semantic choices.
- [[RaceCondition]] - interleaved async execution can make operation ordering observable even without physical parallelism.

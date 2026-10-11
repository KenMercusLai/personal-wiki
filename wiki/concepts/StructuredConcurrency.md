---
title: "Structured Concurrency"
type: concept
tags: [concurrency, cpp, cancellation, software-architecture]
sources:
  - agent-shi-dai-de-clice
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[StructuredConcurrency]] is a concurrency discipline that binds asynchronous task lifetime, parent-child relationships, and cancellation propagation to an explicit structure rather than leaving detached work to ad hoc ownership.

## Current Synthesis
The clice case begins with a thin C++20 coroutine wrapper over libuv. Syntax improved, but dynamic tasks still required manual detach, release, and deletion-like lifetime management, and complex cancellation paths became difficult to maintain. This matters in a C++ language server because superseded edits can leave expensive parses occupying a worker pool, while module builds introduce dependency graphs in which changing one import should cancel an obsolete cascade rather than only one leaf task.

The replacement framework models all work as one asynchronous graph with strict parent-child lifetime. A task carries normal, error, and cancellation channels as `<T, E, C>`: errors remain explicit, while cancellation propagates implicitly through the structure. The inspected graph shows tasks and task groups connected through `WhenAll` nodes and synchronization resources including mutexes, semaphores, events, condition variables, system I/O, and their waiters. Exporting this live graph makes the ownership and waiting topology available for debugging as well as execution.

## Key Claims
- Coroutine syntax alone does not structure the lifetime or cancellation of asynchronous work.
- Superseded expensive tasks should be cancelled rather than merely have their eventual result dropped when background work can exhaust scarce workers.
- Parent-child task structure can unify lifetime management with cancellation propagation.
- Error and cancellation are distinct outcomes: a task can expose explicit error flow while cancellation travels through its containing graph.
- Dependency-shaped work such as C++20 module compilation requires cascade behavior across more than one task.
- Exportable task graphs can turn hidden waits and synchronization relationships into debuggable runtime state.

## Evidence
- Failure of thin wrapping: [[agent-shi-dai-de-clice]] reports that coroutine-wrapped libuv retained manual dynamic lifetime management and difficult async bugs.
- Superseded parse case: [[agent-shi-dai-de-clice]] explains how an obsolete 100,000-line edit can continue consuming compiler threads if cancellation is unsupported.
- Dependency cancellation: [[agent-shi-dai-de-clice]] uses a changed C++20 module import to show why an obsolete dependency cascade must be cancelled coherently.
- Outcome model: [[agent-shi-dai-de-clice]] describes `task<T, E, C>` with normal value, error, and cancellation channels and strict parent-child lifetime.
- Diagram evidence: [[agent-shi-dai-de-clice]] retains an exported graph containing task groups, `WhenAll`, synchronization resources, waiters, and directional task relationships.

## Counterevidence & Qualifications
The evidence describes one custom C++ framework rather than comparing structured-concurrency implementations or proving a universal API design. The graph demonstrates observability but not cancellation latency, absence of leaks, deadlock freedom, fairness, or performance under load. Simpler language servers with cheap parsing may reasonably drop stale results without interrupting computation, and explicit versus implicit propagation choices depend on language semantics and failure policy.

## What Changed
- Created the concept from clice's cancellation-first C++20 coroutine redesign and inspected runtime graph.

## Related Concepts
- [[ConcurrentProgramming]] - structured concurrency adds lifetime and cancellation discipline to concurrent task execution.
- [[ConcurrencyFailureModes]] - leaked work, saturated worker pools, and tangled synchronization motivate explicit structure.
- [[Clice]] - applies the model to language-server requests and compilation dependencies.
- [[Kotatsu]] - packages the reported implementation in its async module.
- [[InterprocessCommunication]] - clice combines structured task control with worker-process isolation and messaging.

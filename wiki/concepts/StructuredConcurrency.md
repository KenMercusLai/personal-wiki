---
title: "Structured Concurrency"
type: concept
tags: [concurrency, cpp, cancellation, software-architecture]
sources:
  - agent-shi-dai-de-clice
  - 2608.20677
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[StructuredConcurrency]] is a concurrency discipline that binds asynchronous task lifetime and parent-child relationships to explicit scopes or dependency structure rather than leaving detached work to ad hoc ownership.

## Current Synthesis
Structured concurrency primarily constrains task extent: child work is tied to the scope or lifetime of a parent instead of surviving indefinitely by default. That structure improves ownership, resource safety, composition, and observability, but it does not fully specify scope-exit behavior. Swift cancels and awaits child tasks while suppressing unawaited failures; Trio awaits children without first cancelling them and propagates their failures. Destruction and exception propagation therefore remain independent design choices.

The clice case extends the idea from strict scope trees toward an explicit asynchronous dependency graph. Its task type distinguishes normal, error, and cancellation outcomes, propagates cancellation through parent-child structure, and exposes synchronization relationships for debugging. This is operationally important when obsolete parses can exhaust worker pools or module changes should cancel a dependency cascade, though the implementation remains one custom C++ system rather than comparative evidence.

## Key Claims
- Coroutine syntax alone does not structure the lifetime or cancellation of asynchronous work.
- Dynamic task extent binds child lifetime to a parent scope and prevents unaccounted work from surviving by default.
- Structured lifetime does not uniquely determine whether scope exit awaits or cancels children or whether child failures propagate.
- Superseded expensive tasks should be cancelled rather than merely have their eventual result dropped when background work can exhaust scarce workers.
- Parent-child task structure can unify lifetime management with cancellation propagation.
- Error and cancellation are distinct outcomes: a task can expose explicit error flow while cancellation travels through its containing graph.
- Exportable task graphs can turn hidden waits and synchronization relationships into debuggable runtime state.

## Evidence
- Comparative semantics: [[2608.20677]] classifies Swift and Trio as dynamic-extent systems but shows that their destruction and failure-propagation policies differ.
- Resource boundary: [[2608.20677]] argues that dynamic extent prevents child work from continuing to use resources after its containing scope cleans them up.
- Failure of thin wrapping: [[agent-shi-dai-de-clice]] reports that coroutine-wrapped libuv retained manual dynamic lifetime management and difficult async bugs.
- Superseded parse case: [[agent-shi-dai-de-clice]] explains how an obsolete 100,000-line edit can continue consuming compiler threads if cancellation is unsupported.
- Dependency cancellation: [[agent-shi-dai-de-clice]] uses a changed C++20 module import to show why an obsolete dependency cascade must be cancelled coherently.
- Outcome model: [[agent-shi-dai-de-clice]] describes `task<T, E, C>` with normal value, error, and cancellation channels and strict parent-child lifetime.
- Diagram evidence: [[agent-shi-dai-de-clice]] retains an exported graph containing task groups, `WhenAll`, synchronization resources, waiters, and directional task relationships.

## Counterevidence & Qualifications
The comparative taxonomy covers Swift task groups and Trio nurseries rather than every structured-concurrency implementation, and strict hierarchy cannot directly represent every shared-child dependency graph. The clice evidence describes one custom C++ framework and demonstrates topology, not cancellation latency, absence of leaks, deadlock freedom, fairness, or performance under load. Cancellation is also separable from structure: cleanup policy, awareness, persistence, and error propagation require additional decisions.

## What Changed
- Reframed structured concurrency as dynamic task extent rather than a complete cancellation and error policy.
- Added the Swift-versus-Trio contrast showing distinct scope-exit destruction and propagation semantics.
- Preserved clice's dependency-graph extension as an implementation case beyond a simple scope tree.

## Related Concepts
- [[ConcurrentProgramming]] - structured concurrency adds lifetime and cancellation discipline to concurrent task execution.
- [[StraightLineAsynchrony]] - provides the broader async design space in which task extent is only one dimension.
- [[ConcurrencyFailureModes]] - leaked work, saturated worker pools, and tangled synchronization motivate explicit structure.
- [[Clice]] - applies the model to language-server requests and compilation dependencies.
- [[Kotatsu]] - packages the reported implementation in its async module.
- [[InterprocessCommunication]] - clice combines structured task control with worker-process isolation and messaging.

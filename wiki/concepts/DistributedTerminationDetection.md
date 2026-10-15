---
title: "Distributed Termination Detection"
type: concept
tags: [distributed-systems, concurrency, termination, asynchronous-systems]
sources:
  - lychee-recursion
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[DistributedTerminationDetection]] is the problem of determining that a dynamic asynchronous computation has reached quiescence: no work is active, queued, or still capable of generating further work.

## Current Synthesis
The lychee recursion history shows why ordinary stream exhaustion is insufficient. In a one-way pipeline, closing input and draining in-flight work establishes completion. In a crawler, every response may discover more inputs, so an empty queue or momentary zero counter can be observed before asynchronous discovery and submission finish.

Termination therefore needs an invariant separate from cyclic channel closure. Lychee's later `WaitGroup` represents work with cloneable guards: a task clones its guard before creating descendants and releases its own guard after processing, while one waiter completes only when the final guard is dropped. This expresses dynamic reachability of work more directly than a separately updated integer, although correctness still depends on acquiring a child guard before the parent can make the system appear quiescent.

## Key Claims
- Exhausting the initial input stream does not prove completion when completed work may create more work.
- A momentary empty queue or zero counter is unsafe if discovery and admission occur asynchronously outside the counted lifecycle.
- Channel closure cannot serve as termination detection when a cyclic stage must retain a sender to generate future inputs.
- Dynamic work needs an ownership or credit invariant transferred to descendants before their parent completes.
- Cloneable guards can encode outstanding work through lifetime: the last drop signals quiescence without separately balancing increments and decrements.
- Termination detection is distinct from concurrency limiting, backpressure, deduplication, cancellation, and rate limiting.

## Evidence
- Recursive-work boundary: [[lychee-recursion]] shows responses creating fresh requests, invalidating input-stream exhaustion as a completion test.
- Counter failures: [[lychee-recursion]] reports both a plain expected-work counter and an atomic remaining-work counter hanging or observing completion incorrectly under asynchronous discovery.
- Channel-cycle failure: [[lychee-recursion]] explains that the recursive sender prevents natural closure while the recursion handler itself waits for the response stream to end.
- Guard invariant: [[lychee-recursion]] describes a merged `WaitGroup` whose waiter fires only after every cloneable `WaitGuard`, including guards held by recursively created work, has dropped.

## Counterevidence & Qualifications
The source is one maintainer's retrospective rather than a formal proof or comparison of Dijkstra–Scholten, token-passing, credit-distribution, and runtime task-scope algorithms. A guard model can still be misused if work is scheduled before acquiring a guard, a guard leaks, or detached work is omitted. It identifies quiescence but does not guarantee progress, fairness, bounded memory, successful completion, cancellation safety, or absence of deadlock elsewhere.

## What Changed
- Created the concept from the common termination failure across four recursion attempts.
- Distinguished dynamic-work completion from stream closure and concurrency control.
- Added cloneable lifetime guards as lychee's proposed completion invariant.

## Related Concepts
- [[Lychee]] - its recursive crawler is the concrete dynamic-work case.
- [[ConcurrencyFailureModes]] - premature exit, permanent waiting, and miscounted work are observable failure outcomes.
- [[Deadlock]] - cyclic channel dependencies can prevent both progress and a natural termination signal.
- [[AdaptiveBackpressure]] - capacity control is necessary but does not establish that all work is finished.
- [[StructuredConcurrency]] - both approaches make asynchronous work lifetime explicit, though a guard set need not form a strict parent-child tree.
- [[TaskQueueDesign]] - queue state is only one part of the global quiescence condition.

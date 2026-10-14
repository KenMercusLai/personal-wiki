---
title: "Adaptive Backpressure"
type: concept
tags: [distributed-systems, backpressure, load-shedding, concurrency, queues]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
  - how-we-found-a-bug-in-the-hyper-http-library
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Definition
[[AdaptiveBackpressure]] is a distributed control loop in which a service communicates changing capacity or overload to upstream components so they can redirect, delay, shed, or reject work before queues and retries cause wider failure.

## Current Synthesis
Backpressure is effective when it responds to actual workload and travels far enough upstream to reduce admitted work. Static concurrency, rate, or circuit-breaker thresholds can be useful bounds, but become brittle when request cost, resource availability, and traffic shape vary. Local services are often best placed to estimate immediate capacity because they know their active work, buffers, and request metadata.

The Imgix case combines local and upstream decisions. Workers could refuse individual transformations before becoming globally unhealthy; Spillway tried other workers, then used bounded queues, and finally rejected work so HAProxy and the client could retry with backoff. The design does not eliminate queueing. It makes queue placement, bounds, and failure behavior explicit, while queue depth becomes an overload signal.

The Cloudflare Images incident adds a correctness boundary below admission control. A reader that paused for only milliseconds could fill a Unix socket's outbound buffer, causing hyper's flush to return `Poll::Pending`. Backpressure itself was legitimate, but hyper discarded that signal and shut down before its internal buffer drained. This distinguishes backpressure from overload: even a brief local capacity mismatch must be propagated through asynchronous lifecycle control so that completion waits rather than silently losing data.

## Key Claims
- Unbounded concurrency is a common route from rising demand to queueing, latency, timeouts, retries, and sustained degradation.
- Feedback should reflect current application capacity rather than only static infrastructure thresholds.
- Admission decisions can be request-specific when work items have materially different cost.
- Backpressure must propagate through the call chain or excess work accumulates elsewhere.
- Bounded queues and explicit rejection make overload behavior finite and observable.
- Local decision-making can scale without global coordination, but does not eliminate the need for broader rate limits.
- Backpressure is also a correctness signal: an incomplete write must prevent shutdown or other terminal state changes until buffered data is delivered or an error is surfaced.

## Evidence
- Failure mechanism: [[health-checks-and-graceful-degradation-in-distributed-systems]] links unbounded concurrency to excessive queueing, higher RPC latency, timeouts, and retries.
- Dynamic feedback: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes HAProxy agent checks that can change backend weight, maximum connections, and operational state.
- Request-specific admission: [[health-checks-and-graceful-degradation-in-distributed-systems]] says Imgix workers used active-work statistics, request metadata, and socket-buffer heuristics to accept or refuse transformations.
- Bounded fallback: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes three alternate dispatch attempts, LIFO/FIFO/priority queues, rejection when full, and client retry with backoff.
- Observability: [[health-checks-and-graceful-degradation-in-distributed-systems]] identifies aggregate broker queue size as a closely monitored Prometheus alert signal.
- Socket-level trigger: [[how-we-found-a-bug-in-the-hyper-http-library]] says a briefly slower reader filled the outbound buffer during large responses and caused `poll_flush` to return `Poll::Pending`.
- Lost signal: [[how-we-found-a-bug-in-the-hyper-http-library]] traces data loss to the state machine discarding pending flush status and issuing shutdown with bytes still buffered.
- Controlled validation: [[how-we-found-a-bug-in-the-hyper-http-library]] reproduces the condition with a stream that accepts one chunk and then blocks, confirming that the fix waits.

## Counterevidence & Qualifications
Backpressure moves, delays, or limits work; it does not create capacity. Retries can worsen overload unless attempts, budgets, and backoff are bounded. Local decisions may be mutually inconsistent or unfair, while centralized coordination can become a bottleneck. The Spillway source does not compare its policy with alternatives or provide quantitative outcomes. The Cloudflare incident is not a general overload study: a temporary reader pause exposed a pre-existing hyper defect, and its first-party account provides no fleet-wide incidence or measured reader-speed comparison. Its initial dispatch-loop fix also shows that propagating `Pending` at the wrong layer can reduce unrelated progress or break keepalive semantics.

## What Changed
- Added asynchronous I/O readiness as a correctness-bearing backpressure signal, not only an overload-control input.
- Distinguished brief local buffer saturation from service-wide overload.
- Added the requirement that terminal lifecycle actions wait for buffered work or surface failure.
- Preserved the placement tradeoff: reacting too early in a dispatch loop can impede reads and keepalive behavior.

## Related Concepts
- [[ServiceHealthChecks]] - capacity-sensitive health is the feedback signal used by upstream controllers.
- [[NetworkLoadBalancing]] - routers redirect or reduce traffic in response to backend feedback.
- [[DependencyDegradation]] - shedding optional or excess work helps preserve core service under partial failure.
- [[TaskQueueDesign]] - bounded queues, policy choice, and recovery semantics determine where delayed work accumulates.
- [[SystemReliability]] - overload containment prevents local saturation from becoming a cascading failure.
- [[Hyper]] - mishandled a pending socket flush until shutdown was changed to await it.
- [[RaceCondition]] - flush and shutdown ordering turned ordinary buffer pressure into intermittent truncation.
- [[ServiceObservability]] - syscall traces showed whether queued bytes actually crossed the socket boundary.

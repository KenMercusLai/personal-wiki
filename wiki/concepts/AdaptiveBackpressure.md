---
title: "Adaptive Backpressure"
type: concept
tags: [distributed-systems, backpressure, load-shedding, concurrency, queues]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[AdaptiveBackpressure]] is a distributed control loop in which a service communicates changing capacity or overload to upstream components so they can redirect, delay, shed, or reject work before queues and retries cause wider failure.

## Current Synthesis
Backpressure is effective when it responds to actual workload and travels far enough upstream to reduce admitted work. Static concurrency, rate, or circuit-breaker thresholds can be useful bounds, but become brittle when request cost, resource availability, and traffic shape vary. Local services are often best placed to estimate immediate capacity because they know their active work, buffers, and request metadata.

The Imgix case combines local and upstream decisions. Workers could refuse individual transformations before becoming globally unhealthy; Spillway tried other workers, then used bounded queues, and finally rejected work so HAProxy and the client could retry with backoff. The design does not eliminate queueing. It makes queue placement, bounds, and failure behavior explicit, while queue depth becomes an overload signal.

## Key Claims
- Unbounded concurrency is a common route from rising demand to queueing, latency, timeouts, retries, and sustained degradation.
- Feedback should reflect current application capacity rather than only static infrastructure thresholds.
- Admission decisions can be request-specific when work items have materially different cost.
- Backpressure must propagate through the call chain or excess work accumulates elsewhere.
- Bounded queues and explicit rejection make overload behavior finite and observable.
- Local decision-making can scale without global coordination, but does not eliminate the need for broader rate limits.

## Evidence
- Failure mechanism: [[health-checks-and-graceful-degradation-in-distributed-systems]] links unbounded concurrency to excessive queueing, higher RPC latency, timeouts, and retries.
- Dynamic feedback: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes HAProxy agent checks that can change backend weight, maximum connections, and operational state.
- Request-specific admission: [[health-checks-and-graceful-degradation-in-distributed-systems]] says Imgix workers used active-work statistics, request metadata, and socket-buffer heuristics to accept or refuse transformations.
- Bounded fallback: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes three alternate dispatch attempts, LIFO/FIFO/priority queues, rejection when full, and client retry with backoff.
- Observability: [[health-checks-and-graceful-degradation-in-distributed-systems]] identifies aggregate broker queue size as a closely monitored Prometheus alert signal.

## Counterevidence & Qualifications
Backpressure moves and limits work; it does not create capacity. Retries can worsen overload unless attempts, budgets, and backoff are bounded. Local decisions may be mutually inconsistent or unfair, while centralized coordination can become a bottleneck. The source does not compare the Spillway policy with alternatives or provide quantitative outcomes.

## What Changed
- Established feedback propagation, request-specific admission, bounded queues, and explicit rejection as one adaptive overload-control loop.
- Preserved centralized rate limiting as a complement to distributed local decisions.

## Related Concepts
- [[ServiceHealthChecks]] - capacity-sensitive health is the feedback signal used by upstream controllers.
- [[NetworkLoadBalancing]] - routers redirect or reduce traffic in response to backend feedback.
- [[DependencyDegradation]] - shedding optional or excess work helps preserve core service under partial failure.
- [[TaskQueueDesign]] - bounded queues, policy choice, and recovery semantics determine where delayed work accumulates.
- [[SystemReliability]] - overload containment prevents local saturation from becoming a cascading failure.

---
title: "Service Health Checks"
type: concept
tags: [distributed-systems, reliability, health-checks, quality-of-service]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[ServiceHealthChecks]] are observations used by infrastructure to decide whether a service should receive traffic, have traffic reduced, or be restarted, with the signal chosen to match the decision being made.

## Current Synthesis
Service health is not one universal boolean. A process can be alive and responsive to a trivial probe while queueing so much real work that requests miss their latency objective. The useful measure for routing is therefore application-level quality of service: success, latency, correctness, concurrency pressure, queue depth, or ability to complete a representative unit of work.

Different control planes need different abstractions. An orchestrator may reasonably use a conservative binary liveness signal to restart a crashed or deadlocked process. A load balancer needs finer readiness and capacity information so it can reduce traffic before the same process becomes completely unavailable. End-to-end probes are more representative than pings, but they must stay cheap enough not to become load and should be interpreted alongside live workload feedback.

## Key Claims
- Health signals should be selected for the action they control.
- Process reachability is weak evidence that representative work will complete within an acceptable latency.
- Restart decisions can use coarse liveness while routing decisions need graded readiness and capacity.
- Queue depth, concurrency, work latency, and correctness can expose partial degradation before total failure.
- A health endpoint that always returns success independently of real work can create false confidence.
- Accurate health information is a prerequisite for effective load shedding and graceful degradation.

## Evidence
- Decision-specific probes: [[health-checks-and-graceful-degradation-in-distributed-systems]] distinguishes Kubernetes-style liveness restarts from readiness-based traffic removal and argues that routing needs more detail than orchestration.
- Representative work: [[health-checks-and-graceful-degradation-in-distributed-systems]] uses database query success and end-to-end latency to show why CPU, lock, error, or ping signals can produce false positives and negatives.
- Partial degradation: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes responsive processes whose queues and concurrency cause requests to miss service latency expectations.
- Routing consequence: [[health-checks-and-graceful-degradation-in-distributed-systems]] connects accurate service health to circuit breaking, load shedding, and avoidance of cascading failure.

## Counterevidence & Qualifications
No single comprehensive probe is universally best. End-to-end checks can be expensive, may depend on other services, and can amplify trouble if run aggressively. Live-traffic measurements are representative but can lag behind the onset of overload. The source is a practitioner argument and historical case rather than a comparative evaluation of health-check designs.

## What Changed
- Established service health as a decision-specific quality-of-service spectrum rather than one binary status.
- Separated restart-oriented liveness from routing-oriented readiness and capacity.

## Related Concepts
- [[AdaptiveBackpressure]] - graded health and capacity signals drive upstream admission and load reduction.
- [[NetworkLoadBalancing]] - routing consumes service-health information when choosing viable backends.
- [[DependencyDegradation]] - accurate health allows a system to reduce capability without collapsing entirely.
- [[ServiceObservability]] - monitoring supplies latency, error, saturation, and queue evidence used to judge health.
- [[SystemReliability]] - health checks are one feedback mechanism within broader failure detection and recovery.

---
title: "HAProxy"
type: entity
tags: [software, load-balancer, proxy]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
  - how-i-made-twitter-back-end
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[HAProxy]] is a load balancer and proxy presented both as a simple request router across application services and as a control point capable of using backend reachability and richer capacity feedback.

## Current Profile
The sources span two levels of design. The Twitter-like backend sketch places HAProxy in front of Auth, Tweet, and Timeline services and assigns it request-routing responsibility without specifying algorithms, redundancy, or failure behavior. The Imgix account supplies the more operationally detailed layer: HAProxy's agent check lets a backend advertise proportional weight, a connection limit, readiness, drain or maintenance mode, and down or up state, while HAProxy can retry work rejected by Spillway after backoff.

## Key Characteristics
- Separates regular connectivity checks from auxiliary application feedback.
- Routes requests across independently deployed application services.
- Can adjust backend weight and maximum connections dynamically.
- Supports ready, drain, maintenance, down, and up state changes.
- Requires the agent to reverse state changes it initiated.

## Evidence
- Agent protocol: [[health-checks-and-graceful-degradation-in-distributed-systems]] reproduces HAProxy documentation for weight, `maxconn`, and administrative or operating states.
- Recovery responsibility: [[health-checks-and-graceful-degradation-in-distributed-systems]] notes that only the agent can reverse its own drain or down action.
- Imgix role: [[health-checks-and-graceful-degradation-in-distributed-systems]] places HAProxy at the edge and as the retrying client when Spillway rejects work.
- Basic service routing: [[how-i-made-twitter-back-end]] diagrams HAProxy directing incoming requests toward separate Auth, Tweet, and Timeline services.

## Qualifications
The Imgix article cites HAProxy 1.7-era documentation and a historical deployment. Current syntax, defaults, and behavior require current documentation, and that source provides no benchmark of agent checks against other feedback mechanisms. The Twitter-like design is an educational architecture sketch; it does not describe balancing policy, discovery integration, TLS termination, high availability, retries, overload protection, or measured performance.

## What Changed
- Added the simpler role of routing requests across Auth, Tweet, and Timeline services.
- Distinguished a conceptual routing diagram from the richer application-feedback controls in the Imgix account.

## Relationships
- [[AdaptiveBackpressure]] - agent feedback changes how much new work a backend receives.
- [[ServiceHealthChecks]] - ordinary reachability and graded capacity are separate signals.
- [[Spillway]] - downstream Imgix broker in the described request path.
- [[NetworkLoadBalancing]] - HAProxy applies health and capacity signals to traffic distribution.
- [[HybridTimelineFanout]] - routes requests toward the feed services whose background path performs fan-out.

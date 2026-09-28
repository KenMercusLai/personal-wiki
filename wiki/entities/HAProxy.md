---
title: "HAProxy"
type: entity
tags: [software, load-balancer, proxy]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[HAProxy]] is a load balancer and proxy presented as supporting both ordinary reachability checks and a separate agent channel for dynamic backend feedback.

## Current Profile
The source highlights HAProxy's agent check as a richer control interface than a binary health probe. A backend agent can advertise proportional weight, a connection limit, readiness, drain or maintenance mode, and down or up state. In the Imgix case, HAProxy also sat upstream of Spillway and could retry rejected requests after backoff.

## Key Characteristics
- Separates regular connectivity checks from auxiliary application feedback.
- Can adjust backend weight and maximum connections dynamically.
- Supports ready, drain, maintenance, down, and up state changes.
- Requires the agent to reverse state changes it initiated.

## Evidence
- Agent protocol: [[health-checks-and-graceful-degradation-in-distributed-systems]] reproduces HAProxy documentation for weight, `maxconn`, and administrative or operating states.
- Recovery responsibility: [[health-checks-and-graceful-degradation-in-distributed-systems]] notes that only the agent can reverse its own drain or down action.
- Imgix role: [[health-checks-and-graceful-degradation-in-distributed-systems]] places HAProxy at the edge and as the retrying client when Spillway rejects work.

## Qualifications
The article cites HAProxy 1.7-era documentation and a historical deployment. Current syntax, defaults, and behavior require current documentation; the source provides no benchmark of agent checks against other feedback mechanisms.

## What Changed
- Established HAProxy's agent-check role as an example of application-informed load balancing.

## Relationships
- [[AdaptiveBackpressure]] - agent feedback changes how much new work a backend receives.
- [[ServiceHealthChecks]] - ordinary reachability and graded capacity are separate signals.
- [[Spillway]] - downstream Imgix broker in the described request path.
- [[NetworkLoadBalancing]] - HAProxy applies health and capacity signals to traffic distribution.

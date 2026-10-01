---
title: "HAProxy"
type: entity
tags: [software, load-balancer, proxy]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
  - how-i-made-twitter-back-end
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
  - nick-craver-stack-overflow-how-we-do-deployment-2016-edition
  - nick-craver-stack-overflow-the-architecture-2016-edition
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[HAProxy]] is a load balancer and proxy represented as a request router, TLS boundary, traffic-measurement point, graded capacity controller, and rolling-deployment coordinator.

## Current Profile
The sources span several levels. A Twitter-like educational backend places HAProxy in front of Auth, Tweet, and Timeline services without specifying balancing or failure policy. The Imgix account adds application feedback: agent checks let backends advertise proportional weight, connection limits, readiness, drain or maintenance modes, and up or down state, while HAProxy retries work rejected after bounded backoff.

Stack Overflow's architecture makes HAProxy an edge control plane. Four load balancers terminated TLS, separated external and DMZ links, routed mainly by host header, rate-limited traffic, and captured application timing headers into per-request syslog. The retained dashboard shows nine primary web servers simultaneously healthy with similar cumulative inbound and outbound traffic, supporting the prose's claim of distributed load. The later HTTPS account adds multiple HAProxy processes, abstract-socket forwarding, trusted scheme metadata, listener separation, and a large TLS session cache for secure websocket reconnection.

The deployment account adds explicit traffic-state orchestration: drain one IIS server, wait for requests to finish, hold it down during replacement, and require three successful polls before return. HAProxy therefore appears not merely as a request distributor but as a boundary where transport, measurement, overload feedback, maintenance state, and change safety meet.

## Key Characteristics
- Routes requests across service or server backends using host and health information.
- Separates basic connectivity checks from auxiliary application capacity feedback.
- Can adjust backend weight, maximum connections, readiness, drain, maintenance, and up/down state.
- Can terminate TLS, cache sessions, and forward trusted connection metadata to HTTP backends.
- Supports rate limiting and per-request metric capture at the traffic boundary.
- Coordinates rolling deployment through drain, down, readiness, and verified return-to-service states.
- Makes connection, port, file-handle, memory, retry, and health semantics part of application operations.

## Evidence
- Agent protocol: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes weight, `maxconn`, administrative state, and agent responsibility for reversing agent-initiated drain or down actions.
- Basic routing: [[how-i-made-twitter-back-end]] diagrams HAProxy directing incoming requests toward Auth, Tweet, and Timeline services.
- Architecture role: [[nick-craver-stack-overflow-the-architecture-2016-edition]] describes four load balancers performing TLS termination, host routing, rate limiting, session reuse, and timing-header capture.
- Traffic distribution: [[nick-craver-stack-overflow-the-architecture-2016-edition]] retains an Opserver view showing nine healthy web backends with broadly similar cumulative traffic totals.
- High-volume TLS and websockets: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes process separation, abstract sockets, scheme headers, tier-specific listeners, and more than 600,000 concurrent secure websockets.
- Deployment control: [[nick-craver-stack-overflow-how-we-do-deployment-2016-edition]] shows drain, down, restart, and three-poll readiness gating around each IIS update.

## Qualifications
The sources span HAProxy 1.5- and 1.7-era behavior plus an educational design sketch. Current syntax, defaults, health features, HTTP versions, TLS behavior, and operational recommendations require current documentation. None benchmarks HAProxy against alternatives. Stack Overflow's memory, traffic, connection, and dashboard figures are first-party historical observations; balanced cumulative bytes do not establish equal latency, error rate, or request cost. Passing repeated health polls does not prove cache warmth or full behavior under production load.

## What Changed
- Added the earlier architecture view of HAProxy as rate limiter, host router, session cache, request-metric collector, and balanced web-tier distributor.
- Connected deployment, TLS, websocket, measurement, and overload-feedback roles into one traffic-boundary profile.
- Added network and resource limits as qualifications to high-volume websocket handling.

## Relationships
- [[AdaptiveBackpressure]] - agent feedback changes how much work each backend receives.
- [[ServiceHealthChecks]] - reachability, readiness, and graded capacity drive different controls.
- [[NetworkLoadBalancing]] - HAProxy applies routing and health decisions across backends.
- [[StackOverflow]] - uses HAProxy for TLS, routing, metrics, rate limits, and deployments.
- [[HTTPSMigration]] - HAProxy supplies the origin-side secure endpoint and scheme context.
- [[RollingDeployment]] - HAProxy withdraws and restores each updated server.
- [[Spillway]] - downstream Imgix broker whose rejections HAProxy can retry.
- [[HybridTimelineFanout]] - educational service architecture routed through HAProxy.

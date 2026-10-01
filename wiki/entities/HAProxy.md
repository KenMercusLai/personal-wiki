---
title: "HAProxy"
type: entity
tags: [software, load-balancer, proxy]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
  - how-i-made-twitter-back-end
  - nick-craver-https-on-stack-overflow-the-end-of-a-long-road
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[HAProxy]] is a load balancer and proxy presented both as a simple request router across application services and as a control point capable of using backend reachability and richer capacity feedback.

## Current Profile
The sources span three levels of design. The Twitter-like backend sketch places HAProxy in front of Auth, Tweet, and Timeline services and assigns it request-routing responsibility without specifying algorithms, redundancy, or failure behavior. The Imgix account supplies an application-feedback layer: HAProxy's agent check lets a backend advertise proportional weight, a connection limit, readiness, drain or maintenance mode, and down or up state, while HAProxy can retry work rejected by Spillway after backoff.

The [[StackOverflow]] HTTPS retrospective adds high-volume TLS termination. Four HAProxy processes separated HTTP handling from three HTTPS negotiation workers, forwarded decrypted traffic through abstract named sockets, attached trusted scheme metadata, and exposed separate listeners for primary, secondary, websocket, and development tiers. This shows HAProxy as both router and protocol boundary, with session resumption improving reconnect performance at a measurable memory cost.

## Key Characteristics
- Separates regular connectivity checks from auxiliary application feedback.
- Routes requests across independently deployed application services.
- Can adjust backend weight and maximum connections dynamically.
- Supports ready, drain, maintenance, down, and up state changes.
- Requires the agent to reverse state changes it initiated.
- Can terminate TLS, isolate negotiation work, and forward trusted connection metadata to HTTP application backends.

## Evidence
- Agent protocol: [[health-checks-and-graceful-degradation-in-distributed-systems]] reproduces HAProxy documentation for weight, `maxconn`, and administrative or operating states.
- Recovery responsibility: [[health-checks-and-graceful-degradation-in-distributed-systems]] notes that only the agent can reverse its own drain or down action.
- Imgix role: [[health-checks-and-graceful-degradation-in-distributed-systems]] places HAProxy at the edge and as the retrying client when Spillway rejects work.
- Basic service routing: [[how-i-made-twitter-back-end]] diagrams HAProxy directing incoming requests toward separate Auth, Tweet, and Timeline services.
- TLS termination: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] describes dedicated HTTPS processes, OpenSSL support, abstract sockets, scheme headers, and tier-specific port 443 listeners.
- Websocket scale: [[nick-craver-https-on-stack-overflow-the-end-of-a-long-road]] reports more than 600,000 concurrent secure websocket connections and a large TLS session cache on 64GB load balancers.

## Qualifications
The Imgix article cites HAProxy 1.7-era documentation, while the Stack Overflow account describes HAProxy 1.5-era TLS support and a 2017 deployment. Current syntax, defaults, protocol support, and behavior require current documentation; neither source benchmarks HAProxy against alternatives. The Twitter-like design is an educational architecture sketch and does not describe balancing policy, discovery integration, TLS termination, high availability, retries, overload protection, or measured performance. Stack Overflow's connection and memory figures are first-party point-in-time observations.

## What Changed
- Added high-volume TLS termination, process separation, abstract-socket forwarding, and secure-websocket handling.
- Distinguished the 2017 deployment snapshot from current HAProxy protocol capabilities.

## Relationships
- [[AdaptiveBackpressure]] - agent feedback changes how much new work a backend receives.
- [[ServiceHealthChecks]] - ordinary reachability and graded capacity are separate signals.
- [[Spillway]] - downstream Imgix broker in the described request path.
- [[NetworkLoadBalancing]] - HAProxy applies health and capacity signals to traffic distribution.
- [[HybridTimelineFanout]] - routes requests toward the feed services whose background path performs fan-out.
- [[StackOverflow]] - used HAProxy as the local load-balancing and TLS-termination layer.
- [[HTTPSMigration]] - HAProxy supplied the origin-side HTTPS endpoint and forwarded secure-connection context.

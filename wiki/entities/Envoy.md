---
title: "Envoy"
type: entity
tags: [software, service-mesh, proxy, load-balancing]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Envoy]] is a proxy and service-mesh data-plane example used to illustrate that routing systems may prioritize health-check information over service-discovery membership.

## Current Profile
The source places Envoy at the load-balancing layer, where health information determines whether an otherwise discovered instance should receive traffic. It is also cited in relation to the brittleness of static threshold-based circuit breaking and rate limiting.

## Key Characteristics
- Participates in service-mesh traffic routing.
- Uses health information in addition to service-discovery data.
- Illustrates the need for routing controls that account for overload and cascading failure.

## Evidence
- Health-aware routing: [[health-checks-and-graceful-degradation-in-distributed-systems]] says Envoy gives health-check information precedence over discovery data when deciding whether to route to an instance.
- Overload context: [[health-checks-and-graceful-degradation-in-distributed-systems]] cites Envoy material while warning that static rate and circuit-breaker thresholds can be brittle.

## Qualifications
The article provides Envoy as an example rather than a complete product analysis, and its description dates to 2018. Current features and configuration are outside this source's scope.

## What Changed
- Established Envoy as a health-aware routing example in the service-health argument.

## Relationships
- [[ServiceHealthChecks]] - health observations qualify service-discovery membership for routing.
- [[AdaptiveBackpressure]] - routing and circuit-breaking controls respond to overload signals.
- [[NetworkLoadBalancing]] - Envoy is an application-aware traffic-distribution layer.

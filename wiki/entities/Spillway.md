---
title: "Spillway"
type: entity
tags: [software, reverse-proxy, request-broker, image-processing]
sources:
  - health-checks-and-graceful-degradation-in-distributed-systems
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Spillway]] was an internal Imgix reverse proxy and request broker that routed image-transformation work while containing overload.

## Current Profile
The described deployment split Spillway into a CPU-bound frontend and a broker colocated on the same host. The frontend preprocessed requests and checked that source images were available in the datacenter cache. The broker tracked a fixed worker pool, preferred suitable non-overloaded workers with local file affinity, retried dispatch across workers, queued temporarily when necessary, and rejected work when all bounded queues were full.

## Key Characteristics
- Separated frontend preprocessing from broker coordination because their performance profiles differed.
- Tracked worker capacity and local-file affinity for routing.
- Tried up to three different workers before queueing a refused request.
- Maintained bounded LIFO, FIFO, and priority queues.
- Rejected work when queues were full so clients could retry with backoff.
- Exposed aggregate queue depth as a Prometheus monitoring and alerting signal.

## Evidence
- Component split: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes separate frontend and broker binaries deployed on one host.
- Routing: [[health-checks-and-graceful-degradation-in-distributed-systems]] describes worker health tracking, local-file preference, and three successive dispatch attempts.
- Queue and rejection policy: [[health-checks-and-graceful-degradation-in-distributed-systems]] names LIFO, FIFO, and priority queues and rejection after all were full.
- Monitoring: [[health-checks-and-graceful-degradation-in-distributed-systems]] says broker queue size was closely monitored and alerted through Prometheus.

## Qualifications
The source is a retrospective practitioner account. It does not quantify queue bounds, request-class policy, throughput, tail latency, fairness, drops, retry amplification, or performance relative to another broker design.

## What Changed
- Established Spillway as a concrete service-to-router feedback and bounded-overload design.

## Relationships
- [[Imgix]] - company and image-processing platform in which Spillway operated.
- [[AdaptiveBackpressure]] - Spillway propagated worker refusal into rerouting, queueing, rejection, and retry.
- [[ServiceHealthChecks]] - worker health included capacity for a specific unit of work.
- [[HAProxy]] - upstream client that could retry rejected work after backoff.
- [[Prometheus]] - monitored broker queue depth.

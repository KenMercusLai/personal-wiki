---
title: "FlowVisor"
type: entity
tags: [project, networking, sdn, openflow, virtualization]
sources:
  - sherwood-et-al-can-the-production-network-be-the-testbed
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[FlowVisor]] is a research prototype that partitions shared [[OpenFlow]] network hardware into independently controlled slices so production traffic and experiments can coexist.

## Current Profile
The prototype sits transparently between OpenFlow switches and multiple slice controllers. A policy gives each slice a topology, flowspace, bandwidth allocation, switch-CPU budget, forwarding-table quota, and controller endpoint; FlowVisor then filters, rewrites, expands, throttles, or rejects control messages to enforce those boundaries. Because established flows remain in hardware, packets can continue at line rate while the proxy mediates control-plane events.

The paper reports one instance serving a Stanford deployment with multiple slices and more than 40 devices, plus staged use at six other campuses. This demonstrates feasibility in a bounded historical environment, not universal production readiness: CPU exhaustion, slow-path behavior, legacy-device interactions, linear rule lookup, and incomplete OpenFlow exposure remained important limitations.

## Key Characteristics
- Transparent proxy between shared OpenFlow data planes and multiple independent controllers.
- Partitions authority by flowspace and topology while allocating bandwidth, device CPU, and forwarding entries.
- Enforces policy through control-message filtering, rewriting, rule intersection, quotas, queues, and rate limits.
- Preserves line-rate steady-state forwarding because it is not placed in the packet data path.
- Supports per-flow user opt-in and simultaneous production, monitoring, and experimental slices.
- Historically demonstrated in a campus production network and a wider multi-campus test infrastructure.

## Evidence
- Architecture and policy: [[sherwood-et-al-can-the-production-network-be-the-testbed]] describes FlowVisor as an approximately 8,000-line C proxy with per-slice resource and flowspace definitions.
- Isolation mechanisms: [[sherwood-et-al-can-the-production-network-be-the-testbed]] documents port and topology pruning, rule intersection, action rewriting, per-port queues, message throttling, and flow-entry quotas.
- Performance: [[sherwood-et-al-can-the-production-network-be-the-testbed]] reports line-rate data forwarding, roughly 16 ms average new-flow overhead, and 0.48 ms average port-status-response overhead.
- Deployment: [[sherwood-et-al-can-the-production-network-be-the-testbed]] reports continuous Stanford use from June 2009 and deployment on six additional campus test networks.

## Qualifications
The profile reflects a 2010 prototype and paper rather than current software or standards. The evaluation used selected hardware, traffic, and workloads; minimum bandwidth reservations were imperfect, flowspace matching was linear, and the switch CPU remained a difficult shared resource. Transparency also adds a critical mediation layer whose faults or policy errors can affect every attached slice.

## What Changed
- Created a bounded historical profile of the prototype's architecture, enforcement mechanisms, measurements, deployment, and limits.

## Relationships
- [[OpenFlow]] - supplies the control/data-plane protocol and forwarding abstraction used by the prototype.
- [[NetworkSlicing]] - is the resource-partitioning model FlowVisor implements.
- [[ProductionNetworkExperimentation]] - is the research workflow FlowVisor was built to enable.
- [[NetworkResilienceTradeoffs]] - frames the isolation benefits and shared control-layer risks introduced by the design.

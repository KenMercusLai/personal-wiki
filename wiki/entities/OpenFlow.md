---
title: "OpenFlow"
type: entity
tags: [project, networking, sdn, protocol]
sources:
  - sherwood-et-al-can-the-production-network-be-the-testbed
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[OpenFlow]] is represented in this source as an open protocol that separates network control logic from switch and router forwarding, exposing hardware flow tables to an external controller.

## Current Profile
An OpenFlow flow entry combines a packet-header match, actions, and counters. Hardware handles matching entries at line rate; a packet without a match can trigger a controller event, after which the controller installs a rule for later packets. This interface made deployed commercial forwarding hardware programmable enough for the paper's experiments, but a single controller alone did not provide safe multi-researcher sharing.

[[FlowVisor]] uses the protocol as a mediation boundary: it presents itself as switches to controllers and as a controller to switches, allowing multiple control planes to share one data plane. The paper treats OpenFlow as one possible implementation substrate rather than a requirement of the broader slicing architecture.

## Key Characteristics
- Separates external programmable control logic from hardware packet forwarding.
- Represents forwarding behavior through header matches, actions, and counters in flow tables.
- Lets established flows continue in switch hardware without consulting the controller for every packet.
- Provides the common message channel that FlowVisor can inspect and rewrite.
- Exposes a vendor-neutral lowest common denominator rather than every device capability.

## Evidence
- Forwarding model: [[sherwood-et-al-can-the-production-network-be-the-testbed]] explains flow entries, table lookup, unmatched-packet events, and controller-installed rules.
- Hardware path: [[sherwood-et-al-can-the-production-network-be-the-testbed]] says modern switches already implement comparable flow tables, often in TCAM, enabling firmware-level support and line-rate forwarding.
- Slicing boundary: [[sherwood-et-al-can-the-production-network-be-the-testbed]] uses OpenFlow messages as the enforceable interface between multiple controllers and shared switches.
- Capability boundary: [[sherwood-et-al-can-the-production-network-be-the-testbed]] says the minimal common interface omits many scheduling, tunneling, and arbitrary packet-processing capabilities.

## Qualifications
This is a source-bounded description of OpenFlow around version 1.0/1.1, not a current protocol history or implementation survey. Controller contact on misses adds setup latency, hardware support varies, slow-path behavior can exhaust switch CPUs, and the abstraction does not make arbitrary packet processing or multi-tenant isolation automatic.

## What Changed
- Created a historical profile of the protocol as the programmable forwarding substrate and mediation boundary used by FlowVisor.

## Relationships
- [[FlowVisor]] - proxies and rewrites OpenFlow messages to share hardware among controllers.
- [[NetworkSlicing]] - requires isolation mechanisms beyond the base protocol's single-controller programmability.
- [[ProductionNetworkExperimentation]] - uses OpenFlow-capable deployed hardware to reduce the gap between prototype and production behavior.

---
title: "Network Slicing"
type: concept
tags: [networking, virtualization, isolation, resource-allocation]
sources:
  - sherwood-et-al-can-the-production-network-be-the-testbed
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkSlicing]] partitions shared network forwarding and control resources into policy-bounded virtual networks whose controllers can act independently without exceeding their assigned traffic, topology, or resource authority.

## Current Synthesis
The FlowVisor design shows why traffic separation alone is insufficient. A slice needs a bounded view of nodes and ports, a set of packet headers or flowspace it may control, link-bandwidth guarantees, switch-CPU limits, and a quota on finite forwarding entries. Enforcement sits at the control/data-plane boundary: messages are filtered or rewritten, requested matches are intersected with allowed flowspace, invalid actions are rejected, bandwidth is mapped to queues, and control demand is throttled.

This architecture enables different production, monitoring, and experimental controllers to share line-rate hardware while remaining unaware of most mediation. Its strength is also its risk boundary. The slicer becomes shared control infrastructure, and isolation quality depends on what the hardware abstraction exposes; slow paths, variable message costs, imperfect queues, and undisclosed device behavior can cross intended boundaries.

## Key Claims
- Slice isolation must cover topology, bandwidth, device CPU, forwarding-table capacity, and control authority, not only packet labels.
- Flowspace provides fine-grained assignment of traffic and supports opt-in at user, application, or individual-flow scope.
- Transparent mediation can preserve unmodified controllers and switches while constraining their interaction.
- Control-message rewriting and rejection can enforce authority without placing the slicer in the steady-state data path.
- Hardware and protocol abstractions determine whether resource limits are precise, portable, and safe.
- A shared slicer adds a common policy and failure surface that must itself be operated as production infrastructure.

## Evidence
- Resource dimensions: [[sherwood-et-al-can-the-production-network-be-the-testbed]] identifies topology, bandwidth, switch CPU, and forwarding entries as separate slicing requirements.
- Flowspace and opt-in: [[sherwood-et-al-can-the-production-network-be-the-testbed]] maps ordered allow, deny, and read-only header rules to slices and lets users assign selected traffic.
- Authority enforcement: [[sherwood-et-al-can-the-production-network-be-the-testbed]] intersects controller rules with allowed flowspace, prunes visible ports, rewrites actions, and returns errors for invalid requests.
- Resource enforcement: [[sherwood-et-al-can-the-production-network-be-the-testbed]] uses queues, token-bucket-style suppression, controller throttling, slow-path conversion, and flow-entry quotas.
- Isolation limits: [[sherwood-et-al-can-the-production-network-be-the-testbed]] reports imperfect bandwidth results and device- and message-dependent CPU behavior.

## Counterevidence & Qualifications
The evidence comes from one historical prototype and selected campus deployments. The design did not perfectly isolate every resource, did not support arbitrary packet processing or all virtual topologies, and relied on OpenFlow and hardware features that varied by device. Minimum guarantees are not maximum caps, policy rewriting can expand rules, and a transparent proxy can become a bottleneck or common failure domain.

## What Changed
- Established a multidimensional definition of network slicing grounded in traffic authority and finite hardware resources.
- Added the slicer itself and the hardware abstraction as explicit isolation and reliability boundaries.

## Related Concepts
- [[ProductionNetworkExperimentation]] - uses slices to expose experiments to realistic infrastructure and traffic.
- [[NetworkResilienceTradeoffs]] - evaluates the balance between bounded failure domains and added shared control complexity.
- [[NetworkSegmentation]] - separates traffic domains but does not necessarily grant independent programmable control planes or resource quotas.
- [[NetworkAutomation]] - can configure and operate slice policy but requires validation and change controls.

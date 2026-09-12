---
title: "Network Load Balancing"
type: concept
tags: [networking, infrastructure, load-balancing]
sources:
  - jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[NetworkLoadBalancing]] is the infrastructure practice of distributing client traffic across backend servers while preserving valid packet routing, connection identity, performance, and availability.

## Current Synthesis
The source presents network load balancing as a packet-flow problem before it is a product feature or algorithm choice. A load balancer must choose a backend, but its real constraints come from how packets move afterward: which MAC address or IP address is rewritten, whether the backend can see the client IP, whether response traffic returns through the load balancer, and whether the load balancer must sit in the same VLAN or gateway path as the real servers.

The article's practical lesson is that performance and deployment flexibility usually trade against each other. Direct server return can remove the response path from the load balancer and avoid a major bottleneck, especially when responses are larger than requests. More flexible cross-VLAN designs often need additional address translation, TCP option handling, encapsulation, or provider-specific kernel modules to keep routing and application-visible identity coherent.

## Key Claims
- Network load-balancing behavior is determined by packet rewriting and return-path design, not only by scheduling policy.
- Direct server return improves throughput by keeping response traffic away from the load balancer.
- Same-VLAN or gateway requirements arise when a forwarding mode depends on L2 MAC rewriting or needs the response packet to revisit the load balancer.
- Cross-VLAN deployment often requires full address translation, tunneling, or host-side packet-processing support.
- Client-IP preservation becomes a separate engineering problem once the load balancer rewrites the packet source address.
- Cloud load-balancing products add routing, session synchronization, kernel modules, DPDK, and offload to make basic packet-forwarding modes operational at scale.

## Evidence
- Packet rewriting: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] compares DR, NAT, full NAT, ENAT, and IP TUN by following source IP, destination IP, MAC, and encapsulation changes.
- Direct return: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] says DR, ENAT, and IP TUN avoid sending normal response traffic back through LVS.
- VLAN and gateway constraints: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] explains why DR requires L2 adjacency and why NAT needs the load balancer to see the return path.
- Client identity: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes TOA/VTOA/CTK-style modules for recovering or carrying client address information when full NAT or ENAT hides it.
- Cloud scaling: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes Alibaba Cloud SLB/NGLB using dynamic routing, session synchronization, DPDK, huge pages, cache-line tuning, token-bucket sharding, and flow offload.

## Counterevidence & Qualifications
The source is a technical explanation and vendor-context case study rather than a neutral benchmark. Its Alibaba Cloud details are useful as implementation evidence, but the exact modules, performance figures, and product behavior should be treated as source-date and provider-specific.

## What Changed
- Created the concept page for general network load balancing.
- Added packet rewriting, return-path design, and client-IP preservation as central load-balancing concerns.
- Connected cloud productization to routing, high availability, and packet-processing optimization.

## Related Concepts
- [[LVSForwardingModes]] - LVS forwarding modes are the source's concrete taxonomy for network load-balancing tradeoffs.
- [[InferenceLoadBalancing]] - both distribute work across backends, but inference routing operates at the model-serving workload layer rather than the packet-forwarding layer.
- [[QUIC]] - QUIC connection identity can interact with load balancers that route by transport-level tuples.
- [[CloudCostOptimization]] - both involve infrastructure tradeoffs, but this page focuses on traffic forwarding rather than spend reduction.

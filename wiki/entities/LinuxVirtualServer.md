---
title: "Linux Virtual Server"
type: entity
tags: [networking, linux, load-balancing]
sources:
  - jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[LinuxVirtualServer]] is the LVS load-balancing system discussed in the source as a packet-forwarding foundation for DR, NAT, full NAT, ENAT, and IP tunneling modes.

## Current Profile
The source presents Linux Virtual Server as a Layer 4 load-balancing foundation whose behavior is best understood through packet rewriting and routing paths. It can be deployed in multiple modes, each moving the bottleneck and operational burden to a different place: the load balancer, the real server's network configuration, host-side kernel modules, or the surrounding routing fabric.

In Alibaba Cloud's context, LVS-like infrastructure becomes part of a larger SLB/NGLB product stack. Dynamic routing, session synchronization, DPDK packet processing, cache-line tuning, rate-limit sharding, and flow offload are used to scale the basic forwarding model.

## Key Characteristics
- Provides a virtual-IP front end that selects real servers for backend traffic.
- Supports several forwarding modes with different address-rewrite and return-path properties.
- Can become a bottleneck when both request and response traffic pass through it.
- Depends on surrounding network topology, gateway placement, ARP behavior, tunneling, or host modules depending on mode.
- Can be productized with routing protocols, session synchronization, and high-performance packet processing.

## Evidence
- Forwarding role: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] defines LVS through VIP, RIP, real server, and director terminology.
- Mode diversity: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] compares DR, NAT, full NAT, ENAT, and IP TUN.
- Bottleneck risk: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] repeatedly notes that modes sending both directions through LVS can overload it.
- Topology dependence: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] ties DR to L2 adjacency, NAT to gateway placement, and full NAT/TUN to L3 reachability or encapsulation.
- Product scaling: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes OSPF/ECMP/BGP routing, session sync, DPDK, huge pages, and flow offload in cloud LVS evolution.

## Qualifications
The wiki currently knows Linux Virtual Server only through Plantegg's explanatory article, not through upstream LVS documentation or independent production benchmarks.

## What Changed
- Created the Linux Virtual Server entity page.
- Captured LVS as both a forwarding-mode taxonomy and a cloud-scale packet-processing foundation.

## Relationships
- [[LVSForwardingModes]] - Linux Virtual Server is the system whose modes this concept names.
- [[NetworkLoadBalancing]] - LVS is presented as a concrete network load-balancing implementation.
- [[AlibabaCloud]] - Alibaba Cloud's SLB/NGLB details show how LVS-like designs are productized and optimized.

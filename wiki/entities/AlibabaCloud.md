---
title: "Alibaba Cloud"
type: entity
tags: [cloud, networking, load-balancing]
sources:
  - jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[AlibabaCloud]] is the cloud provider used in the source to illustrate how LVS-style packet forwarding becomes SLB/NGLB load-balancing infrastructure.

## Current Profile
The source presents Alibaba Cloud through its SLB and NGLB networking products rather than as a general company profile. Its role is to show why a cloud provider cannot stop at textbook LVS modes: public cloud load balancing needs client-IP recovery, backend compatibility, cross-VLAN reachability, high availability, session continuity, and high-throughput packet processing.

Alibaba Cloud's implementation examples include FNAT behavior, TOA/VTOA/CTK-style modules, dynamic route advertisement for disaster recovery, ECMP across LVS nodes, session synchronization for long connections, DPDK acceleration, cache-line and prefetch tuning, sharded rate limiting, and hardware flow offload for large single flows.

## Key Characteristics
- Provides SLB/NGLB-style load-balancing products built around LVS-like forwarding behavior.
- Uses auxiliary modules to preserve or recover client and VIP information across translated traffic.
- Treats high availability as a routing and session-continuity problem, not just a process uptime problem.
- Optimizes packet forwarding through DPDK, memory layout tuning, and flow offload.
- Shows how cloud products trade convenience against extra provider-controlled complexity.

## Evidence
- SLB FNAT: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] says Alibaba Cloud SLB uses full NAT-like behavior and provider-side mechanisms to expose the real client IP.
- Host modules: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes TOA, VTOA, CTK, and VCTK modules for FNAT, ENAT, and NGLB scenarios.
- High availability: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes BGP/OSPF route advertisement and primary/backup datacenter behavior.
- Node balancing: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes ECMP across LVS nodes and session synchronization to preserve long connections after node failure.
- Performance work: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes DPDK, huge pages, cache-line layout, prefetching, lock-reduced token buckets, and offload for large flows.

## Qualifications
This page reflects Alibaba Cloud only as described in one source about load-balancing architecture. It should not be read as a complete profile of Alibaba Cloud's company, product line, or current 2026 behavior.

## What Changed
- Created the Alibaba Cloud entity page from the LVS forwarding source.
- Captured SLB/NGLB as an example of cloud productization of network load balancing.

## Relationships
- [[LinuxVirtualServer]] - Alibaba Cloud's SLB/NGLB examples are presented as LVS-like packet-forwarding infrastructure.
- [[NetworkLoadBalancing]] - Alibaba Cloud provides the cloud-product case study for the concept.
- [[LVSForwardingModes]] - Alibaba Cloud examples extend full NAT, ENAT, and NGLB-style forwarding tradeoffs.

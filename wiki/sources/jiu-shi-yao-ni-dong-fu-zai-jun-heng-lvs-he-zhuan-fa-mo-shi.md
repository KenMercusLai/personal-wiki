---
title: "就是要你懂负载均衡--lvs和转发模式"
type: source
tags: [networking, load-balancing, lvs, cloud-infrastructure]
date: 2019-06-20
source_file: /mnt/ken_personal_wiki/Articles/就是要你懂负载均衡--lvs和转发模式.md
---

## Summary
[[Plantegg]] explains [[LinuxVirtualServer]] forwarding modes by following packet address changes rather than memorizing deployment slogans. The article compares DR, NAT, full NAT, ENAT, and IP TUN as tradeoffs in [[NetworkLoadBalancing]] and [[LVSForwardingModes]], then uses [[AlibabaCloud]] SLB/NGLB details to show why public-cloud load balancing must balance performance, client-IP visibility, deployment flexibility, and high availability.

## Key Claims
- [[LVSForwardingModes]] are easiest to understand by tracing packet source IP, destination IP, MAC address, and return path.
- DR has the best forwarding performance because only inbound packets pass through LVS and LVS mainly changes the destination MAC address.
- NAT is simple and supports port mapping, but both request and response traffic must traverse LVS and LVS generally needs to be the RS gateway.
- Full NAT removes the same-VLAN requirement by rewriting both source and destination IPs, but hides the client IP from the real server unless an auxiliary mechanism restores it.
- ENAT and IP TUN try to combine flexible routing with direct server return, but both depend on extra host-side kernel modules or encapsulation support.
- [[AlibabaCloud]] SLB/NGLB adds provider-side modules, dynamic routing, session synchronization, DPDK, and flow offload to turn the basic LVS model into a cloud product.

## Key Quotes
> "DR模式性能最好但是部署不灵活；NAT性能差部署灵活多了" - on why rote mode comparisons hide the packet-flow reasons.

> "这就是基础知识的力量" - on deriving tradeoffs from packet movement.

## Connections
- [[Plantegg]] - author of the technical explanation.
- [[LinuxVirtualServer]] - the core load-balancing system whose forwarding modes are compared.
- [[NetworkLoadBalancing]] - the article's broader infrastructure problem: distributing traffic without creating a bottleneck or routing mismatch.
- [[LVSForwardingModes]] - the article's main taxonomy of DR, NAT, full NAT, ENAT, and IP TUN.
- [[AlibabaCloud]] - cloud provider whose SLB/NGLB implementation shows how LVS-like ideas are productized.

## Contradictions
- No direct contradictions with existing wiki content. The source extends the infrastructure thread from AI inference routing into lower-level network packet forwarding.

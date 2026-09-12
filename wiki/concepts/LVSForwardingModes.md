---
title: "LVS Forwarding Modes"
type: concept
tags: [networking, lvs, load-balancing]
sources:
  - jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[LVSForwardingModes]] are the packet-forwarding strategies used by [[LinuxVirtualServer]] and LVS-like systems, including DR, NAT, full NAT, ENAT, and IP tunneling.

## Current Synthesis
The source treats LVS forwarding modes as different answers to the same routing puzzle: after a client targets a virtual IP, how does the selected real server receive the request and send a response that the client will accept? DR answers by changing only the destination MAC address and letting the real server reply directly from the VIP, which is fast but requires L2 adjacency and careful ARP/VIP setup. NAT answers by changing the request destination IP and using LVS as the return-path gateway, which is simpler but makes LVS carry both directions of traffic.

Full NAT, ENAT, and IP TUN relax different constraints at different costs. Full NAT rewrites both source and destination addresses so LVS and real servers only need L3 reachability, but the real server loses the original client IP unless extra metadata or modules restore it. ENAT pushes reply rewriting to the real-server side so response traffic can bypass LVS, while IP TUN encapsulates the original packet so cross-VLAN real servers can decapsulate and directly return. These modes show why deployment flexibility usually requires extra translation, encapsulation, or kernel support.

## Key Claims
- DR changes the destination MAC address while preserving the packet's VIP destination, so the real server must be prepared to accept VIP traffic locally.
- DR performs well because LVS handles only inbound requests and response packets return directly to the client.
- NAT supports simpler setup and port mapping, but LVS must stay on the return path to rewrite backend replies into VIP replies.
- Full NAT removes the same-VLAN/gateway requirement by rewriting both client-facing and backend-facing addresses.
- Full NAT hides the client IP from the real server unless TCP-option or kernel-module support restores it.
- ENAT and IP TUN preserve more flexible backend placement while avoiding normal response traffic through LVS, at the cost of custom modules or encapsulation.

## Evidence
- DR behavior: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] says LVS changes the destination MAC, real servers share the VIP on loopback, and replies go directly to the client.
- NAT behavior: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] explains that LVS rewrites the destination IP toward the real server and later rewrites the reply source IP back to the VIP.
- Full NAT behavior: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] shows LVS rewriting both source and destination IPs so the real server's response is routed back to LVS by IP routing rather than by gateway placement.
- ENAT behavior: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes carrying client information in TCP options and using CTK-style backend modules to rewrite replies before direct return.
- IP TUN behavior: [[jiu-shi-yao-ni-dong-fu-zai-jun-heng-lvs-he-zhuan-fa-mo-shi]] describes IP-in-IP encapsulation, backend IPIP decapsulation, VIP on tunl0, and direct response to the client.

## Counterevidence & Qualifications
The source emphasizes forwarding mechanics and Alibaba Cloud practice rather than covering every scheduler, operational failure mode, security concern, or modern cloud-provider variation. The ENAT, TOA/VTOA, CTK, and NGLB details are especially provider-specific.

## What Changed
- Created a dedicated concept page for LVS forwarding-mode tradeoffs.
- Added DR, NAT, full NAT, ENAT, and IP TUN as packet-flow patterns rather than memorized mode names.
- Added client-IP visibility and host-side module requirements as qualifications.

## Related Concepts
- [[NetworkLoadBalancing]] - LVS forwarding modes are one concrete implementation family for network load balancing.
- [[LinuxVirtualServer]] - LVS is the system whose forwarding modes are being described.
- [[QUIC]] - both areas expose how load balancers can depend on packet identity and routing assumptions.
- [[InferenceLoadBalancing]] - both are load-balancing domains, but the unit of routing differs: packets and connections here, tokenized inference workload there.

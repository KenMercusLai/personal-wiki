---
title: "L2VPN"
type: concept
tags: [networking, mpls, vpn]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[L2VPN]] is a layer-2 VPN service family that carries Ethernet or VLAN attachment-circuit traffic across a provider network using pseudowires.

## Current Synthesis
The source presents L2VPN as a packet-encapsulation and service-compatibility problem. The important behavior is not just that two sites are connected, but how VLAN tags, QoS priority, MPLS labels, control words, and pseudowire types preserve or transform what the customer edge sends.

VPLS and EoMPLS sit inside this broader family with different operational constraints. In the VPLS tests, IOS XR passthrough behavior prevents dummy VLAN insertion; in the EoMPLS Type 4 tests, IOS XR adds a VLAN ID 0 tag that carries 802.1p priority when VLAN rewrite would otherwise remove the customer tag.

## Key Claims
- L2VPN behavior depends on pseudowire type, transport mode, and attachment-circuit rewrite rules.
- VLAN tag handling matters because it can carry QoS information through 802.1p priority bits.
- Type 4 and Type 5 pseudowires differ in how they handle Ethernet VLAN service cases.
- VPLS and EoMPLS can expose different transport-mode constraints under IOS XR.
- Packet captures are necessary to verify where tags, control words, and labels actually appear.

## Evidence
- Service family: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] tests VPLS and EoMPLS under an L2VPN configuration.
- VLAN/QoS handling: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] tracks 802.1p priority through visible VLAN tags and dummy VLAN tags.
- Transport modes: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] compares Type 5, Type 4 passthrough, and Type 4 `transport-mode vlan`.
- Packet verification: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] uses Wireshark screenshots to locate MPLS labels, control word, Ethernet header, and VLAN tag.

## Counterevidence & Qualifications
The source focuses on Cisco IOS XR lab behavior, not a cross-vendor taxonomy of all L2VPN implementations. It also uses dated platform behavior, so current deployments may require vendor documentation and fresh captures.

## What Changed
- Created the L2VPN concept from a Cisco IOS XR dummy VLAN investigation.

## Related Concepts
- [[VPLS]] - VPLS is one L2VPN service model tested in the source.
- [[EoMPLS]] - EoMPLS is another L2VPN service model tested in the source.
- [[PseudowireTransportTypes]] - pseudowire type controls Ethernet/VLAN encapsulation behavior.
- [[L2VPNDummyVLAN]] - dummy VLAN is a tag-handling mechanism inside the L2VPN problem.
- [[NetworkLoadBalancing]] - both require packet-path reasoning, but L2VPN focuses on layer-2 service transport rather than backend traffic distribution.

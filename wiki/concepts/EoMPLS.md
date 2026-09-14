---
title: "EoMPLS"
type: concept
tags: [networking, l2vpn, mpls]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[EoMPLS]] is an Ethernet-over-MPLS L2VPN service that carries Ethernet or VLAN attachment-circuit traffic over an MPLS pseudowire.

## Current Synthesis
The source uses EoMPLS as the successful test case for observing IOS XR dummy VLAN behavior. After VPLS passthrough fails to reveal the dummy tag, the author switches to EoMPLS Type 4 with `transport-mode vlan` and captures the expected VLAN ID 0 tag carrying 802.1p priority.

EoMPLS also clarifies what the dummy VLAN can and cannot do. It preserves priority metadata, but because the tag appears in the ordinary Ethernet VLAN-tag location after the L2 header, it cannot replace the control word or FAT label for packet ordering or load-balancing behavior.

## Key Claims
- EoMPLS Type 4 with `transport-mode vlan` can reveal dummy VLAN insertion in the tested IOS XR setup.
- The dummy VLAN appears as an 802.1Q tag with VLAN ID 0 and priority copied from the original traffic.
- Control word and FAT label remain separate mechanisms from dummy VLAN priority preservation.
- The successful test uses packet capture after configuring Type 4 transport mode in the pseudowire class.
- EoMPLS is useful when the two ends use different VLAN IDs and VLAN rewrite is needed.

## Evidence
- Successful configuration: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows `pw-class CW` with `transport-mode vlan`.
- Packet capture: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows the MPLS label stack, control word, Ethernet header, and 802.1Q tag with PRI 5 and ID 0.
- Mechanism separation: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] captures FAT label and control word before the dummy VLAN appears, then concludes the dummy VLAN cannot solve the load-balancing/order issue.
- VLAN rewrite need: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] explains Type 5 works when both sides have the same VLAN, while Type 4 is needed when VLANs differ.

## Counterevidence & Qualifications
The source's EoMPLS conclusion is based on one lab setup and IOS XR platform behavior. It establishes the observed packet layout in that test, not a universal guarantee for all MPLS devices.

## What Changed
- Created the EoMPLS concept as the positive dummy VLAN test case.

## Related Concepts
- [[L2VPN]] - EoMPLS is a point-to-point L2VPN service model in the source.
- [[VPLS]] - VPLS is the contrasting case where passthrough mode prevents dummy VLAN insertion.
- [[L2VPNDummyVLAN]] - EoMPLS Type 4 produces the observed dummy VLAN tag.
- [[PseudowireTransportTypes]] - Type 4 transport mode is central to the EoMPLS result.

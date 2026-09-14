---
title: "L2VPN Dummy VLAN"
type: concept
tags: [networking, l2vpn, vlan, qos]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[L2VPNDummyVLAN]] is a VLAN ID 0 tag inserted in some L2VPN pseudowire cases to carry 802.1p priority when a normal customer VLAN tag has been stripped by rewrite.

## Current Synthesis
The source narrows dummy VLAN from a vague vendor behavior to a concrete packet artifact. It is not a real customer VLAN and does not identify a customer broadcast domain. Its useful content is the priority metadata, visible in Wireshark as an 802.1Q tag with PRI 5, CFI 0, and ID 0.

The investigation also bounds when the behavior appears. IOS XR VPLS Type 4 passthrough does not add the dummy tag, and the tested VPLS configuration rejects non-passthrough Type 4. EoMPLS Type 4 with `transport-mode vlan`, by contrast, produces the dummy VLAN after VLAN rewrite.

The packet location matters. The dummy VLAN sits where a normal VLAN tag would sit in the Ethernet frame, not between the MPLS label stack and the L2 header, so it cannot substitute for the control word or FAT label in load-balancing/order problems.

## Key Claims
- A dummy VLAN is VLAN ID 0 used to carry 802.1p priority, not a customer VLAN membership marker.
- Dummy VLAN insertion depends on pseudowire type and platform-supported transport mode.
- IOS XR VPLS passthrough does not insert the dummy VLAN in the tested configuration.
- IOS XR EoMPLS Type 4 can insert the dummy VLAN after rewrite strips the original VLAN tag.
- The dummy VLAN preserves QoS metadata but does not change MPLS label-stack placement or solve control-word/FAT-label ordering concerns.

## Evidence
- Meaning of the tag: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] describes dummy VLAN as a tag that carries QoS fields and occupies a VLAN-tag slot without being a real VLAN.
- VPLS negative case: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows VPLS Type 4 passthrough captures without dummy VLAN insertion after rewrite.
- EoMPLS positive case: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows Wireshark decoding an 802.1Q tag with PRI 5, CFI 0, and ID 0.
- Packet placement: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] notes that the dummy VLAN appears in the same place as the original VLAN rather than between the L2 header and bottom MPLS label.
- QoS verification: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows the far-end output using VLAN 10 while retaining PRI 5.

## Counterevidence & Qualifications
The article's claims are tied to Cisco IOS XR lab behavior and dated platform defaults. It also distinguishes passthrough Type 4 from Type 4 with `transport-mode vlan`, so a shorthand statement that "Type 4 adds dummy VLAN" would be too broad.

## What Changed
- Created the concept page for dummy VLAN as an evidence-backed L2VPN packet artifact.

## Related Concepts
- [[L2VPN]] - dummy VLAN is a tag-handling mechanism inside L2VPN pseudowires.
- [[VPLS]] - VPLS passthrough is the negative case in the source.
- [[EoMPLS]] - EoMPLS Type 4 is the positive case in the source.
- [[PseudowireTransportTypes]] - dummy VLAN behavior depends on Type 4/Type 5 and passthrough distinctions.
- [[NetworkLoadBalancing]] - both require packet placement reasoning, but dummy VLAN carries QoS rather than balancing traffic.

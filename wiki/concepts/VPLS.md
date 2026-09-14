---
title: "VPLS"
type: concept
tags: [networking, l2vpn, mpls]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[VPLS]] is a multipoint Ethernet L2VPN service that uses provider pseudowires to make separated customer sites behave like they share a layer-2 domain.

## Current Synthesis
In the source, VPLS is the first testing ground for dummy VLAN expectations. Type 5 and Type 4 passthrough both preserve visible VLAN priority when the VLAN tag is present, but IOS XR VPLS passthrough does not add a dummy VLAN after rewrite removes the tag.

The key operational lesson is that the word "Type 4" is not enough. IOS XR's VPLS support in the tested case is constrained to ethernet/vlan passthrough mode, and passthrough is explicitly the mode that does not insert the dummy tag.

## Key Claims
- VPLS can carry VLAN-tagged traffic across a provider MPLS network.
- IOS XR VPLS Type 4 passthrough does not insert a dummy VLAN tag in the tested setup.
- IOS XR rejects non-passthrough Type 4 transport mode for VPLS in the article's configuration.
- Preserving customer QoS in IOS XR VPLS may require 1-to-1 VLAN rewrite rather than relying on dummy VLAN insertion.
- VPLS behavior must be verified against the platform's supported transport modes, not inferred from pseudowire type names alone.

## Evidence
- Initial topology: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows a VPLS BGP auto-discovery plus LDP-signaled topology between ASR9K routers through a 7609.
- Passthrough result: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows Type 4 passthrough packet captures carrying PRI 5 on VLAN 20 when no rewrite is used.
- Rewrite result: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows the rewrite plus passthrough case still lacking a dummy VLAN tag.
- Commit constraint: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] includes the IOS XR error that only ethernet/vlan passthrough transport mode is supported in VPLS.
- QoS workaround: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] says IOS XR VPLS can preserve customer QoS by using 1-to-1 rewrite.

## Counterevidence & Qualifications
The source documents one Cisco IOS XR lab path and does not claim that all VPLS implementations reject non-passthrough Type 4 or handle dummy tags identically.

## What Changed
- Created the VPLS concept with a transport-mode qualification for dummy VLAN behavior.

## Related Concepts
- [[L2VPN]] - VPLS is a multipoint L2VPN service.
- [[EoMPLS]] - both are tested L2VPN forms, but EoMPLS exposes the dummy VLAN in this source.
- [[PseudowireTransportTypes]] - VPLS behavior depends on pseudowire type and passthrough mode.
- [[L2VPNDummyVLAN]] - VPLS passthrough is the case where the expected dummy VLAN does not appear.

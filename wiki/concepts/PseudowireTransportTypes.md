---
title: "Pseudowire Transport Types"
type: concept
tags: [networking, mpls, l2vpn]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[PseudowireTransportTypes]] are service-type and transport-mode choices that define how an MPLS pseudowire carries Ethernet or VLAN frames.

## Current Synthesis
The source uses Type 4 and Type 5 as practical categories for VLAN handling. Type 5 can preserve VLAN tags when both ends use the same VLAN, but it is insufficient when the two ends use different VLAN IDs and rewrite is required. Type 4 is the needed form for VLAN service behavior, but IOS XR's exact transport mode still controls whether a dummy VLAN appears.

The important refinement is the passthrough distinction. A Type 4 passthrough service can keep an original dot1q tag but does not insert a dummy tag. In EoMPLS, Type 4 with `transport-mode vlan` produces the VLAN ID 0 dummy tag after rewrite; in VPLS, the tested platform rejects the non-passthrough configuration.

## Key Claims
- Type 5 Ethernet pseudowire behavior can pass VLAN-tagged frames when both service ends match.
- Type 4 Ethernet VLAN pseudowire behavior is needed for cases involving different VLAN IDs or VLAN rewrite.
- Type 4 passthrough is special because it does not insert a dummy VLAN tag.
- Platform support constrains which transport-mode choices are valid for VPLS versus EoMPLS.
- Pseudowire type must be interpreted together with rewrite rules, control word/FAT label behavior, and packet captures.

## Evidence
- Type 5 baseline: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows Type 5 carrying VLAN 20 with PRI 5 when no rewrite is used.
- Type 4 passthrough: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows passthrough preserving the tag when present but not adding a dummy VLAN after rewrite.
- EoMPLS Type 4: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows `transport-mode vlan` leading to a PW type of Ethernet VLAN and a captured dummy VLAN tag.
- VPLS constraint: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] includes IOS XR's rejection of non-passthrough Type 4 for VPLS.
- Default table: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] records a 2015 platform table where default VC type varies by service and platform.

## Counterevidence & Qualifications
The source's type discussion is vendor- and time-specific. The 2015 default VC-type table should be treated as historical evidence, not current vendor documentation.

## What Changed
- Created the concept page for Type 4/Type 5 pseudowire transport distinctions.

## Related Concepts
- [[L2VPN]] - pseudowire types define the encapsulation behavior for L2VPN services.
- [[VPLS]] - VPLS support constrains the transport-mode options in the source.
- [[EoMPLS]] - EoMPLS Type 4 produces the successful dummy VLAN capture.
- [[L2VPNDummyVLAN]] - dummy VLAN insertion depends on the exact pseudowire transport type.

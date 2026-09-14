---
title: "How to Sniffer Dummy VLAN on L2VPN"
type: source
tags: [networking, l2vpn, mpls, vlan, qos]
date: 2014-12-27
source_file: /mnt/ken_personal_wiki/Articles/Blog - Zhao CS - How to Sniffer Dummy VLAN on L2VPN.md
---

## Summary
[[ZhaoCS]] documents a packet-capture investigation into when [[CiscoIOSXR]] adds a [[L2VPNDummyVLAN]] in MPLS [[L2VPN]] services. The experiments show that VPLS Type 4 passthrough does not insert the dummy tag, while EoMPLS Type 4 can insert an 802.1Q tag with VLAN ID 0 that carries 802.1p priority through the pseudowire.

## Key Claims
- A dummy VLAN is not a customer VLAN; it is an 802.1Q VLAN ID 0 tag used to carry priority fields when rewrite behavior would otherwise remove the VLAN tag.
- VPLS on IOS XR supports only ethernet/vlan passthrough transport mode in the tested configuration, so it does not add the dummy VLAN tag.
- EoMPLS Type 4 with `transport-mode vlan` can produce the dummy VLAN, visible as an 802.1Q tag with PRI 5 and ID 0 after the pseudowire control word and Ethernet header.
- The dummy VLAN preserves QoS priority but cannot replace the control word or FAT label for load-balancing/order problems because it sits in the normal VLAN-tag position, not between the MPLS label stack and the L2 header.
- Type 5 works when both ends use the same VLAN, but Type 4 becomes necessary when the two attachment circuits need VLAN rewrite or different VLAN IDs.
- In IOS XR VPLS cases without dummy VLAN insertion, customer QoS can be preserved through 1-to-1 rewrite rather than expecting a dummy tag.

## Key Quotes
> "dummy VLAN传递802.1p，使两端的QOS完整" - Zhao CS on the purpose of the dummy VLAN after the successful EoMPLS capture.

> "Only ethernet/vlan passthrough transport mode is supported in VPLS" - IOS XR commit failure explaining why non-passthrough Type 4 was rejected for VPLS.

## Connections
- [[ZhaoCS]] - author of the hands-on packet-capture investigation.
- [[ZhaoCSInfo]] - publication context for the networking article.
- [[CiscoIOSXR]] - platform under test, shown through ASR9K/ASR9000 configuration and command output.
- [[L2VPN]] - service family in which VPLS and EoMPLS pseudowires are configured.
- [[VPLS]] - tested first; passthrough Type 4 does not insert the dummy VLAN.
- [[EoMPLS]] - tested second; Type 4 with `transport-mode vlan` reveals the dummy VLAN behavior.
- [[L2VPNDummyVLAN]] - central behavior: VLAN ID 0 tag carrying 802.1p priority after VLAN rewrite.
- [[PseudowireTransportTypes]] - Type 4 versus Type 5 explains the different tag-handling behavior.
- [[Cisco]] - vendor context for IOS XR and ASR9K/ASR9000 equipment.

## Contradictions
- None identified; the article qualifies rather than contradicts the wiki's existing packet-path material by showing a different layer of VLAN/MPLS encapsulation.

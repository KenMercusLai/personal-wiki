---
title: "Zhao CS"
type: entity
tags: [author, networking]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[ZhaoCS]] is the author of the [[ZhaoCSInfo]] networking article on sniffing dummy VLAN behavior in IOS XR L2VPN pseudowires.

## Current Profile
In this source, Zhao CS writes as a hands-on network practitioner. The article is organized around packet captures, IOS XR configuration attempts, and operational hypotheses about why expected dummy VLAN behavior did or did not appear.

## Key Characteristics
- Uses lab packet captures to verify vendor behavior rather than relying only on documentation.
- Focuses on MPLS L2VPN, VPLS, EoMPLS, VLAN rewrite, and QoS preservation.
- Revisits an unresolved 2013 experiment in 2014 to complete the dummy VLAN investigation.

## Evidence
- Packet-capture method: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] walks through multiple Wireshark observations before accepting the final EoMPLS Type 4 result.
- Domain focus: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] discusses IOS XR L2VPN configuration, pseudowire types, control word, FAT label, and 802.1p priority.
- Iterative investigation: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] states that the initial VPLS experiment happened on 2013-12-02 and the successful continuation happened on 2014-12-25.

## Qualifications
The source identifies Zhao CS as author but does not provide a broader biography, employer, or platform ownership context.

## What Changed
- Created the entity page for Zhao CS as a network-practitioner author.

## Relationships
- [[ZhaoCSInfo]] - Zhao CS publishes the article on this site.
- [[L2VPNDummyVLAN]] - Zhao CS investigates this behavior through packet captures.
- [[CiscoIOSXR]] - Zhao CS tests IOS XR configuration and packet behavior.

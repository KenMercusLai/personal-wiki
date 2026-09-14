---
title: "Cisco IOS XR"
type: entity
tags: [networking, operating-system, cisco]
sources:
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[CiscoIOSXR]] is the Cisco network operating system shown in the source through ASR9K/ASR9000 L2VPN configuration, show commands, and commit validation.

## Current Profile
The article treats IOS XR as the operating environment where L2VPN pseudowire transport mode choices determine VLAN-tag handling. Its behavior is concrete rather than abstract: VPLS rejects non-passthrough Type 4 in the tested configuration, while EoMPLS Type 4 with `transport-mode vlan` can expose a dummy VLAN tag carrying 802.1p priority.

## Key Characteristics
- Provides IOS XR L2VPN configuration surfaces such as bridge groups, bridge domains, VFI neighbors, pw-classes, and transport modes.
- Enforces platform semantics at commit time, including rejecting unsupported VPLS transport-mode combinations.
- On ASR9K/ASR9000 in the source, can add a dummy VLAN in EoMPLS Type 4 but not in VPLS passthrough mode.

## Evidence
- Configuration surface: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows IOS XR `l2vpn`, `bridge group`, `bridge-domain`, `vfi`, `pw-class`, and `transport-mode vlan` configuration.
- Commit validation: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] includes an IOS XR failure saying only ethernet/vlan passthrough transport mode is supported in VPLS.
- Packet behavior: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows EoMPLS Type 4 packet captures where a VLAN ID 0 dummy tag carries PRI 5.

## Qualifications
The source is a dated lab investigation from 2014 with a 2015 VC-type update table. It should not be read as current coverage for every IOS XR release, platform, or feature combination.

## What Changed
- Created the IOS XR entity around L2VPN pseudowire and dummy VLAN behavior.

## Relationships
- [[Cisco]] - IOS XR is a Cisco platform context in the source.
- [[L2VPN]] - IOS XR is used to configure the L2VPN examples.
- [[VPLS]] - IOS XR constrains VPLS transport mode in the tested case.
- [[EoMPLS]] - IOS XR exposes dummy VLAN behavior in the successful EoMPLS Type 4 test.

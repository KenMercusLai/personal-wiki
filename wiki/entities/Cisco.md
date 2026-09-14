---
title: "Cisco"
type: entity
tags: [networking, vendor, infrastructure]
sources:
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[Cisco]] is represented in the wiki as both a network-equipment vendor target for automation tooling and the vendor context for IOS XR L2VPN behavior.

## Current Profile
Cisco appears in two roles. At the ecosystem level, it is a major network-equipment target that helps make multivendor automation meaningful. At the packet-behavior level, ASR9K/ASR9000 equipment running [[CiscoIOSXR]] becomes a concrete lab environment for testing L2VPN pseudowire transport modes, VPLS constraints, EoMPLS behavior, and dummy VLAN insertion.

The combined profile is therefore pragmatic rather than brand-general. Cisco is not evaluated as a whole company; it is represented through platform surfaces that operators automate, configure, validate, and inspect when encapsulation behavior depends on labels, control words, VLAN tags, and QoS bits.

## Key Characteristics
- Appears as a supported network-equipment target.
- Helps establish the multivendor framing of Ansible's network-automation launch.
- Provides the IOS XR/ASR platform context for a detailed L2VPN dummy VLAN investigation.
- Shows platform-specific constraints around VPLS transport mode and EoMPLS Type 4 behavior.
- Requires packet-level verification when operational behavior depends on labels, control words, VLAN tags, and QoS bits.

## Evidence
- Launch support: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] names Cisco kit as supported by Ansible's networking framework.
- Multivendor claim: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] frames networking teams as able to use Ansible in multivendor environments.
- IOS XR platform behavior: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] uses Cisco ASR9K/ASR9000 IOS XR configuration and command output to test L2VPN behavior.
- VPLS constraint: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows IOS XR rejecting non-passthrough Type 4 transport mode for VPLS.
- EoMPLS dummy VLAN: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows a Cisco IOS XR EoMPLS Type 4 capture where VLAN ID 0 carries PRI 5.

## Qualifications
The Ansible source does not specify which Cisco platforms, operating systems, or feature areas were supported. The Zhao CS source is a 2014 lab investigation with a 2015 update table, so its platform details should not be treated as current coverage for all Cisco devices or IOS XR releases.

## What Changed
- Added Cisco IOS XR/ASR L2VPN behavior as a second Cisco evidence path.
- Qualified Cisco's profile by distinguishing generic automation support from specific packet-level platform behavior.

## Relationships
- [[Ansible]] - Cisco is a supported network target in Ansible's launch list.
- [[NetworkAutomation]] - Cisco represents one vendor surface for multivendor automation.
- [[CiscoIOSXR]] - Cisco IOS XR is the platform under test in the dummy VLAN source.
- [[L2VPN]] - Cisco equipment is used to test L2VPN encapsulation behavior.
- [[L2VPNDummyVLAN]] - Cisco IOS XR is the source's observed implementation context for dummy VLAN behavior.

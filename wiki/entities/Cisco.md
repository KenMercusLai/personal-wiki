---
title: "Cisco"
type: entity
tags: [networking, vendor, infrastructure]
sources:
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
  - cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[Cisco]] is represented in the wiki as a network-equipment vendor, an automation target, the platform context for IOS XR packet behavior, and the author of prescriptive SD-WAN control-plane trust guidance.

## Current Profile
Cisco appears in three roles. At the ecosystem level, it is a major network-equipment target that helps make multivendor automation meaningful. At the packet-behavior level, ASR9K/ASR9000 equipment running [[CiscoIOSXR]] becomes a concrete lab environment for testing L2VPN pseudowire transport modes, VPLS constraints, EoMPLS behavior, and dummy VLAN insertion. At the system-design level, Cisco documents how [[CiscoCatalystSDWAN]] combines certificate roots, signed device identities, organization matching, challenge-response, and authorized inventories across its control complex and WAN Edge fleet.

The combined profile is therefore pragmatic rather than brand-general. Cisco is not evaluated as a whole company; it is represented through platform surfaces that operators automate, configure, validate, inspect, and renew. The SD-WAN source also makes vendor guidance itself part of the evidence, so its recommendations and compatibility claims require release-aware verification rather than being treated as independent security evaluation.

## Key Characteristics
- Appears as a supported network-equipment target.
- Helps establish the multivendor framing of Ansible's network-automation launch.
- Provides the IOS XR/ASR platform context for a detailed L2VPN dummy VLAN investigation.
- Shows platform-specific constraints around VPLS transport mode and EoMPLS Type 4 behavior.
- Requires packet-level verification when operational behavior depends on labels, control words, VLAN tags, and QoS bits.
- Documents an SD-WAN trust architecture that separates certificate identity from inventory-based authorization.
- Recommends Cisco PKI while retaining manual Cisco and enterprise-CA deployment paths.

## Evidence
- Launch support: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] names Cisco kit as supported by Ansible's networking framework.
- Multivendor claim: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] frames networking teams as able to use Ansible in multivendor environments.
- IOS XR platform behavior: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] uses Cisco ASR9K/ASR9000 IOS XR configuration and command output to test L2VPN behavior.
- VPLS constraint: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows IOS XR rejecting non-passthrough Type 4 transport mode for VPLS.
- EoMPLS dummy VLAN: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows a Cisco IOS XR EoMPLS Type 4 capture where VLAN ID 0 carries PRI 5.
- SD-WAN trust model: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] combines CA-chain validation, organization checks, protected device identities, signed challenges, and authorized lists before DTLS/TLS control sessions form.
- Certificate operations: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] recommends automated Cisco PKI and documents manual Cisco PKI, enterprise-CA, root-chain migration, status, invalidation, and staged renewal paths.

## Qualifications
The Ansible source does not specify which Cisco platforms, operating systems, or feature areas were supported. The Zhao CS source is a 2014 lab investigation with a 2015 update table, so its platform details should not be treated as current coverage for all Cisco devices or IOS XR releases. The SD-WAN source is Cisco-authored, mixes procedures across historical releases, and does not independently test the security or availability of its recommended architecture.

## What Changed
- Added Cisco Catalyst SD-WAN trust, authorization, and certificate lifecycle as a third evidence path.
- Distinguished vendor-prescribed operational design from independent evaluation.

## Relationships
- [[Ansible]] - Cisco is a supported network target in Ansible's launch list.
- [[NetworkAutomation]] - Cisco represents one vendor surface for multivendor automation.
- [[CiscoIOSXR]] - Cisco IOS XR is the platform under test in the dummy VLAN source.
- [[L2VPN]] - Cisco equipment is used to test L2VPN encapsulation behavior.
- [[L2VPNDummyVLAN]] - Cisco IOS XR is the source's observed implementation context for dummy VLAN behavior.
- [[CiscoCatalystSDWAN]] - Cisco develops and documents this overlay architecture.
- [[CertificateBasedDeviceIdentity]] - Cisco's guide supplies a concrete CA-root and signed-device implementation.
- [[AuthorizedDeviceLists]] - Cisco's Manager distributes explicit component and WAN Edge admission inventories.

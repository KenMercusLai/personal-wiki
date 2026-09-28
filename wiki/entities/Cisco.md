---
title: "Cisco"
type: entity
tags: [networking, vendor, infrastructure]
sources:
  - ansible-charges-into-network-automation-with-cisco-juniper-the-register
  - blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn
  - cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide
  - enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog
  - from-campus-drive-to-cisco-our-journey-with-appdynamics
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Overview
[[Cisco]] is represented in the wiki as a network-equipment vendor, an automation target and publisher, the platform context for IOS XR packet behavior, the author of prescriptive SD-WAN control-plane trust guidance, and the customer-acquirer in [[AppDynamics]]' transaction story.

## Current Profile
Cisco appears in five related roles. At the ecosystem level, it is a major network-equipment target that helps make multivendor automation meaningful. As an automation publisher, it describes `nxos_command`, `nxos_config`, and `nxos_template` for [[CiscoNXOS]] on [[CiscoNexus]], with SSH or NX-API transport and examples spanning Day 0 through Day 2 work. At the packet-behavior level, ASR9K/ASR9000 equipment running [[CiscoIOSXR]] becomes a concrete lab environment for testing L2VPN pseudowire modes, VPLS constraints, EoMPLS behavior, and dummy VLAN insertion. At the system-design level, Cisco documents how [[CiscoCatalystSDWAN]] combines certificate roots, signed device identities, organization matching, challenge-response, and authorized inventories. At the corporate-strategy level, an AppDynamics investor says Cisco moved from being a significant customer to proposing an acquisition during the software company's IPO roadshow, with application-plus-infrastructure analytics as the stated rationale.

The combined profile is therefore pragmatic rather than brand-general. Cisco is not evaluated as a whole company; it is represented through platform surfaces that operators automate, configure, validate, inspect, and renew, plus one investor-authored acquisition account. Vendor guidance and transaction advocacy both require independent and time-aware verification.

## Key Characteristics
- Appears as a supported network-equipment target that helps establish the multivendor framing of Ansible's launch.
- Publishes Cisco-specific Ansible guidance for NX-OS commands, configurations, templates, transports, and credentials.
- Provides the IOS XR/ASR platform context for a detailed L2VPN dummy VLAN investigation.
- Shows platform-specific constraints around VPLS transport mode and EoMPLS Type 4 behavior.
- Requires packet-level verification when operational behavior depends on labels, control words, VLAN tags, and QoS bits.
- Documents an SD-WAN trust architecture that separates certificate identity from inventory-based authorization and supports multiple PKI paths.
- Appears as an enterprise-software customer whose acquisition proposal was framed around joining application and infrastructure analytics.

## Evidence
- Launch support: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] names Cisco kit as supported by Ansible's networking framework.
- Multivendor claim: [[ansible-charges-into-network-automation-with-cisco-juniper-the-register]] frames networking teams as able to use Ansible in multivendor environments.
- NX-OS automation: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] names three Ansible 2.0 modules, SSH and NX-API transports, and Day 0/1/2 examples for Nexus devices.
- Credential claim: [[enabling-devops-approach-with-cisco-nx-os-and-ansible-cisco-blog]] says jump-host delegation and managed SSH keys can avoid keeping passwords in Ansible configuration files.
- IOS XR platform behavior: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] uses Cisco ASR9K/ASR9000 IOS XR configuration and command output to test L2VPN behavior.
- VPLS constraint: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows IOS XR rejecting non-passthrough Type 4 transport mode for VPLS.
- EoMPLS dummy VLAN: [[blog-zhao-cs-how-to-sniffer-dummy-vlan-on-l2vpn]] shows a Cisco IOS XR EoMPLS Type 4 capture where VLAN ID 0 carries PRI 5.
- SD-WAN trust model: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] combines CA-chain validation, organization checks, protected device identities, signed challenges, and authorized lists before DTLS/TLS control sessions form.
- Certificate operations: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] recommends automated Cisco PKI and documents manual Cisco PKI, enterprise-CA, root-chain migration, status, invalidation, and staged renewal paths.
- Customer-to-acquirer path: [[from-campus-drive-to-cisco-our-journey-with-appdynamics]] describes Cisco as a significant AppDynamics customer before its CEO proposed a merger during the IPO roadshow.
- Transaction rationale: [[from-campus-drive-to-cisco-our-journey-with-appdynamics]] attributes to the transaction a plan to combine application and infrastructure analytics using Cisco's reach and resources.

## Qualifications
The Register's Ansible source does not specify which Cisco platforms, operating systems, or feature areas were supported; Cisco's own post narrows one path to Nexus and NX-OS but is promotional, historically tied to early Ansible releases, and does not independently validate outcomes. The Zhao CS source is a 2014 lab investigation with a 2015 update table and should not be generalized to all Cisco platforms. The SD-WAN source is Cisco-authored and does not independently test its recommended architecture. The AppDynamics evidence is a celebratory investor account written around the transaction; it cannot establish Cisco's internal reasoning, purchase economics, integration result, or realized analytics advantage.

## What Changed
- Added Cisco's customer-to-acquirer role in AppDynamics' pre-IPO transaction.
- Added the attributed application-plus-infrastructure analytics rationale while preserving the absence of integration outcomes.

## Relationships
- [[Ansible]] - Cisco is a supported network target in Ansible's launch list.
- [[NetworkAutomation]] - Cisco represents one vendor surface for multivendor automation.
- [[CiscoNXOS]] - Cisco publishes the operating-system-specific automation guidance.
- [[CiscoNexus]] - Cisco positions Nexus as the shared platform across ACI and direct NX-OS operation.
- [[CiscoIOSXR]] - Cisco IOS XR is the platform under test in the dummy VLAN source.
- [[L2VPN]] - Cisco equipment is used to test L2VPN encapsulation behavior.
- [[L2VPNDummyVLAN]] - Cisco IOS XR is the source's observed implementation context for dummy VLAN behavior.
- [[CiscoCatalystSDWAN]] - Cisco develops and documents this overlay architecture.
- [[CertificateBasedDeviceIdentity]] - Cisco's guide supplies a concrete CA-root and signed-device implementation.
- [[AuthorizedDeviceLists]] - Cisco's Manager distributes explicit component and WAN Edge admission inventories.
- [[AppDynamics]] - Cisco was described as a customer before becoming the company's acquirer.
- [[SaaSLandAndExpand]] - AppDynamics' account expansion helped frame the subscription asset Cisco acquired.

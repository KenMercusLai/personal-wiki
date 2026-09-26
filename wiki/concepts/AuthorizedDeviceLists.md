---
title: "Authorized Device Lists"
type: concept
tags: [security, authorization, device-inventory, networking]
sources:
  - cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[AuthorizedDeviceLists]] are explicit inventories that map known device identities to permission to join or remain in a networked system after authentication succeeds.

## Current Synthesis
The Cisco SD-WAN guide distinguishes two inventories. Administrators create the authorized control-component list by adding Validators, Managers, and Controllers in Manager, which distributes the resulting identity set through the control complex. WAN Edge authorization originates from sales-account and controller-profile data in Plug and Play Connect, a downloaded signed provisioning file, automatic synchronization, or a supported unsigned CSV.

Device state is policy, not merely display metadata. Valid edges participate fully, staging edges establish control relationships without forwarding traffic or advertising routes, and invalid edges cannot establish control connections. Distribution and validation are separate actions: uploading or synchronizing a list does not necessarily make every edge valid until Manager sends the intended state to the Controllers.

## Key Claims
- Authentication and authorization are separate: trusted credentials identify a device, while an authorized list decides whether that identity may participate.
- Control components and WAN Edge devices have different inventory origins and distribution paths.
- Valid, staging, and invalid states permit graduated participation rather than a single binary connection flag.
- Central list distribution makes inventory freshness and Manager operations part of control-plane availability.
- Manual, synchronized, signed, and unsigned inputs create different governance and integrity assumptions.

## Evidence
- Control inventory: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] says Manager creates the authorized control-component list from administrator-added devices and distributes it to the control components.
- Edge inventory: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] describes PnP synchronization, signed file download/upload, and supported CSV input.
- Participation states: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] defines valid, staging, and invalid behavior and requires sending state to Controllers.
- Enforcement: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] shows serial/chassis checks and signed challenge verification before control connections form.

## Counterevidence & Qualifications
This page describes a vendor-specific authorized-list model rather than a universal device-authorization standard. Centralized inventories can reduce accidental admission but also create stale-data, account-governance, synchronization, credential, and availability risks. The guide does not compare compromise rates, propagation delay, revocation latency, audit quality, or signed versus unsigned inventory security, and the Validator has path-specific exceptions to some list checks.

## What Changed
- Created the concept and distinguished device identity proof from explicit inventory-based admission.

## Related Concepts
- [[CertificateBasedDeviceIdentity]] - provides the cryptographically validated identity matched against the list.
- [[CiscoCatalystSDWAN]] - supplies the control-component and WAN Edge implementation case.
- [[ZeroTrustAccess]] - shares the separation between reachability, identity evidence, and authorization policy.
- [[NetworkSegmentation]] - complements identity inventories by limiting reachable paths and blast radius.

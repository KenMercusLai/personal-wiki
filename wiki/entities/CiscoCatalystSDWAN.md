---
title: "Cisco Catalyst SD-WAN"
type: entity
tags: [networking, sd-wan, overlay, cisco]
sources:
  - cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[CiscoCatalystSDWAN]] is Cisco's software-defined WAN overlay represented here through its control-complex identity, authorization, certificate deployment, and renewal procedures.

## Current Profile
The architecture separates orchestration, management, control, and data-plane roles. The Validator securely introduces WAN Edge devices and supplies control-component locations; Manager centralizes configuration, monitoring, certificate operations, and authorized lists; Controllers distribute topology and policy; WAN Edge devices forward encrypted site traffic.

Membership is explicit rather than a consequence of network reachability. Control components and edges establish mutually authenticated DTLS/TLS sessions only after certificate-chain, organization, device-identity, and applicable allowlist checks succeed. The operational system therefore includes PKI, time, DNS, transport access, account integration, inventory distribution, device state, renewal, and recovery rather than only the three control-component applications.

## Key Characteristics
- Separates Validator, Manager, Controller, and WAN Edge responsibilities across four planes.
- Uses certificates and trusted CA chains for device identity and mutual control-session authentication.
- Adds administrator-controlled component and edge inventories as an authorization layer.
- Supports automated Cisco PKI, manual Cisco PKI, and enterprise-CA certificate workflows.
- Treats renewal and root-chain migration as staged availability-sensitive operations.

## Evidence
- Plane separation: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] maps Validator, Manager, Controller, and WAN Edge functions to orchestration, management, control, and data planes.
- Trust establishment: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] describes CA-chain validation, organization checks, protected device keys, signed challenges, and DTLS/TLS setup.
- Authorization: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] distinguishes administrator-defined control components from signed, synchronized, manually uploaded, or CSV WAN Edge inventories.
- Certificate operations: [[cisco-cisco-catalyst-sd-wan-control-components-certificates-deployment-guide]] gives automated Cisco, manual Cisco, and enterprise-CA deployment paths plus renewal and migration procedures.

## Qualifications
The evidence is a Cisco-authored prescriptive guide, not an independent security evaluation or availability study. Its procedures span several historical Manager and edge releases, so version-specific UI paths, service endpoints, certificate constraints, and support boundaries require current product documentation before production use. The described one-Manager, one-Validator, one-Controller topology is an instructional example, not a high-availability design.

## What Changed
- Created the product profile around its control-plane trust and authorization architecture.

## Relationships
- [[Cisco]] - develops and documents Cisco Catalyst SD-WAN.
- [[CertificateBasedDeviceIdentity]] - supplies cryptographic identity for control components and WAN Edge devices.
- [[AuthorizedDeviceLists]] - constrains which cryptographically identified devices may join the overlay.
- [[NetworkSegmentation]] - separates transport and management contexts in the guide's example.
- [[ZeroTrustAccess]] - shares the principle that reachability does not itself confer authorization.

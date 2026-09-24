---
title: "Zero-Trust Access"
type: concept
tags: [security, access-control, identity, device-trust]
sources:
  - beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[ZeroTrustAccess]] is an access-control model that does not grant implicit trust from network location and instead authorizes a user-to-application request from contextual evidence such as identity, authentication strength, device state, and resource sensitivity.

## Current Synthesis
The source contrasts zero-trust access with a castle-and-moat VPN model. A VPN can encrypt and authenticate entry, but if entry also confers broad internal trust, stolen credentials, compromised endpoints, or a breached perimeter can expose many applications. Zero-trust access narrows the decision to the requested application and evaluates it continuously from identity and device evidence.

Google's [[BeyondCorp]] case supplies one concrete architecture: device inventory, security keys, device certificates, TLS, graduated trust tiers, a policy engine, and a reverse proxy. The durable principle is not simply publishing internal applications or removing VPN software; it is making each access path explicitly authenticated, encrypted, policy-governed, and limited. The system's assurance is therefore bounded by the quality and availability of every decision input and enforcement component.

## Key Claims
- Network location is weak evidence of legitimacy and should not create broad implicit trust.
- Authorization should be scoped to a requested application and evaluated from current user and device context.
- Strong user authentication is necessary but insufficient when endpoint identity, health, or ownership is unknown.
- Resource-sensitive tiers can align verification strength with potential impact.
- Central proxies and policy engines improve consistent enforcement but become critical security and availability dependencies.
- Replacing a VPN does not eliminate perimeter risk automatically; it redistributes controls across identity, devices, transport, policy, applications, and recovery.

## Evidence
- Perimeter weakness: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] argues that once a trusted internal network is breached, associated applications become exposed.
- Contextual authorization: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] names user identity, authentication strength, device identity, device knowledge, and requested trust tier as access inputs.
- Layered controls: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] describes security keys, device certificates, TLS, live inventory, a trust engine, a reverse proxy, and vulnerability scanning.
- Graduated access: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] says lower access tiers require less stringent device checks.
- Migration discipline: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] reports recorded-traffic replay before switching users and services.

## Counterevidence & Qualifications
This page currently rests on one historical Google case presented by company representatives. The source does not compare zero-trust and VPN environments on attack frequency, blast radius, false decisions, latency, availability, user burden, staffing, or cost. VPNs can still provide encryption, device routing, private addressing, and useful containment; the criticized failure is treating presence behind a perimeter as sufficient authorization. A zero-trust label is not evidence of safety unless inventory, identity, device posture, policy, application security, logging, exceptions, and recovery are implemented and tested coherently.

## What Changed
- Created the concept and separated the general access-control principle from Google's BeyondCorp implementation.

## Related Concepts
- [[BeyondCorp]] - concrete Google implementation described by the source.
- [[AuthenticationInfrastructure]] - supplies identity proof and authentication signals used in access decisions.
- [[NetworkSegmentation]] - provides network-level blast-radius controls that can complement per-application authorization.
- [[ProductionAccessControl]] - applies similar least-privilege and contextual-grant reasoning to administrative production access.
- [[WeakCredentialExposure]] - illustrates why network placement alone cannot compensate for weak authentication.
- [[CleartextProtocolExposure]] - transport encryption remains necessary even when authorization is context-aware.

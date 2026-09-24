---
title: "BeyondCorp"
type: concept
tags: [security, zero-trust, remote-access, google]
sources:
  - beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[BeyondCorp]] is Google's implementation of [[ZeroTrustAccess]] for employee-facing applications, replacing a privileged VPN perimeter with application-level authorization based on user identity, authentication strength, device state, and resource sensitivity.

## Current Synthesis
The reported architecture separates reachability from authorization. Employee applications can have public IP addresses while remaining behind an access proxy; the proxy consults a trust engine before forwarding a request and its credentials. Live device inventory, security keys, device certificates, TLS, and tiered policy make access conditional on the request's context rather than on whether it originated inside a corporate network.

The migration method is as important as the target design. Google reportedly recorded behavior on the old network and replayed about 80 TB of traffic per day against the new controls to find incompatible services and users who could move safely. This turns policy rollout into an observable compatibility exercise, but the article does not independently establish that the resulting system reduced breaches, avoided policy errors, or generalized beyond Google's web-oriented internal applications.

## Key Claims
- BeyondCorp removes network location as the primary proof that an employee request should be trusted.
- A central proxy enforces application-level decisions from identity, authentication, device, and resource context.
- Device inventory and certificates bind authorization to managed endpoint state rather than user credentials alone.
- Trust tiers let checks increase with resource sensitivity instead of granting one broad level of internal access.
- Recorded-traffic replay can expose compatibility gaps before users are moved from the legacy network path.
- Automation can reduce VPN administration and endpoint-provisioning work, but it transfers complexity into inventory accuracy, policy engineering, and proxy reliability.

## Evidence
- Perimeter replacement: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] reports that Google's employee-facing applications used public IP addresses rather than a corporate VPN boundary.
- Contextual decision: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] describes policy inputs covering user identity, authentication strength, device identity, device knowledge, and trust tier.
- Enforcement path: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] places corporate resources behind a reverse proxy that forwards authorized requests with credentials after a trust-engine decision.
- Device and transport controls: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] names security keys, Google-issued device certificates, TLS termination, live device inventory, and application vulnerability scanning.
- Migration validation: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] reports replaying roughly 80 TB of daily employee traffic to find services that would break and users who could migrate.
- Operational claim: [[beyondcorp-how-google-ditched-vpns-for-remote-employee-access-the-new-stack]] says Chromebook configuration for a new employee could take about 90 seconds.

## Counterevidence & Qualifications
The evidence is a 2018 trade-publication account of a Google conference presentation, not a controlled or independent security evaluation. It reports architecture and migration claims but no breach frequency, attack detection, false authorization, denial rates, availability impact, inventory staleness, exception burden, total operating cost, or user-support outcomes. Google's web-based internal applications and engineering capacity may make the approach easier to adopt than legacy, non-web, offline, or specialized enterprise systems. Public reachability also remains safe only if the proxy, identity, device inventory, certificates, policy engine, application security, and recovery paths work together.

## What Changed
- Created the concept from Google's reported VPN-to-contextual-access migration.

## Related Concepts
- [[ZeroTrustAccess]] - BeyondCorp is Google's named implementation of the broader access model.
- [[AuthenticationInfrastructure]] - identity proof, security keys, certificates, and policy decisions support authorization.
- [[NetworkSegmentation]] - BeyondCorp relocates the meaningful boundary from network zones to application requests.
- [[ProductionAccessControl]] - both favor narrow, contextual grants over broad standing access, although their resource scopes differ.
- [[Google]] - organization that designed and deployed the reported model.

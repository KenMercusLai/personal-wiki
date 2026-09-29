---
title: "Tailscale"
type: entity
tags: [networking, vpn, remote-access]
sources:
  - claude-code-on-the-go
  - how-nat-traversal-works
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[Tailscale]] is represented as an encrypted mesh-networking product that connects devices across private networks while minimizing direct public service exposure.

## Current Profile
The two sources show complementary layers of the product. A practitioner uses Tailscale as the private network path from a phone to a disposable cloud development VM with no public SSH listener. Tailscale's own technical article explains how such reachability is built: coordinate candidate endpoints, start through DERP, probe for direct UDP connectivity, transparently upgrade to a better path when possible, and fall back when the path fails. WireGuard supplies the encrypted upper-layer tunnel, so changing transport paths do not become identity boundaries.

## Key Characteristics
- Provides private device-to-device reachability for remote administration and development workflows.
- Uses a coordination side channel to exchange endpoint information and synchronize traversal attempts.
- Uses DERP both as an immediately available encrypted relay path and as support for upgrading to direct peer-to-peer connectivity.
- Treats connectivity as dynamic by probing candidates, selecting better paths, and returning to relay service after failure.
- Relies on end-to-end cryptographic identity rather than IP-address stability when routes change.

## Evidence
- Remote access: [[claude-code-on-the-go]] uses Tailscale between a phone and a Vultr VM so SSH need not listen publicly.
- Direct-connect architecture: [[how-nat-traversal-works]] describes shared UDP sockets, STUN, simultaneous probing, port mapping, NAT64 handling, and candidate racing.
- Relay and recovery: [[how-nat-traversal-works]] says DERP is preselected for immediate communication, remains the fallback when traversal fails, and supports rediscovery after path loss.
- Security boundary: [[how-nat-traversal-works]] places authentication and encryption in the upper protocol, while [[claude-code-on-the-go]] also limits VM secrets and production access.

## Qualifications
The NAT traversal account is first-party and reflects Tailscale's 2020 design, including historical protocol choices and connectivity estimates. The mobile development source is one 2026 implementation case, not a comparative VPN evaluation. Neither source measures current latency, relay load, operating cost, audit results, enterprise policy features, or performance against alternative overlay networks.

## What Changed
- Created a cross-source profile joining Tailscale's traversal architecture to a concrete private-SSH workflow.

## Relationships
- [[NATTraversal]] - Tailscale coordinates, probes, relays, and upgrades paths across NAT and firewall boundaries.
- [[RemoteAdministrationExposure]] - private overlay access can avoid publishing an SSH listener to the open internet.
- [[MobileAgentDevelopment]] - Tailscale carries the phone-to-cloud control path in the documented coding-agent setup.
- [[SystemReliability]] - relay-first startup and path fallback make connectivity resilient to traversal and route failure.

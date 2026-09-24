---
title: "BeyondCorp: How Google Ditched VPNs for Remote Employee Access - The New Stack"
type: source
tags: [beyondcorp, zero-trust, security, remote-access]
date: 2018-01-03
source_file: "/mnt/ken_personal_wiki/Articles/BeyondCorp- How Google Ditched VPNs for Remote Employee Access - The New Stack.md"
---

## Summary
The New Stack reports Google presenters Neal Mueller and Max Saltonstall's account of replacing employee VPN access with [[BeyondCorp]], an identity- and device-aware access model in which the network itself is untrusted. A device inventory, tiered trust decisions, security keys, device certificates, TLS, and a central access proxy combine to evaluate each application request from its context rather than granting broad access after entry to a protected network. Google reportedly prepared the migration by replaying recorded employee traffic against the new controls, while the article supplies no independent security outcomes or post-migration failure rates.

## Key Claims
- Traditional perimeter-and-VPN security concentrates risk because a successful breach can expose a broadly trusted internal network and its applications.
- [[ZeroTrustAccess]] evaluates who the user is, how strongly they authenticated, which device they are using, and what is known about that device instead of treating network location as sufficient trust.
- [[BeyondCorp]] combines live device inventory, ascending trust tiers, security keys, Google-issued device certificates, TLS, and an access proxy backed by a policy decision engine.
- Applications remain behind the proxy and receive forwarded requests and credentials only after the trust engine authorizes access for the requested resource.
- Lower-sensitivity access can require less stringent device checks, making policy proportional to the resource rather than uniformly permissive or restrictive.
- Google prepared its migration by recording old-network behavior and replaying about 80 TB of daily traffic against the new model to identify incompatible services and users ready to move.
- The article reports operational benefits including globally location-independent access and Chromebook provisioning with roughly 90 seconds of configuration.

## Key Quotes
> "Do not trust your network." - Max Saltonstall's summary of the perimeter model's weakness.

> "The access is granted based on context" - Saltonstall on identity, authentication, and device evidence.

## Connections
- [[Google]] - company presented as migrating employee-facing applications away from VPN-only perimeter access.
- [[BeyondCorp]] - Google's named implementation of context-aware, application-level access.
- [[ZeroTrustAccess]] - broader security model in which network position does not establish trust.
- [[AuthenticationInfrastructure]] - security keys, user identity, device certificates, and policy decisions participate in each authorization.
- [[NetworkSegmentation]] - BeyondCorp shifts the boundary from a privileged internal network toward per-application enforcement.
- [[ProductionAccessControl]] - related principle of narrow, contextual, monitored authorization, although this source concerns employee-facing applications rather than production administration.

## Contradictions
- No direct contradiction was found. The source sharpens the wiki's open question about how VPN, internal-network, and zero-trust exposure should change security severity by rejecting network location as a sufficient control.
- The migration and operational results are presenter-reported. The article gives no breach-rate comparison, false-allow or false-deny rate, policy-maintenance cost, legacy-application coverage, user-support burden, or independent evaluation.

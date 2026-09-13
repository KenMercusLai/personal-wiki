---
title: "Production Access Control"
type: concept
tags: [security, operations, production, access-control]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ProductionAccessControl]] is the design of administrative paths, permissions, monitoring, and temporary grants that govern how engineers can directly interact with production systems.

## Current Synthesis
The source accepts that engineers may sometimes need invasive production access during an outage, such as SSH, sudo, or packet capture. The design recommendation is to make that path intentional and rare: observability should reduce the need for direct host access, bastion hosts can centralize the route, and temporary grants can make stolen credentials or former employees less dangerous.

This control also protects reliability, not only confidentiality. Casual manual production changes create drift, and drift can become an outage source. Treating administrative access as exceptional therefore limits both compromise risk and operator-introduced inconsistency.

## Key Claims
- Direct production access may be necessary in crises but should be designed as rare and special.
- Monitoring and centralized logs can reduce the need for invasive host-level troubleshooting.
- Bastion-host models create an intentional route for high-security administrative access.
- Temporary grants reduce risk from stolen credentials and departed employees.
- Limiting manual production intervention also reduces drift-induced outages.

## Evidence
- Crisis scenario: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] describes an engineer wanting to SSH, sudo, and run tcpdump during a production outage.
- Observability substitute: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says centralized logging, New Relic, or Datadog can reduce the need to invade production directly.
- Bastion route: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] recommends a bastion-host network and authentication model for administrative access.
- Temporary access: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] cites temporary production grants as a way to lower stolen-credential and former-employee risk.
- Drift reduction: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] links production-access limits to reducing manually invoked drift.

## Counterevidence & Qualifications
Overly rigid production access can slow emergency diagnosis if monitoring, runbooks, and temporary-access workflows are not reliable. The source argues for controlled availability of crisis access, not permanent elimination of direct troubleshooting.

## What Changed
- Created the concept for the article's bastion, temporary access, monitoring, and drift-control guidance.

## Related Concepts
- [[RemoteAdministrationExposure]] - production administration paths are a high-impact remote-access surface.
- [[CentralizedLogging]] - better logs lower the need for direct host access.
- [[ServiceObservability]] - monitoring and performance tools substitute for invasive troubleshooting.
- [[StartupSecurityDebt]] - casual production access is an early workflow that can harden into debt.
- [[InfrastructureAsCode]] - limiting manual intervention keeps production closer to reviewed infrastructure definitions.

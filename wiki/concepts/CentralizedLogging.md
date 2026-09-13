---
title: "Centralized Logging"
type: concept
tags: [logging, observability, security, operations]
sources:
  - an-infrastructure-guide-for-founders-starting-up-security-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[CentralizedLogging]] is the practice of collecting application, host, and infrastructure logs into a shared, queryable system for investigation, troubleshooting, dashboards, and policy decisions.

## Current Synthesis
The source treats centralized logging as an early infrastructure primitive because local or missing logs give teams little leverage during incidents. The same log corpus helps security investigation and product availability: developers can debug performance and outages without chasing scattered files, while security teams can reconstruct events and make policy choices from observed usage.

For an AWS startup, the article suggests CloudWatch Logs as a reasonable default because it can ingest logs at scale, provide a single query surface, and support rudimentary dashboards. The important design move is not the specific product but the decision to corral application logs, `/var/log` system logs, CloudTrail, and optional network flow data into a place the team can actually use.

## Key Claims
- Local or absent logs provide little incident-response leverage.
- Centralized logs serve availability and troubleshooting as much as security investigation.
- Application, system, and cloud-provider logs should be considered as separate but connected streams.
- A queryable default logging location lets teams build dashboards and make policy decisions from actual usage.
- Logging design should happen early because later retrofits leave gaps in historical evidence.

## Evidence
- Incident leverage: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] says a team without coherent logging will be mostly useless during a security incident.
- Availability value: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] argues logs often help product availability more than security risk.
- Log buckets: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] separates application, system, and infrastructure logs including CloudTrail and network flow data.
- AWS default: [[an-infrastructure-guide-for-founders-starting-up-security-medium]] recommends CloudWatch Logs as a practical early default for scalable centralized logging and basic dashboards.

## Counterevidence & Qualifications
The source does not compare CloudWatch Logs with alternatives or specify retention, privacy, redaction, cost-control, or incident-response runbook details. Centralization also creates a sensitive evidence store that needs access control and retention policy.

## What Changed
- Created the concept from the article's logging-first security and availability argument.

## Related Concepts
- [[ServiceObservability]] - centralized logs are one layer of broader observability.
- [[StartupSecurityDebt]] - missing or scattered logs are an early form of security debt.
- [[ProductionAccessControl]] - better logs reduce the need for invasive production host access.
- [[SystemReliability]] - queryable logs support outage diagnosis and recovery.

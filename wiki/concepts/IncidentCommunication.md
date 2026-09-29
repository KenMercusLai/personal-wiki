---
title: "Incident Communication"
type: concept
tags: [incident-response, communication, reliability, customer-trust]
sources:
  - gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time
  - incident-management-at-google-adventures-in-sre-land-google-cloud-blog
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[IncidentCommunication]] is the practice of giving affected users timely, candid, actionable, and audience-appropriate information while a service failure is being diagnosed and repaired.

## Current Synthesis
The Atlassian case treats communication as part of incident response rather than a public-relations layer added after technical work. Customers needed early acknowledgment, a usable support path, an honest scope and recovery range, enough technical context to brief their own organizations, and visible executive ownership. Repeating low-information status text while restoration stretched across days amplified uncertainty and made the provider appear less in control.

Communication cannot substitute for recovery, and uncertain facts should not be presented as settled. Its operational value is to reduce surprise, let customers activate workarounds, help technical buyers manage internal expectations, and preserve credibility by distinguishing what is known, unknown, changing, and being done next.

Google's account adds an internal coordination layer. External Communications became an explicit incident role within seven minutes, while a central incident tool gave Googlers one place to discover ongoing incidents and navigate to detailed issues and response channels. This role-and-tool design lets technical investigation, command, and audience updates proceed in parallel rather than making communication an improvised side task.

## Key Claims
- Incident communication is a reliability responsibility because customers use it to make operational and continuity decisions.
- Early acknowledgment and a support channel independent of the failed service are basic response capabilities.
- Updates should distinguish known facts, uncertainty, current mitigation, customer actions, and the next update time.
- Technical decision-makers need enough detail to brief their own stakeholders without false certainty or empty reassurance.
- Visible leadership ownership becomes more important as severity and duration increase, but should complement rather than interrupt response work.
- Dedicated communication ownership and a shared incident record reduce coordination ambiguity during active response.

## Evidence
- Delayed acknowledgment: [[gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time]] says Atlassian's first executive acknowledgment arrived on day nine.
- Low-information updates: [[gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time]] describes repeated status language with little technical or customer-specific detail.
- Support dependency: [[gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time]] reports that some customers could not use the Jira-based path intended for reporting service problems.
- Decision context: [[gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time]] says technical leaders lacked enough information to explain the incident internally or plan confidently.
- Trust impact: [[gergely-orosz-the-scoop-inside-the-longest-atlassian-outage-of-all-time]] connects the response to backup plans, incident-management switching, and weakened confidence in cloud migration.
- Role ownership: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] says support assumed the External Communications role within seven minutes of declaration.
- Shared communication state: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] describes a central incident tool that points internal users to detailed issues and coordination channels.

## Counterevidence & Qualifications
The sources document two very different cases and do not compare communication strategies experimentally. Google's account says a role was filled quickly but supplies no customer-facing messages or outcome measure, so role assignment alone should not be mistaken for communication quality. Fast, detailed disclosure can itself create error, security, privacy, legal, or response-coordination risks when facts are unstable. The appropriate cadence and technical depth depend on severity, audience, contractual obligations, and what responders can verify; the stronger principle is candid, useful uncertainty rather than maximum detail at every moment.

## What Changed
- Added dedicated communication ownership and a central incident record as active-response coordination mechanisms.
- Distinguished fast role assignment from evidence that messages were useful or effective.

## Related Concepts
- [[SystemReliability]] - communication helps customers manage the consequences of degraded or unavailable systems.
- [[ServiceObservability]] - reliable updates depend on trustworthy evidence about scope, impact, and recovery.
- [[FailureOwnership]] - candid acknowledgment makes responsibility and follow-up legible.
- [[ReliabilityInvestment]] - resilient status and support channels require preparation before an outage.
- [[SaaSOperatingTransparency]] - incident updates are a time-critical form of operating transparency.
- [[IncidentManagement]] - communication is a defined workstream inside coordinated incident response.

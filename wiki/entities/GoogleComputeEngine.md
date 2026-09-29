---
title: "Google Compute Engine"
type: entity
tags: [product, cloud-computing, google, reliability]
sources:
  - incident-management-at-google-adventures-in-sre-land-google-cloud-blog
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[GoogleComputeEngine]] is represented here as the Google cloud-computing service and SRE-team context for [[PaulNewson]]'s first primary on-call incident.

## Current Profile
The source does not explain Compute Engine's product architecture. It instead shows the service as an operational environment with service-specific peer training, primary and secondary on-call coverage, development-team escalation, formal incident roles, progressive release, rollback, postmortems, and weekly incident review.

An internal user's test-automation failure exposed unusual behavior in several instances, leading responders to suspect broader impact and declare an incident. The problem was traced to a change in an active rollout, remained relatively limited, and was mitigated by rollback. The account therefore contributes an incident-response profile, not a general evaluation of Compute Engine reliability.

## Key Characteristics
- Google cloud service supported by a dedicated SRE team and structured on-call preparation in the source.
- Operational context where internal user evidence could trigger investigation and formal incident declaration.
- Used progressive rollout and rollback to constrain and mitigate one release-related fault.
- Used common postmortems and weekly review to distribute incident lessons across SREs and developers.

## Evidence
- SRE operating model: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] describes service-specific training, shadowing, primary and secondary on-call, and cross-team escalation.
- Incident case: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] traces an instance anomaly from internal report through declaration, scoped investigation, change identification, and rollback.
- Learning loop: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] describes an automatically created postmortem and weekly Compute Engine incident-review meeting.

## Qualifications
The source is a Google-authored 2017 narrative with no customer-impact measure, architecture detail, exact timeline beyond one role transition, or independent reliability comparison. One successfully contained incident cannot establish the service's typical performance or current operating process.

## What Changed
- Added Google Compute Engine as the service and team context for Google's incident-management case.

## Relationships
- [[Google]] - company operating Google Compute Engine.
- [[PaulNewson]] - SRE Mission Controller whose first incident occurred with the service team.
- [[IncidentManagement]] - formal response process used after instance anomalies suggested wider impact.
- [[ChangeSafety]] - progressive rollout and rollback constrained the change-induced failure.
- [[BlamelessPostmortem]] - structured learning process used after service restoration.

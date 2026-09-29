---
title: "Incident Management"
type: concept
tags: [incident-response, reliability, operations, coordination]
sources:
  - incident-management-at-google-adventures-in-sre-land-google-cloud-blog
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[IncidentManagement]] is the prepared coordination system used when a service problem has enough potential impact, scope, or complexity to require explicit authority, divided responsibilities, shared operational state, escalation, communication, mitigation, and closure.

## Current Synthesis
Google's case begins before failure. General instruction, service-specific peer training, scenario drills, shadowing, and secondary on-call work build response judgment before an engineer becomes the primary responder. Primary responsibility does not imply solitary expertise: the responder is expected to pull in experienced support and specialist operators.

Declaration is a coordination threshold, not merely a severity label. Once uncertainty and possible scope justify coordinated work, a shared incident record establishes a common reference point and directs participants to technical detail and communication channels. Explicit command, operations, assistance, and external-communication responsibilities reduce ambiguity without requiring every incident to fill every possible role.

Response and learning form a loop. The immediate goal is to understand scope, mitigate impact, and close the incident; afterward, a structured postmortem converts the event into owned prevention, detection, and mitigation work. Common templates and recurring reviews can then turn individual cases into organization-wide reliability knowledge.

## Key Claims
- Incident readiness depends on repeated practice, service context, shadowing, and supported escalation before primary on-call responsibility.
- Incident declaration should occur when potential impact, scope, or complexity calls for coordinated work with explicit ownership.
- Clear command, operations, assistance, and communication roles let diagnosis, mitigation, and stakeholder updates proceed in parallel.
- A central incident record should connect shared status, detailed issue tracking, and response communication channels.
- Effective incident management continues through closure into owned follow-up work and recurring organizational learning.

## Evidence
- Readiness and support: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] describes training, weekly drills, shadowing, secondary duty, and an experienced secondary supporting the first-time primary.
- Declaration and shared state: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] defines declaration by potential impact, scope, and complexity, then describes a central incident tool linking technical and communication resources.
- Role separation: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] identifies Incident Commander, External Communications, effective Operations Lead, and Assistant Incident Commander responsibilities.
- Mitigation-to-learning loop: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] moves from progressive-rollout detection and rollback through closure, postmortem creation, nine owned actions, and weekly review.

## Counterevidence & Qualifications
The evidence is one company-authored account of a limited Google Compute Engine incident, not a comparison of response structures or proof that Google's role model fits every team, severity, or regulated environment. Formal roles can add overhead during small events, while sparse teams may need one person to hold several responsibilities. A central tool improves coordination only if responders keep it current and it remains available. The source also withholds detailed impact, timing, root cause, decision errors, and follow-up completion, so it demonstrates a process more clearly than its outcome.

## What Changed
- Established incident management as a practiced coordination and learning system, not only live troubleshooting.
- Added declaration criteria, explicit response roles, and a central shared incident record.
- Connected incident closure to owned postmortem actions and recurring cross-team review.

## Related Concepts
- [[SystemReliability]] - incident management is the operational response layer when preventive controls do not preserve service.
- [[IncidentCommunication]] - dedicated communication ownership translates evolving response state for affected audiences.
- [[ChangeSafety]] - progressive rollout and rollback can bound and mitigate change-induced incidents.
- [[BlamelessPostmortem]] - post-incident learning converts response evidence into system improvements and owned actions.
- [[ServiceObservability]] - declaration, scoping, diagnosis, and closure depend on trustworthy operational signals.

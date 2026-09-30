---
title: "Incident Management"
type: concept
tags: [incident-response, reliability, operations, coordination]
sources:
  - incident-management-at-google-adventures-in-sre-land-google-cloud-blog
  - instapaper-outage-cause-recovery-making-instapaper-medium
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[IncidentManagement]] is the prepared coordination system used when a service problem has enough potential impact, scope, or complexity to require explicit authority, divided responsibilities, shared operational state, escalation, communication, mitigation, and closure.

## Current Synthesis
Google's case begins before failure. General instruction, service-specific peer training, scenario drills, shadowing, and secondary on-call work build response judgment before an engineer becomes the primary responder. Primary responsibility does not imply solitary expertise: the responder is expected to pull in experienced support and specialist operators.

Declaration is a coordination threshold, not merely a severity label. Once uncertainty and possible scope justify coordinated work, a shared incident record establishes a common reference point and directs participants to technical detail and communication channels. Explicit command, operations, assistance, and external-communication responsibilities reduce ambiguity without requiring every incident to fill every possible role.

Response and learning form a loop. The immediate goal is to understand scope, mitigate impact, and close the incident; afterward, a structured postmortem converts the event into owned prevention, detection, and mitigation work. Common templates and recurring reviews can then turn individual cases into organization-wide reliability knowledge.

Instapaper shows what this prepared structure must accomplish under an unfamiliar infrastructure failure. The team initially lacked an immediate escalation path to Pinterest SRE, underestimated dump time from row counts, and delayed the degraded-service path while pursuing a full rebuild. Once Pinterest and AWS specialists were engaged, parallel recovery workflows and provider-only filesystem operations accelerated restoration. Incident management therefore includes early specialist and vendor escalation, explicit decision points between full and degraded recovery, and estimates grounded in tested throughput rather than intuition.

## Key Claims
- Incident readiness depends on repeated practice, service context, shadowing, and supported escalation before primary on-call responsibility.
- Incident declaration should occur when potential impact, scope, or complexity calls for coordinated work with explicit ownership.
- Clear command, operations, assistance, and communication roles let diagnosis, mitigation, and stakeholder updates proceed in parallel.
- A central incident record should connect shared status, detailed issue tracking, and response communication channels.
- Specialist and provider escalation should be triggered by failure scope and access boundaries before the local team exhausts slower paths.
- Recovery strategy should use measured restore times and explicit degraded-service criteria rather than optimistic estimates.
- Effective incident management continues through closure into owned follow-up work and recurring organizational learning.

## Evidence
- Readiness and support: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] describes training, weekly drills, shadowing, secondary duty, and an experienced secondary supporting the first-time primary.
- Declaration and shared state: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] defines declaration by potential impact, scope, and complexity, then describes a central incident tool linking technical and communication resources.
- Role separation: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] identifies Incident Commander, External Communications, effective Operations Lead, and Assistant Incident Commander responsibilities.
- Mitigation-to-learning loop: [[incident-management-at-google-adventures-in-sre-land-google-cloud-blog]] moves from progressive-rollout detection and rollback through closure, postmortem creation, nine owned actions, and weekly review.
- Escalation boundary: [[instapaper-outage-cause-recovery-making-instapaper-medium]] says system-wide Instapaper outages had no immediate Pinterest SRE escalation workflow before the incident.
- Recovery decision: [[instapaper-outage-cause-recovery-making-instapaper-medium]] says the team delayed limited-service restoration because its six-to-eight-hour dump estimate proved far too optimistic.
- Parallel expertise: [[instapaper-outage-cause-recovery-making-instapaper-medium]] describes Pinterest SRE guidance and AWS engineers running Aurora, MySQL import, ext4 migration, and replication workflows in parallel.

## Counterevidence & Qualifications
The evidence comes from two company-authored incidents, not a comparison of response structures or proof that Google's role model fits every team. Formal roles can add overhead during small events, while sparse teams may combine responsibilities. A central tool helps only if it remains available and current. Google's account withholds impact, timing, and detailed root cause; Instapaper gives richer recovery timings but does not independently test whether its new escalation and monthly-backup practices improved later outcomes. Provider escalation can unlock privileged recovery operations without transferring the customer's responsibility for preparation and decisions.

## What Changed
- Added early specialist and cloud-provider escalation when the incident crosses local expertise or access boundaries.
- Added measured restore duration and degraded-service activation as explicit incident-command decisions.

## Related Concepts
- [[SystemReliability]] - incident management is the operational response layer when preventive controls do not preserve service.
- [[IncidentCommunication]] - dedicated communication ownership translates evolving response state for affected audiences.
- [[ChangeSafety]] - progressive rollout and rollback can bound and mitigate change-induced incidents.
- [[BlamelessPostmortem]] - post-incident learning converts response evidence into system improvements and owned actions.
- [[ServiceObservability]] - declaration, scoping, diagnosis, and closure depend on trustworthy operational signals.
- [[BackupAndRecovery]] - restore testing supplies the timing and feasibility evidence needed for incident decisions.

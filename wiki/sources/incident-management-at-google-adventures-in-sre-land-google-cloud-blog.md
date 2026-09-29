---
title: "Incident management at Google — adventures in SRE-land"
type: source
tags: [google, sre, incident-management, reliability, postmortem]
date: 2017-02-27
source_file: "/mnt/ken_personal_wiki/Articles/Incident management at Google — adventures in SRE-land - Google Cloud Blog.md"
---

## Summary
[[PaulNewson]] recounts his first primary on-call incident with the [[GoogleComputeEngine]] SRE team, showing [[IncidentManagement]] as a rehearsed coordination system rather than improvised troubleshooting. The case joins explicit response roles, a central incident record, progressive rollout and tested rollback, then closes the loop through a [[BlamelessPostmortem]] whose owned follow-ups and common template support both local repair and cross-incident learning at [[Google]].

## Key Claims
- On-call readiness was built through general SRE training, weekly peer instruction, scenario drills, shadowing, and secondary duty before primary responsibility; the primary responder still relied on experienced colleagues rather than acting alone.
- Declaring an incident means judging that potential impact, scope, or complexity requires coordinated work with defined roles, then creating a shared incident record that points responders to the issue tracker and communication channels.
- The response separated command, operations, assistance, and external communication: Newson served as Incident Commander, support assumed External Communications within seven minutes, Parya effectively led operations, and Benson acted as Assistant Incident Commander.
- The release-related fault remained limited because the change was rolling out progressively, and a known, tested rollback mechanism allowed responders to mitigate it quickly after identifying the responsible change.
- Google frames blameless postmortems around improving systems, tools, and processes rather than punishing well-intentioned people; this incident produced nine owned follow-up issues despite limited impact.
- Common postmortem templates and weekly review meetings let teams aggregate recurring causes, find additional actions, share case-based reliability knowledge, and reinforce norms against individual blame.

## Key Quotes
> "I may be on point, but I’m not alone." - on primary on-call responsibility remaining supported by a wider response system.

> "an issue is of sufficient potential impact, scope and complexity that it will require a coordinated effort with well defined roles" - on the threshold for declaring an incident.

> "you need to look to how you can improve the systems, tools and processes around the people" - on the purpose of blameless postmortems.

## Connections
- [[PaulNewson]] - Google SRE Mission Controller and first-person author of the incident account.
- [[Google]] - organization whose SRE preparation, incident protocol, tooling, rollback practice, and postmortem culture the article describes.
- [[GoogleComputeEngine]] - service and SRE team in which the incident occurred.
- [[IncidentManagement]] - coordinated response model with declaration criteria, defined roles, shared state, escalation, and closure.
- [[BlamelessPostmortem]] - system-focused learning process used after mitigation to generate owned actions and shared lessons.
- [[ChangeSafety]] - progressive rollout constrained the fault while a tested rollback restored service.
- [[SystemReliability]] - training, response coordination, mitigation, and learning form one operational reliability loop.
- [[IncidentCommunication]] - a dedicated role and central incident tool kept internal responders and affected parties informed.

## Contradictions
- The article's successful rollback is a bounded case, not evidence that rollback can restore every system: it does not describe persistent-state mutation, incompatible clients, dependent-object damage, or the other recovery limits documented in [[ChangeSafety]].
- This is a first-person, company-published account of one relatively limited 2017 incident. It does not provide impact measurements, exact duration, technical root-cause detail, independent evaluation, or follow-up completion outcomes.
- The sole effective image in the saved Markdown is a generic Google Cloud social-card URL whose asset now returns HTTP 404. It could not be opened or interpreted and was not retained; no visual claim is used in this note.

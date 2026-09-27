---
title: "Asana"
type: entity
tags: [company, software, engineering]
sources:
  - 7-best-practices-for-doing-code-reviews
  - asanas-september-8-outage
  - details-on-the-january-9th-2017-asana-outage
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Asana]] is a work-management software company whose engineering blog provides source material on code review practice and production incident response.

## Current Profile
In this wiki, Asana appears as both an engineering-practice publisher and an outage-postmortem author. The code-review source uses a new team member's experience to present review as a way to spread knowledge, learn coworkers' thinking, run and inspect code locally, and avoid unnecessary blocking.

Operationally, Asana is represented by two 2016-2017 outage postmortems. An 83-minute September 8, 2016 outage began with a logging bug in a late deployment; recovery was slowed by misleading database hypotheses, dogfooding infrastructure that did not share the production overload, uncertainty about the safe revision, and the need to blacklist the bad client revision. A January 9, 2017 partial outage instead began in capacity control: a provisioning job hung while holding a lock over the weekend, unusually high Monday demand exceeded the reduced fleet, and memory pressure killed the process master before expensive process startup saturated CPU. Manual scaling and free-user throttling restored service progressively.

## Key Characteristics
- Publisher of a practitioner engineering article on code review.
- Engineering context where code review is framed as team learning and knowledge sharing.
- Source setting for a workflow that combines human review with running the app, breakpoints, tests, and IDE context.
- Publicly reports production outages with concrete timelines, proximate causes, recovery steps, and response-improvement commitments.
- Treats incident learning as a 5 Whys process focused on detection, triage speed, and time-to-fix.
- Uses traffic throttling as a load-shedding mechanism when immediate demand exceeds healthy fleet capacity.

## Evidence
- Publisher context: [[7-best-practices-for-doing-code-reviews]] is categorized under Asana engineering and points readers to Asana's engineering team page.
- Team learning: [[7-best-practices-for-doing-code-reviews]] describes joining Asana and improving review technique through team practice.
- Workflow context: [[7-best-practices-for-doing-code-reviews]] recommends running changes locally, using IDE tooling, and giving clear approval feedback.
- Outage timeline: [[asanas-september-8-outage]] says Asana was down for about 83 minutes, from 7:25am to 8:48am PDT, after a Wednesday-night deploy.
- Response diagnosis: [[asanas-september-8-outage]] says engineers initially investigated database and queue symptoms before identifying maxed-out web-server CPU tied to the prior release.
- Postmortem posture: [[asanas-september-8-outage]] says Asana judged its response as the failure and committed to better detection, triage, and fix-time safeguards.
- Capacity-control failure: [[details-on-the-january-9th-2017-asana-outage]] says a lock-holding provisioning job hung indefinitely after contacting a bad EC2 node, while non-paging timeout alerts went unnoticed.
- Overload behavior: [[details-on-the-january-9th-2017-asana-outage]] traces a shift from memory exhaustion and failed forks to OOM termination of the master process and CPU saturation.
- Staged restoration: [[details-on-the-january-9th-2017-asana-outage]] says free-user throttling restored health almost immediately while operators added servers manually.

## Qualifications
The sources do not describe Asana's full engineering organization, product strategy, or current internal processes. They support Asana as the publication and workplace context for a 2016 code-review essay and as the reporting company for two historical outage postmortems. Both incident accounts are first-party explanations rather than independent audits.

## What Changed
- Created the entity page for Asana as the publisher context for the code-review source.
- Added Asana's September 8 outage as an operations and incident-response case.
- Added the January 9 capacity outage as an autoscaling, overload-collapse, load-shedding, and recovery-speed case.

## Relationships
- [[CodeReviewPractice]] - Asana's engineering blog supplies the source for this concept.
- [[SoftwareVerification]] - the article connects Asana's review advice to execution-backed validation.
- [[PRReviewHygiene]] - the article informs reviewer-facing feedback and approval flow.
- [[SystemReliability]] - Asana's outage shows how code, capacity, diagnosis, and recovery interact.
- [[ChangeSafety]] - the outage was triggered by deployed code and resolved through revert selection plus bad-revision blacklisting.
- [[ServiceObservability]] - the response depended on pages, metric interpretation, customer-support escalation, and environment visibility.

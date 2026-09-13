---
title: "Asana's September 8 Outage"
type: source
tags: [software-engineering, reliability, incident-response, outage]
date: 2016-09-10
source_file: /mnt/ken_personal_wiki/Articles/Asana's September 8 outage.md
---

## Summary
[[Asana]] describes an 83-minute outage on September 8, 2016, caused by a Wednesday-night deployment whose security logging bug drove unexpected web-server CPU load. The incident shows [[SystemReliability]] depending on [[ServiceObservability]], [[ChangeSafety]], and [[DeploymentAutomation]]: engineers first investigated the database and non-critical queues, then correlated maxed-out web CPU with the prior release, reverted to a known-good revision, blacklisted the bad client revision, and later used a 5 Whys review to improve detection, triage, and repair.

## Key Claims
- A small logging change can become a severe [[SystemReliability]] incident when traffic, CPU saturation, request latency, database-connection hold time, and queue backoff interact.
- [[ServiceObservability]] must surface customer-impacting symptoms clearly; in this outage, initial pages pointed at search indexing and the API while dogfooding infrastructure stayed healthy, delaying severity recognition.
- [[ChangeSafety]] depends on rapid correlation between symptoms and recent releases, plus confidence about which revision is actually safe to restore.
- [[DeploymentAutomation]] and rollback tooling need to handle client behavior and bad-revision blacklisting, not only server-side deploy state.
- Post-incident [[FailureOwnership]] should distinguish proximate technical causes from response failures and produce concrete improvements in detection, triage, and time-to-fix.

## Key Quotes
> "the worst outage that we've ever had" - on customer impact.

> "the databases were actually underloaded" - on the misleading initial investigation.

> "our failure during this incident was our response" - on the 5 Whys conclusion.

## Connections
- [[Asana]] - company reporting the outage and engineering response.
- [[SystemReliability]] - central reliability lesson around interacting load, latency, database connections, queues, and recovery.
- [[ServiceObservability]] - monitoring, paging, dogfooding visibility, and support escalation shaped detection and diagnosis.
- [[ChangeSafety]] - faulty deployed code, revision selection, revert execution, and client revision blacklisting drove the restoration path.
- [[DeploymentAutomation]] - frequent deploys, late-night release timing, revert choice, and blacklist mechanics are part of the release system.
- [[FailureOwnership]] - the postmortem accepts response failure and turns it into improvements.
- [[AWS]] - Asana's dogfooding version ran on different AWS EC2 instances than production.

## Contradictions
- No direct contradictions found. The source complements existing reliability pages by adding a concrete outage in which recovery was delayed by misleading symptoms, dogfooding-environment divergence, and uncertainty about a safe revert target.

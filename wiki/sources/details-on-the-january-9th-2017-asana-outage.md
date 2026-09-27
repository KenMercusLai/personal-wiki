---
title: "Details on the January 9th, 2017 Asana Outage"
type: source
tags: [software-engineering, reliability, incident-response, outage, capacity]
date: 2017-01-25
source_file: /mnt/ken_personal_wiki/Articles/Details on the January 9th, 2017 Asana outage.md
---

## Summary
[[Asana]] describes just under three hours of partial downtime on January 9, 2017, caused by a stalled web-server provisioning job, unusually high post-holiday Monday traffic, and an ungraceful overload cascade. The incident extends [[SystemReliability]] and [[ServiceObservability]] beyond ordinary capacity shortage: missing timeouts and non-paging lock alerts left autoscaling stuck over the weekend, while memory pressure killed a fork master and pushed each server into CPU saturation; manual scaling and load-balancer throttling then restored service in stages.

## Key Claims
- Capacity automation needs bounded operations and actionable alerts: one bad EC2 node hung a lock-holding cron job indefinitely, preventing later provisioning runs while timeout alerts went unnoticed because they did not page.
- [[SystemReliability]] depends on conservative baseline capacity and demand-aware planning as well as autoscaling; Asana's weekend fleet level could not absorb an unusually busy second Monday after New Year's when automated scale-up failed.
- Overload can create nonlinear collapse: exhausted memory prevented cheap process forks, the OOM killer terminated the preinitialized master process, and expensive from-scratch startup then saturated CPU.
- Load shedding can restore partial availability faster than capacity arrives; blocking a fraction of free-user traffic made the fleet healthy almost immediately while preserving all paying customers and about 90% of free users.
- Recovery speed depends on practiced provisioning paths: Asana's first manual expansion took one hour and forty minutes after an intervention, while a second expansion took 22 minutes.
- [[ServiceObservability]] must escalate stalled control-plane work, not only user-facing symptoms, because warning signals that nobody acts on do not protect availability.

## Key Quotes
> "too much load and not enough webservers" - the immediate capacity diagnosis.

> "We didn't have appropriate timeouts set for the job" - on why provisioning could remain stuck indefinitely.

> "our web servers became healthy almost immediately" - on the effect of traffic throttling.

## Connections
- [[Asana]] - company reporting the outage, response, and post-incident review.
- [[SystemReliability]] - the incident joins capacity margin, demand variance, overload behavior, load shedding, and recovery speed.
- [[ServiceObservability]] - non-paging lock-timeout alerts failed to turn a stalled provisioning job into timely action.
- [[DeploymentAutomation]] - the final provisioning step depended on a lock-holding cron job that configured servers and attached them to load balancers.
- [[AWS]] - the web fleet used EC2 nodes and an auto scaling group.
- [[ChangeSafety]] - the response reduced blast radius through staged traffic throttling while operators restored capacity.

## Contradictions
- No direct contradiction found. The incident strengthens the wiki's fail-fast and capacity-protection guidance by showing the opposite behavior: overloaded servers kept accepting work, entered memory pressure, lost their process master, and became still less efficient.

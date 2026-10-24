---
title: "Telstra"
type: entity
tags: [telecommunications, australia, mobile-network, reliability]
sources:
  - telestra-outage-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[Telstra]] is an Australian telecommunications company represented here through a secondary reconstruction of its July 8, 2026 mobile-network outage.

## Current Profile
The account presents Telstra as operating a geographically distributed NTP hierarchy across Sydney, Melbourne, and Perth to support its mobile core. A 2020 timing-system migration changed redundancy and source-selection behavior; a later Melbourne GPS failover, deferred firmware update, and maintenance restart exposed a rollover defect that spread incorrect time into Sydney and disrupted mobile service.

## Key Characteristics
- Operates critical mobile infrastructure whose control plane depends on accurate shared time.
- Used Sydney, Melbourne, and Perth NTP exchange sites with National Measurement Institute reference sources.
- Experienced architectural drift in which documentation, configuration, vendor warnings, and staff understanding did not remain aligned.
- Required both clock restoration and repair of date-corrupted IP-prefix records after the outage.

## Evidence
- Timing architecture: [[telestra-outage-report]] reconstructs the cross-site NTP strata, lost local redundancy, symmetric peering, and GPS failover path.
- Outage mechanism: [[telestra-outage-report]] traces a post-maintenance GPS rollover from Melbourne through a shared client into Sydney.
- Customer impact: [[telestra-outage-report]] reports disrupted voice, messaging, data, and emergency calls, plus roughly 45% peak call-and-session impact.
- Persistent repair: [[telestra-outage-report]] says about 30,000 IP-prefix records were corrupted with the wrong date and required later repair.

## Qualifications
This profile is bounded to Hochstein's secondary reconstruction, which relies on a public review, testimony, vendor documentation, and explicit inference. It does not describe Telstra's broader business, current architecture, complete incident record, or independently verified remediation, and the evidence conflicts over whether the GPS card was part of the intended design.

## What Changed
- Established a source-bounded profile around Telstra's mobile timing architecture and July 2026 outage.

## Relationships
- [[LorinHochstein]] - authored the secondary technical reconstruction used here.
- [[SSU2000]] - timing platform whose GPS card and chassis behavior were central to the outage.
- [[NetworkTimeSynchronization]] - critical infrastructure function that supplied time to Telstra's mobile core.
- [[SystemReliability]] - frames the interaction of architecture, maintenance, latent defects, overload, and state repair.

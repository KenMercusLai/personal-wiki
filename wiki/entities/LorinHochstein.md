---
title: "Lorin Hochstein"
type: entity
tags: [software-reliability, incident-analysis, technical-writing]
sources:
  - telestra-outage-report
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[LorinHochstein]] is represented here as the author of a 2026 technical reconstruction of Telstra's July 8 mobile outage.

## Current Profile
Hochstein combines the public findings report, vendor documentation, Senate testimony, standards, and his own diagrams to make a sparse incident account more legible. He marks uncertainty unusually clearly: the post distinguishes report evidence from guesses about NTP mode, product behavior, topology, and telecom-specific components, then uses the remaining gaps to criticize investigations that prescribe more discipline without studying how work was actually performed.

## Key Characteristics
- Reconstructs incident mechanisms through chronological architecture and state-transition diagrams.
- Separates sourced facts from assumptions and openly states limits in NTP and telecom expertise.
- Connects technical failure to maintenance, migration, redundancy, organizational understanding, and postmortem quality.
- Treats reliability mechanisms themselves as possible sources of latent risk.

## Evidence
- Reconstruction method: [[telestra-outage-report]] uses eleven diagrams or screenshots to trace the NTP topology from 2010 through the 2026 propagation event.
- Uncertainty discipline: [[telestra-outage-report]] repeatedly labels assumptions about peering, SSU routing, Perth impact, and telecom vendors.
- Systems analysis: [[telestra-outage-report]] links a migration, failover card, deferred update, repair restart, timing loop, overload, and corrupted state.
- Investigation critique: [[telestra-outage-report]] argues that recommendations about competence and curiosity are incomplete without understanding decision context and everyday work.

## Qualifications
The wiki currently represents Hochstein through one blog post. His reconstruction is secondary, some mechanisms remain inferred, and he explicitly says he lacks domain expertise in the mobile technologies involved.

## What Changed
- Established Hochstein's source-bounded profile around incident reconstruction and work-context analysis.

## Relationships
- [[Telstra]] - operator of the system and outage he analyzes.
- [[NetworkTimeSynchronization]] - principal technical domain of the reconstruction.
- [[BlamelessPostmortem]] - related framework for his criticism of hindsight-centered investigation.
- [[SystemReliability]] - broader field through which he interprets interacting technical and organizational risks.

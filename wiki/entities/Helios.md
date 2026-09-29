---
title: "Helios"
type: entity
tags: [container-orchestration, infrastructure, spotify]
sources:
  - improving-critical-infrastructure-rollouts-labs
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Helios]] is Spotify's Docker orchestration tool in the 2017 account of fleet-wide infrastructure upgrades.

## Current Profile
Within this source, Helios routes work among Docker containers and runs through agents distributed across thousands of hosts. An earlier Docker upgrade left orphaned containers holding their original ports, which caused Helios to route traffic to the wrong container. Spotify later used [[Tsunami]] to roll new Helios versions gradually across the fleet.

## Key Characteristics
- Orchestrates Docker workloads in Spotify's backend environment.
- Depends on accurate container and port ownership for routing.
- Uses host agents whose versions can be changed progressively.
- Became one of the infrastructure components managed through Tsunami.

## Evidence
- Routing failure: [[improving-critical-infrastructure-rollouts-labs]] reports that orphaned containers retained ports and led Helios to route traffic to the wrong container.
- Fleet deployment: [[improving-critical-infrastructure-rollouts-labs]] describes a Helios version rollout across thousands of hosts over 24 hours.
- Tsunami use: [[improving-critical-infrastructure-rollouts-labs]] lists Helios among the components Spotify upgraded through Tsunami.

## Qualifications
The source uses Helios to explain Docker failure impact and Tsunami rollout behavior; it is not a complete architecture or operational history. The remote rollout chart could not be opened, so its distributions and axes were not independently interpreted.

## What Changed
- Created Helios as Spotify's Docker orchestration and routing context for the rollout case.
- Recorded both its exposure to orphaned-container port conflicts and its later progressive upgrade path.

## Relationships
- [[Spotify]] - organization operating Helios across its backend fleet.
- [[Docker]] - container runtime Helios orchestrates.
- [[Tsunami]] - service used to roll out Helios versions gradually.
- [[ProgressiveInfrastructureRollout]] - practice used to limit the blast radius of Helios changes.

---
title: "Tsunami"
type: entity
tags: [infrastructure, progressive-delivery, desired-state]
sources:
  - improving-critical-infrastructure-rollouts-labs
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Tsunami]] is Spotify's internally developed service for unattended, gradual rollout of infrastructure versions and configuration across a large host fleet.

## Current Profile
The 2017 Spotify Labs account presents Tsunami as a central desired-state allocator rather than the component that performs each upgrade. Its primary abstraction is a variable with permitted values and a time-dependent transition; hosts query the service for a flat JSON desired state and remain responsible for applying it locally. Spotify used the service to spread [[Docker]], [[Helios]], and Puppet changes over hours or weeks so faults could be detected before they reached most of the fleet.

Centralization also creates a shared control plane for audit history, host-percentage rules by role, minimum or maximum affected-host bounds, and intended automatic stopping when service-level objectives are breached. These are reported design capabilities, not measured evidence of incident reduction or safe recovery.

## Key Characteristics
- Allocates desired infrastructure state gradually over a configured interval.
- Represents each rollout target as a variable with constrained values and transitions.
- Returns flat JSON while leaving state enactment to client hosts.
- Supports role-aware percentage allocation with floor and ceiling rules.
- Centralizes rollout audit history and prospective service-level-objective stopping.
- Was reported in use for Docker, Helios, Puppet, and restart-inducing configuration changes.

## Evidence
- Time-based allocation: [[improving-critical-infrastructure-rollouts-labs]] describes specifying a Docker upgrade from version A to B over two weeks.
- Client boundary: [[improving-critical-infrastructure-rollouts-labs]] says hosts query Tsunami for desired versions and apply the returned state themselves.
- Shared controls: [[improving-critical-infrastructure-rollouts-labs]] lists audit logging, role-aware percentages with floors or ceilings, and automatic termination on service-level-objective breaches.
- Reported scope: [[improving-critical-infrastructure-rollouts-labs]] says Spotify used Tsunami for Docker, Helios, Puppet, and configuration changes that restart services.

## Qualifications
The evidence is one first-party 2017 retrospective. It does not specify Tsunami's storage, assignment consistency, cohort randomization, authentication, failure behavior, client convergence guarantees, rollback semantics, or measured effect on incidents. The article says Spotify hoped to open-source the system, but this source does not establish that this occurred.

## What Changed
- Created Tsunami as the central desired-state allocator in Spotify's gradual infrastructure rollout system.
- Separated central allocation and policy from client-side enactment.
- Preserved the difference between reported controls and measured reliability outcomes.

## Relationships
- [[Spotify]] - organization that developed and operated Tsunami.
- [[Docker]] - infrastructure component whose risky upgrades motivated the service.
- [[Helios]] - orchestration software upgraded through Tsunami.
- [[ProgressiveInfrastructureRollout]] - operating practice Tsunami implements through time-based allocation.
- [[DeploymentAutomation]] - clients enact centrally supplied desired state.
- [[ChangeSafety]] - audit, bounded exposure, and health-based stopping are safety controls.

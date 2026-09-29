---
title: "Progressive Infrastructure Rollout"
type: concept
tags: [infrastructure, reliability, progressive-delivery, operations]
sources:
  - improving-critical-infrastructure-rollouts-labs
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Definition
[[ProgressiveInfrastructureRollout]] is the controlled propagation of infrastructure versions or configuration through representative production cohorts over time so detection and stopping can occur before a fault reaches the full fleet.

## Current Synthesis
Spotify's Docker experience makes infrastructure progression a fleet-allocation problem rather than a single preproduction gate. Early upgrade regressions were manageable when Docker served a few prototypes, but the same change pattern became unsafe once thousands of hosts ran mission-critical access, login, event, and client-connectivity services. Restart concentration could itself harm users and create downstream reconnect storms, while heterogeneous production workloads exposed failures that infrastructure-team and testing instances did not.

The reported response separates desired-state allocation from enactment. [[Tsunami]] changes the proportion of hosts assigned to each permitted value over time; each host queries for a flat JSON target and applies it locally. Central audit, role-aware percentage floors or ceilings, and service-level-objective stopping can make that allocation observable and bounded. Progression therefore reduces maximum initial exposure and buys detection time, but it does not eliminate faults or prove that cohorts, health signals, client convergence, and recovery behavior are correct.

## Key Claims
- Infrastructure risk grows with fleet size, workload criticality, restart coupling, and service heterogeneity.
- Representative production exposure may reveal incompatibilities that narrow testing populations cannot reproduce.
- Time-distributed cohort assignment can limit initial blast radius and create an observation window.
- A central desired-state service can standardize audit, allocation policy, and health-based stopping while clients retain enactment responsibility.
- Role-aware floors and ceilings matter because a percentage alone may select no hosts in a small role or too many in a sensitive one.
- A gradual rollout remains conditional on trustworthy selection, observability, convergence, stopping, and recovery mechanisms.

## Evidence
- Scale and criticality: [[improving-critical-infrastructure-rollouts-labs]] reports growth from hundreds of prototype instances to thousands of hosts, with 80% of production backend services containerized by February 2017.
- Failure diversity: [[improving-critical-infrastructure-rollouts-labs]] describes hostname and command regressions, orphaned containers, retained ports, and orphaned proxy processes across Docker upgrades.
- Restart coupling: [[improving-critical-infrastructure-rollouts-labs]] says simultaneous restarts of login and access services can degrade user experience and topple downstream systems through reconnect storms.
- Allocation design: [[improving-critical-infrastructure-rollouts-labs]] describes Tsunami variables, time-based interpolation, client-enacted JSON desired state, role percentages, audit logs, and service-level-objective stopping.

## Counterevidence & Qualifications
This is a first-party 2017 case without a control group or before-and-after measures of failure rate, affected users, detection time, or recovery time. Production exposure intentionally places some real workloads at risk, and a percentage of hosts is not necessarily the same as a percentage of users, traffic, or dependency load. Central control may also introduce assignment, availability, authorization, and correlated-failure risks not discussed in the article. The inaccessible rollout chart prevents independent inspection of the example's axes, transition smoothness, anomalies, or cohort distribution.

## What Changed
- Created the concept from Spotify's shift from environment-wide upgrades to time-based production cohort allocation.
- Distinguished desired-state assignment from client-side enactment.
- Added representative production diversity as both a detection need and an ethical operational risk.

## Related Concepts
- [[ChangeSafety]] - progressive propagation bounds initial exposure and adds detection and stopping opportunities.
- [[DeploymentAutomation]] - clients automatically converge toward centrally selected infrastructure state.
- [[DeploymentReleaseSeparation]] - both separate change preparation from broader exposure, though infrastructure restart share need not equal traffic share.
- [[ServiceObservability]] - safe expansion and termination depend on reliable user- and service-level signals.
- [[SystemReliability]] - the practice aims to keep infrastructure faults from becoming fleet-wide incidents.

---
title: "Improving Critical Infrastructure Rollouts"
type: source
tags: [infrastructure, progressive-delivery, docker, reliability]
date: 2017-06-22
source_file: "/mnt/ken_personal_wiki/Articles/Improving Critical Infrastructure Rollouts - Labs.md"
---

## Summary
This Spotify Labs retrospective explains why fleet-wide [[Docker]] changes became unacceptable as container adoption grew from prototypes to mission-critical services on thousands of hosts. After recurrent upgrade regressions and a harmful 2016 configuration rollout, [[Spotify]] built [[Tsunami]] to assign desired infrastructure state gradually across a representative production population while centralizing audit, percentage controls, and prospective service-level-objective stopping. The account is a first-party design narrative rather than comparative reliability evidence, and its duplicated remote rollout chart is no longer retrievable.

## Key Claims
- Infrastructure rollout risk grew with Docker adoption: by February 2017, Spotify reported that 80% of production backend services ran as containers across thousands of hosts.
- Docker upgrades produced progressively harder-to-detect failures, including changed hostname and command semantics, orphaned containers retaining ports, and orphaned `docker-proxy` processes preventing new containers from starting.
- Fleet-wide restarts must be gradual because simultaneous restarts of access and login services can degrade user experience and trigger reconnect storms in downstream systems.
- Testing only infrastructure-team or nonproduction instances did not cover the heterogeneous production services needed to expose upgrade incompatibilities.
- [[Tsunami]] models a rollout as a variable whose permitted values change over time and returns a flat JSON desired state that each client is responsible for enacting.
- Central control can provide shared audit history, role-aware percentage floors and ceilings, and automatic rollout termination when service-level objectives are breached.
- Spotify reports using Tsunami for [[Helios]], Docker, and Puppet upgrades plus restart-inducing configuration changes, but supplies no comparison of incident frequency, detection latency, or recovery outcomes before and after adoption.

## Key Quotes
> "Tsunami is essentially linear interpolation as a service." - concise description of time-based fleet allocation

> "We need to upgrade on real production services" - reason a slow, representative rollout was necessary

## Connections
- [[Spotify]] - production setting in which Docker became critical infrastructure and broad changes became too risky.
- [[Docker]] - container runtime whose upgrades and configuration changes motivated the rollout service.
- [[Tsunami]] - desired-state service that allocates infrastructure versions gradually across the fleet.
- [[Helios]] - Spotify orchestration system upgraded through Tsunami and affected by orphaned-container port conflicts.
- [[ProgressiveInfrastructureRollout]] - practice of spreading infrastructure changes across time and representative production cohorts.
- [[ChangeSafety]] - gradual exposure, monitoring, audit, and stopping controls bound change risk.
- [[DeploymentAutomation]] - clients automatically enact centrally selected desired state.

## Contradictions
- No direct contradiction was found. The source strengthens the wiki's staged-change guidance but qualifies test-first models: some infrastructure incompatibilities appeared only across the diversity of real production workloads.
- Gradual allocation limits exposure but does not by itself prove safe cohort selection, client convergence, rollback, dependency compatibility, or causal detection of a service-level-objective breach.

## Image Notes
- The Markdown embeds one unique remote PNG three times: once as a lead image and twice beside prose describing a 24-hour Helios rollout. The origin now returns HTTP 410, so the image could not be opened, classified reliably, or retained; no claim here relies on visual details inferred from its filename, alt text, caption, or surrounding prose.

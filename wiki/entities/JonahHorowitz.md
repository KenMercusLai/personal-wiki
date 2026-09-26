---
title: "Jonah Horowitz"
type: entity
tags: [infrastructure, devops, release-engineering]
sources:
  - configuration-management-is-an-antipattern-by
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Overview
[[JonahHorowitz]] is the practitioner identified by the `@jonahhorowitz` handle on the source's slides, presenting an experience-based critique of mutable configuration management and an alternative based on immutable images.

## Current Profile
Horowitz describes a progression from manual CVS, `scp`, and service restarts, through shell and Perl deployment tooling, to CFEngine, Chef, and Puppet. He credits configuration management with making infrastructure reproducible and understandable, then argues that cloud images and containers provide a safer release boundary by moving assembly into a tested build pipeline and replacing instances rather than repairing them in place.

The talk also draws on his reported Netflix experience: performance and security teams contributed to a base AMI, application packages were installed into derived images, base images were canaried and promoted regularly, and deployment tooling moved the same artifacts across regions. These are first-person practitioner claims, not an independent evaluation of the systems or their outcomes.

## Key Characteristics
- Grounds infrastructure recommendations in a personal path from manual deployment to configuration management and immutable delivery.
- Treats release engineering, fleet consistency, recovery speed, security response, and autoscaling as one operational system.
- Credits configuration management's historical benefits while arguing that its mutable convergence model has reached a practical limit.
- Advocates base images, application packages, canaries, rolling or blue/green replacement, service discovery, and feature flags.

## Evidence
- Operational progression: [[configuration-management-is-an-antipattern-by]] recounts manual CVS releases, a shell script that grew into a large Perl tool, and later CFEngine, Chef, and Puppet use.
- Configuration-management assessment: [[configuration-management-is-an-antipattern-by]] reports strong CFEngine gains but emphasizes ownership bottlenecks, dangerous shared authority, partial runs, and fleet drift.
- Netflix practice: [[configuration-management-is-an-antipattern-by]] attributes weekly base-AMI promotion, faster security rebuilds, and Aminator-based image creation to Netflix experience.
- Delivery recommendation: [[configuration-management-is-an-antipattern-by]] advocates application-specific AMIs or Docker images deployed through rolling or blue/green strategies.

## Qualifications
The source supplies no conventional author byline, biography, publication date, or measured comparative study; the attribution rests on the repeated `@jonahhorowitz` slide handle and the first-person narrative. Reported operational outcomes and tool recommendations are historical and context-specific.

## What Changed
- Added Jonah Horowitz as the slide author and practitioner voice behind the immutable-infrastructure argument.

## Relationships
- [[Netflix]] - employer context named for base-image construction and promotion practices.
- [[ConfigurationManagement]] - technology whose benefits and failure modes structure the talk.
- [[ImmutableInfrastructure]] - replacement model Horowitz recommends.
- [[DeploymentAutomation]] - rolling and blue/green release mechanisms used to promote images.

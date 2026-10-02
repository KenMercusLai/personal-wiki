---
title: "Full Cycle Development"
type: concept
tags: [software-engineering, devops, production-ownership, team-design]
sources:
  - full-cycle-developers-at-netflix-operate-what-you-build
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[FullCycleDevelopment]] is a team operating model in which developers collectively own design, development, testing, deployment, operation, and support, with platform tooling, training, staffing, and work design making that breadth sustainable.

## Current Synthesis
Netflix Edge Engineering presents full-cycle development as a response to fragmented lifecycle ownership. Specialist handoffs can protect developer focus and create depth within each function, but they also separate operational pain from the people able to change the code, introduce communication loss and queues, and slow detection, diagnosis, deployment, and learning. A partial hybrid leaves the same bottleneck when nominally empowered developers still defer to a release specialist.

The model closes that loop by assigning lifecycle responsibility to the development team rather than requiring every individual to work on every concern simultaneously. Developers apply engineering discipline to operational and support problems, while an on-call rotation protects focused work for teammates. Central platform specialists turn recurring needs into deployment, rollback, monitoring, alerting, and self-service capabilities; domain teams retain local responsibility and can depart from the paved road when the value justifies the cost.

This is an organizational system, not a mandate to add unlimited duties. Broader ownership raises cognitive load and requires interest in breadth, training, adequate staffing, planning capacity, management support, and prioritization of automation alongside feature work. Deep specialist roles remain valuable, and organizations without Netflix's scale should adopt only the complexity their needs and resources can sustain.

## Key Claims
- End-to-end team ownership can shorten feedback loops that specialist handoffs make indirect or lossy.
- Full-cycle responsibility spans design, development, testing, deployment, operation, and support.
- Central specialists scale their depth by building reusable tools and supported paved roads rather than taking domain responsibility away from teams.
- Sustainable ownership requires training, staffing headroom, operational prioritization, and rotations that contain interrupt work.
- The model preserves specialist roles and allows local variation; it does not require every developer to become equally expert in every domain.
- Wider responsibility increases cognitive load and can cause burnout when authority and duties are not matched by support and capacity.

## Evidence
- Handoff problem: [[full-cycle-developers-at-netflix-operate-what-you-build]] reports slower releases, higher detection and resolution time, and second-hand feedback under separate Edge Engineering operations ownership.
- Hybrid limit: [[full-cycle-developers-at-netflix-operate-what-you-build]] says developers with deploy access still deferred to release specialists while daily operations work displaced automation.
- Ownership scope: [[full-cycle-developers-at-netflix-operate-what-you-build]] assigns development teams responsibility for deployment, performance, capacity, alerting, incidents, and support across the full lifecycle.
- Platform enablement: [[full-cycle-developers-at-netflix-operate-what-you-build]] describes centralized specialist teams producing common infrastructure, deployment pipelines, monitoring, and reusable tools.
- Sustainability controls: [[full-cycle-developers-at-netflix-operate-what-you-build]] requires bootcamps, ongoing training, staffing headroom, planning, automation investment, platform partnerships, and on-call rotation.
- Reported outcome: [[full-cycle-developers-at-netflix-operate-what-you-build]] says Edge Engineering reached routine frequent releases, hour-scale rather than day-scale canaries, and faster issue investigation.

## Counterevidence & Qualifications
The source is a first-party retrospective from one Netflix organization, not a controlled comparison. Its before-and-after claims lack definitions, time series, exact release, detection, recovery, incident, support-load, retention, and burnout measures, so platform investment, architecture, staffing, culture, and organizational learning cannot be separated from the ownership change. Breadth may reduce specialist depth, and regulated, safety-critical, high-risk, or separation-of-duties environments may require independent operation or review. A rotation only protects focus if interrupt work is bounded; otherwise responsibility can spread to everyone. The durable claim is team-level closed-loop ownership with proportionate enablement, not that every person or company should copy Netflix's roles or tools.

## What Changed
- Created the concept around full-lifecycle team ownership and its enabling organizational system.
- Made staffing, training, platform leverage, rotation design, and operational prioritization prerequisites rather than implementation details.
- Preserved specialist depth and local adaptation as explicit boundaries on the model.

## Related Concepts
- [[ProductionOwnership]] - supplies the deploy, operate, support, and recovery responsibility inside the broader lifecycle model.
- [[DevOpsCulture]] - provides the shared-responsibility and feedback-loop principles that full-cycle teams operationalize.
- [[InternalDeveloperPlatform]] - packages recurring operational expertise into reusable paved-road capabilities.
- [[ContinuousDelivery]] - provides repeatable delivery and rollback mechanisms needed for routine team-owned releases.
- [[ServiceObservability]] - makes production behavior visible enough for owning teams to detect and diagnose failure.
- [[DeveloperExperience]] - determines whether broad responsibility is supported by usable workflows or converted into toil.
- [[PsychologicalSafety]] - helps operational accountability produce learning rather than blame.

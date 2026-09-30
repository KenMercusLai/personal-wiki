---
title: "Jimmy Bogard"
type: entity
tags: [software-architecture, microservices]
sources:
  - jimmy-bogard-my-microservices-faq
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[JimmyBogard]] is a software practitioner represented here through a 2018 FAQ that defines microservices by [[ServiceAutonomy]] rather than by size metrics or technology choices.

## Current Profile
Bogard's account is deliberately contextual. He treats a microservice as the smallest boundary that can still be independently owned, built, deployed, run, secured, and recovered, then tests common architecture choices against that autonomy requirement. His advice resists universal prescriptions: containers, languages, repositories, REST, messaging, streams, and queues are enabling choices whose value depends on whether they preserve the boundary.

The profile is source-bounded. The wiki has one concise practitioner article and no biography, project history, comparative evidence, or later statement establishing whether these views persisted unchanged.

## Key Characteristics
- Defines microservices through autonomous responsibility rather than a fixed physical size.
- Separates architecture properties from containers, languages, protocols, and repository layouts.
- Treats domain, organizational, technical, and business context as determinants of viable service boundaries.
- Uses coupling and independent operation to distinguish services from modules.
- Frames architecture adoption around delivery-value-stream bottlenecks rather than fashion.

## Evidence
- Boundary definition: [[jimmy-bogard-my-microservices-faq]] defines a microservice as a service focused on the smallest autonomous boundary.
- Technology neutrality: [[jimmy-bogard-my-microservices-faq]] rejects containers, particular languages, REST, messaging, and repository layout as defining properties.
- Coupling test: [[jimmy-bogard-my-microservices-faq]] argues that RPC-only communication or forced coordinated repository changes can reveal modules inside a larger service.
- Decision framing: [[jimmy-bogard-my-microservices-faq]] asks whether service size is actually constraining delivery speed before recommending microservices.

## Qualifications
The profile derives from one self-authored FAQ published in 2018. Its definitions are normative and unmeasured, and the article does not show how Bogard applied them in a specific system or how often the proposed tests produce better architecture outcomes.

## What Changed
- Created a source-bounded profile centered on Bogard's autonomy-based microservice definition.

## Relationships
- [[ServiceAutonomy]] - central architectural property in Bogard's microservice definition.
- [[ModularMonolith]] - adjacent architecture that can preserve cohesive boundaries without independent deployment.
- [[MicroservicePlatformEngineering]] - enabling capabilities that can make autonomous services operable.
- [[DevOpsCulture]] - broader delivery ownership Bogard associates with microservice adoption.

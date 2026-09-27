---
title: "Engineers Shouldn’t Write ETL: A Guide to Building a High Functioning Data Science Department"
type: source
tags: [data-science, organization-design, data-platform, etl]
date: 2016-03-16
source_file: "/mnt/ken_personal_wiki/Articles/Engineers Shouldn’t Write ETL- A Guide to Building a High Functioning Data Science Department - Stitch Fix Technology – Multithreaded.md"
---

## Summary
[[JeffMagnusson]] argues that the conventional split among data-science “thinkers,” data-engineering “doers,” and infrastructure “plumbers” creates slow handoffs, misaligned incentives, and weak production ownership. Drawing on [[StitchFix]], he proposes that data scientists own vertically focused work from ETL through deployed algorithms or APIs, while engineers build horizontal platforms, services, abstractions, and resilience that make this autonomy safe and repeatable. The proposal deliberately trades some technical specialization and efficiency for velocity, ownership, and accountability.

## Key Claims
- The thinker-doer handoff makes engineers accountable for implementing and supporting other people’s ideas while separating scientists from production consequences.
- Many companies do not operate at a scale that justifies highly specialized big-data roles, and specialization can generate unnecessary technical and organizational complexity.
- [[DataScienceOrganizationDesign]] should give data scientists end-to-end ownership of domain-specific pipelines, analysis, business logic, deployed algorithms, and operational service levels.
- [[DataSciencePlatformEngineering]] should focus engineers on reusable horizontal capabilities for building, scheduling, deploying, observing, and recovering data-science workloads.
- Scientists and engineers still need close partnership, but the durable boundary is shared platform versus domain logic rather than an assembly-line handoff.
- Autonomy can increase iteration speed and improve domain-sensitive trade-offs even when scientist-written implementations are less technically efficient.
- The model depends on strong platform engineers anticipating needs, usable self-service primitives, and organizational discipline when incidents create pressure to recentralize ownership.

## Key Quotes
> “Engineers should not write ETL.” — shorthand for rejecting ETL as a dedicated handoff role rather than eliminating engineering support for data pipelines.

> “Engineers design new Lego blocks that data scientists assemble in creative ways to create new data science.” — analogy for horizontal platform work supporting vertical ownership.

## Connections
- [[JeffMagnusson]] — author presenting the Stitch Fix organizational model.
- [[StitchFix]] — company case behind the proposed data-science operating model.
- [[DataScienceOrganizationDesign]] — broader choice of ownership, reporting, collaboration, and production responsibility.
- [[DataSciencePlatformEngineering]] — horizontal platform role proposed for engineers supporting data scientists.
- [[DataScienceEngineeringPractice]] — production ownership requires scientists to develop, deploy, monitor, debug, and support their work.
- [[IndustryDataScience]] — domain-focused practice expected to produce operational algorithms and APIs rather than only reports.
- [[InternalDeveloperPlatform]] — related self-service pattern that packages infrastructure and operational defaults.

## Contradictions
- The source’s categorical title is narrower in substance: engineers still build ETL frameworks and partner on initial solutions, while scientists own domain-specific pipeline composition and business logic.
- The proposed model accepts lower local technical efficiency and offers a first-party practitioner account rather than comparative evidence that the ownership structure improves reliability, retention, velocity, or business outcomes across organizations.
- The claim that most companies lack “big data” is tied to the technology and scale assumptions of 2016 and does not remove later governance, privacy, security, lineage, reliability, or regulatory reasons for specialist data-engineering work.

---
title: "The Strong and Weak Forces of Architecture"
type: source
tags: [architecture, governance, organizational-design]
date: 2021-11-10
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Martin Fowler - The Strong and Weak Forces of Architecture.md"
---

## Summary
[[MartinFowler]] uses [[MYOB]]'s team, domain, and vertical structure to argue that architecture governance should vary with organizational alignment forces rather than applying one coupling rule everywhere. The article introduces [[ArchitectureAlignmentForces]]: tight alignment inside a domain can support faster change and some tighter coupling, while weaker alignment across verticals or the whole organization requires looser coupling, stronger contracts, versioning, and slower governance mechanisms such as [[TechnologyRadar]].

## Key Claims
- Architecture governance should be sensitive to decision scope and blast radius rather than using one strict rule at all organizational levels.
- Within a domain, high-bandwidth communication, shared domain knowledge, and shared delivery priorities create strong alignment forces that can make tighter coupling tolerable.
- Across domains within a vertical, alignment is weaker, so negotiation slows and technology choices, shared code, and integration practices need more care.
- Across the whole organization, alignment forces are weak, so published APIs, event schemas, shared infrastructure, and technology guidance need high encapsulation, versioning, and deprecation discipline.
- [[DefaultTrialRetire]] and [[TechnologyRadar]] fit different levels of alignment: local agreement can be informal in domains, while broader technology choice needs more formal communication.
- Highly coupled integration, including ETL or database-level integration, becomes much more costly as social distance and blast radius increase.

## Key Quotes
> "Neither of those approaches are ideal." - on uniform strict governance versus unconstrained team autonomy

> "Being aware of these forces of alignment within our organisation allows us to understand what is going to be easy and what is going to be hard" - core use of the model

## Connections
- [[MartinFowler]] - author presenting the architecture-governance model.
- [[MYOB]] - organization used as the worked example.
- [[ArchitectureAlignmentForces]] - central concept of varying governance by organizational alignment strength.
- [[DefaultTrialRetire]] - domain-level technology choices can use local leadership and small agreed sets.
- [[TechnologyRadar]] - organization-level technology direction mechanism for weak alignment forces.
- [[IntegrationStrategy]] - integration contracts need stronger versioning and encapsulation as scope grows.
- [[CapabilityOrientedIntegration]] - clean capability boundaries become more important as consumers are farther away organizationally.

## Contradictions
- No direct contradiction found. The source qualifies architecture-governance material by arguing that coupling, shared code, and contribution models should be evaluated by organizational scope rather than treated as universally good or bad.

---
title: "User Journey Mapping"
type: concept
tags: [ux-research, product-design, journey-mapping]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
  - blog-martinfowler-com-building-infrastructure-platforms
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[UserJourneyMapping]] is the practice of representing how users move through a product to accomplish important goals, often with personas, steps, pain points, and repeated flows.

## Current Synthesis
The Crashlytics source uses journey mapping to turn scattered product knowledge into team alignment. The product manager identified four critical journeys, and the designer mapped them into persona-based flows. Reviewing and revising those maps with the team created a shared foundation for the redesign and revealed the recurring [[InvestigateAndFixFlow]] that cut across monitoring, stability checking, crash prioritization, and customer debugging.

The infrastructure-platform source applies the method to an internal service. Mapping onboarding across developer, system, and platform-team lanes makes handoffs, loops, waiting, manual work, and missing automation visible. Its three diagrams distinguish a complex current journey, an idealized three-step self-service path, and a realistic intermediate release, showing that journey maps can express both diagnosis and staged improvement rather than only a final design.

## Key Claims
- Journey maps help a redesign team agree on how the product is actually used.
- Experienced product managers, long-tenured teammates, developer relations, researchers, and users can all supply journey evidence.
- Mapping multiple journeys can reveal a recurring micro-flow that should shape product structure.
- Sharing and revising maps with the team turns research into alignment rather than a private design artifact.
- Journey maps are most useful when they precede solution design and problem framing.
- Cross-team swimlanes reveal ownership handoffs and work hidden behind a user's apparent task.
- Comparing current, ideal, and intermediate journeys can guide staged automation without pretending that full self-service is immediate.

## Evidence
- Evidence gathering: [[advocating-for-a-complete-product-redesign-google-design-medium]] describes talking with teammates, developer relations, user researchers, and users before redesigning.
- Four journeys: [[advocating-for-a-complete-product-redesign-google-design-medium]] lists monitoring a new release, checking stability, prioritizing crashes, and debugging customer problems.
- Flow mapping: [[advocating-for-a-complete-product-redesign-google-design-medium]] says each journey was mapped into flows using personas.
- Team alignment: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the flows were shared with the team and revised as needed.
- Image evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected journey diagrams that show multi-step monitoring and investigate-and-fix sequences.
- Platform onboarding: [[blog-martinfowler-com-building-infrastructure-platforms]] identifies nine developer steps, cross-team handoffs, loops, waiting, and manual platform-team activity in the complex onboarding example.
- Staged target: [[blog-martinfowler-com-building-infrastructure-platforms]] contrasts that current journey with a three-step self-service ideal and an intermediate path that still involves the platform team.

## Counterevidence & Qualifications
The Crashlytics journey diagrams are low-resolution, so only their broad structure is legible. The infrastructure-platform diagrams make lane crossings and loops visible but omit step labels, so the prose supplies the nine-step and self-service interpretation. Neither source compares journey mapping against other research methods or measures whether the maps independently improved redesign or platform outcomes. An idealized short journey can also hide implementation, governance, or support complexity behind the interface.

## What Changed
- Added internal-platform onboarding as a cross-team journey-mapping case.
- Added current, ideal, and intermediate maps as a staged service-design pattern.

## Related Concepts
- [[ProductRedesign]] - journey maps grounded the redesign case.
- [[InvestigateAndFixFlow]] - recurring flow discovered through journey mapping.
- [[InformationHierarchy]] - product hierarchy should match the important journey steps.
- [[CustomerLedProductDevelopment]] - user journeys translate customer behavior into product decisions.
- [[UXResearchInformationDesign]] - maps organize observed behavior into a communicable structure.
- [[InfrastructurePlatformProductManagement]] - uses journey maps to prioritize self-service and automation work.
- [[DeveloperExperience]] - onboarding friction is a direct developer-facing product outcome.

---
title: "Adtech"
type: concept
tags: [advertising, tracking, privacy, automation]
sources:
  - doc-searls-brands-need-to-fire-adtech
  - engineering-to-improve-marketing-effectiveness-part-1
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[Adtech]] is the technical and operational system used to create, localize, deliver, target, measure, and optimize advertising; some uses depend on identity and behavioral tracking, while others focus on creative production and campaign workflow.

## Current Synthesis
The sources expose two different meanings of adtech. [[DocSearls]] uses the term narrowly for tracking-based direct response that finds targetable people across cheap inventory; that mechanism can weaken control over adjacency, publisher revenue, and personal data. Netflix uses “AdTech” as the name of a broader internal engineering charter covering creative-asset workflow, cross-channel campaign creation, experimentation, measurement, and spend optimization.

The useful synthesis separates capabilities from practices. Automation can support asset localization, encoding, campaign visibility, contextual buying, or deliberate sponsorship without requiring behavioral surveillance. Conversely, measurement and targeting can still create privacy, placement, fraud, and power risks even when they sit beside legitimate operational tooling. Evaluating an adtech system therefore requires its data inputs, optimization objective, inventory controls, causal measurement, consent model, and human decision boundary rather than the label alone.

## Key Claims
- Adtech can include creative production, localization, campaign operations, delivery, targeting, measurement, and optimization rather than one uniform business model.
- Tracking-led systems optimize audience delivery and measurable response rather than the contextual association central to [[BrandAdvertising]].
- Identity and inferred profiles can make individual behavior an input to targeting, retargeting, and measurement.
- Automated cost optimization can place brands beside objectionable or fraudulent content when media quality is not the primary objective.
- Operational automation can reduce repetitive asset work and expose campaign bottlenecks while preserving human creative and strategic judgment.
- Adtech evaluation must distinguish attributed response from [[MarketingIncrementality]] and inspect privacy, consent, placement, and intermediary incentives.

## Evidence
- Objective and lineage: [[doc-searls-brands-need-to-fire-adtech]] traces adtech to direct-response and direct-mail practice rather than to contextual brand sponsorship.
- Placement mechanism: [[doc-searls-brands-need-to-fire-adtech]] argues that automated systems chase selected audiences through cheaper inventory, explaining brand-safety failures.
- Externalities: [[doc-searls-brands-need-to-fire-adtech]] connects tracking-based delivery to privacy invasion, fraud, malware, fake-news incentives, and content-volume pressure.
- Publisher control: [[doc-searls-brands-need-to-fire-adtech]] says publishers outsourced sales and income production to many third-party systems because practical online alternatives were scarce.
- User response: [[doc-searls-brands-need-to-fire-adtech]] frames blocking and tracking protection as legitimate reactions and proposes open user-controlled interest signaling.
- Broader operating scope: [[engineering-to-improve-marketing-effectiveness-part-1]] uses AdTech for asset workflow, campaign execution, experimentation, measurement, and optimization across online and offline channels.
- Automation boundary: [[engineering-to-improve-marketing-effectiveness-part-1]] assigns title, market, and creative strategy to human teams while engineering standardizes repeatable production and delivery work.
- Measurement objective: [[engineering-to-improve-marketing-effectiveness-part-1]] says paid media should seek incremental outcomes rather than conversions that would have happened anyway.

## Counterevidence & Qualifications
Searls's source is a polemical 2017 essay rather than a neutral taxonomy or comparative effectiveness study. Its near-zero effectiveness claim is unsupported, and its forecast that GDPR would extinguish adtech is not evaluated with later evidence. The Netflix source demonstrates broader industry usage but is also a first-party account: it does not disclose targeting data, consent practice, inventory controls, privacy effects, experiment methods, or measured improvements, so operational breadth does not answer Searls's normative critique.

## What Changed
- Expanded the concept from surveillance-led placement to include creative production and campaign-operations infrastructure.
- Preserved privacy and brand-safety criticism as capability-specific evaluation rather than treating broader terminology as a rebuttal.
- Added incrementality and the human creative boundary as criteria for judging optimization systems.

## Related Concepts
- [[ProgrammaticAdvertising]] - supplies automated buying and placement mechanisms used by part of the adtech stack.
- [[BehavioralTargeting]] - converts observed actions into audience labels for ad delivery.
- [[BrandAdvertising]] - contrasts with direct-response adtech by prioritizing media context and association.
- [[AdBlocking]] - is a user-side response to unwanted advertising and tracking.
- [[WebAdEconomics]] - describes the publisher, platform, and content incentives surrounding adtech.
- [[IdentityResolution]] - links identifiers and behavior across contexts for targeting and measurement.
- [[MarketingOperations]] - coordinates the campaign, asset, data, and workflow layer of the broader adtech definition.
- [[MarketingAssetPipeline]] - covers creative production, localization, encoding, and delivery capabilities.
- [[MarketingIncrementality]] - asks whether optimized advertising changed outcomes rather than merely receiving credit.

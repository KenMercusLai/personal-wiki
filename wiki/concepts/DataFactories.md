---
title: "Data Factories"
type: concept
tags: [data, analytics, platforms, privacy, operating-models]
sources:
  - data-factories-stratechery-by-ben-thompson
  - demystifying-data-monetization
  - dont-post-your-kid-online
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DataFactories]] are repeatable organizational and technical systems that collect, combine, transform, analyze, and deliver data-derived outputs such as recommendations, targeting segments, operational decisions, insights, and customer-facing services.

## Current Synthesis
The two sources use the factory metaphor at complementary levels. Thompson describes the transformation engine beneath large consumer aggregators: user, behavior, content, advertiser, third-party, and off-platform inputs become recommendations, distribution decisions, targeting, and inferred profiles. Gandhi and coauthors describe the capability a company deliberately builds to monetize data internally and externally: a shared platform, enrichment pipelines, self-service analytics, operating model, management oversight, governance, security, privacy, and partner compliance.

Together they imply that a data factory is not merely a warehouse or model pipeline. It is an operating system connecting inputs to repeatable decisions and services, with responsibility for the resulting outputs. The sharenting source makes the represented person visible inside that system: family posts, purchases, browsing, social ties, device data, and third-party records can begin constructing a child's profile before the child can consent. Its broker diagrams also show that the output does not end at a stored record; profiles are validated, enhanced, activated across channels, and updated through response feedback.

A single source of truth and scalable automation can make reuse efficient, but centralization also concentrates access, inference, security, and consent risk. Raw-input access therefore remains an incomplete governance response when the most consequential artifacts are derived profiles, predictions, activations, and prescribed actions.

## Key Claims
- A data factory is defined by repeatable transformation and delivery across multiple sources, not by collection or storage alone.
- Its outputs can create internal operational value, external customer value, and targeting or profile value for advertisers, including profiles of people who never supplied the full record themselves.
- Content, interfaces, and advertisements can act as catalysts that generate additional behavioral inputs as people use the system.
- A shared platform can harmonize data into a usable source of truth and expose analysis, modeling, visualization, and self-service access.
- Technology alone is insufficient; operating structure, management oversight, metrics, commercialization, governance, legal policy, security, privacy, and supplier obligations belong inside the system boundary.
- Raw-data access and portability do not reveal every inferred, matched, scored, activated, or recommended output created by the factory.
- Automation and centralization improve reuse while increasing the need for access control, output accountability, and demonstrable protection.

## Evidence
- Multi-sided transformation: [[data-factories-stratechery-by-ben-thompson]] describes user actions, content, advertiser uploads, third-party records, and embedded controls becoming product and advertising outputs.
- Monetization pipeline: [[demystifying-data-monetization]] defines a data factory as automated collection, enrichment, transformation, and insight derivation for internal and external opportunities.
- Processed value: [[data-factories-stratechery-by-ben-thompson]] says the outputs improve connection, discovery, supplier reach, and niche advertising efficiency; [[demystifying-data-monetization]] adds cost, revenue, insight, and analytical-service outcomes.
- Platform layer: [[demystifying-data-monetization]] calls for storage, harmonization, processing, scalable computing, intuitive interfaces, self-service analytics, and visualization.
- Operating layer: [[demystifying-data-monetization]] includes organizational structure, oversight, KPIs, profit, governance, compliance, legal and technical counsel, cybersecurity, privacy, and supplier requirements.
- Hidden output: [[data-factories-stratechery-by-ben-thompson]] contrasts downloadable submitted data with undisclosed profiles produced by matching all sources.
- Unexpected reuse: [[data-factories-stratechery-by-ben-thompson]] cites targeting through contact details supplied or known in other contexts, including a phone number supplied for account security.
- Child-profile accumulation: [[dont-post-your-kid-online]] argues that parent browsing, purchases, contacts, photos, metadata, and milestone posts can become inputs to a child's profile before meaningful consent is possible.
- Broker activation loop: [[dont-post-your-kid-online]] retains an Acxiom diagram in which multi-channel signals are unified, enhanced with first-, second-, and third-party data, activated across channels, and returned through a continuous improvement cycle.
- Attribute breadth: [[dont-post-your-kid-online]] retains a Cracked Labs comparison attributing wide demographic, household, financial, health, purchase, search, political, and behavioral fields to Acxiom and Oracle profiles.

## Counterevidence & Qualifications
All three sources are 2018 strategic or journalistic accounts rather than technical audits or comparative outcome studies. "Single source of truth" is an architectural aspiration: harmonization can centralize errors, hide lineage disagreements, or impose one team's ontology. A factory metaphor can also obscure judgment, labor, consent, and the rights of people represented in the data—especially children whose profiles may be assembled through adult activity. Anonymization, aggregation, policy, and cybersecurity claims require specific controls and evidence; the MIT Sloan source does not provide them. The sharenting article names serious downstream uses but does not trace a child's post into a verified adverse decision. Processed-profile disclosure may improve legibility but can expose sensitive inferences or third-party data and does not guarantee comprehension, correction, switching, competition, or reduced harm.

## What Changed
- Broadened the concept from aggregator profiling to an enterprise operating system for internal and external data value.
- Added platform, self-service analytics, organizational design, governance, security, privacy, and supplier compliance as system components.
- Added the tension between scalable centralization and concentrated inference, access, and security risk.
- Added child-profile formation before consent and the broker cycle from multi-channel unification through enhancement, activation, and feedback.

## Related Concepts
- [[DataMonetization]] - supplies the internal and external outcomes a data factory is built to create.
- [[DataAsAService]] - is one external product that can emerge from the factory's acquisition, transformation, and delivery capabilities.
- [[AggregationTheory]] - explains the demand power within which major consumer-platform data factories operate.
- [[BehavioralTargeting]] - converts behavior into one class of targetable factory output.
- [[OrganizationalDataSharing]] - broadens usable inputs across teams while creating semantic and governance coordination needs.
- [[PrivacyProtectionResourceInequality]] - qualifies governance models that require individuals to inspect and act on disclosed outputs.
- [[Sharenting]] - shows how adult family activity can feed a child's profile before the represented person can consent.

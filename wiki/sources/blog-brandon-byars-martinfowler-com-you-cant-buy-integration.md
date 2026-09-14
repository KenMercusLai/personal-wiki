---
title: "You Can't Buy Integration"
type: source
tags: [integration, architecture, enterprise-architecture, api]
date: 2021-12-14
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Brandon Byars (martinfowler.com) - You Can't Buy Integration.md"
---

## Summary
Brandon Byars argues that commercial integration products are not a way to buy integration itself; they are specialized programming environments that can simplify tactical workflow and connectivity work. The strategic integration problem is designing clean interfaces over digital capabilities, usually managed in a general-purpose language so teams can evolve abstractions, tests, observability, and delivery practices over time.

## Key Claims
- Integration strategy should shift from wiring systems together to exposing clean interfaces over business capabilities.
- Commercial integration tools are most useful when bounded to implementation concerns such as workflow, connectivity, adapters, and slow-moving B2B integration tails.
- Low-code integration DSLs can become harmful when enterprise mandates force interface evolution, transformations, resilience, and strategic API design into tool-specific source and runtimes.
- APIs should abstract capabilities such as ordering, plans, or eligibility rather than expose system names like SAP, Salesforce, or billing.
- Diagramming choices matter because tool-centered or system-centered diagrams encourage tactical implementation thinking, while capability diagrams make organizational agility visible.

## Key Quotes
> "You can't buy integration." — core thesis about build-versus-buy category error

> "Abstract the capability, not the system." — principle for API and integration design

## Connections
- [[BrandonByars]] — author of the article and Thoughtworks technology leader.
- [[IntegrationStrategy]] — the article's central architectural argument.
- [[CapabilityOrientedIntegration]] — captures the capability-over-system interface principle.
- [[IntegrationDSL]] — describes the commercial low-code integration tool category Byars critiques and bounds.
- [[SourceDiagramIsomorphism]] — names the graphical-palette/markup duality in tools such as AWS Step Functions.
- [[ChannelAPI]] — captures the article's preferred framing for channel-specific APIs and B2B adapters.
- [[DeveloperExperience]] — low-code integration tools are criticized for weaker diffing, modularity, testing, observability, and ecosystem support.
- [[TechnologyStackComplexity]] — integration lines become a hidden source of organizational technical debt as systems multiply.
- [[Thoughtworks]] — Byars is identified in the source as Head of Technology for Thoughtworks North America.

## Visual Evidence
- Figure 1 shows AWS Step Functions with JSON source on the left and a graphical workflow on the right, supporting the source-diagram-isomorphism claim.
- Figures 3-5 contrast generic application boxes, implementation-language diagrams, and tool-centered integration diagrams, showing how diagram focus can shift attention from capabilities to implementation details.
- Figure 6 shows Step Functions actions named as AWS implementation operations such as Lambda Invoke, SNS Publish, and DynamoDB PutItem.
- Figures 8-9 show Mulesoft's experience/process/system layering and the author's redrawn version, supporting his critique that the model keeps ESB-style implementation layering.
- Figure 10 illustrates the recommended inversion from a DSL-owning interface that calls Java to a Java-owned interface that uses DSL components tactically.
- Figure 11 shows B2B partner integrations mediated by DSL adapters into a common channel API.
- Figure 12 shows a web eCommerce channel API calling clean capability APIs for plans, eligibility, ordering, and provisioning.
- Figure 13 plots digital capabilities over time, with a digital organization accelerating faster after investing in clean interfaces.

## Contradictions
- No direct contradictions with existing wiki pages found. The source qualifies rather than rejects existing [[DeveloperExperience]] and [[TechnologyStackComplexity]] themes by applying them to enterprise integration tooling.

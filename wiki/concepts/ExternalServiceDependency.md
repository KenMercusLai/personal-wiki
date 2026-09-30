---
title: "External Service Dependency"
type: concept
tags: [software, suppliers, reliability, business-models]
sources:
  - just-landed-is-shutting-down-jon-grall-medium
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[ExternalServiceDependency]] is the operational and business risk created when a product needs another organization's data, infrastructure, API, pricing, policy, or continued existence to deliver its core value.

## Current Synthesis
The Just Landed case shows why a dependency can be both enabling and constraining. Commercial intermediaries made normalized flight data available to a small app team that could not reasonably contract with every airline, but supplier concentration left the team with little leverage over price, reliability, accuracy, modernization, or features. Supporting dependencies created a second burden: when StackMob, Urban Airship, Bing Maps, traffic, or mapping arrangements disappeared or restructured, the product absorbed replacement work and higher cost.

Dependency risk is therefore not limited to technical outages. It also includes data quality blamed on the downstream product, supplier-market concentration, changing terms, rising unit cost, migration labor, and the possibility that no economical replacement exists. Mitigation can include redundancy, portability, contracts, monitoring, fallbacks, self-hosting, and pricing that reflects consumption, but the source does not show that these measures were available or affordable for Just Landed.

## Key Claims
- External services can make a small product possible while simultaneously limiting its autonomy.
- Supplier concentration weakens the downstream product's leverage over price, quality, reliability, modernization, and feature development.
- Users experience upstream errors through the product they bought, so responsibility cannot be fully outsourced with the dependency.
- Service shutdowns, restructurings, restrictive terms, and replacement migrations create cumulative operating cost even when the core product is stable.
- Dependency exposure interacts with pricing: variable upstream consumption is dangerous when downstream revenue is fixed at purchase.
- Planned closure can be rational when a core dependency is likely to fail or become uneconomic before a viable fallback exists.

## Evidence
- Enabling dependency: [[just-landed-is-shutting-down-jon-grall-medium]] says flight-data intermediaries made the app feasible because direct airline contracts and normalization were impractical for its small team.
- Concentration and quality: [[just-landed-is-shutting-down-jon-grall-medium]] describes an effective flight-data duopoly and attributes nearly all customer complaints to inaccuracies outside the team's direct control.
- Replacement burden: [[just-landed-is-shutting-down-jon-grall-medium]] names StackMob, Urban Airship, and Bing Maps among services whose demise or restructuring required adaptation.
- Cost interaction: [[just-landed-is-shutting-down-jon-grall-medium]] says traffic, mapping, and flight data became more expensive while professional cohorts consumed far more data under one-time pricing.
- Closure trigger: [[just-landed-is-shutting-down-jon-grall-medium]] says the team preferred a scheduled shutdown to waiting until a key provider disappeared without an easy replacement.

## Counterevidence & Qualifications
The concept is grounded in one founder retrospective and does not independently verify supplier concentration, service quality, pricing changes, contract terms, architecture, or feasible alternatives. Direct sourcing, multiple providers, caching, degraded modes, enterprise pricing, subscriptions, usage caps, or a rewrite might reduce risk in other contexts. Those controls also carry engineering, legal, commercial, and user costs, so dependence is not itself evidence that a product is badly designed.

## What Changed
- Created the concept to distinguish business-critical supplier and data reliance from runtime-only graceful degradation.

## Related Concepts
- [[DependencyDegradation]] - handles runtime fallback and overload when dependencies partially fail.
- [[PlatformDistributionDependence]] - narrows external dependence to platform-controlled acquisition, data, and return traffic.
- [[DeveloperPlatformTrust]] - confidence in another organization's APIs, policy, pricing, and support affects willingness to build.
- [[UnitEconomics]] - variable supplier cost must be matched by sustainable revenue per user or transaction.
- [[ProductLifecycleTrust]] - downstream continuity depends partly on how external providers manage their own lifecycles.

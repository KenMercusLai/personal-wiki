---
title: "Compute Hurdle Rate"
type: concept
tags: [ai, compute, capital-allocation, cloud, strategy]
sources:
  - a-script-for-mark-zuckerberg
last_updated: 2026-10-26
knowledge_schema: synthesis-v1
---

## Definition
[[ComputeHurdleRate]] is a proposed capital-allocation rule in which the observable revenue from temporarily renting compute sets the minimum return an internal workload must exceed before capacity is reclaimed for company use.

## Current Synthesis
[[a-script-for-mark-zuckerberg]] applies the rule to [[MetaPlatforms]]. The company would build ahead of expected AI demand, rent a portion of unused capacity on short terms, and preserve the right to take it back. External rental revenue would both subsidize construction and expose an opportunity cost for internal projects: recommendation, advertising, generative content, or other uses should receive capacity only when their expected value exceeds the rental alternative.

The proposal turns a strategic forecast into a recurring allocation decision, but only imperfectly. Spot price is observable; the lifetime value, option value, learning benefit, reliability need, and user impact of an internal workload are not. Rental demand can also be volatile or correlated with Meta's own peak needs, and recall rights may lower the price customers will pay. The hurdle is therefore a decision aid rather than a complete valuation model.

## Key Claims
- Short-term external rental can convert otherwise idle compute into revenue while internal demand develops.
- A rental market supplies an observable opportunity cost against which internal AI projects can be compared.
- Recall rights preserve strategic access to capacity but may reduce customer value and attainable rental price.
- Internal allocation should include incremental revenue and strategic option value rather than treating utilization alone as success.
- A market hurdle can discipline overbuilding only if prices, workloads, recall terms, and shared infrastructure costs are comparable.

## Evidence
- Funding mechanism: [[a-script-for-mark-zuckerberg]] proposes using rental proceeds to support an even larger compute buildout.
- Opportunity-cost rule: [[a-script-for-mark-zuckerberg]] says Meta should take rented capacity back only when it can make more money using that capacity itself.
- Strategic scope: [[a-script-for-mark-zuckerberg]] expects qualifying internal uses to come primarily from advertising, recommendation, entertainment, shopping, and consumer connection.
- Capacity option: [[a-script-for-mark-zuckerberg]] requires the external arrangement to be short term and reclaimable because future internal demand is expected to grow.

## Counterevidence & Qualifications
The source proposes the mechanism but supplies no rental contract, capacity quantity, spot-price series, interruption policy, customer evidence, networking allocation, utilization forecast, or comparison of internal and external contribution margins. Rental price can understate internal value when a workload creates learning, retention, resilience, or a future option, and overstate it when outside demand is temporary. Reclaimable capacity is not equivalent to ordinary cloud supply if customers bear displacement risk. Power, cooling, accelerator mix, data locality, software, and network topology can also prevent nominally spare compute from being economically fungible.

## What Changed
- Created the concept from Thompson's proposed market-based discipline for Meta's AI capacity.
- Distinguished observable rental revenue from broader internal strategic value.
- Added recall rights, workload comparability, and correlated-demand limits.

## Related Concepts
- [[AIInfrastructureFinancing]] - rental proceeds can supplement the capital structures used to fund compute construction.
- [[ProductiveCapitalAllocation]] - the hurdle compares two competing uses of the same capital asset.
- [[ProductionCapacityBuffer]] - spare capacity has resilience and option value beyond immediate utilization.
- [[OpportunityCost]] - external rental revenue is the forgone alternative when compute is assigned internally.
- [[MetaPlatforms]] - company to which the source applies the proposed rule.

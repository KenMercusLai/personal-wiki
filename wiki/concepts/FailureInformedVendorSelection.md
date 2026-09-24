---
title: "Failure-Informed Vendor Selection"
type: concept
tags: [procurement, enterprise-software, due-diligence, incentives]
sources:
  - ask-a-repair-shop-philip-yurchuk
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[FailureInformedVendorSelection]] is the practice of evaluating products through people who repeatedly implement, repair, support, or replace them, using their exposure to downstream failures to supplement feature lists and vendor sales claims.

## Current Synthesis
The method begins with an information-location claim: the people selling a product know how to present it, while the people repairing or integrating products across brands see recurring defects, customization burden, maintainability, and the consequences of a poor choice. In consumer purchases this may be a repair shop; in enterprise software it may be a system integrator whose engineers have implemented several competing platforms.

That position is informative but not automatically independent. An integrator may depend on vendor certification, partner leads, referral revenue, or kickbacks, and a repairer may prefer products that suit its own skills or economics. Failure-informed selection therefore means triangulating several downstream accounts, asking about concrete failure modes and abandoned projects, checking disclosed incentives, and combining practitioner evidence with problem fit, pilots, references, contracts, and internal evaluation.

## Key Claims
- Post-sale practitioners observe recurring failures and maintenance costs that pre-sale feature comparisons often omit.
- Cross-vendor experience is more useful than familiarity with one product because it enables comparative judgments.
- Reputational exposure can motivate repairers and implementers to avoid products whose repeated failures customers may blame on them.
- Direct vendor engagement creates an information asymmetry when polished sales teams face buyers without comparable implementation evidence.
- Adviser incentives must be investigated because partnerships and vendor-dependent revenue can suppress candid criticism.
- Concrete failure questions and multiple independent accounts are stronger diligence inputs than an unqualified recommendation from one intermediary.

## Evidence
- Repair and reputation: [[ask-a-repair-shop-philip-yurchuk]] describes a shop refusing GE washer work because repeated product failures could be attributed to the repairer.
- Cross-product implementation: [[ask-a-repair-shop-philip-yurchuk]] argues that experienced system integrators learn product quality through customization and projects involving several vendors.
- Sales asymmetry: [[ask-a-repair-shop-philip-yurchuk]] contrasts vendor sales expertise with buyers' lack of inside knowledge despite the financial scale of enterprise purchases.
- Incentive conflict: [[ask-a-repair-shop-philip-yurchuk]] records concerns about partner agreements, leads, kickbacks, and revenue dependence distorting supposedly independent advice.

## Counterevidence & Qualifications
The evidence is anecdotal and does not show that repairers or integrators reliably predict total ownership cost or project success. Downstream experts may over-weight visible failures, repairability, familiar systems, billable customization, or products aligned with their certifications. Vendors may possess roadmap, security, support, and scale information that outside practitioners lack. The method is therefore a complement to structured requirements, technical trials, customer references, incentive disclosure, contractual diligence, and analysis of organizational fit, not a substitute for them.

## What Changed
- Created the concept from Yurchuk's comparison of appliance repair shops with enterprise system integrators.

## Related Concepts
- [[ContextualTechnologySelection]] - tests whether a candidate fits the buyer's workload, constraints, and organization.
- [[IntegrationStrategy]] - exposes the interface and customization work that enterprise product selection can conceal.
- [[TechnologyStackComplexity]] - names operational burden that downstream practitioners are positioned to observe.
- [[BenefitsRisksMitigations]] - provides a structured way to compare practitioner-reported strengths and failure modes.

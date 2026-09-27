---
title: "Optimal Decisions Group"
type: entity
tags: [company, insurance, pricing, optimization]
sources:
  - designing-great-data-products-oreilly
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[OptimalDecisionsGroup]] is the insurance-pricing company used in the Drivetrain Approach article as an early commercial example of connecting predictive models, simulation, and optimization to a business decision.

## Current Profile
The source says ODG began in 1999 by defining insurance pricing around the net-present value of multi-year customer profit under constraints such as market share. It modeled price acceptance, conditional profit, claims, servicing cost, and retention; explored controllable and external inputs through simulation; and optimized over the resulting outcome surface. The authors report gains of hundreds of millions of dollars for insurers, but provide no client-level methods or independent verification.

## Key Characteristics
- Treats policy price, coverage, marketing, service, and competitor response as controllable or modeled decision inputs.
- Uses randomized price changes to learn customer price elasticity.
- Combines acceptance, profit, and retention models across a multi-year horizon.
- Uses simulation to evaluate scenarios and optimization to select prices under constraints.
- Is presented through a source coauthored by its founder.

## Evidence
- Objective and constraints: [[designing-great-data-products-oreilly]] describes maximizing discounted multi-year profit while maintaining constraints such as market share.
- Experimental data: [[designing-great-data-products-oreilly]] says insurers randomized prices across hundreds of thousands of policies over months to estimate response.
- Model assembly: [[designing-great-data-products-oreilly]] links price elasticity, conditional profit, claims, overhead, and retention models.
- Decision system: [[designing-great-data-products-oreilly]] describes a simulator for scenario surfaces and an optimizer for desirable and catastrophic outcomes.

## Qualifications
The account is retrospective, contains no reproducible model specification or uncertainty analysis, and is not independent because coauthor Jeremy Howard founded ODG. Randomized price changes may impose customer, fairness, regulatory, and reputational costs, while optimizing expected profit can omit distributional and consumer-welfare effects unless explicitly constrained.

## What Changed
- Created a source-bounded profile of ODG's reported insurance-pricing system.

## Relationships
- [[JeremyHoward]] - founder and coauthor of the source describing ODG.
- [[DrivetrainApproach]] - general framework illustrated by ODG's pricing process.
- [[CustomerLifetimeValue]] - multi-year value objective used in the pricing model.
- [[IndustryDataScience]] - organizational practice that turns the component models into an operational product.
- [[DataExploration]] - randomized policy prices provide the interventional variation needed to learn response.

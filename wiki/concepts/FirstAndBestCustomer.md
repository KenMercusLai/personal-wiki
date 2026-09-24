---
title: "First-and-Best Customer"
type: concept
tags: [strategy, platforms, infrastructure, economies-of-scale]
sources:
  - amazons-new-customer-stratechery-by-ben-thompson
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[FirstAndBestCustomer]] is a platform-building pattern in which a company uses its own large, demanding operation—or an acquired anchor business—to justify high fixed-cost infrastructure before selling the resulting modular services to outside customers.

## Current Synthesis
[[BenThompson]] uses [[AWS]] as the clearest case: Amazon's ecommerce operation justified investment in computing infrastructure, while modular primitives made the same capacity useful to outside developers and increased returns to scale. He applies the same pattern to fulfillment, third-party sellers, and prospective logistics services.

Groceries expose the missing precondition. Perishable inventory, quality variance, spoilage, and city-level scale made AmazonFresh costly while it lacked enough dependable local demand. Thompson interprets the [[WholeFoods]] acquisition as buying that demand: Whole Foods could become the first-and-best customer for modular grocery procurement and fulfillment, after which delivery operations, other stores, or restaurants might become additional customers. The retained diagram makes the architecture explicit by placing several customer types above a shared high-fixed-cost service layer and modularized suppliers below it.

## Key Claims
- Internal or acquired anchor demand can make high fixed-cost infrastructure rational before an external market exists.
- Modular primitives let the same infrastructure serve heterogeneous outside customers without rebuilding an integrated system for each one.
- External customers increase utilization and returns to scale, potentially deepening the platform's moat.
- The pattern is strongest when the anchor customer is unusually demanding and therefore forces broadly useful capabilities to mature.
- Local, perishable, or otherwise scale-sensitive markets may require acquiring an anchor rather than waiting for organic demand.
- An anchor customer reduces initial utilization risk but does not prove that a profitable external platform will emerge.

## Evidence
- Internal cloud demand: [[amazons-new-customer-stratechery-by-ben-thompson]] says Amazon's ecommerce operation justified AWS's fixed costs before infrastructure primitives were sold externally.
- Fulfillment extension: [[amazons-new-customer-stratechery-by-ben-thompson]] says third-party merchants increase fulfillment-center utilization and Prime value after Amazon built distribution for itself.
- Grocery gap: [[amazons-new-customer-stratechery-by-ben-thompson]] argues AmazonFresh remained subscale because it lacked a first-and-best customer for perishable local inventory.
- Acquired anchor: [[amazons-new-customer-stratechery-by-ben-thompson]] interprets Whole Foods as guaranteed demand capable of underwriting a modular grocery-services layer.
- Diagrammed architecture: [[amazons-new-customer-stratechery-by-ben-thompson]] visually separates modular suppliers, Amazon Grocery Services, and customer channels including Whole Foods, delivery, and restaurants.

## Counterevidence & Qualifications
The concept is derived from one 2017 strategic essay and uses analogy more than outcome evidence. A captive anchor can hide poor unit economics, distort product design toward one customer's needs, or fail to create external demand. The source does not establish that Amazon's predicted grocery-services or restaurant-supply platform was built, profitable, or beneficial to suppliers and consumers.

## What Changed
- Established the anchor-customer mechanism as a distinct explanation for how Amazon funds and scales service platforms.
- Added acquisition as one route to obtaining the demand that organic platform growth cannot initially supply.

## Related Concepts
- [[AmazonCapabilityLedExpansion]] - converts capabilities matured for an anchor operation into adjacent external services.
- [[LogisticsVerticalIntegration]] - shows how constrained infrastructure may first be built for internal demand before possible commercialization.
- [[PlatformStickiness]] - describes a different moat mechanism based on ecosystem dependence rather than fixed-cost utilization.
- [[TimelessBusinessStrategy]] - anchors infrastructure investment in durable customer demand while the delivery mechanism changes.

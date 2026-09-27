---
title: "First-and-Best Customer"
type: concept
tags: [strategy, platforms, infrastructure, economies-of-scale]
sources:
  - amazons-new-customer-stratechery-by-ben-thompson
  - emergent-layers-chapter-3-explosive-growth-the-startup-medium
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[FirstAndBestCustomer]] is a platform-building pattern in which a company uses its own large, demanding operation—or an acquired anchor business—to justify high fixed-cost infrastructure before selling the resulting modular services to outside customers.

## Current Synthesis
[[BenThompson]] uses [[AWS]] as the clearest case: Amazon's ecommerce operation justified investment in computing infrastructure, while modular primitives made the same capacity useful to outside developers and increased returns to scale. He applies the same pattern to fulfillment, third-party sellers, and prospective logistics services.

[[AlexDanco]] supplies a compatible earlier account of the operating sequence. Amazon first builds an abstraction for itself, dogfoods and stress-tests it, then can turn an internal cost into an external revenue source and progress from a first-party wedge toward service, moat, marketplace, and platform. Danco extends the examples across publishing, fulfillment, cloud infrastructure, Prime, media, and voice commerce. Thompson gives the anchor-demand mechanism a sharper name and fixed-cost logic; neither source proves that every internally useful capability will generalize into a profitable outside platform.

Groceries expose the missing precondition. Perishable inventory, quality variance, spoilage, and city-level scale made AmazonFresh costly while it lacked enough dependable local demand. Thompson interprets the [[WholeFoods]] acquisition as buying that demand: Whole Foods could become the first-and-best customer for modular grocery procurement and fulfillment, after which delivery operations, other stores, or restaurants might become additional customers. The retained diagram makes the architecture explicit by placing several customer types above a shared high-fixed-cost service layer and modularized suppliers below it.

## Key Claims
- Internal or acquired anchor demand can make high fixed-cost infrastructure rational before an external market exists.
- Modular primitives let the same infrastructure serve heterogeneous outside customers without rebuilding an integrated system for each one.
- External customers increase utilization and returns to scale, potentially deepening the platform's moat.
- The pattern is strongest when the anchor customer is unusually demanding and therefore forces broadly useful capabilities to mature.
- Local, perishable, or otherwise scale-sensitive markets may require acquiring an anchor rather than waiting for organic demand.
- An anchor customer reduces initial utilization risk but does not prove that a profitable external platform will emerge.
- Internal dogfooding and stress-testing can mature a service before release, but internal fitness does not guarantee external demand.

## Evidence
- Internal cloud demand: [[amazons-new-customer-stratechery-by-ben-thompson]] says Amazon's ecommerce operation justified AWS's fixed costs before infrastructure primitives were sold externally.
- Fulfillment extension: [[amazons-new-customer-stratechery-by-ben-thompson]] says third-party merchants increase fulfillment-center utilization and Prime value after Amazon built distribution for itself.
- Grocery gap: [[amazons-new-customer-stratechery-by-ben-thompson]] argues AmazonFresh remained subscale because it lacked a first-and-best customer for perishable local inventory.
- Acquired anchor: [[amazons-new-customer-stratechery-by-ben-thompson]] interprets Whole Foods as guaranteed demand capable of underwriting a modular grocery-services layer.
- Diagrammed architecture: [[amazons-new-customer-stratechery-by-ben-thompson]] visually separates modular suppliers, Amazon Grocery Services, and customer channels including Whole Foods, delivery, and restaurants.
- Internal-to-external sequence: [[emergent-layers-chapter-3-explosive-growth-the-startup-medium]] says Amazon builds abstractions for its own use, tests them internally, and may convert the former cost into a revenue source.
- Portfolio illustrations: [[emergent-layers-chapter-3-explosive-growth-the-startup-medium]] applies the sequence to Kindle publishing, fulfillment, AWS, Prime, entertainment, and Alexa-linked commerce.

## Counterevidence & Qualifications
The concept is derived from two strategy essays and uses analogy more than outcome evidence. A captive anchor can hide poor unit economics, distort product design toward one customer's needs, or fail to create external demand. Thompson does not establish that Amazon's predicted grocery-services or restaurant-supply platform was built, profitable, or beneficial to suppliers and consumers; Danco's selected 2016 examples likewise do not compare failed internal platforms or distinguish the mechanism from Amazon's capital, distribution, and market power.

## What Changed
- Added internal dogfooding, stress-testing, and cost-to-revenue conversion as the operational sequence behind the anchor-customer mechanism.
- Extended the evidence beyond grocery to publishing, fulfillment, cloud, Prime, media, and voice while preserving the external-demand boundary.

## Related Concepts
- [[AmazonCapabilityLedExpansion]] - converts capabilities matured for an anchor operation into adjacent external services.
- [[LogisticsVerticalIntegration]] - shows how constrained infrastructure may first be built for internal demand before possible commercialization.
- [[PlatformStickiness]] - describes a different moat mechanism based on ecosystem dependence rather than fixed-cost utilization.
- [[TimelessBusinessStrategy]] - anchors infrastructure investment in durable customer demand while the delivery mechanism changes.
- [[EmergentLayerTheory]] - frames Amazon's internal abstractions as deliberate transitions from old constraints to new service and platform layers.

---
title: "Xeneta"
type: entity
tags: [company, saas, sea-freight, market-intelligence]
sources:
  - per-harald-borgen-boosting-sales-with-machine-learning
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[Xeneta]] is presented as a SaaS company that supplies sea-freight market intelligence to help container shippers identify lanes where they may be paying above the market average.

## Current Profile
The source defines Xeneta's prospecting problem through a broad customer set united less by industry than by meaningful exposure to container shipping. It reports that companies shipping more than 500 containers per year are likely candidates for savings analysis, then describes an experimental machine-learning pipeline that ranks prospects from their company descriptions before human qualification.

## Key Characteristics
- Provides comparative sea-freight market intelligence.
- Targets organizations with substantial container-shipping activity across otherwise diverse industries.
- Uses company descriptions as imperfect proxy evidence of shipping relevance.
- Tested automated lead ranking as decision support for its sales team.
- Built the experiment from historical customers and manually disqualified companies.

## Evidence
- Product and customer profile: [[per-harald-borgen-boosting-sales-with-machine-learning]] describes price comparison for container shippers and names annual shipment volume as a prospect signal.
- Cross-industry market: [[per-harald-borgen-boosting-sales-with-machine-learning]] lists automotive, freight forwarding, chemicals, consumer and retail, and low-paying commodities as target categories.
- Qualification workflow: [[per-harald-borgen-boosting-sales-with-machine-learning]] explains the use of company descriptions to sort prospects before sales review.
- Training labels: [[per-harald-borgen-boosting-sales-with-machine-learning]] says 1,000 Xeneta users supplied the positive examples while a representative manually rejected 1,000 negative examples.

## Qualifications
This profile is limited to a first-person 2016 engineering and sales experiment. The source does not establish Xeneta's current product, customer threshold, data sources, organizational practices, or later model performance, and it supplies no measured effect on sales productivity or revenue.

## What Changed
- Created a source-bounded profile of Xeneta's product, target-customer logic, and experimental lead-ranking workflow.

## Relationships
- [[PerHaraldBorgen]] - author who describes building the lead-qualification experiment at Xeneta.
- [[TextClassification]] - technique used to score descriptions as qualified or disqualified prospects.
- [[NaturalLanguageProcessing]] - processing layer used to convert company prose into model features.
- [[BagOfWordsModel]] - count-vector representation used in the experiment.
- [[TFIDFRanking]] - weighting method applied to the count vectors before classification.

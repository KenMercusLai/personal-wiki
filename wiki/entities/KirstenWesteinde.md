---
title: "Kirsten Westeinde"
type: entity
tags: [software-engineer, software-architecture, shopify]
sources:
  - deconstructing-the-monolith-shopify-engineering
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[KirstenWesteinde]] is the Shopify engineer who authored the 2019 account of turning Shopify's large Ruby on Rails application into a [[ModularMonolith]].

## Current Profile
In the source, Westeinde presents architecture as an evolving response to observed constraints rather than a fashionable end state. Her account connects developer surveys, business-domain code organization, dependency measurement, and eventual enforcement into a practical componentization path that preserves one codebase and deployment unit.

## Key Characteristics
- Author of Shopify's 2019 modular-monolith case study.
- Frames architecture choice as dependent on application and team scale.
- Advocates learning domain boundaries before paying microservice costs.
- Documents both organizational discovery and technical enforcement work.

## Evidence
- Authorship: [[deconstructing-the-monolith-shopify-engineering]] is Westeinde's Shopify Engineering article published on 2019-02-21.
- Architecture stance: [[deconstructing-the-monolith-shopify-engineering]] argues that monoliths, modular monoliths, and service-oriented architectures suit different scales and phases.
- Implementation account: [[deconstructing-the-monolith-shopify-engineering]] describes Shopify's survey, roughly 6,000-class mapping, automated move, Wedge analysis, and proposed runtime enforcement.

## Qualifications
The source establishes Westeinde's authorship and the claims in this article, but it is not a comprehensive biography or a later retrospective on how Shopify's architecture evolved after 2019.

## What Changed
- Established Westeinde's boundary-first, stage-sensitive architecture perspective from the Shopify case study.

## Relationships
- [[Shopify]] - employer and system context documented in her article.
- [[ModularMonolith]] - architecture she explains and advocates for Shopify's scale at the time.
- [[Wedge]] - internal measurement tool described in her implementation account.
- [[MicroserviceOperationalOverhead]] - cost category informing Shopify's decision not to split immediately into services.

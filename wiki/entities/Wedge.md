---
title: "Wedge"
type: entity
tags: [developer-tooling, software-architecture, shopify]
sources:
  - deconstructing-the-monolith-shopify-engineering
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Wedge]] is Shopify's internal tool for measuring how closely components in its Ruby on Rails [[ModularMonolith]] adhere to declared domain boundaries.

## Current Profile
Wedge turns component isolation into observable engineering work. CI instrumentation uses Ruby tracepoints to build a call graph, groups callers and callees by component, and sends cross-component calls plus code-analysis data about ActiveRecord associations and inheritance to Wedge. The tool classifies violations, calculates component scores, and exposes the results in a dashboard so teams can track progress rather than treating modularity as an undocumented intention.

## Key Characteristics
- Analyzes cross-component runtime calls collected in CI.
- Adds static information about associations and inheritance.
- Treats cross-component associations as violations.
- Allows calls only through explicitly public component interfaces.
- Produces isolation scores and component-level violation lists.
- Displays public calls, internal associations, and public-interface status by component.

## Evidence
- Call graph: [[deconstructing-the-monolith-shopify-engineering]] says Shopify hooked Ruby tracepoints during CI and grouped cross-component callers and callees.
- Rule model: [[deconstructing-the-monolith-shopify-engineering]] says associations across components violated the model, while calls were allowed only to explicit public APIs.
- Dashboard: [[deconstructing-the-monolith-shopify-engineering]] includes an inspected Wedge screen ranking components by progress and showing percentages for public calls and internal associations.
- Roadmap: [[deconstructing-the-monolith-shopify-engineering]] says score trends, meaningful diffs, and fuller inheritance handling were future work.

## Qualifications
The article describes Wedge as a beta-era internal progress tracker in February 2019. It does not establish later production behavior, false-positive rates, developer adoption, or whether planned trend and enforcement features shipped. Measurement highlighted violations; separate runtime or test enforcement was still being researched.

## What Changed
- Established Wedge as a measurement layer for incremental component isolation rather than the enforcement mechanism itself.

## Relationships
- [[Shopify]] - organization and Rails codebase in which Wedge operated.
- [[KirstenWesteinde]] - author documenting the tool and componentization program.
- [[ModularMonolith]] - architecture whose internal boundaries Wedge measured.
- [[CDComponentization]] - Wedge makes component coupling visible during delivery work.
- [[BoundedContext]] - domain boundaries provide the conceptual units whose crossings Wedge analyzes.

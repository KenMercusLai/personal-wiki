---
title: "Go.CD"
type: entity
tags: [ci-cd, continuous-delivery, developer-tools]
sources:
  - architecting-for-continuous-delivery-thoughtworks
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[GoCD]] is described in the Thoughtworks source as an on-premise continuous-delivery tool for complex pipeline dependencies, useful for large teams and enterprises.

## Current Profile
The article uses Go.CD's value-stream map as the complex deployment-pipeline example. The surrounding text says it displays commit state, application dependencies, packaging needs, and production confidence across a dependency-aware release flow.

## Key Characteristics
- On-premise CI/CD product associated with Thoughtworks in the source.
- Supports complex pipeline dependencies.
- Provides value-stream visualization for commits and dependent components.
- Serves as the article's enterprise-oriented pipeline example.

## Evidence
- Product role: [[architecting-for-continuous-delivery-thoughtworks]] says Go.CD is an on-premise tool for complex pipeline dependencies.
- Value-stream map: [[architecting-for-continuous-delivery-thoughtworks]] says the Go.CD example displays dependencies involved in a deployment workflow down to production.
- Delivery confidence: [[architecting-for-continuous-delivery-thoughtworks]] says the visualization indicates whether the application is releasable at a point in time.

## Qualifications
The source is a 2016 article and should not be read as a current product-positioning statement without newer sources.

## What Changed
- Created the entity from the Thoughtworks article.

## Relationships
- [[Thoughtworks]] - company associated with Go.CD in the source.
- [[DeploymentPipeline]] - Go.CD is used to illustrate dependency-aware pipeline flow.
- [[ContinuousDelivery]] - delivery practice Go.CD supports in the source.
- [[CDComponentization]] - component dependencies can be represented in Go.CD-style value-stream maps.

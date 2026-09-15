---
title: "Apache Camel"
type: entity
tags: [integration, messaging, software-architecture]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[ApacheCamel]] appears in the wiki as an integration and transformation tool for connecting a microservice bounded context to backend or legacy systems.

## Current Profile
Posta names Apache Camel in the flight-booking example, where the Ticketing bounded context consumes a `NewBookingCreated` event and interacts with backend ticketing systems. Camel's role in the source is not to define the domain model, but to help implement integration and data transformation after the boundary and event flow have been chosen.

## Key Characteristics
- Supports integration and data transformation in the source's microservice example.
- Is associated with the Ticketing bounded context consuming booking events.
- Is positioned as implementation support after boundary design.

## Evidence
- Integration role: [[christian-posta-the-hardest-part-about-microservices-your-data]] says Apache Camel would be useful for integration and data transformation with backend ticketing systems.
- Event context: [[christian-posta-the-hardest-part-about-microservices-your-data]] places Camel after Booking publishes a `NewBookingCreated` event and Ticketing consumes it.

## Qualifications
The source does not compare Camel with other integration frameworks or describe Camel patterns in detail.

## What Changed
- Created the entity page for Apache Camel from Posta's ticketing integration example.

## Relationships
- [[EventDrivenConsistency]] - Camel appears downstream of an event consumed across a bounded context.
- [[MicroserviceDataBoundaries]] - integration tooling supports but does not replace boundary design.
- [[AntiCorruptionLayer]] - integration and transformation often protect model boundaries.

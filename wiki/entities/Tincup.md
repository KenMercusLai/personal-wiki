---
title: "Tincup"
type: entity
tags: [software-service, currency, microservices]
sources:
  - emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[Tincup]] was [[Uber]]'s currency and exchange-rate microservice, used in a 2016 engineering account as a small production case for learning and applying a new service stack.

## Current Profile
Tincup exposed endpoints for retrieving a currency object and the current exchange rate per US dollar, supporting transactions in nearly sixty currencies. Its business logic was placed in an MVCS service layer, while its data moved from a PostgreSQL database with incremental IDs to Uber's globally replicated UDR datastore for multi-data-center availability. The service also used Tornado, TChannel over Hyperbahn, Thrift, Hailstorm, uContainer, and uDestroy for non-blocking execution, routing, contracts, load testing, isolation, and resilience testing.

## Key Characteristics
- Served current currency and exchange-rate data for a global transaction platform.
- Kept application logic separate from persistence-specific code through an MVCS service layer.
- Used globally replicated storage to fit Uber's all-active data-center architecture.
- Served as a small, simple domain on which engineers could learn a broader microservice stack.
- Passed through load, isolation, and controlled-failure preparation before production use.

## Evidence
- Service role: [[emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering]] says Tincup returned currency objects and current per-USD exchange rates for nearly sixty currencies.
- Data design: [[emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering]] describes the MVCS separation and replacement of PostgreSQL with UDR.
- Runtime and interface: [[emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering]] names Tornado, TChannel over Hyperbahn, and Thrift as the execution, routing, and contract layers.
- Production readiness: [[emily-reinhold-the-opportunities-microservices-provide-at-uber-engineering]] describes Hailstorm load testing, uContainer isolation, and uDestroy disruption tests.

## Qualifications
The source is a 2016 first-party overview rather than a service specification or outcome study. It does not report Tincup's traffic, latency, availability, incident history, data-consistency semantics, rollout results, or later lifecycle, and its descriptions of internal systems are necessarily abbreviated.

## What Changed
- Created Tincup's profile as Uber's currency and exchange-rate service.

## Relationships
- [[Uber]] - owner and operator of Tincup.
- [[EmilyReinhold]] - author of the implementation account.
- [[MicroservicePlatformEngineering]] - shared platform and process used to build and operate Tincup.
- [[MicroserviceDataBoundaries]] - Tincup separated business logic from persistence and moved its data boundary to a replicated store.
- [[ChaosEngineering]] - uDestroy tested Tincup and related services through controlled disruption.

---
title: "Sean Kelly"
type: entity
tags: [software-engineering, software-architecture, microservices]
sources:
  - sean-kelly-microservices-please-dont
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[SeanKelly]] is a software engineer and writer represented in the wiki through a cautionary 2016 analysis of premature microservice adoption.

## Current Profile
Kelly draws on experience at a company that attempted to decompose a legacy monolith. His position is conditional rather than anti-microservice: improve domain boundaries inside the code first, understand distributed workflows and their failures, and extract services only when organizational readiness and demonstrable value justify the additional topology.

## Key Characteristics
- Separates code modularity from network and deployment boundaries.
- Treats distributed transactions, testing, and recovery as architecture costs that require explicit design.
- Connects system topology to team coordination, shared ownership, and business value.

## Evidence
- Architecture position: [[sean-kelly-microservices-please-dont]] recommends internal service modules before independently deployed services.
- Operational position: [[sean-kelly-microservices-please-dont]] identifies network failure, local setup, integration testing, and monitoring as costs of distribution.
- Organizational position: [[sean-kelly-microservices-please-dont]] warns that isolated service teams can increase coordination delay and fragmented responsibility.

## Qualifications
The wiki currently has one 2016 practitioner article by Kelly. It does not provide comparative measurements or establish how his recommendations generalize across system scale, regulatory needs, fault-containment requirements, or organizational structures.

## What Changed
- Created the profile from Kelly's qualified critique of premature microservice adoption.

## Relationships
- [[ModularMonolith]] - Kelly recommends explicit internal service boundaries as a precursor or alternative to networked services.
- [[DistributedSystemRestraint]] - his readiness test delays distribution until its costs and value are understood.
- [[MicroserviceOperationalOverhead]] - his article supplies network, testing, development, and coordination examples of that overhead.

---
title: "Domain Model Driven Data"
type: concept
tags: [domain-driven-design, data-modeling, software-architecture]
sources:
  - christian-posta-the-hardest-part-about-microservices-your-data
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[DomainModelDrivenData]] is the principle that physical data-store models should be derived from explicit domain models and boundaries rather than letting database shape define business meaning.

## Current Synthesis
Posta distinguishes the domain model from the data model to avoid a common microservice mistake: splitting or sharing tables before deciding what the data means in the business context. In his framing, the domain model defines which assertions are correct within a boundary, and only then should teams choose the physical representation in MySQL, Elasticsearch, or another store.

This is a corrective to both shared-database convenience and service-count ideology. The first inspected diagram shows services with different stores, but the article's point is not store diversity for its own sake. Store choice follows the bounded model and the autonomy needed by the team that owns that model.

## Key Claims
- Physical data models should follow explicit domain models.
- Database structure alone cannot resolve ambiguous business meaning.
- A boundary lets teams assert what is correct inside one model.
- Different bounded contexts may validly store different representations of similar terms.
- Store choice should support a service's model and autonomy rather than drive the model.

## Evidence
- Model direction: [[christian-posta-the-hardest-part-about-microservices-your-data]] says the data model is driven by the domain model, not the other way around.
- Ambiguity example: [[christian-posta-the-hardest-part-about-microservices-your-data]] uses "book" to show why business meaning must precede storage design.
- Boundary correctness: [[christian-posta-the-hardest-part-about-microservices-your-data]] says boundaries let teams make assertions about what is correct or incorrect in their model.
- Diagram evidence: [[christian-posta-the-hardest-part-about-microservices-your-data]] shows service areas using MySQL and Elasticsearch stores according to their roles.

## Counterevidence & Qualifications
The source does not deny that operational database constraints matter. Its claim is ordering and authority: domain meaning should guide storage design, while storage technology and consistency properties still shape implementation tradeoffs.

## What Changed
- Created the concept from Posta's distinction between domain model and data model.

## Related Concepts
- [[BoundedContext]] - domain model driven data depends on explicit context boundaries.
- [[MicroserviceDataBoundaries]] - data ownership begins with model boundaries.
- [[AggregateTransactionBoundary]] - aggregate invariants refine which data must change atomically.
- [[DatabaseTransactionIsolation]] - database semantics implement some but not all domain invariants.

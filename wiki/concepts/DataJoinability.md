---
title: "Data Joinability"
type: concept
tags: [data, identifiers, interoperability, data-modeling]
sources:
  - blog-auren-hoffman-safegraph-data-as-a-service-bible
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[DataJoinability]] is the degree to which records from separate datasets can be reliably connected through shared identifiers, compatible keys, time, geography, or other resolvable dimensions.

## Current Synthesis
The source treats joinability as a primary driver of data value because isolated facts answer fewer questions than connected datasets. A data provider should organize its catalog around a coherent theme—such as people, products, places, companies, or procedures—and expose keys that customers can retain and map to other systems. Its SIMPLE test asks whether an identifier is storable, immutable, meticulous, portable, low-cost, and established. Those criteria express interoperability goals, not guarantees: real entities merge, split, move, change names, have incomplete coverage, and can be falsely matched, while person-level linkage can create serious privacy and security risk.

## Key Claims
- Joining datasets increases the range of questions they can answer and can make their combined value exceed their isolated value.
- A coherent entity theme provides a primary-key spine across otherwise disparate attributes.
- Time and geography are broadly reusable join dimensions, especially for temporal or place-based analysis.
- SIMPLE identifiers aim for offline storage, stability, high precision, portability, low transaction cost, and high coverage.
- Providers create ecosystem value when they make keys usable with complementary datasets rather than forcing customers into closed silos.
- Entity resolution quality must be measured because false joins and missed joins propagate into downstream analysis and prediction.

## Evidence
- Combination value: [[blog-auren-hoffman-safegraph-data-as-a-service-bible]] uses weather, operations, geography, and stock-price data to show how multiple keys enable cross-dataset questions.
- Theme model: [[blog-auren-hoffman-safegraph-data-as-a-service-bible]] groups common data businesses around people, products, places, companies, and procedures.
- Identifier criteria: [[blog-auren-hoffman-safegraph-data-as-a-service-bible]] defines the six SIMPLE properties and uses Social Security numbers as its main illustrative key.
- Open complements: [[blog-auren-hoffman-safegraph-data-as-a-service-bible]] argues that cheap or free keys and complementary public data can raise the value of a provider's own dataset.
- Resolution risk: [[blog-auren-hoffman-safegraph-data-as-a-service-bible]] asks how providers assign observations to the right entity and measure the downstream effect of accuracy.

## Counterevidence & Qualifications
Joinability can increase misuse as well as usefulness. Stable cross-context identifiers enable surveillance, reidentification, unauthorized enrichment, and breaches, especially for people data. Immutability may conflict with correction, identity change, deletion rights, or legitimate separation of contexts. Time, location, and entity definitions also differ in granularity and semantics, so syntactically compatible keys do not prove causal or conceptual compatibility. The source's claim that question value grows exponentially is directional rhetoric rather than a measured law.

## What Changed
- Established joinability and the SIMPLE identifier test as a bounded interoperability framework with privacy and semantic qualifications.

## Related Concepts
- [[DataAsAService]] - uses joinable keys to make external data more useful to customers.
- [[IdentityResolution]] - performs probabilistic or deterministic linkage across person-level identifiers.
- [[DomainModelDrivenData]] - supplies semantic boundaries that keys alone cannot guarantee.
- [[LocationDataPrivacy]] - constrains linkage through geographic and mobility signals.
- [[OrganizationalDataSharing]] - governs how data moves across institutional boundaries after it becomes linkable.

---
title: "Privacy-Preserving Product Measurement"
type: concept
tags: [privacy, product-management, analytics, security]
sources:
  - dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[PrivacyPreservingProductMeasurement]] is the practice of learning how a product is used while deliberately limiting the collection of behavioral or identifying data, even when that reduces analytical precision.

## Current Synthesis
The 1Password case makes the tradeoff explicit. AgileBits' security posture discouraged broad user data collection, but the same choice prevented the company from answering a basic segment question about desktop-free iOS use. Support conversations and sales totals supplied partial signals, while the remaining estimate depended on informed judgment. Privacy and measurement are therefore not independent goals: minimizing collection can protect trust and reduce exposure, but product teams still need bounded evidence channels whose limits are named rather than disguised as precise telemetry.

## Key Claims
- Data minimization can be a product and company principle, not only a compliance control.
- Collecting less behavioral data reduces the ability to measure segment size and feature usage precisely.
- Support cases, sales, and direct conversations can supply useful but incomplete alternatives to pervasive telemetry.
- Teams should distinguish measured facts from informed estimates when privacy limits the available evidence.
- Resource allocation under data minimization requires explicit uncertainty rather than invented precision.

## Evidence
- Privacy principle: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] quotes Teare describing AgileBits as a security company that did not want to mine user data.
- Measurement cost: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] says the company could not answer what share of iOS users had no desktop and found investment choices harder as a result.
- Alternative signals: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] uses recurring support contacts, observable sales, and Teare's approximate judgment to characterize the segment.
- Epistemic boundary: [[dave-teare-at-wwdc-how-one-month-for-1password-became-8-years-the-mac-observer]] presents the roughly 10% desktop-free figure as a guess while identifying the near-50/50 platform sales split as something the company could track.

## Counterevidence & Qualifications
One 2013 company interview does not establish the optimal analytics design for security products or show that all relevant measurement would have required invasive collection. Aggregation, opt-in research, privacy-preserving computation, local processing, short retention, or deliberately sampled telemetry may create other tradeoffs, but this source does not evaluate them. Support contacts also overrepresent users with problems, and sales do not reveal active use or cross-platform overlap.

## What Changed
- Created the concept from a concrete case where a security company's data-minimization principle constrained segment measurement and resource planning.

## Related Concepts
- [[CustomerLedProductDevelopment]] - direct conversations and support cases can provide bounded evidence when telemetry is limited.
- [[ProductUserSegmentation]] - segment design depends on knowing which groups exist and how their needs differ.
- [[DataInformedCulture]] - data-informed judgment should expose the limits of available measurement.
- [[PrivacyPovertyDivide]] - privacy choices and protections are unevenly available across products and users.
- [[LocationDataPrivacy]] - another domain where collection scope and utility must be balanced explicitly.

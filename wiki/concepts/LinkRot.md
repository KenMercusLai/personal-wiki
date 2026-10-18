---
title: "Link Rot"
type: concept
tags: [web, preservation, urls, reliability]
sources:
  - chinese-blogs-link-rot-2022
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Definition
[[LinkRot]] is the loss of retrievability or intended meaning at a previously usable URL because its site, domain, route, certificate, hosting, content, or redirect chain no longer provides the referenced resource.

## Current Synthesis
Link rot occurs at more than one level. A whole blog can disappear through domain, DNS, hosting, or operational failure, while an otherwise surviving blog can break individual article URLs during permalink or platform migration. In the source's Chinese independent-blog samples, the author calculates 8.41% annual site loss over a 17-month window and later reports 10–12% annual article-link loss from 196 URLs. These estimates are useful indicators, not general web constants: the samples, units, classifications, and follow-up periods differ, and the calculations assume stable exponential decay.

Hosting changes the distribution of risk rather than eliminating it. Managed static hosting may lower each publisher's maintenance burden and make durable files easier to retain, while also creating correlated dependence on a few providers. Curated, established blogs appear more durable in the supplied comparison, but its “abnormal” category includes non-closure cases, so the calculated rate is only an upper bound. Preservation copies protect content availability but do not by themselves preserve the original URL, ownership, identity, or redirect continuity.

## Key Claims
- Site disappearance and article-URL failure are distinct measurements and should not be collapsed into one rate.
- Permalink changes without redirects can create link rot even when the publisher and content continue to exist.
- Annualized loss and half-life figures depend on a stable-hazard assumption that may not hold as platforms and publishing practices change.
- Established, quality-screened blogs may persist longer, although cohort selection and failure definitions can explain part of the difference.
- Managed static hosting trades lower individual operating risk for shared provider dependence and possible correlated failure.
- Archival copies preserve content access but do not necessarily preserve the original live link or site identity.

## Evidence
- Site-level decay: [[chinese-blogs-link-rot-2022]] reports 113 missing blogs among 965 observed over 17 months and calculates an 8.41% annual site-loss rate.
- Article-level decay: [[chinese-blogs-link-rot-2022]] reports 13 HTTP 404s plus 12 domain, hosting, or TLS failures among 196 article URLs, then gives a 10–12% annual estimate.
- Migration failure: [[chinese-blogs-link-rot-2022]] attributes roughly half of the 404 responses to permalink changes made without redirects.
- Cohort difference: [[chinese-blogs-link-rot-2022]] calculates roughly 3.5% annual abnormality for 999 [[ForeverBlog]] entries and says actual disappearance is lower because some flags were content-related.
- Hosting tradeoff: [[chinese-blogs-link-rot-2022]] argues that static Pages services reduce some individual risks but concentrate many blogs behind common providers.

## Counterevidence & Qualifications
The source is one blogger's analysis rather than a reproducible longitudinal study. It does not publish the exact site snapshots, article sampling procedure, test dates, retry policy, confidence intervals, or a complete failure-classification protocol in the supplied text. Temporary DNS, TLS, or network faults can be mistaken for permanent loss, while content reachable through a new URL may be unavailable only at its former address. The site and article samples cover different periods and units, and the source's initial 20–30% article estimate was explicitly subjective before the smaller measured follow-up. Exponential half-life projections should therefore be read as scenario calculations, not forecasts.

## What Changed
- Created the concept with separate site-level and article-level failure models.
- Identified redirect discipline and hosting concentration as mechanisms that shape link survival.
- Bounded the reported rates by their sampling, classification, and stable-hazard assumptions.

## Related Concepts
- [[DigitalContentDurability]] - link continuity is one component of keeping content retrievable and usable over time.
- [[WebCentralization]] - common hosting platforms can turn independent publishers into a correlated dependency set.
- [[OfflineWebDistribution]] - reader-held packages can preserve access after live links fail, though not the original URL.
- [[KnowledgeDurability]] - preserved meaning may outlive a specific address when provenance and usable copies survive.

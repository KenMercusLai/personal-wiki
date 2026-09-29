---
title: "I Understand Google Better than Google"
type: source
tags: [google-flights, technical-seo, javascript, canonicalization]
date: 2018-10-05
source_file: "/mnt/ken_personal_wiki/Articles/I Understand Google Better than Google - Elephate - Medium.md"
---

## Summary
[[BartoszGoralewicz]] argues that [[GoogleFlights]] lost nearly all of its Google Search visibility after its March 2018 relaunch combined client-rendered JavaScript with weak crawl and indexing controls. The worked diagnosis attributes the decline to several interacting [[TechnicalSEO]] failures, especially competing trailing-slash URL variants, inaccessible or unindexed rendered content, redirect chains, and JavaScript blocking. The article is a practitioner case based on third-party visibility tools and spot checks rather than independently reproducible traffic, indexing, or revenue data.

## Key Claims
- Google Flights' March 2018 redesign added a more usable interface and a Flights tab in Google Search, but the article says the site launched with unresolved JavaScript SEO and internal-linking problems.
- SearchMetrics visibility reportedly fell from about 20,000 to 47 over seven months and had previously reached zero, which the author interprets as loss of rankings even for branded queries.
- Sistrix reportedly showed the non-trailing-slash URL gaining visibility while the trailing-slash version lost it, supporting the diagnosis that two URL forms competed for the same content rather than consolidating cleanly.
- The article treats client-side rendering, blocked JavaScript, content absent from the searchable index, and stacked redirects as compounding discoverability failures rather than isolated checklist violations.
- Footer links apparently added for organic visibility were later removed; the author argues that link tactics cannot compensate for broken rendering, URL, redirect, and indexing foundations.
- The title's claim of losing hundreds of thousands of dollars per month is rhetorical and unsupported by disclosed traffic, conversion, booking, or revenue data.

## Key Quotes
> "Google Flights had lost ALL visibility and rankings in Google" - the author's interpretation of the third-party visibility data.

> "both ... are competing for the same content" - on the two trailing-slash URL variants.

## Connections
- [[BartoszGoralewicz]] - Elephate cofounder and technical SEO practitioner making the diagnosis.
- [[GoogleFlights]] - JavaScript-powered travel-search product used as the technical failure case.
- [[Google]] - both operator of the affected product and rule-setting search platform.
- [[TechnicalSEO]] - rendering, crawling, redirects, canonical URL identity, internal links, and indexing form the article's causal model.
- [[SEOConsultantSelection]] - complements Google's consultant guidance by showing the kinds of implementation risks that technical review is meant to surface.

## Contradictions
- Google's own [[do-you-need-an-seo-search-console-help]] guidance treats technical auditing and transparent search-safe implementation as foundational; this source argues that a Google-operated property nevertheless failed on several of those basics.
- The article reports correlation and practitioner diagnosis, not server logs, Search Console evidence, source code, controlled tests, or Google confirmation. A visibility score is not direct organic traffic, bookings, or revenue, and later product behavior cannot be inferred from this October 2018 snapshot.

## Image Notes
All five effective local image references were opened. Three airplane photographs were duplicate decoration and the animated portrait was an author avatar, so they were omitted. The only potentially evidentiary graphic is a 60-by-9-pixel image placed beside the Sistrix comparison; its labels, axes, dates, values, and series cannot be recovered reliably, so it was not retained and provides no independent visual confirmation of the prose.

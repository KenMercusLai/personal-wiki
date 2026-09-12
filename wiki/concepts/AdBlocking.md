---
title: "Ad Blocking"
type: concept
tags: [web, advertising, privacy]
sources:
  - 402-payment-required-david-humphrey-medium
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AdBlocking]] is the use of browser or user-agent mechanisms to prevent advertising and related third-party content from loading or displaying.

## Current Synthesis
The source treats ad blocking less as a settled moral verdict and more as a forcing function. Apple's iOS 9 Safari content-filtering hooks made mobile ad blocking easier, which intensified the conflict between users who resent tracking-heavy advertising and publishers who depend on ad revenue. For Humphrey, the important implication is that blocking ads reveals how little imagination browsers have shown between rendering everything and rendering nothing.

## Key Claims
- Ad blocking changes the rules of web experience by allowing users to create ad-free spaces through software.
- The conflict is intense because web content has become deeply dependent on advertising revenue.
- Advertising imposes costs beyond visual clutter, including tracking, download bloat, security risk, and privacy invasion.
- Blocking ads without better payment alternatives leaves publishers and users in an all-or-nothing access model.
- Browser-mediated payments are proposed as one way to move the debate from implicit ad exchange toward explicit user choice.

## Evidence
- iOS 9 trigger: [[402-payment-required-david-humphrey-medium]] says Apple did not ship an ad blocker but added Safari content-filtering APIs.
- Hidden costs: [[402-payment-required-david-humphrey-medium]] lists ad networks, trackers, analytics, bloated downloads, third-party scripts, security risk, and privacy invasion.
- Public-space analogy: [[402-payment-required-david-humphrey-medium]] compares ad blocking with [[SaoPauloCleanCityLaw]] removing outdoor advertisements.
- Payment alternative: [[402-payment-required-david-humphrey-medium]] proposes [[BrowserPaymentBroker]] and [[HTTP402PaymentRequired]] as a middle path.

## Counterevidence & Qualifications
The source does not deny that advertising funds web content. Its critique is that the current bargain is often implicit and bundled with unwanted technical and privacy costs. The article predates later privacy, browser, and web-payments developments.

## What Changed
- Created the ad-blocking concept page around the article's iOS 9 debate framing.

## Related Concepts
- [[WebAdEconomics]] - ad blocking exposes the implicit economics of ad-funded access.
- [[BrowserPaymentBroker]] - browser-mediated payment is the proposed alternative.
- [[HTTP402PaymentRequired]] - HTTP 402 is the suggested protocol hook.
- [[SaoPauloCleanCityLaw]] - the physical-world analogy for ad-free public space.

---
title: "Ad Blocking"
type: concept
tags: [web, advertising, privacy]
sources:
  - 402-payment-required-david-humphrey-medium
  - your-next-browser-will-pay-you-by-daniel-colin-james
  - video-is-the-new-html-benedict-evans
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[AdBlocking]] is the use of browser or user-agent mechanisms to prevent advertising and related third-party content from loading or displaying.

## Current Synthesis
The sources treat ad blocking less as a settled moral verdict and more as a forcing function. Apple's iOS 9 Safari content-filtering hooks made mobile ad blocking easier, intensifying the conflict between users who resent tracking-heavy advertising and publishers who depend on ad revenue. Humphrey proposes explicit browser payments as a middle path; the Brave source instead proposes default blocking followed by optional, browser-delivered ads whose targeting and attention measurement remain on-device and whose revenue is shared with users and publishers. Evans adds a distribution consequence: when content and ads arrive inside encrypted, proprietary audiovisual streams, filtering becomes harder, and blocking pressure may encourage publishers to leave the open web for platform-controlled formats.

## Key Claims
- Ad blocking changes the rules of web experience by allowing users to create ad-free spaces through software.
- The conflict is intense because web content has become deeply dependent on advertising revenue.
- Advertising imposes costs beyond visual clutter, including tracking, download bloat, security risk, and privacy invasion.
- Blocking ads without better payment alternatives leaves publishers and users in an all-or-nothing access model.
- Browser-mediated payments are proposed as one way to move the debate from implicit ad exchange toward explicit user choice.
- Brave proposes another replacement path: block incumbent ads and trackers by default, then offer opt-in browser-mediated advertising with token rewards.
- Ad resistance can be designed into the delivery container when content and advertising share one proprietary stream.

## Evidence
- iOS 9 trigger: [[402-payment-required-david-humphrey-medium]] says Apple did not ship an ad blocker but added Safari content-filtering APIs.
- Hidden costs: [[402-payment-required-david-humphrey-medium]] lists ad networks, trackers, analytics, bloated downloads, third-party scripts, security risk, and privacy invasion.
- Public-space analogy: [[402-payment-required-david-humphrey-medium]] compares ad blocking with [[SaoPauloCleanCityLaw]] removing outdoor advertisements.
- Payment alternative: [[402-payment-required-david-humphrey-medium]] proposes [[BrowserPaymentBroker]] and [[HTTP402PaymentRequired]] as a middle path.
- Adoption trend: [[your-next-browser-will-pay-you-by-daniel-colin-james]] includes a PageFair chart showing desktop ad-blocking devices rising from 21 million in January 2010 to 236 million in 2016, while mobile devices rise from 145 million in 2015 to 380 million in 2016.
- Brave alternative: [[your-next-browser-will-pay-you-by-daniel-colin-james]] frames default blocking as the first step before an optional local-targeting and BAT-funded replacement.
- Platform-stream response: [[video-is-the-new-html-benedict-evans]] argues that encrypted data from one IP, rendered in a proprietary runtime with an ad inside the audiovisual stream, is difficult for a blocker to separate.

## Counterevidence & Qualifications
None of the sources denies that advertising funds web content. Their critique is that the current bargain is often implicit and bundled with unwanted technical and privacy costs. All predate later privacy, browser, advertising, streaming, and web-payments developments. The PageFair chart is a historical device-count series rather than a current adoption measure, the Brave source is promotional evidence for a proposed replacement, and Evans's claim that mobile blocking would drive publishers from the open web is a 2016 prediction rather than demonstrated outcome evidence.

## What Changed
- Created the ad-blocking concept page around the article's iOS 9 debate framing.
- Added Brave's default-blocking and opt-in attention-advertising proposal, with historical and promotional qualifications.
- Added the proprietary-stream response in which integrated content and ads are harder to filter and can shift distribution away from the open web.

## Related Concepts
- [[WebAdEconomics]] - ad blocking exposes the implicit economics of ad-funded access.
- [[BrowserPaymentBroker]] - browser-mediated payment is the proposed alternative.
- [[HTTP402PaymentRequired]] - HTTP 402 is the suggested protocol hook.
- [[SaoPauloCleanCityLaw]] - the physical-world analogy for ad-free public space.
- [[AttentionBasedAdvertising]] - proposed opt-in advertising layer after default blocking.
- [[Brave]] - browser used to implement the source's block-then-replace strategy.

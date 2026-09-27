---
title: "Ad Blocking"
type: concept
tags: [web, advertising, privacy]
sources:
  - 402-payment-required-david-humphrey-medium
  - your-next-browser-will-pay-you-by-daniel-colin-james
  - video-is-the-new-html-benedict-evans
  - doc-searls-brands-need-to-fire-adtech
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[AdBlocking]] is the use of browser or user-agent mechanisms to prevent advertising and related third-party content from loading or displaying.

## Current Synthesis
The sources treat ad blocking less as a settled moral verdict and more as a forcing function and market signal. Apple's iOS 9 Safari content-filtering hooks made mobile blocking easier, intensifying the conflict between users who reject tracking-heavy delivery and publishers who depend on ad revenue. Searls argues that blocking and tracking protection are legitimate responses to surveillance rather than external attacks on publishers. Humphrey proposes explicit browser payments as a middle path; Brave proposes default blocking followed by optional browser-delivered ads matched locally, while Evans warns that integrated proprietary streams can make filtering harder and encourage movement away from the open web.

## Key Claims
- Ad blocking lets users reject advertising, tracking, and related third-party content at the user-agent boundary.
- The conflict is intense because ad-funded content depends on revenue from delivery users may experience as intrusive, slow, insecure, or privacy-invasive.
- Blocking and tracking protection can be read as legitimate market feedback about the terms of the exchange, not only as threats to publishers.
- Blocking without a replacement leaves publishers and users in an all-or-nothing access model.
- Browser-mediated payments offer one path toward explicit purchase, while Brave proposes opt-in local advertising and shared token revenue.
- User-controlled interest signaling could separate a willingness to receive relevant offers from consent to third-party surveillance.
- Integrated proprietary content-and-ad streams can make technical filtering harder and may shift distribution away from the open web.

## Evidence
- iOS 9 trigger: [[402-payment-required-david-humphrey-medium]] says Apple did not ship an ad blocker but added Safari content-filtering APIs.
- Hidden costs: [[402-payment-required-david-humphrey-medium]] lists ad networks, trackers, analytics, bloated downloads, third-party scripts, security risk, and privacy invasion.
- Public-space analogy: [[402-payment-required-david-humphrey-medium]] compares ad blocking with [[SaoPauloCleanCityLaw]] removing outdoor advertisements.
- Payment alternative: [[402-payment-required-david-humphrey-medium]] proposes [[BrowserPaymentBroker]] and [[HTTP402PaymentRequired]] as a middle path.
- Adoption trend: [[your-next-browser-will-pay-you-by-daniel-colin-james]] includes a PageFair chart showing desktop ad-blocking devices rising from 21 million in January 2010 to 236 million in 2016, while mobile devices rise from 145 million in 2015 to 380 million in 2016.
- Brave alternative: [[your-next-browser-will-pay-you-by-daniel-colin-james]] frames default blocking as the first step before an optional local-targeting and BAT-funded replacement.
- Platform-stream response: [[video-is-the-new-html-benedict-evans]] argues that encrypted data from one IP, rendered in a proprietary runtime with an ad inside the audiovisual stream, is difficult for a blocker to separate.
- Market-response framing: [[doc-searls-brands-need-to-fire-adtech]] treats blocking and tracking protection as user responses to surveillance and repeated ineffective opt-outs.
- Control alternative: [[doc-searls-brands-need-to-fire-adtech]] proposes open user-controlled preference signaling rather than tracker-defined interest profiles.

## Counterevidence & Qualifications
None of the sources denies that advertising funds web content. Their critique is that the bargain is often implicit and bundled with unwanted technical and privacy costs. All predate later privacy, browser, advertising, streaming, and web-payments developments. The PageFair chart is a historical device-count series, the Brave source is promotional evidence for a proposed replacement, Searls's market-response framing does not measure publisher losses or user willingness to pay, and Evans's open-web consequence is a prediction rather than demonstrated outcome evidence.

## What Changed
- Added blocking and tracking protection as market feedback about surveillance and failed opt-out controls.
- Added open, user-controlled interest signaling as a possible alternative to tracker-defined profiles.

## Related Concepts
- [[WebAdEconomics]] - ad blocking exposes the implicit economics of ad-funded access.
- [[BrowserPaymentBroker]] - browser-mediated payment is the proposed alternative.
- [[HTTP402PaymentRequired]] - HTTP 402 is the suggested protocol hook.
- [[SaoPauloCleanCityLaw]] - the physical-world analogy for ad-free public space.
- [[AttentionBasedAdvertising]] - proposed opt-in advertising layer after default blocking.
- [[Brave]] - browser used to implement the source's block-then-replace strategy.
- [[Adtech]] - tracking-heavy delivery is a major target of blocking and protection tools.

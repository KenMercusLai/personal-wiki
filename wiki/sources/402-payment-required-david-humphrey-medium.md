---
title: "402: Payment Required"
type: source
tags: [web, payments, advertising, browsers]
date: 2015-09-29
source_file: /mnt/ken_personal_wiki/Articles/402- Payment Required - David Humphrey - Medium.md
---

## Summary
[[DavidHumphrey]] uses the iOS 9 ad-blocking debate and Sao Paulo's Clean City Law as prompts to ask how the web might fund content without relying so heavily on implicit advertising tradeoffs. The article argues that browsers could do more than render or block pages: they could use the reserved [[HTTP402PaymentRequired]] status and configured payment providers to let users pay for content, rentals, subscriptions, and services through a trusted [[BrowserPaymentBroker]].

## Key Claims
- Ad blocking exposes the web's hidden [[WebAdEconomics]] bargain: users often pay indirectly through tracking, scripts, page weight, privacy loss, and security risk rather than through explicit purchase.
- Sao Paulo's removal of outdoor advertising and Apple's iOS 9 Safari content-filtering APIs are both framed as rule systems that create ad-free public spaces.
- Mobile app stores, in-app payments, Amazon, Netflix, and Google Play show that users can accept small payments when the purchasing surface is easy, understandable, and trusted.
- Browsers are unusually trusted user agents, but they mostly broker rendering, authentication, passwords, and history rather than cross-site content purchases.
- [[HTTP402PaymentRequired]] could let a site return payment metadata so the browser can present provider-backed options such as buying, renting, or subscribing.
- Browser-level payment infrastructure could help the web's long tail by handling payment providers, taxes, regions, currencies, and transaction trust that small publishers cannot easily build alone.

## Key Quotes
> "Friends, I'm here to tell you that we're living in the future" - on reviving HTTP 402 for web payments.

> "the web has the potential to be the largest app store in the world" - on browsers brokering web transactions.

## Connections
- [[DavidHumphrey]] - author of the article.
- [[WebAdEconomics]] - the article's central critique of implicit ad-funded web exchange.
- [[AdBlocking]] - the iOS 9 trigger that makes the revenue question urgent.
- [[BrowserPaymentBroker]] - the article's proposed browser role.
- [[HTTP402PaymentRequired]] - the reserved status code used as the article's protocol hook.
- [[HTTP]] - the protocol family whose status-code semantics make the proposal legible.
- [[Apple]] - Apple created iOS 9 Safari content-filtering hooks and supplies the App Store payment precedent.
- [[AppStore]] - used as evidence that centralized, trusted microtransactions can become normal for users.
- [[Google]] - Google Play is used as another mobile payment precedent.
- [[Netflix]] - used as a subscription example for ad-free access.
- [[Stripe]] - named as one possible browser-configured payment processor.
- [[Mozilla]] - the browser vendor Humphrey especially wants to lead on integrated payments.
- [[SaoPauloCleanCityLaw]] - the physical-world advertising-ban analogy.

## Contradictions
- No direct contradictions with existing wiki content. The source adds a web-payment and advertising-economics layer to the existing HTTP, mobile-platform, and product-distribution material.

---
title: "CS183C Session 11: Patrick Collison, Stripe"
type: source
tags: [startup, stripe, payments, hiring, scaling, management]
date: 2015-11-28
source_file: "/mnt/ken_personal_wiki/Articles/CS183C Session 11- Patrick Collison, Stripe - Blitzscaling- Class Notes and Essays - Medium.md"
---

## Summary
In this CS183C interview, [[PatrickCollison]] traces how he and [[JohnCollison]] turned the difficulty of accepting online payments into [[Stripe]], first testing a private `/dev/payments` prototype among [[YCombinator]] companies and friends. The discussion then moves from founding and market opportunity into slow high-conviction hiring, developer-led product decisions, conservative organization design, API compatibility, and the shift toward written communication and delegated leadership as Stripe grew.

## Key Claims
- Stripe began from a concrete developer problem: building products was becoming easy, but accepting internet payments remained disproportionately difficult.
- A long prior relationship can help co-founders resolve inevitable conflict, although the interview offers correlation and personal experience rather than comparative evidence.
- Early hiring should optimize for known quality before expressed interest; a great early hire also affects the many later people attracted or recruited through them.
- Product-market pull did not remove the need for years of additional infrastructure and product work, including Connect for coordinating marketplace money flows.
- Conventional organization structures reduce avoidable risk, while interviews should approximate the real work instead of copying weak proxies such as GPA or whiteboard algorithms.
- Reliable infrastructure can continue innovating when compatibility layers isolate customers from API changes and deprecations are handled directly.
- Growth makes explicit broadcast communication and durable writing necessary because new employees lack the context of earlier decisions.

## Key Quotes
> "Most technology companies are building cars; Stripe is building roads." — on infrastructure as an enabling layer.

> "You should generally shift from speaking to writing." — on preserving context as the company scales.

## Connections
- [[PatrickCollison]] - interview subject and Stripe co-founder describing the company's origin and operating choices.
- [[JohnCollison]] - co-founder whose long relationship with Patrick preceded Stripe.
- [[Stripe]] - payment infrastructure company at the center of the interview.
- [[YCombinator]] - community that supplied many of Stripe's first 20–30 users.
- [[StartupHiringAtScale]] - the interview explains slow early recruiting, work trials, persistence, and the downstream leverage of each hire.
- [[ScalingCommunication]] - Stripe's growth made formal broadcast communication and persistent writing necessary.
- [[CoFounderFit]] - the Collison brothers are presented as a case where a long shared history supports conflict resolution.
- [[ProductMarketFit]] - initial interest was real but incomplete and required substantial later product and infrastructure work.
- [[APIBackwardCompatibility]] - Stripe used a translation layer and direct migration requests to combine reliability with API evolution.
- [[CEOScalingRole]] - Collison frames the CEO role around strategy, culture, senior management, and optionally one function.

## Contradictions
- The source qualifies simplistic product-market-fit stories: early user interest and word of mouth did not mean the product, partnerships, or operating system were already complete.
- Its preference for conventional organization design coexists with criticism of copied hiring rituals, implying that defaults should reduce risk but still be tested against evidence and real work.

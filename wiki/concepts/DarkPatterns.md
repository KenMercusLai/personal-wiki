---
title: "Dark Patterns"
type: concept
tags: [product-design, consumer-protection, pricing, choice-architecture]
sources:
  - heres-how-turbotax-just-tricked-you-into-paying-to-file-your-taxes-propublica
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[DarkPatterns]] are interface and journey choices that exploit attention, ambiguity, timing, defaults, or friction to steer people toward outcomes they might not choose with clear, symmetric information and controls.

## Current Synthesis
The TurboTax case shows that a dark pattern can be distributed across an acquisition and service journey rather than confined to one misleading button. Commercial search ads repeat “free”; a landing page guarantees free filing; similar names blur a simple-return commercial offer with an income-qualified public program; extensive data entry creates commitment before price disclosure; internal state places the visitor outside the public-program route; and the genuine free path requires different search language or an IRS directory. On an intermediate page, an eligibility control competes with a “Start for Free” control that returns to the commercial funnel.

The useful unit of analysis is therefore the whole decision environment: claims, product taxonomy, ranking, entry points, timing, data already surrendered, visual prominence, exit and switching costs, and whether the less profitable route is realistically discoverable. Harm is especially consequential when the obscured alternative is a negotiated public benefit and the affected users have lower incomes. Still, observed asymmetry does not by itself prove the intent behind every component; prevalence, consumer loss, and causal effects require broader evidence than two reported test journeys.

## Key Claims
- Deceptive steering can emerge from the composition of search, naming, routing, disclosure timing, and control hierarchy even when each screen contains some technically accurate text.
- Reusing “free” across materially different products increases the burden on users to understand which eligibility regime they entered.
- Delaying a disqualifying condition or price until after substantial data entry can exploit commitment and switching friction.
- Discoverability is part of meaningful access: an eligible option that requires special vocabulary, an unlinked URL, or a multi-page directory can be functionally hidden.
- Competing calls to action should be evaluated by destination and visual emphasis, not label alone.
- Public-private programs need oversight of provider journeys, not only contractual eligibility rules.
- Intent, incidence, and total harm remain separate empirical questions from documenting a misleading observed path.

## Evidence
Acquisition and naming:
- [[heres-how-turbotax-just-tricked-you-into-paying-to-file-your-taxes-propublica]] retains commercial search ads and a landing screen repeatedly promising free filing while distinguishing Free Edition from Free File/Freedom Edition.

Delayed price and commitment:
- [[heres-how-turbotax-just-tricked-you-into-paying-to-file-your-taxes-propublica]] records two profiles supplying extensive information before seeing $119.99 and $59.99 upgrade screens.

Routing and discoverability:
- [[heres-how-turbotax-just-tricked-you-into-paying-to-file-your-taxes-propublica]] reports the “NONFFA” state, a FAQ saying the program required the right URL, and successful discovery after searching “TurboTax Freedom.”

Control hierarchy and public-benefit context:
- [[heres-how-turbotax-just-tricked-you-into-paying-to-file-your-taxes-propublica]] shows the eligibility and commercial-start controls together and places them inside the fragmented IRS provider system.

## Counterevidence & Qualifications
The source supplies a detailed journalistic walkthrough and screenshots, not a controlled usability experiment, representative sample, or estimate of aggregate overpayment. Intuit maintained that its commercial edition was genuinely free for simple returns and published eligibility details. Similar product names can arise from legacy programs as well as deliberate confusion, and the article does not expose the decision history behind every label or control. The durable finding is a materially asymmetric observed journey; claims about present interfaces or current law require fresh evidence.

## What Changed
- Created a journey-level model joining acquisition claims, product naming, delayed pricing, hidden routing, and control hierarchy.
- Added discoverability and public-benefit access as dimensions of deceptive design.
- Separated documented asymmetry from proof of intent, prevalence, and aggregate harm.

## Related Concepts
- [[InterfaceCopywriting]] - dark patterns can invert clear-copy principles through ambiguous labels and incomplete outcome disclosure.
- [[FirstMileProductExperience]] - initial orientation can steer newcomers toward or away from the option that best fits them.
- [[ProductFlowFriction]] - delayed disclosure and difficult switching make an unwanted path costly to leave.
- [[Usability]] - a flow may be easy to complete while still undermining informed choice.
- [[UserTrustCapital]] - misleading promises and surprise charges can rapidly consume accumulated goodwill.
- [[SearchPlatformDisintermediation]] - ranked and paid discovery layers can shape which option a user perceives as available.

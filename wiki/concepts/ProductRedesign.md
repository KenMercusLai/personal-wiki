---
title: "Product Redesign"
type: concept
tags: [product-design, ux, product-development]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
  - designing-the-new-uber-app-uber-design-medium
  - unboxing-chrome-hannah-lee-medium
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[ProductRedesign]] is a deliberate reworking of a product's user experience, information architecture, and interface when accumulated design debt or changed context makes incremental visual updates insufficient.

## Current Synthesis
The Crashlytics source presents redesign as a case-building problem before it is a screen-design problem. A platform migration into [[Firebase]] and [[MaterialDesign]] made a visual update necessary, but the designer argued that the deeper issue was accumulated design debt: users could not reach the information they cared about and sometimes did not know existing features were present. The redesign case therefore required user understanding, journey mapping, internal co-design, recurring pain-theme synthesis, stakeholder context, and explicit problem framing before the team committed to changing the dashboard and issue-detail experience.

Uber adds a consumer-product case in which the original simplifying premise stopped scaling. A ride-first flow and product slider became error-prone as offerings, scheduling, pickup decisions, and trip states multiplied. Daily interviews with Framer and Swift prototypes supported an [[OutcomeFirstProductFlow]]: ask for the destination early, then use it to contextualize fares, arrival times, pickup preparation, and driver matching. Together the cases show that redesign is warranted when the product's underlying information sequence or operating assumption no longer fits its complexity, not merely when the interface looks old.

Chrome adds a mature cross-platform system case. The omnibox looked like one control but expanded into thousands of combinations across languages, fonts, colors, density, hardware, accessibility, and interaction. The redesign began by auditing code-level text and icon variants, then reduced the palette, built shared components from a code library, tested touch and visual-balance compromises, and explored stable geometry that worked in light and Incognito contexts. Redesign here is partly consolidation: the visible result becomes simpler because the team first makes hidden variation and debt explicit.

## Key Claims
- Redesign should be grounded in how users currently use the product, not only in a new visual system.
- A required visual refresh can become a strategic opportunity to repair user-experience, implementation, and component-system debt.
- Teams need shared journey maps and problem statements before committing to broad redesign work.
- Internal experts can contribute useful redesign evidence when their context is separated into independent sessions and connected back to customer pain.
- The case for redesign is stronger when stakeholders participate throughout the research process.
- Redesign diagnosis may require inventories of code styles, states, platform variants, and touch geometry as well as journeys and information hierarchy.
- A redesign may replace an interaction premise or consolidate hidden variation when the old simplification causes errors, inconsistency, or avoidable cognitive change.

## Evidence
- Visual trigger: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the need to adopt Firebase's Material Design surface created the opportunity to rethink Crashlytics' whole UX.
- User grounding: [[advocating-for-a-complete-product-redesign-google-design-medium]] describes talking with teammates, developer relations, user researchers, and users before designing.
- Journey alignment: [[advocating-for-a-complete-product-redesign-google-design-medium]] identifies four key Crashlytics journeys and a recurring investigate-and-fix flow.
- Internal co-design: [[advocating-for-a-complete-product-redesign-google-design-medium]] describes paper-cutout sessions where teammates independently rearranged the dashboard.
- Problem framing: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the final pitch centered on unclear information hierarchy.
- Image evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected before/after screenshots showing clearer overview cards, filters, trend charts, issues, device details, session tabs, and stack-trace surfaces in the Firebase redesign.
- Flow premise: [[designing-the-new-uber-app-uber-design-medium]] says Uber replaced a ride-first interaction with destination-first entry after product growth made its slider crowded and contributed to wrong selections.
- Iterative research: [[designing-the-new-uber-app-uber-design-medium]] reports daily interviews using Framer and Swift prototypes before the team settled on contextual product comparisons.
- System scope: [[designing-the-new-uber-app-uber-design-medium]] describes redesigning the rider flow while simultaneously building foundations, components, motion, maps, loading states, and other design-system elements.
- Hidden scope: [[unboxing-chrome-hannah-lee-medium]] reports that one omnibox represented more than 2,000 static and 20,000 interactive permutations.
- Inventory and consolidation: [[unboxing-chrome-hannah-lee-medium]] describes a code audit that reduced 95 greys to eight and classified more than 400 icon variants before shared components were specified.
- Interaction tradeoffs: [[unboxing-chrome-hannah-lee-medium]] shows touch-target size, visual spacing, theme contrast, transition complexity, and brand meaning shaping the final rounded control.
- Before/after evidence: [[unboxing-chrome-hannah-lee-medium]] retains interface comparisons, state diagrams, design explorations, light and Incognito treatments, and the final mobile result.

## Counterevidence & Qualifications
All three sources are first-party team retrospectives and do not provide controlled before/after outcome comparisons. Their strongest evidence is process evidence, repeated qualitative themes, and described or inspected interface artifacts. Internal co-design should not replace direct user research; in the Crashlytics case, it worked alongside users, developer relations, support patterns, and long-tenured product knowledge. Uber reports frequent prototype interviews but not the sample, tasks, alternatives, accessibility findings, or post-launch outcomes, and its captured UI images are too small for independent detail-level interpretation. Chrome reports permutation counts, palette and asset reductions, product-size improvement, and favorable user-study judgments without releasing the underlying inventory, methods, sample, or effect sizes.

## What Changed
- Created the concept page for product redesign as evidence-backed case-building rather than a purely visual refresh.
- Added legacy interaction premises and product-option growth as redesign triggers, with daily prototype research and concurrent design-system work as the response.
- Added code-level inventory and hidden cross-platform permutations as redesign inputs, with consolidation and stable geometry as possible outcomes.

## Related Concepts
- [[InformationHierarchy]] - unclear hierarchy was the central problem the redesign addressed.
- [[UserJourneyMapping]] - journey maps created shared understanding before redesign work.
- [[InternalCoDesign]] - internal dashboard redesign sessions generated pain-point evidence.
- [[InvestigateAndFixFlow]] - repeated user flow shaped the redesigned Crashlytics experience.
- [[CustomerLedProductDevelopment]] - customer and support signals justified changing product direction.
- [[UXResearchInformationDesign]] - research findings had to be organized into a stakeholder-readable case.
- [[OutcomeFirstProductFlow]] - Uber's redesign changed the sequence of interaction so destination context could guide later choices.
- [[DesignOperations]] - broad redesigns may require product surfaces and shared system components to evolve together.
- [[CognitiveOverheadInProductDesign]] - stable geometry and restrained visual change can reduce what users must notice and remember during redesigned flows.

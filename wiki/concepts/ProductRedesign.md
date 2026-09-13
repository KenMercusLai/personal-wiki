---
title: "Product Redesign"
type: concept
tags: [product-design, ux, product-development]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ProductRedesign]] is a deliberate reworking of a product's user experience, information architecture, and interface when accumulated design debt or changed context makes incremental visual updates insufficient.

## Current Synthesis
The Crashlytics source presents redesign as a case-building problem before it is a screen-design problem. A platform migration into [[Firebase]] and [[MaterialDesign]] made a visual update necessary, but the designer argued that the deeper issue was accumulated design debt: users could not reach the information they cared about and sometimes did not know existing features were present. The redesign case therefore required user understanding, journey mapping, internal co-design, recurring pain-theme synthesis, stakeholder context, and explicit problem framing before the team committed to changing the dashboard and issue-detail experience.

## Key Claims
- Redesign should be grounded in how users currently use the product, not only in a new visual system.
- A required visual refresh can become a strategic opportunity to repair deeper user-experience debt.
- Teams need shared journey maps and problem statements before committing to broad redesign work.
- Internal experts can contribute useful redesign evidence when their context is separated into independent sessions and connected back to customer pain.
- The case for redesign is stronger when stakeholders participate throughout the research process.
- Information hierarchy is a common redesign target when users scroll, click, or ask for already-existing features because important material is buried.

## Evidence
- Visual trigger: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the need to adopt Firebase's Material Design surface created the opportunity to rethink Crashlytics' whole UX.
- User grounding: [[advocating-for-a-complete-product-redesign-google-design-medium]] describes talking with teammates, developer relations, user researchers, and users before designing.
- Journey alignment: [[advocating-for-a-complete-product-redesign-google-design-medium]] identifies four key Crashlytics journeys and a recurring investigate-and-fix flow.
- Internal co-design: [[advocating-for-a-complete-product-redesign-google-design-medium]] describes paper-cutout sessions where teammates independently rearranged the dashboard.
- Problem framing: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the final pitch centered on unclear information hierarchy.
- Image evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected before/after screenshots showing clearer overview cards, filters, trend charts, issues, device details, session tabs, and stack-trace surfaces in the Firebase redesign.

## Counterevidence & Qualifications
The source is a single team retrospective and does not provide quantitative before/after metrics. Its strongest evidence is process evidence, repeated qualitative pain themes, and inspected interface artifacts. Internal co-design should not replace direct user research; in this case, it worked because the team also drew on users, developer relations, support patterns, and long-tenured product knowledge.

## What Changed
- Created the concept page for product redesign as evidence-backed case-building rather than a purely visual refresh.

## Related Concepts
- [[InformationHierarchy]] - unclear hierarchy was the central problem the redesign addressed.
- [[UserJourneyMapping]] - journey maps created shared understanding before redesign work.
- [[InternalCoDesign]] - internal dashboard redesign sessions generated pain-point evidence.
- [[InvestigateAndFixFlow]] - repeated user flow shaped the redesigned Crashlytics experience.
- [[CustomerLedProductDevelopment]] - customer and support signals justified changing product direction.
- [[UXResearchInformationDesign]] - research findings had to be organized into a stakeholder-readable case.

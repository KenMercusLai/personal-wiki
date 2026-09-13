---
title: "Information Hierarchy"
type: concept
tags: [ux, product-design, information-architecture]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
  - an-8-min-guide-to-app-landing-pages-the-startup-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[InformationHierarchy]] is the ordering and visual prioritization of information so users can find important data, actions, and features at the moment they need them.

## Current Synthesis
The sources treat information hierarchy as both an in-product and pre-product marketing problem. The Crashlytics redesign source shows the in-product version: users were scrolling, clicking through less important UI, and asking for features that already existed because useful data and capabilities were buried. The team also struggled to place new features because the product lacked a clear hierarchy for itself. The redesign's inspected images show the intended repair: critical crash-free statistics, event trends, filters, issue counts, versions, users, device breakdowns, sessions, logs, keys, data, and stack traces are grouped into more legible overview and issue-detail surfaces. The Appster landing-page source adds a simpler marketing rule: a page should answer the visitor's questions in sequence, putting product explanation, benefit, objection handling, CTA, and proof where they reduce effort rather than compete for attention.

## Key Claims
- Poor hierarchy can make existing features effectively invisible.
- Users reveal hierarchy problems through scrolling, repeated clicks, support questions, and requests for already-present functionality.
- Teams also suffer from unclear hierarchy because they do not know where new features belong.
- Redesign work should distinguish important diagnostic information from lower-priority surrounding UI.
- Visual grouping, cards, filters, tables, tabs, and detail panes can make product structure easier to scan when tied to real user journeys.
- Landing pages need an information sequence that explains the offer before asking for action.

## Evidence
- Buried information: [[advocating-for-a-complete-product-redesign-google-design-medium]] says users had to scroll or click multiple times to get to what they cared about.
- Hidden features: [[advocating-for-a-complete-product-redesign-google-design-medium]] reports users asking for a logging feature that already existed but was buried.
- Team confusion: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the team also found it hard to know where to put features.
- Repeated theme: [[advocating-for-a-complete-product-redesign-google-design-medium]] says every internal cutout participant focused on improving filters and information hierarchy.
- Interface evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected before/after screenshots showing overview metrics and issue details reorganized into clearer Firebase surfaces.
- Landing-page sequence: [[an-8-min-guide-to-app-landing-pages-the-startup-medium]] cites a hierarchy that moves from pain point, benefit, unique position, objections, CTA, and proof.
- Headline ambiguity: [[an-8-min-guide-to-app-landing-pages-the-startup-medium]] uses the inspected Zendesk screenshot to argue that vague headline copy can hide the clearer product explanation below it.

## Counterevidence & Qualifications
The sources argue from qualitative evidence, screenshots, and practitioner frameworks rather than instrumented task-completion metrics. Hierarchy solutions remain domain-specific: crash debugging requires surfacing trends, issue priority, affected users, versions, and diagnostic detail, while landing pages prioritize offer comprehension, objections, action, and trust.

## What Changed
- Created the concept page for information hierarchy as the main UX problem in the Crashlytics redesign.
- Added landing-page hierarchy as a marketing-page version of the same ordering problem.

## Related Concepts
- [[ProductRedesign]] - redesign can be justified when hierarchy debt blocks use.
- [[UserJourneyMapping]] - hierarchy decisions should follow the user's actual journey.
- [[InvestigateAndFixFlow]] - Crashlytics hierarchy centered on investigating and fixing crashes.
- [[UXResearchInformationDesign]] - report hierarchy and product hierarchy both turn information into usable structure.
- [[CognitiveLoadInUXResearch]] - poor hierarchy increases the mental work required to interpret an interface.
- [[AppLandingPages]] - landing pages need a visitor-question sequence as well as visual priority.

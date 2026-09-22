---
title: "Information Hierarchy"
type: concept
tags: [ux, product-design, information-architecture]
sources:
  - advocating-for-a-complete-product-redesign-google-design-medium
  - an-8-min-guide-to-app-landing-pages-the-startup-medium
  - are-users-trying-to-make-developers-angry-exception-not-found
  - university-websites-the-so-so-the-bad-and-the-egregious-university-affairs
last_updated: 2026-09-22
knowledge_schema: synthesis-v1
---

## Definition
[[InformationHierarchy]] is the ordering and visual prioritization of information, actions, labels, and cues so users can find important data, understand what is possible, and act at the moment they need to.

## Current Synthesis
The sources treat information hierarchy as an in-product, marketing, everyday usability, and institution-wide governance problem. The Crashlytics redesign source shows the mature-product version: users were scrolling, clicking through less important UI, and asking for features that already existed because useful data and capabilities were buried. The team also struggled to place new features because the product lacked a clear hierarchy for itself. The redesign's inspected images show the intended repair: critical crash-free statistics, event trends, filters, issue counts, versions, users, device breakdowns, sessions, logs, keys, data, and stack traces are grouped into more legible overview and issue-detail surfaces. The Appster landing-page source adds a marketing rule: a page should answer the visitor's questions in sequence, putting product explanation, benefit, objection handling, CTA, and proof where they reduce effort rather than compete for attention. The Exception Not Found source adds a support-level version: placement and labels can make users infer that a link leads away from the task or that a combined search field cannot accept city, state, and zip, even when the builder sees those actions as obvious.

The university website source extends the problem beyond one page or application. When navigation mirrors departments, political claims on the homepage, and recruitment priorities, essential tasks can be buried even if each local page appears reasonable. Users seeking fees, dates, maps, contacts, transcripts, or academic support should not need to know which office owns the information. Hierarchy is therefore not only a visual ordering decision; at institutional scale it is an outcome of purpose, governance, content ownership, staffing, and the authority to organize around user tasks.

## Key Claims
- Poor hierarchy can make existing features effectively invisible.
- Users reveal hierarchy problems through scrolling, repeated clicks, support questions, and requests for already-present functionality.
- Teams also suffer from unclear hierarchy because they do not know where new features belong.
- Redesign work should distinguish important information from lower-priority UI and use grouping, filters, tables, tabs, or detail panes only when they clarify real user journeys.
- Landing pages need an information sequence that explains the offer before asking for action.
- Placement and labeling shape what users believe an action or input can do.
- Institution-wide hierarchy fails when it reproduces organizational silos and political priorities instead of user tasks.

## Evidence
- Buried information: [[advocating-for-a-complete-product-redesign-google-design-medium]] says users had to scroll or click multiple times to get to what they cared about.
- Hidden features: [[advocating-for-a-complete-product-redesign-google-design-medium]] reports users asking for a logging feature that already existed but was buried.
- Team confusion: [[advocating-for-a-complete-product-redesign-google-design-medium]] says the team also found it hard to know where to put features.
- Repeated theme: [[advocating-for-a-complete-product-redesign-google-design-medium]] says every internal cutout participant focused on improving filters and information hierarchy.
- Interface evidence: [[advocating-for-a-complete-product-redesign-google-design-medium]] includes inspected before/after screenshots showing overview metrics and issue details reorganized into clearer Firebase surfaces.
- Landing-page sequence: [[an-8-min-guide-to-app-landing-pages-the-startup-medium]] cites a hierarchy that moves from pain point, benefit, unique position, objections, CTA, and proof.
- Headline ambiguity: [[an-8-min-guide-to-app-landing-pages-the-startup-medium]] uses the inspected Zendesk screenshot to argue that vague headline copy can hide the clearer product explanation below it.
- Misread affordances: [[are-users-trying-to-make-developers-angry-exception-not-found]] describes a user avoiding a link because its placement made it look like it would navigate to another tool.
- Missing implied capability: [[are-users-trying-to-make-developers-angry-exception-not-found]] describes a user assuming address search had been removed because separate city, state, and zip fields were absent.
- Institutional hierarchy: [[university-websites-the-so-so-the-bad-and-the-egregious-university-affairs]] says university sites commonly organize information around presumed audience categories and internal structures, requiring users to understand the institution before finding a service.
- Operational consequences: [[university-websites-the-so-so-the-bad-and-the-egregious-university-affairs]] reports essential information buried behind clicks, loops, PDFs, large menus, and weak search, while homepage and navigation space reflect recruitment goals and internal political competition.

## Counterevidence & Qualifications
The sources argue from qualitative evidence, screenshots, support anecdotes, practitioner frameworks, Twitter responses, and reader comments rather than instrumented task-completion metrics. Hierarchy solutions remain domain-specific: crash debugging requires surfacing trends, issue priority, affected users, versions, and diagnostic detail; landing pages prioritize offer comprehension, objections, action, and trust; internal work tools need labels and placement that match users' task expectations; and university sites must reconcile many audiences, regulatory duties, distributed owners, and long-lived content. Task-centered architecture does not by itself resolve insufficient staffing, inaccessible data, or contested institutional priorities.

## What Changed
- Created the concept page for information hierarchy as the main UX problem in the Crashlytics redesign.
- Added landing-page hierarchy as a marketing-page version of the same ordering problem.
- Added support evidence that misleading placement and absent labels can make available actions seem unsafe or unavailable.
- Extended the concept to institution-wide architecture, where governance and organizational structure determine what users can find.

## Related Concepts
- [[ProductRedesign]] - redesign can be justified when hierarchy debt blocks use.
- [[UserJourneyMapping]] - hierarchy decisions should follow the user's actual journey.
- [[InvestigateAndFixFlow]] - Crashlytics hierarchy centered on investigating and fixing crashes.
- [[UXResearchInformationDesign]] - report hierarchy and product hierarchy both turn information into usable structure.
- [[CognitiveLoadInUXResearch]] - poor hierarchy increases the mental work required to interpret an interface.
- [[AppLandingPages]] - landing pages need a visitor-question sequence as well as visual priority.
- [[BuilderUserFluencyGap]] - hierarchy problems can expose a gap between builder obviousness and user inference.
- [[UniversityWebsiteGovernance]] - institutional ownership, staffing, and priorities shape hierarchy across a university web estate.

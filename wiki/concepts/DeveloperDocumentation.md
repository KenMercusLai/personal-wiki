---
title: "Developer Documentation"
type: concept
tags: [documentation, developer-experience, technical-writing]
sources:
  - writing-great-documentation-taylor-singletary-medium
  - eva-parish-what-i-think-about-when-i-edit
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[DeveloperDocumentation]] is the designed system of task guidance, concepts, examples, reference facts, links, and feedback loops that helps developers begin, act, recover, and gain mastery with a technical product.

## Current Synthesis
Taylor Singletary treats developer documentation as both narrative and interface. A guide should identify its audience and purpose, make the reader the actor, and use active language, examples, exercises, and useful inline tools to move from easy entry toward mastery. The collection around that guide should separate reusable atomic topics, link them wherever relevant, provide canonical FAQ answers for smaller questions, and use strong visual hierarchy because readers often skim before returning with a specific problem.

The writing process is inseparable from product learning. Authors should test the thing they explain, outline the intended journey, report ambiguity and limitations back to the product team, and monitor repeated questions or integration failures after publication. Parish sharpens the diagnostic role of prose: rewriting “an alert is triggered and the job is started” in active voice forces the author to identify which service triggers the alert and which component runs the job. Her wider editing method adds imperative instructions, expanded acronyms, concise context, verification and closure, consistent tone, and screen-oriented whitespace. Reference material has a different local form from a tutorial: its job is rapid lookup through plain language, compact grouping, and consistent labels, illustrated by Singletary's nutrition-label analogy.

## Key Claims
- Reader-centered narrative gives task documentation a beginning, progression, and successful outcome.
- Active, actionable instructions and worked practice reduce interpretation cost and support learning by doing.
- Atomic topics, repeated cross-links, and canonical FAQ answers make documentation reusable and discoverable.
- Visual hierarchy and compact reference layouts serve scanning without requiring every reader to follow a linear path.
- Product testing should precede documentation, and writing should expose product ambiguity through a feedback loop.
- Documentation quality depends on maintenance and observation of recurring user problems, not publication alone.
- Explicit actors, defined terms, direct instructions, and completion checks reduce ambiguity while testing whether the author understands the documented system.

## Evidence
- Reader action and mastery: [[writing-great-documentation-taylor-singletary-medium]] recommends making the reader the protagonist, using active voice, and combining easy entry with examples, exercises, tools, and a path to deeper capability.
- Linked knowledge system: [[writing-great-documentation-taylor-singletary-medium]] advocates atomic content, deliberate interlinking, selective repetition, and FAQs as canonical answers for topics too small for full pages.
- Scan and lookup design: [[writing-great-documentation-taylor-singletary-medium]] recommends whitespace, emphasis, callouts, consistent labels, columns, and plain language; its retained nutrition-label image demonstrates dense but glanceable reference structure.
- Product feedback: [[writing-great-documentation-taylor-singletary-medium]] says authors should test before writing and use the resulting experience to reveal limitations and ambiguity.
- Maintenance signal: [[writing-great-documentation-taylor-singletary-medium]] recommends repairing stale content, threading new concepts through older artifacts, and tracking repeated questions or problems.
- Editorial precision: [[eva-parish-what-i-think-about-when-i-edit]] uses direct imperatives, defined acronyms, named system actors, completion verification, tone consistency, and whitespace to reduce reader inference and expose gaps in the author's system model.

## Counterevidence & Qualifications
The sources are practitioner essays, not controlled comparisons of documentation styles or measured support outcomes. Narrative, humor, conspicuous callouts, pseudocode, deliberate repetition, imperatives, and active voice depend on audience, brand, risk, and task: safety-critical or exact integration work may require restrained tone, executable examples, formal reference detail, accessibility testing, or passive constructions that appropriately foreground the affected object. The warning against turnkey abstraction is also conditional; abstraction can reduce error when its behavior, escape hatches, and support boundary remain clear.

## What Changed
- Created a dedicated concept joining reader-centered narrative, actionable instruction, atomic linking, scan design, product feedback, and maintenance.
- Distinguished tutorial progression from compact reference lookup.
- Preserved the source's warning that excessive abstraction can hide platform mechanics and increase support difficulty.
- Added editing as a system-understanding check through explicit agency, terminology, context, verification, and scan-oriented structure.

## Related Concepts
- [[ExplanatoryWriting]] - developer documentation applies audience-centered explanation to technical tasks and products.
- [[DeveloperExperience]] - documentation is a developer-facing interface for onboarding, action, recovery, and mastery.
- [[APIErrorHandling]] - errors can route developers from failure context to relevant documentation and recovery steps.
- [[InformationHierarchy]] - visual structure determines whether important facts are discoverable while scanning.
- [[TechnicalAccessibility]] - lower-friction explanations and examples make technical capability easier to approach.
- [[KnowledgeAsCode]] - versioning and validation can operationalize documentation maintenance at repository scale.
- [[EditingForClarity]] - intent, explicit agency, defined terms, concision, and scan design reduce documentation ambiguity.

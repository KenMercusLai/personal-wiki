---
title: "Notes to Myself on Software Engineering"
type: source
tags: [software-engineering, api-design, career, productivity, ethics]
date: 2018-09-08
source_file: "/mnt/ken_personal_wiki/Articles/Notes to Myself on Software Engineering - Featured Stories - Medium.md"
---

## Summary
[[FrancoisChollet]] presents a compact set of practitioner principles for software development, [[APIDesign]], and technical careers. The recurring standard is holistic impact: readable code, selective features, explicit and automatable processes, reversible experimentation, domain-shaped interfaces, useful documentation, fast but risk-sensitive decisions, teamwork, agency, and deliberate ethical responsibility. The advice is broad and internally coherent, but it is a personal checklist rather than comparative evidence or a complete operating method.

## Key Claims
- Code is both executable behavior and team communication, so readability, naming, factoring, and explanation are part of [[InternalSoftwareQuality]].
- Features carry continuing maintenance, documentation, and user-cognition costs; teams should reject weak requests or satisfy the underlying use case by extending a coherent existing model.
- Continuous integration, broad unit-test coverage, early reversion, explicit rules, documented workflows, and automation create a safer environment for iterative development.
- [[APIDesign]] is user-experience design: common workflows should minimize cognitive load, match domain mental models, use meaningful arguments, provide deliberate feedback, and remain simple without blocking complex cases.
- Documentation belongs to the API and should demonstrate end-to-end use with concrete examples rather than merely explain internal mechanisms.
- Career progress should be judged by impact, teamwork, agency, values, and service to real needs rather than management span, visible contribution, or short-term self-interest.
- Product and technical choices are ethically directional because they shape access, incentives, benefits, harms, and how capabilities are used.

## Key Quotes
> "Code is also a means of communication across a team." - why readability is fundamental rather than decorative.

> "Your API has users, thus it has a user experience." - the article's central API-design frame.

## Connections
- [[FrancoisChollet]] - author of the engineering, API, and career principles.
- [[APIDesign]] - user-centered interface design grounded in workflows, domain models, feedback, naming, and documentation.
- [[SoftwareEngineering]] - connects implementation with product judgment, process design, reversibility, ethics, and user impact.
- [[InternalSoftwareQuality]] - readability, testing, CI, explicit rules, and simplicity protect communication and safe change.
- [[DeveloperExperience]] - developers are the users of APIs, documentation, errors, and workflows.
- [[ReversibleDecisionMaking]] - early experimentation is safer when incorrect choices can be identified and reverted.
- [[DecisionQuality]] - decision speed should vary with uncertainty and the cost of error.

## Contradictions
- The call for full unit-test coverage is stronger than the wiki's risk-sensitive [[SoftwareVerification]] synthesis, which treats test mix and depth as dependent on architecture, failure cost, observability, and the value of each check.
- The source favors simplicity and low cognitive load but does not define how to measure either, and defaults or abstraction can conceal consequential choices, expert controls, accessibility needs, or failure modes.
- The career and ethics principles are reflective practitioner advice; they do not show that impact, agency, fast decisions, or values-led choices reliably produce career satisfaction or better organizational outcomes across different power and resource conditions.

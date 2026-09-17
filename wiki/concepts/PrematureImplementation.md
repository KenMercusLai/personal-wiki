---
title: "Premature Implementation"
type: concept
tags: [software-engineering, problem-solving, project-management]
sources:
  - understand-design-build-a-framework-for-problem-solving-lob-blog
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[PrematureImplementation]] is the failure mode of starting to build before the business problem, its blocker, and the existing technical landscape are understood, which produces frequent information interrupts and solutions that do not solve the intended problem.

## Current Synthesis
The Lob source treats premature implementation as the main explanation for software projects that fail or take two to ten times longer than they should. Two costs appear together. The team must repeatedly stop work to ask others for information it should already have, and the eventual deliverable turns out not to solve the problem, so the code is discarded. The source's remedy is an understanding step that answers what business outcome is wanted, what prevents it today, and what already exists in the codebase or infrastructure that helps or hinders change, plus writing design docs and holding kickoffs so that context is cached locally instead of retrieved repeatedly. The failure is therefore not laziness or slowness; it is work spent on the wrong question, paid for in interrupts by the implementer and in rework by the project.

Within the wiki, this is the negative image of [[UnderstandDesignBuild]] and the delivery-side relative of [[ProblemPersistence]]: both hold that the problem, not the current artifact, is what should stay fixed. It is also distinct from the wiki's productive build-early material, where a small build is deliberately framed as the cheapest way to answer a named question.

## Key Claims
- The cost of skipping understanding appears both as interrupts and as a deliverable that misses the problem.
- Interrupts are expensive because they change context for more than the person asking.
- Teams that implement before understanding finish work that does not solve the problem and then throw it away.
- Unfamiliarity with existing code, infrastructure, and prior solutions also destroys estimation accuracy.
- Caching problem context locally - through design docs, kickoffs, and shared understanding - is the preventive mechanism.

## Evidence
- Failure and overrun: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says projects fail or take 2x to 10x too long when the implementer built something that did not solve the problem or did not function well.
- Interrupt cost: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says implementers without a solid understanding must frequently stop to ask others for information and that interrupts introduce context changes, usually for more than one individual.
- Wrong-solution builds: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] names building something that does not solve the problem as the second consequence of starting implementation without understanding.
- Estimation damage: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says estimates will be orders of magnitude off without familiarity with what already exists.
- Prevention through cached context: [[understand-design-build-a-framework-for-problem-solving-lob-blog]] says design docs and kickoffs try to jam as much understanding of the business problem as possible into everyone involved.

## Counterevidence & Qualifications
The failure mechanism is a practitioner's explanation, not a measured comparison of projects with and without an understanding phase. Deliberately building before full understanding can be rational when the build is the cheapest way to learn, as the wiki's [[MinimumViableProduct]] and [[StartupHypothesisTesting]] material argues; the difference is whether the build is framed as a test with a stated question rather than as delivery of the answer. The source also does not separate interrupts caused by missing business context from interrupts caused by legitimate collaboration, review, or changing requirements, and its claim that premature implementation is "almost always" the cause overstates a diagnostic that other wiki sources attribute to different mechanisms, including unclear ownership and design that is recognized as unfinished only late.

## What Changed
- Created the concept from Lob's 2019 engineering-blog post.

## Related Concepts
- [[UnderstandDesignBuild]] - the framework whose first step prevents this failure.
- [[AttentionManagement]] - interrupt cost is the attention-side half of the failure.
- [[ProblemPersistence]] - both keep the problem, not the artifact, as the fixed point.
- [[MinimumViableProduct]] - qualification: a deliberately scoped build can be the fastest way to understand a problem.
- [[StartupHypothesisTesting]] - framing build work as a test is what separates useful early building from premature implementation.
- [[ContinuousDelivery]] - short feedback loops are the alternative route to the understanding this failure mode lacks.

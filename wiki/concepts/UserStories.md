---
title: "User Stories"
type: concept
tags: [agile, requirements, product-management]
sources:
  - blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas
  - estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[UserStories]] are concise agile requirement descriptions that identify who needs a product capability, what action or activity they want to perform, and why that action is valuable.

## Current Synthesis
The PBB source treats user stories as lightweight containers for shared understanding rather than miniature specifications. Their basic 3Ws form asks who, what, and why; their common wording is "As a role, I want an action, so that a benefit follows." That compactness is deliberate because the written card is supposed to invite conversation and later confirmation, not replace team discovery.

Story quality comes from several complementary checks. INVEST asks whether a story is independent, negotiable, valuable, estimable, sized appropriately, and testable. The 3Cs model separates the card, the conversation that gives it meaning, and the confirmation supplied by acceptance criteria. Product Backlog Building then gives teams a way to generate stories collaboratively by grounding them in personas, features, and PBIs.

A complementary architectural slicing test asks whether a story follows one logical user interaction through the technical layers needed to produce a visible outcome, rather than completing one layer across a broad feature. A “blogs” feature can be narrowed to displaying one user's posts, turning Model, View, and Template work into a deliverable path with acceptance criteria and an estimate.

## Key Claims
- User stories are grounded in the 3Ws: who, what, and why.
- A good story is a conversational artifact, not a fixed contract or complete requirements document.
- INVEST and the 3Cs model provide practical quality checks for story usefulness.
- Acceptance criteria confirm whether the story goal has been met.
- Tasks, UI notes, exploratory enablers, and technical enablers can support a story without pretending every work item has user-facing value.
- Collaborative story writing keeps backlog creation from becoming a Product Owner bottleneck.
- Vertical slicing follows one user-visible interaction through necessary technical layers instead of completing a broad horizontal layer in isolation.

## Evidence
- 3Ws structure: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] defines a user story around who it is for, what action is needed, and why the person will use it.
- Conversational artifact: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says stories should be brief enough to fit on a card and require ongoing conversation.
- INVEST checks: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] lists independent, negotiable, valuable, estimable, sized appropriately, and testable characteristics.
- Confirmation: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says acceptance criteria define how to verify that the story was implemented correctly.
- Supporting detail: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] distinguishes user stories from tasks, UI artifacts, exploratory enablers, and technical enablers.
- Collaborative authorship: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] argues that anyone on the team can and should write user stories.
- Vertical delivery boundary: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] contrasts isolated Django Model, Template, or View work with one end-to-end path that displays a user's posts.
- Acceptance and estimation: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] uses a narrowed story to connect a user-visible result with acceptance criteria and a discussable estimate.

## Counterevidence & Qualifications
Both sources are prescriptive practitioner guidance rather than comparative studies of requirements techniques. The PBB source warns against overusing enablers and implies that stories need team agreement, acceptance criteria, and enough context to be ready; a bare template alone is not enough. The 8th Light example shows one simple Django read path but does not test vertical slicing against dependency-heavy migrations, infrastructure work, security remediation, research, or changes whose value appears only after several slices integrate.

## What Changed
- Created User Stories as a requirements concept grounded in 3Ws, INVEST, 3Cs, acceptance criteria, and collaborative authorship.
- Added vertical slicing as an end-to-end user-outcome boundary across technical layers.

## Related Concepts
- [[ProductBacklogBuilding]] - provides a canvas method for generating stories from personas, features, and PBIs.
- [[AgileSoftwareDevelopment]] - broader practice context where stories support adaptive planning and collaboration.
- [[ExtremeProgramming]] - historical origin context for the User Story term.
- [[ProductManagement]] - adjacent role domain that often organizes backlogs but should not monopolize story authorship.
- [[SoftwareEstimation]] - estimates the effort and uncertainty attached to a scoped story.
- [[PERTEstimation]] - three-scenario method applied to a vertically sliced story in the 8th Light source.

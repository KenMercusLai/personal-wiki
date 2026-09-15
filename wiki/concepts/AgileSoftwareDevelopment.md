---
title: "Agile Software Development"
type: concept
tags: [agile, software-development, collaboration]
sources:
  - blog-martin-fowler-foreword-to-the-art-of-agile-development
  - blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas
  - chris-james-how-to-go-fast
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Definition
[[AgileSoftwareDevelopment]] is a practice-rich approach to software work that combines adaptive planning, customer collaboration, teamwork, and technical execution so teams can discover and deliver valuable software reliably.

## Current Synthesis
The Fowler foreword makes agile a capability system rather than a label. The problem is not that agile became mainstream; it is that mainstream "agile" often preserves ceremonies while losing the connected management and technical practices that let teams adapt and deliver.

In this synthesis, agile has two inseparable halves. Teams must focus on value through customer and user collaboration, adaptive planning, and strong teamwork. They must also deliver reliably through technical practices such as testing, refactoring, design, collaborative development, DevOps culture, and [[ContinuousDelivery]].

Caroli's PBB article adds a concrete requirements-planning mechanism inside that broader capability system. [[UserStories]] remain agile when they are short prompts for conversation, confirmation, and refinement; [[ProductBacklogBuilding]] keeps them grounded in personas, user activities, features, PBIs, acceptance criteria, and team-defined ready/done agreements.

James adds an operating-speed version of the same synthesis. Agile speed comes from small batches, direct user and stakeholder feedback, low WIP, and enough team trust to reduce ceremony. The article is especially explicit that user stories should describe user problems and success measures, while the team decides the implementation through conversation.

## Key Claims
- Agile depends on interconnected practices, not isolated rituals.
- Customer focus and adaptive planning provide value only when paired with reliable delivery skills.
- Technical practices are often under-taught, creating a gap between agile vocabulary and agile capability.
- [[ExtremeProgramming]] is an important practice foundation for the Agile movement.
- Production delivery and observation help teams learn what is valuable in real use.
- Agile requirements work benefits from collaborative story writing, explicit ready/done agreements, and user stories that remain conversation starters.
- Sustainable agile speed depends on small feedback loops, low WIP, and shared understanding of the user's problem.

## Evidence
- Practice web: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] says agile work requires interconnected management and technical practices.
- Mainstream gap: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] argues many teams sincerely believe they are agile while acting unlike the original vision.
- Value focus: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] links agile value work to teamwork, adaptive planning, and close customer or user collaboration.
- Reliable delivery: [[blog-martin-fowler-foreword-to-the-art-of-agile-development]] connects agility to testing, refactoring, design, collaborative development, DevOps, and continuous delivery.
- Collaborative requirements: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] argues that everyone on a team can write user stories when they share persona, feature, and benefit context, with Ready and Done agreements connecting refinement to releasable increments.
- Sustainable speed: [[chris-james-how-to-go-fast]] ties fast delivery to small teams, two-week showcases, deployed increments, low WIP, user observation, and avoiding overbuilt process.
- User-story conversation: [[chris-james-how-to-go-fast]] says user stories should describe user problems and success measures rather than dictate implementation.

## Counterevidence & Qualifications
The current evidence comes from Fowler's foreword and is intentionally normative. It criticizes ceremony-led agile adoption but does not compare named agile frameworks empirically or define when lightweight Scrum-like practice may be sufficient.

The PBB source is also practitioner guidance, so its canvas and checklists should be treated as adaptable team agreements rather than mandatory agile law.

James's advice is similarly context-sensitive. Co-location, no pull requests, and minimal non-live environments depend on a small trusted team, strong tests, close communication, and low-risk release mechanics; larger, distributed, regulated, or safety-critical teams may need additional controls.

## What Changed
- Created the concept from Fowler's foreword.
- Added Product Backlog Building as a concrete agile requirements and refinement practice.
- Added James's sustainable-speed emphasis on low WIP, user-problem clarity, and feedback-loop reduction.

## Related Concepts
- [[ExtremeProgramming]] - agile practice tradition Fowler presents as a central pillar.
- [[AgileFluencyModel]] - capability model used to distinguish shallow adoption from deeper agile skill.
- [[InternalSoftwareQuality]] - technical quality practice needed for reliable agile delivery.
- [[ContinuousDelivery]] - production delivery loop that supports agile learning.
- [[PersonalProductivity]] - both concern work adaptation, though agile is team and product oriented.
- [[UserStories]] - lightweight agile requirements format for conversation and confirmation.
- [[ProductBacklogBuilding]] - collaborative backlog-building practice within agile planning.
- [[CodeReviewPractice]] - review ceremony should be tuned to trust, risk, and feedback-loop cost.

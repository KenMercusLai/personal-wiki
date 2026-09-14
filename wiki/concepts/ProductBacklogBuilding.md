---
title: "Product Backlog Building"
type: concept
tags: [agile, product-backlog, user-stories, facilitation]
sources:
  - blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ProductBacklogBuilding]] is a collaborative canvas technique for deriving product backlog items and [[UserStories]] from personas, user activities, features, benefits, and work-item decomposition.

## Current Synthesis
The PBB canvas gives teams a structured path from product understanding to backlog writing. It begins with personas, including their roles, needs, goals, and activities. Those activities are examined for interactions with the product, which become features. Features are then broken into product backlog items, and each PBI can be composed into a user story by combining the persona, the action, and the feature benefit.

The technique's main contribution is turning backlog creation into a visible, collaborative facilitation process. Instead of asking a Product Owner to invent and maintain stories alone, the canvas lets the team connect user context, product behavior, implementation detail, acceptance criteria, UI artifacts, enablers, and ready/done agreements. It keeps user stories lightweight while still giving implementation enough structure to proceed.

## Key Claims
- PBB starts with personas and their activities so backlog work remains tied to user context.
- Persona activities become candidate product features when they describe interactions the product should support.
- Features are decomposed into PBIs before being written as user stories.
- A PBI becomes a story by combining persona, action, and benefit.
- Acceptance criteria, tasks, UI artifacts, and enablers supply supporting implementation detail.
- Definitions of Ready and Done turn backlog items into team agreements about preparedness and releasability.
- The canvas makes backlog authorship collaborative across the team.

## Evidence
- Persona grounding: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says personas should describe profile, activity, needs, goals, and expectations before feature work begins.
- Feature identification: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says teams reread persona activities and identify interactions with the product as features.
- PBI decomposition: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] says features must be broken into smaller backlog items that represent user actions on the product.
- Story composition: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] shows the canvas filling the "as a," "I want to," and "so that" fields from persona, PBI, and feature benefit.
- Implementation detail: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] explains acceptance criteria, tasks, UI artifacts, exploratory enablers, and technical enablers as add-ons around the core story.
- Team agreements: [[blog-paulo-caroli-martinfowler-com-product-backlog-building-canvas]] defines Ready as enough information to start and Done as the quality agreement for a releasable product increment.

## Counterevidence & Qualifications
The source uses a single Talks Collection example and practitioner checklists, so it should be treated as facilitation guidance rather than a universal process law. It also notes that teams must define their own ready and done checklists and should avoid turning the backlog into enabler-only work.

## What Changed
- Created Product Backlog Building as a collaborative bridge from persona discovery to PBIs, user stories, acceptance criteria, and ready/done agreements.

## Related Concepts
- [[UserStories]] - primary textual output generated from PBB canvas blocks.
- [[ProductManagement]] - related practice area that organizes product work but should not centralize all backlog authorship.
- [[AgileSoftwareDevelopment]] - broader process context for iterative backlog refinement and delivery.
- [[ExtremeProgramming]] - user-story lineage that PBB builds on.
- [[ProductIdeaPrioritization]] - adjacent product-planning concern focused on which ideas deserve investment.

---
title: "Chris James"
type: entity
tags: [software-development, agile]
sources:
  - chris-james-how-to-go-fast
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[ChrisJames]] is represented in the wiki as a software-development practitioner-author arguing for sustainable speed through small teams, continuous delivery, simple architecture, user contact, and low-process agile discipline.

## Current Profile
The source presents James as a pragmatic agile voice rather than as a formal methodology designer. His article rejects large upfront planning, speculative architecture, heavy Jira metrics, and ceremony that delays feedback. The preferred operating model is direct: clarify the user problem, deploy immediately, work in small increments, keep quality high, watch real users, and let design emerge from production learning.

## Key Characteristics
- Advocates sustainable speed rather than burnout-driven delivery.
- Treats [[ContinuousDelivery]] as the default software-development loop from the first deployed increment.
- Favors small trusted teams, pairing, co-location, stakeholder access, and user observation.
- Prefers simple architectures and mature tools until evidence justifies more complexity.
- Frames agile artifacts such as user stories as conversation aids, not prescriptive task contracts.

## Evidence
- Sustainable speed: [[chris-james-how-to-go-fast]] says teams should go fast while protecting system quality and team mental health.
- Delivery loop: [[chris-james-how-to-go-fast]] recommends starting with a deployed "hello world" and continuously deploying green builds to live.
- Team model: [[chris-james-how-to-go-fast]] favors small co-located teams, pairing, direct stakeholder feedback, and sitting with users.
- Simplicity preference: [[chris-james-how-to-go-fast]] argues for monoliths, progressive enhancement, mature tools, simple build setup, and minimal deployment pipelines.
- Agile artifact stance: [[chris-james-how-to-go-fast]] treats user stories as conversation starters around user problems and success measures.

## Qualifications
The evidence is a single practitioner essay. Its strongest recommendations, especially no pull requests, co-location, and production-only environment minimalism, are explicitly scoped to small trusted teams and may not fit high-risk infrastructure, distributed organizations, strict compliance settings, or teams without strong automated tests and pairing norms.

## What Changed
- Created the entity from James's "How to go fast" essay.

## Relationships
- [[AgileSoftwareDevelopment]] - James presents a lightweight practice model for moving fast without ceremony overload.
- [[ContinuousDelivery]] - James treats live deployment on green builds as central to speed.
- [[InternalSoftwareQuality]] - James links tests, refactoring, and simple design to sustainable pace.
- [[CodeReviewPractice]] - James qualifies pull-request review for small trusted teams.

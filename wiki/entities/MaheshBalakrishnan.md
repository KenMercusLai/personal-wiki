---
title: "Mahesh Balakrishnan"
type: entity
tags: [person, distributed-systems, databases]
sources:
  - blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[MaheshBalakrishnan]] appears in the wiki as the author of "42 Things I Learned from Building a Production Database" and as the tech lead who created the [[Delos]] team at [[Facebook]] while on sabbatical from Yale.

## Current Profile
The source presents Balakrishnan as an academic and production infrastructure leader whose advice comes from building a critical storage system in a large-company environment. His authority in this source rests on the Delos case: he started the team in 2017, reached production with three people in under a year, scaled the team beyond thirty engineers, avoided severe outages during four years of leadership, and connected the system to OSDI 2020 and SOSP 2021 papers.

His leadership model is unusually broad. He treats customer contact, manager alignment, IC task allocation, API design, correctness-first storage semantics, code-review culture, observability placement, internal strategy, and research literacy as one production-infrastructure practice rather than separate management and engineering concerns.

## Key Characteristics
- Built his advice from leading the [[Delos]] storage-system effort at [[Facebook]].
- Combines academic distributed-systems orientation with production operations experience.
- Emphasizes direct contact with customer ICs and close understanding of customer code.
- Treats infrastructure leadership as a socio-technical role spanning design, staffing, estimation, review, observability, and strategy.
- Values research and external writing as ways to clarify design assumptions and improve onboarding.

## Evidence
- Delos leadership: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Balakrishnan created and led the Delos team after joining Facebook on sabbatical from Yale in 2017.
- Production outcome: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says Delos reached production with three people in less than a year and had no severe outage above SEV3 during his four-year leadership period.
- Socio-technical scope: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] organizes lessons across customers, project management, design, code review, strategy, observability, and research.
- Customer stance: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] advises direct conversations with customer ICs and reading customer code.
- Research stance: [[blog-mahesh-balakrishnan-42-things-i-learned-from-building-a-production-database]] says teams should track research, try new feasible designs, write papers, and give talks.

## Qualifications
The source is a reflective practitioner essay, not an independent evaluation of Delos or Balakrishnan's full career. Its lessons are explicitly scoped to people leading teams that build new infrastructure at large companies, and Balakrishnan notes that much of the advice may not generalize elsewhere.

## What Changed
- Created the entity from Balakrishnan's production database leadership essay.

## Relationships
- [[Delos]] - Balakrishnan created and led the team building Delos.
- [[Facebook]] - company context for Balakrishnan's sabbatical and production infrastructure work.
- [[ProductionInfrastructureLeadership]] - Balakrishnan's essay is the founding source for this concept.
- [[ServiceObservability]] - his advice includes implementation-independent observability and deployment-integrated checks.
- [[CodeReviewPractice]] - his essay contributes a stricter review stance for critical infrastructure components.

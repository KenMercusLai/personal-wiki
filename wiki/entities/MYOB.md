---
title: "MYOB"
type: entity
tags: [software-company, technology-management]
sources:
  - blog-martin-fowler-default-trial-retire
  - blog-martin-fowler-the-strong-and-weak-forces-of-architecture
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Overview
[[MYOB]] is represented in this wiki as the company Fowler uses to illustrate both an internal [[TechnologyRadar]] and a scope-sensitive architecture-governance model based on domains, verticals, and alignment forces.

## Current Profile
The source uses MYOB as an organization-scale example of technology-choice communication. Rather than relying only on local team discussion, MYOB publishes its own technology radar, following the [[Thoughtworks]] Technology Radar format, to make guidance visible about which technologies teams should adopt, trial, or avoid.

MYOB's simplified operating structure in the wiki now includes product and business-capability teams grouped into domains, with domains grouped into larger customer-segment verticals. Fowler uses this as a model for [[ArchitectureAlignmentForces]]: teams inside a domain share concepts, expertise, priorities, and change cadence, while cross-domain and cross-vertical decisions have larger blast radius and weaker social alignment.

## Key Characteristics
- Uses an internal technology radar for organization-wide technology guidance.
- Collects input from verticals and teams.
- Follows the Thoughtworks Technology Radar format in the source.
- Communicates adopt, trial, and avoidance guidance rather than only listing technologies.
- Organizes the architecture example around teams, domains, and larger verticals.
- Treats domain-local decisions as higher-alignment and organization-wide decisions as lower-alignment.
- Uses alignment strength to vary coupling, shared-code, contribution, technology-choice, and integration guidance.

## Evidence
- Radar publication: [[blog-martin-fowler-default-trial-retire]] says MYOB publishes its own technology radar.
- Input model: [[blog-martin-fowler-default-trial-retire]] says the radar takes input from verticals and teams.
- Format lineage: [[blog-martin-fowler-default-trial-retire]] says MYOB follows the Thoughtworks Technology Radar format.
- Guidance role: [[blog-martin-fowler-default-trial-retire]] says the radar states what teams should adopt, trial, or keep clear of.
- Organization structure: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] shows teams grouped into domains and domains grouped into verticals.
- Alignment model: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says strong domain-level alignment can allow faster change and some tighter coupling, while weak organization-wide alignment needs loose coupling and stronger contracts.

## Qualifications
This page only captures MYOB as represented in the ingested technology-governance and architecture-governance examples. It does not describe MYOB's broader business, product portfolio, or current technology practices.

## What Changed
- Created the entity from the source's MYOB Technology Radar example.
- Added MYOB's team/domain/vertical organization structure and its role in Fowler's strong/weak architecture-forces model.

## Relationships
- [[TechnologyRadar]] - MYOB uses this mechanism for organization-wide technology guidance in the source.
- [[Thoughtworks]] - MYOB follows the Thoughtworks Technology Radar format.
- [[DefaultTrialRetire]] - MYOB's radar is presented as an organization-scale companion to team-level technology limits.
- [[ArchitectureAlignmentForces]] - MYOB is the worked organization-design example for this governance model.
- [[IntegrationStrategy]] - MYOB's integration guidance varies by domain, vertical, and whole-organization scope.

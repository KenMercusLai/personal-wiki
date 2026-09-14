---
title: "Technology Radar"
type: concept
tags: [technology-management, architecture-governance, enterprise-architecture]
sources:
  - blog-martin-fowler-default-trial-retire
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[TechnologyRadar]] is an organizational communication tool that classifies technologies by recommended status, such as adopt, trial, or avoid, so teams can coordinate technology choices beyond local conversations.

## Current Synthesis
The source presents a technology radar as the organization-level counterpart to [[DefaultTrialRetire]]. Team-level limits can be maintained through direct communication, but whole-organization alignment takes longer and migration or consolidation may span many teams. A radar gives the organization a shared vocabulary for preferred, experimental, and discouraged technologies.

The example is [[MYOB]] publishing its own technology radar, following the [[Thoughtworks]] Technology Radar format and incorporating input from verticals and teams. The important function is not the visual format alone; it is the clear statement of which technologies teams should adopt, trial, or keep clear of.

## Key Claims
- Technology radars help organizations communicate technology status when direct team discussion does not scale.
- The radar format can gather input from multiple verticals and teams.
- Status categories make technology guidance more actionable than an undifferentiated approved-tools list.
- Radars can complement local technology-choice limits by distinguishing adoptable defaults, experiments, and avoid/retire zones.

## Evidence
- Organization-scale need: [[blog-martin-fowler-default-trial-retire]] says whole-organization alignment and consolidation take longer than team-level decisions.
- MYOB example: [[blog-martin-fowler-default-trial-retire]] says MYOB publishes its own technology radar.
- Format lineage: [[blog-martin-fowler-default-trial-retire]] says MYOB follows the Thoughtworks Technology Radar format.
- Input model: [[blog-martin-fowler-default-trial-retire]] says MYOB takes input from verticals and teams.
- Status communication: [[blog-martin-fowler-default-trial-retire]] says the radar states what to adopt, trial, or keep clear of.

## Counterevidence & Qualifications
The source describes radar use as an organizational communication practice, not a guarantee of migration completion or technology simplification. A radar can signal direction, but teams still need the capacity and incentives to consolidate, retire, and migrate real systems.

## What Changed
- Created the concept from the source's MYOB Technology Radar example and its link to organization-scale technology alignment.

## Related Concepts
- [[DefaultTrialRetire]] - radars extend the default/trial/retire logic beyond a single team.
- [[TechnologyStackComplexity]] - radars are one governance response to uncontrolled technology variety.
- [[ScalingCommunication]] - radars turn local technology judgment into organization-wide guidance.
- [[IntegrationStrategy]] - radars are another way to keep architecture choices visible beyond individual implementation decisions.

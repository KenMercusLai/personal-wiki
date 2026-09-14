---
title: "Default Trial Retire"
type: source
tags: [technology-management, enterprise-architecture, governance]
date: 2026-09-14
source_file: "/mnt/ken_personal_wiki/Articles/Blog - Martin Fowler - Default Trial Retire.md"
---

## Summary
This Martin Fowler bliki note describes [[DefaultTrialRetire]], a team-level rule for limiting each technology category to three active alternatives: the sensible default, one experiment, and one unwanted legacy option to remove. It connects this local constraint to [[TechnologyStackComplexity]], Innovation Tokens, and organization-level communication through [[TechnologyRadar]] practices such as the [[MYOB]] Technology Radar following the [[Thoughtworks]] Technology Radar format.

## Key Claims
- A normal-sized team should keep each technology class to only a default, a trial, and a retire candidate.
- Adding a new technology when the team is already at the limit should force either legacy migration or cleanup of a failed experiment.
- Team-level constraints work because shared priorities, trust, and high-bandwidth communication make limits discussable and actionable.
- Organization-wide technology alignment is slower and sometimes requires more variation, so broader communication mechanisms are needed.
- A technology radar can make adoption, trial, and avoidance guidance visible across many teams.

## Key Quotes
> "limit the choice of alternatives for any class of technology to three" - core team-level rule

> "adopt, trial, or more importantly which ones to keep clear of" - radar guidance categories

## Connections
- [[DefaultTrialRetire]] - the named technology-choice governance pattern.
- [[TechnologyStackComplexity]] - the problem the pattern is trying to cap.
- [[TechnologyRadar]] - organization-level communication mechanism for technology status.
- [[MYOB]] - company whose internal technology radar is used as the example.
- [[Thoughtworks]] - source of the public Technology Radar format MYOB follows.

## Contradictions
- No direct contradiction found. The source complements existing stack-complexity pages by adding a governance mechanism for controlling technology variety rather than only arguing for smaller stacks after complexity appears.

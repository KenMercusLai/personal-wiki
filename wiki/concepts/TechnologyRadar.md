---
title: "Technology Radar"
type: concept
tags: [technology-management, architecture-governance, enterprise-architecture]
sources:
  - blog-martin-fowler-default-trial-retire
  - blog-martin-fowler-the-strong-and-weak-forces-of-architecture
  - blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[TechnologyRadar]] is an organizational communication tool that classifies technologies by recommended status, such as adopt, trial, or avoid, so teams can coordinate technology choices beyond local conversations.

## Current Synthesis
[[TechnologyRadar]] operates as the organization-level counterpart to [[DefaultTrialRetire]]. Team-level limits can be maintained through direct communication, but whole-organization alignment takes longer and migration or consolidation may span many teams. A radar gives the organization a shared vocabulary for preferred, experimental, held, and retiring technologies.

The example is [[MYOB]] publishing its own technology radar, following the [[Thoughtworks]] Technology Radar format and incorporating input from verticals and teams. The important function is not the visual format alone; it is the clear statement of which technologies teams should adopt, trial, or keep clear of.

The mechanism matters most where alignment forces weaken. Inside a domain, technology alignment can often happen through informal leadership and a small agreed set. Across a vertical or the whole organization, social distance and independent prioritization make alignment slower, so radar-style direction and proposal sharing become a lighter-weight alternative to command-and-control standardization.

A participatory operating model turns the radar into more than published guidance. Teams collectively baseline their actual technology landscape, discuss where effort should increase or decrease, and record relevant blips in [[ArchitectureDecisionRecords]]. A proposed experiment or movement between rings then becomes input to the [[ArchitectureAdvisoryForum]]. The radar is therefore both guidance and a sensing mechanism: it aligns understanding while exposing decisions that may change the shared landscape.

## Key Claims
- Technology radars help organizations communicate technology status when direct team discussion does not scale.
- The radar format can gather input from multiple verticals and teams.
- Status categories make technology guidance more actionable than an undifferentiated approved-tools list.
- Radars can complement local technology-choice limits by distinguishing adoptable defaults, experiments, and avoid/retire zones.
- Radars are especially useful where alignment forces are weak enough that direct negotiation across all affected teams would be slow.
- Collective radar workshops can surface the organization's actual technical landscape and align understanding across roles.
- Linking radar blips to ADRs makes local experiments and status changes visible to architectural conversations.

## Evidence
- Organization-scale need: [[blog-martin-fowler-default-trial-retire]] says whole-organization alignment and consolidation take longer than team-level decisions.
- MYOB example: [[blog-martin-fowler-default-trial-retire]] says MYOB publishes its own technology radar.
- Format lineage: [[blog-martin-fowler-default-trial-retire]] says MYOB follows the Thoughtworks Technology Radar format.
- Input model: [[blog-martin-fowler-default-trial-retire]] says MYOB takes input from verticals and teams.
- Status communication: [[blog-martin-fowler-default-trial-retire]] says the radar states what to adopt, trial, or keep clear of.
- Scope fit: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says the MYOB technology radar sets whole-organization direction where alignment forces are weakest.
- Vertical coordination: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says solution options and proposals help keep technology choices aligned at vertical and organization scope.
- Collective sensing: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] recommends an all-team baseline workshop covering the organization's current technologies and their experiment, adopt, hold, or retire status.
- Decision integration: [[blog-andrew-harmel-law-martinfowler-com-scaling-the-practice-of-architecture-conversationally]] uses relevant radar blips in ADRs to flag conformity, experiments, and proposed ring movement for advisory-forum discussion.

## Counterevidence & Qualifications
The source describes radar use as an organizational communication practice, not a guarantee of migration completion or technology simplification. A radar can signal direction, but teams still need the capacity and incentives to consolidate, retire, and migrate real systems.

Radar guidance also does not replace domain-level judgment. The alignment-forces source treats it as one mechanism among several, used more heavily where direct alignment is weaker.

The workshop and refresh model adds real participation cost: an initial sweep can take four hours or more, and quarterly or half-yearly refreshes are only useful when teams consume the radar. Crowdsourcing also does not guarantee balanced influence or accurate classification.

## What Changed
- Created the concept from the source's MYOB Technology Radar example and its link to organization-scale technology alignment.
- Added the strong/weak forces rationale for using radar-style guidance at vertical and organization scope.
- Added the radar's collective landscape-sensing role and its integration with ADRs and advisory conversations.

## Related Concepts
- [[DefaultTrialRetire]] - radars extend the default/trial/retire logic beyond a single team.
- [[TechnologyStackComplexity]] - radars are one governance response to uncontrolled technology variety.
- [[ScalingCommunication]] - radars turn local technology judgment into organization-wide guidance.
- [[IntegrationStrategy]] - radars are another way to keep architecture choices visible beyond individual implementation decisions.
- [[ArchitectureAlignmentForces]] - radars fit weaker alignment forces where organization-wide direct negotiation is slow.
- [[ArchitectureDecisionRecords]] - make relevant radar status and proposed movement explicit in local decisions.
- [[ArchitectureAdvisoryForum]] - provides a venue for discussing experiments and radar changes.

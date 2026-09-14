---
title: "Default Trial Retire"
type: concept
tags: [technology-management, architecture-governance, software-teams]
sources:
  - blog-martin-fowler-default-trial-retire
  - blog-martin-fowler-the-strong-and-weak-forces-of-architecture
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DefaultTrialRetire]] is a technology-choice rule that limits a normal-sized team's alternatives in any technology category to three: the current sensible default, one technology being tried, and one disliked or legacy technology being retired.

## Current Synthesis
The pattern treats technology variety as an explicit capacity budget. A team can experiment, but an additional option must displace something: either the legacy technology is migrated away from, or the previous failed experiment is cleaned up. This prevents trials from quietly becoming permanent stack sprawl.

The source distinguishes team-level and organization-level governance. Within a team, shared priorities, trust, and high-bandwidth communication make the limit easier to maintain. Across a whole organization, migration and alignment take longer, so teams may need more variation and clearer status communication through mechanisms such as a [[TechnologyRadar]].

The strong/weak forces source supplies the organizational reason for that boundary. Default Trial Retire fits strong alignment forces inside a domain, where technology leaders and teams can negotiate a small set of choices informally. At vertical or whole-organization scope, the same desire for coherence needs more formal proposal sharing or radar-style direction because negotiation is slower and affects more independent priorities.

## Key Claims
- Technology categories should have an explicit small limit rather than unbounded local choice.
- Teams need room for experimentation, but trials must not accumulate without retirement.
- Retire candidates should remain visible so migration or cleanup competes with adding new options.
- The pattern works best where communication is high-trust and priorities are shared.
- At organization scale, the same intent needs slower alignment mechanisms such as technology radars.
- The rule is strongest in domains or teams where alignment forces are high enough to make tradeoffs visible and actionable.

## Evidence
- Three-option limit: [[blog-martin-fowler-default-trial-retire]] defines the set as default, trial, and retire.
- Forced tradeoff: [[blog-martin-fowler-default-trial-retire]] says adding another messaging technology at the limit requires either migrating off legacy technology or removing a failed experiment.
- Team conditions: [[blog-martin-fowler-default-trial-retire]] says common priorities and high-bandwidth communication make team-level limits easier to discuss and act on.
- Organization-scale qualification: [[blog-martin-fowler-default-trial-retire]] says alignment, migration, and consolidation take longer at whole-organization scope.
- Radar mechanism: [[blog-martin-fowler-default-trial-retire]] cites MYOB's technology radar as a way to communicate adoption, trial, and avoidance guidance.
- Domain fit: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says domain-level technology choices can often be governed informally through technology leadership and small agreed sets.
- Broader-scope fit: [[blog-martin-fowler-the-strong-and-weak-forces-of-architecture]] says vertical and whole-organization technology choices need more proposal sharing and radar-style direction because alignment forces weaken.

## Counterevidence & Qualifications
The source presents a practitioner rule, not measured evidence that three is the universally optimal number. It also explicitly relaxes the pattern at whole-organization scale, where slower migration and broader alignment can justify more temporary variation.

The alignment-forces source reinforces that relaxation: weak organization-wide alignment makes a strict local rule harder to apply without adaptation.

## What Changed
- Created the concept from the Fowler bliki note's named rule for capping team technology alternatives.
- Added the alignment-forces explanation for why the rule fits domains better than whole-organization governance.

## Related Concepts
- [[TechnologyStackComplexity]] - Default Trial Retire limits the stack variation that creates operational and reasoning burden.
- [[TechnologyRadar]] - radars communicate broader technology status when team-level discussion is insufficient.
- [[ArchitectureAlignmentForces]] - explains why local technology-choice governance weakens as organizational scope grows.
- [[ToolFamiliarity]] - the default option usually reflects existing sensible team competence.
- [[DistributedSystemRestraint]] - both concepts delay extra technical variety until its cost is justified.
- [[LegacyDisplacement]] - retiring an unwanted technology often requires migration work.

---
title: "Engineering Principles"
type: concept
tags: [software-engineering, decision-making, governance, engineering-culture]
sources:
  - engineering-principles-incyte-studios-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[EngineeringPrinciples]] are a small, revisable set of explicit team commitments used to guide recurring technical, product, and collaboration decisions without requiring case-by-case managerial approval.

## Current Synthesis
The article's central mechanism is shared judgment rather than rule accumulation. A manager makes priorities and decision criteria explicit, the team discusses and ratifies them, and members can then make locally coherent choices without repeatedly escalating through hierarchy. Ratification matters because a manager's preferences do not become collective principles merely by being written down.

The proposed content spans several layers: build work that matters; prefer research and objective data; anticipate organizational, human, dependency, network, and scope risks; repair visible decay; keep knowledge authoritative; favor understandable code; communicate with attention to tone; practice and share craft; protect respectful scientific disagreement; expose work while it is still shapeable; and investigate needs with users. The list therefore acts less like a coding standard than a compact operating model for engineering judgment.

The principles are meant to change with context. Version control, pull requests, and search make them inspectable and amendable, while the author's experience across companies argues against treating the published list as universal. Their value is in prompting a team to articulate what it values and how it decides, not in copying every aphorism unchanged.

## Key Claims
- Shared principles can reduce dependence on hierarchy by giving local decisions a common frame.
- Team discussion and ratification distinguish collective commitments from unilateral managerial preferences.
- Principles should connect business value, empirical inquiry, technical quality, communication, culture, collaboration, and user discovery rather than address code alone.
- A living repository and lightweight retrieval tools can make principles reviewable, changeable, and available during work.
- Early feedback is collaboration when it can still alter direction; late requests for approval are closer to corroboration.
- A principle is a starting heuristic whose application still requires context, evidence, tradeoffs, and explicit exceptions.

## Evidence
- Decentralized coherence: [[engineering-principles-incyte-studios-medium]] argues that a team sharing ratified priorities can make decisions consistent with managerial intent without micromanagement.
- Living governance: [[engineering-principles-incyte-studios-medium]] describes a Git repository, pull requests, Slack lookup, and company-specific revision as the operating infrastructure around the list.
- Breadth of judgment: [[engineering-principles-incyte-studios-medium]] links prioritization and objective data with threat awareness, code clarity, craftsmanship, respectful communication, culture, early review, and user-centered requirements discovery.
- Collaboration timing: [[engineering-principles-incyte-studios-medium]] contrasts feedback at 20% completion, when it can matter, with support requested at 80% completion.
- Reported outcome: [[engineering-principles-incyte-studios-medium]] says introducing principles repeatedly led to discussion of uncodified values and greater coherence.

## Counterevidence & Qualifications
The evidence is one manager's practitioner essay, not a comparative study, and it does not measure coherence, autonomy, delivery, quality, or employee agreement before and after adoption. The absolute claim that principles “always” increase coherence is therefore experience-scoped. Written principles can also disguise unilateral control if ratification is nominal, suppress productive dissent if consistency becomes conformity, or become ceremonial when incentives and decisions contradict them. Several proposed maxims need contextual limits: deduplication can create premature abstraction, immediate cleanup can displace higher-risk work, “clear” and “craft” are contestable, scientific language does not remove value judgments, and hiring for near-term cultural comfort can undermine genuine diversity. Useful principles need owners, revision paths, examples, exceptions, and evidence that actual decisions follow them.

## What Changed
- Created a cross-functional model of living, team-ratified engineering decision principles.
- Preserved the distinction between decentralized coherence and managerial rules presented as consensus.
- Qualified the author's universal outcome claim and the individual maxims as experience-based heuristics.

## Related Concepts
- [[SystemArchitecturePrinciples]] - applies a similar alignment mechanism specifically to architecture decisions and documented deviations.
- [[EvidenceBasedSoftwareEngineering]] - supplies the standard of proof needed to turn “be a scientist” into disciplined inquiry.
- [[WorkplaceCollaboration]] - explains why early visibility, useful disagreement, and explicit decision rights matter around shared principles.
- [[InternalSoftwareQuality]] - provides the risk- and change-sensitive boundary for clarity, repair, refactoring, and craftsmanship norms.
- [[DecentralizedArchitectureGovernance]] - shows how shared guidance can coordinate local technical decisions without a central approval step.
- [[UserCenteredDesign]] - grounds the instruction to investigate requirements by working with users.
- [[OrganizationalCulture]] - principles make selected values explicit but do not by themselves determine lived behavior.

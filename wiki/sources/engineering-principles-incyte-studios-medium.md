---
title: "Engineering Principles"
type: source
tags: [software-engineering, team-principles, decision-making, engineering-culture]
date: 2015-11-16
source_file: "/mnt/ken_personal_wiki/Articles/Engineering Principles - Incyte Studios - Medium.md"
---

## Summary
This 2015 practitioner essay argues that an engineering team can make coherent decisions with less managerial intervention when it ratifies a shared, living set of principles. Its proposed principles join business prioritization and evidence-seeking with code quality, communication, culture, early collaboration, and deeper requirements discovery; the author presents them as a revisable starting point rather than a universal fixed list.

![Tower of Babel illustrating the coordination failure that shared engineering principles are intended to reduce](../../wiki-assets/engineering-principles-incyte-studios-medium/tower-of-babel.jpg)

## Key Claims
- Team-ratified principles can encode what matters to the group and let members make more consistent decisions without waiting for hierarchy.
- Principles should remain living artifacts: the author's version lived in a Git repository, accepted pull requests, was searchable through Slack, and changed at each company where it was introduced.
- Scarce engineering effort should be directed toward problems that materially affect the company.
- Teams should prefer research and objective data to hunches, while identifying recurring threats such as sleep deprivation, weak validation, unreliable networks, dependency risk, scope creep, and Conway's Law.
- Technical quality includes repairing visible decay, keeping knowledge authoritative, favoring clear code over clever code, and treating the weakest part of a product as a constraint on overall quality.
- Collaboration is most useful while work is still shapeable: the essay contrasts peer input at roughly 20% completion with seeking endorsement at 80%.
- Requirements must be uncovered beneath assumptions, misconceptions, and politics by working with users rather than merely collecting surface requests.

## Key Quotes
> "Stating your principles as a team allows an amazing optimization: high-coherence decision making, sans hierarchy." - on the proposed coordination mechanism.

> "These principles are alive." - on maintaining the list through version control, pull requests, and searchable team tooling.

> "Don't gather requirements, dig for them" - on investigating user needs beneath the initial request.

## Connections
- [[EngineeringPrinciples]] - the article's central model for living, team-ratified decision guidance.
- [[EvidenceBasedSoftwareEngineering]] - “be a scientist” makes research and objective data an operating norm, although the article does not empirically test its own outcome claims.
- [[WorkplaceCollaboration]] - the essay favors feedback early enough to change the work rather than late-stage corroboration.
- [[InternalSoftwareQuality]] - broken-window repair, DRY, clarity, and craftsmanship are presented as team-level quality norms.
- [[SystemArchitecturePrinciples]] - both concepts use explicit principles to align decentralized choices, with architecture principles applying the mechanism to a narrower decision domain.
- [[HandwritingIo]] - company whose CTO the author said they were when the essay was published.

## Contradictions
- The claim that introducing principles “always” produces higher coherence is based on the author's experience rather than comparative evidence, creating a tension with the essay's own call for objective data and with [[EvidenceBasedSoftwareEngineering]].
- “Don't live with broken windows” and “don't repeat yourself” are useful heuristics, but applied without cost, risk, and change-frequency judgment they can conflict with [[InternalSoftwareQuality]]'s proportional approach to refactoring and perfection.

---
title: "0 Bugs Policy"
type: source
tags: [agile, bugs, scrum, software-quality]
date: 2016-04-05
source_file: "/mnt/ken_personal_wiki/Articles/Gal Zellermayer - 0 Bugs Policy.md"
---

## Summary
[[GalZellermayer]] proposes the [[ZeroBugsPolicy]]: every newly found defect should be fixed now or in the next sprint, or closed as “won't fix,” rather than retained indefinitely. The practitioner argument connects prompt decisions to [[AgileSoftwareDevelopment]] and [[InternalSoftwareQuality]] by treating in-sprint defects as unfinished work and old defect inventories as costly queues whose context decays. A five-image planning sequence shows how feature pressure repeatedly moves bugs below sprint capacity, but the article supplies no comparative outcome data and does not address environments that require known-defect records or formal risk acceptance.

## Key Claims
- In-sprint bugs must be fixed before a story is considered done; otherwise the feature has not met its tested and accepted definition of completion.
- Other bugs should be fixed immediately or in the next sprint when their value warrants the effort, and otherwise closed as “won't fix.”
- Deferring a defect raises later repair cost because memory fades, environments disappear, and surrounding code changes.
- A bug backlog creates recurring triage and prioritization work while forcing defects to compete with new features that product owners often prefer.
- Hardening phases, dead time, dedicated bug sprints, and mixed feature-and-bug backlogs do not remove the accumulation mechanism described by the author.
- An existing backlog should be cleared through explicit fix-or-close decisions, after which the policy is maintained for new defects.
- The author reports that the policy encouraged developers to pursue higher quality, but offers experience rather than measured evidence for the cultural effect.

![Preplanning backlog mixing two bugs with four user stories](../../wiki-assets/gal-zellermayer-0-bugs-policy/mixed-backlog-before-planning.jpg)

The initial preplanning list interleaves two defects and four user stories, placing one defect first and another third.

![Sprint planning capacity line below two bugs and one user story](../../wiki-assets/gal-zellermayer-0-bugs-policy/sprint-capacity-cutoff.jpg)

The first capacity line initially includes both defects and one feature.

![Critical stop-application story moved above a Safari help-page bug](../../wiki-assets/gal-zellermayer-0-bugs-policy/critical-feature-reprioritization.jpg)

A critical proof-of-concept feature then moves ahead of the Safari defect, pushing that defect below capacity.

![Three feature stories committed while two bugs fall below sprint capacity](../../wiki-assets/gal-zellermayer-0-bugs-policy/bugs-pushed-below-features.jpg)

Further reprioritization leaves three feature stories committed while both defects sit below the line.

![Next sprint backlog with new features ahead of three accumulated bugs](../../wiki-assets/gal-zellermayer-0-bugs-policy/next-sprint-bug-accumulation.jpg)

The following sprint adds a third defect while new feature work again ranks above the older bugs, illustrating the claimed accumulation loop.

## Key Quotes
> “whenever you encounter a new bug, you should either fix that bug, or close it as ‘won't fix’” — the policy's decision rule.

> “If you don't fix it right now, chances are that you never will.” — the author's argument against deferral.

## Connections
- [[GalZellermayer]] - author drawing on five years across several Scrum teams and VMware Israel colleagues.
- [[ZeroBugsPolicy]] - fix-or-close defect-management rule developed in the article.
- [[AgileSoftwareDevelopment]] - definition-of-done and sprint context for the policy.
- [[InternalSoftwareQuality]] - prompt defect resolution and lifecycle repair cost connect the policy to practical quality.
- [[VMware]] - author's management context and organizational setting named in the article.
- [[JoelSpolsky]] - author of “Software Inventory,” cited as an influence.

## Contradictions
- Qualifies feature-and-defect backlog management by arguing that product pressure systematically displaces defects, but this is a single practitioner's experience rather than comparative evidence that mixed backlogs always fail.
- Qualifies any interpretation of zero bugs as zero known defects: low-value defects may be closed unresolved, so the policy targets zero open bug inventory rather than defect-free software.
- Formal traceability, safety, security, regulatory, contractual, and risk-management contexts may require recording accepted defects even when immediate repair is uneconomic; the article does not address those cases.

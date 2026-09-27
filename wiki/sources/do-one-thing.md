---
title: "Do one thing"
type: source
tags: [software-design, single-responsibility, refactoring]
date: 2018-04-28
source_file: /mnt/ken_personal_wiki/Articles/Do one thing.md
---

## Summary
[[NedBatchelder]] argues that the [[SingleResponsibilityPrinciple]] is useful but cannot supply an objective test for what counts as one responsibility. His [[Zellij]] refactoring shows how a class can look cohesive at one stage and later yield a smaller, more reusable abstraction as surrounding needs and understanding change. The appended discussion offers stakeholder, change, coherence, and interface-boundary interpretations without eliminating the need for judgment; all 11 image references resolve to eight decorative comment-author avatars and were omitted.

## Key Claims
- “Do one thing” is an interpretive design heuristic because the boundaries of both the unit and its responsibility can be described at different levels of abstraction.
- Apparently authoritative examples can hide the ambiguity by calling several operations one responsibility without explaining the grouping criterion.
- A design can reasonably satisfy the principle at one point and later be improved when new reuse needs reveal a better boundary.
- In Zellij, extracting fuzzy point matching from `PointMap` into `Defuzzer` made the capability independently reusable and let a standard dictionary replace custom map behavior.
- Stakeholders or reasons to change can help identify boundaries, but the comments show that these formulations remain ambiguous when one stakeholder can request multiple independent changes.
- Presenting a judgment-dependent principle as a binary rule can mislead learners and encourage fragmentation without clearer code.

## Key Quotes
> “It's a guideline that can be interpreted and applied differently by different people.” - Batchelder on the principle's subjectivity.

> “Programming is hard. Principles and guidelines help” - the article's case for teaching judgment alongside rules.

## Connections
- [[NedBatchelder]] - author and Zellij developer reflecting on how his own design boundary changed.
- [[SingleResponsibilityPrinciple]] - central guideline whose value and ambiguity the article examines.
- [[FunctionDesign]] - function-level “do one thing” advice is useful only with an explicit judgment boundary.
- [[Zellij]] - project in which the `PointMap` to `Defuzzer` refactoring supplies the concrete case.
- [[InternalSoftwareQuality]] - refactoring toward a smaller reusable abstraction can improve changeability, but no universal decomposition test follows.

## Contradictions
- Qualifies [[bob-belderbos-10-tips-to-write-better-functions-in-python]]: “do one thing” remains a useful default, but this source rejects treating it as a precise or binary function-design rule.
- Commenters propose one stakeholder, one reason to change, and a clear coherent unit as better tests, but the thread does not converge on an objective definition or supply comparative evidence.

---
title: "How I Review Code"
type: source
tags: [software-engineering, code-review, pull-requests, teamwork]
date: 2018-01-24
source_file: "/mnt/ken_personal_wiki/Articles/cyle — How I review code.md"
---

## Summary
[[Cyle]] describes [[Tumblr]] code review as a human communication and shared-understanding practice for a large, mature codebase. Reviewers should adapt help to the author, demand enough context for future readers, prefer clear and documented code, keep pull requests scoped, respond promptly through the full revision loop, and write with empathy. The source's only image is a decorative avatar and contributes no separate evidence.

## Key Claims
- [[CodeReviewPractice]] should help current authors and future readers understand what changed, why it changed, and how it works.
- Review depth and explanation should reflect the author's experience with the codebase: junior engineers may need examples and references, while experienced engineers may need reminders to document clever abstractions.
- Automated style enforcement lets human reviewers focus more attention on motivation, clarity, documentation, scope, and maintainability.
- [[PRReviewHygiene]] improves when teams use small changes, explicitly identify deferred work, review promptly, and follow revisions through to completion.
- Review archives support [[WorkplaceLearning]] because engineers can study earlier feedback and recover the reasoning behind old changes.
- Humane review means giving authors the benefit of the doubt, making suggestions kindly, and avoiding jokes or language that future readers could misinterpret.

## Key Quotes
> "clear rather than clever" - on preferring maintainable code over compressed ingenuity.

> "remember to be a human" - on treating authors with patience and respect.

## Connections
- [[Cyle]] - author reflecting on a reported average of 25 pull-request reviews per week.
- [[Tumblr]] - engineering context for the multilingual, long-lived shared codebase and review workflow.
- [[CodeReviewPractice]] - central practice of preserving clarity, rationale, shared ownership, and respectful feedback.
- [[PRReviewHygiene]] - small changes, prompt response, ticketed deferral, and revision follow-up keep review moving.
- [[WorkplaceLearning]] - visible review history teaches codebase details and preserves decision context.
- [[GitHub]] - pull-request interface used by Tumblr through an internal instance in the source.

## Contradictions
- Qualifies review models centered on manual style or syntax enforcement: Tumblr automated those checks and used human attention for context, clarity, documentation, scope, and collaboration.
- Qualifies any universal demand that a pull request be fully complete: the source accepts foundation changes and ticket-linked deferred work when scope is explicit and later work remains traceable.

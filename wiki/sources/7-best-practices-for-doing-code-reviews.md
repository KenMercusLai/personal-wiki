---
title: "7 Ways to Uplevel Your Code Review Skills"
type: source
tags: [software-engineering, code-review]
date: 2016-12-20
source_file: /mnt/ken_personal_wiki/Articles/7 best practices for doing code reviews.md
---

## Summary
This Asana engineering article treats [[CodeReviewPractice]] as a team learning and feedback habit rather than a generic bug-catching ritual. It argues that teams should agree on review goals, run the changed app, use development-environment context, visualize call relationships, review promptly, predict the expected change shape before reading the diff, and avoid blocking approval unless there is a demonstrable bug.

## Key Claims
- Teams get more value from [[CodeReviewPractice]] when they explicitly agree whether reviews are for shared understanding, knowledge spread, bug discovery, or style enforcement.
- [[SoftwareVerification]] should carry much of the bug-finding load because running the app, tests, breakpoints, and realistic local tooling reveal behavior better than reading diffs alone.
- Code review can support [[WorkplaceLearning]] when reviewers predict files, visualize call hierarchies, quiz themselves, and learn how coworkers think about the codebase.
- Prompt first-pass reviews and clear next-step communication reduce teammate blocking and preserve trust.
- Reviewers should usually approve when requested changes are simple style or refactoring suggestions and no bug is proven, because extra review rounds can discourage small cleanup changes.

## Key Quotes
> "No one should ever be alone on a team." - on code review as knowledge sharing.

> "The computer is much better at running code than your head is." - on execution-backed review.

> "Always give approval, unless you can prove that there is a bug" - on avoiding unnecessary reviewer blocking.

## Connections
- [[Asana]] - publisher and engineering-team context for the article.
- [[CodeReviewPractice]] - central subject of the article.
- [[PRReviewHygiene]] - related through reviewer-facing workflow, timely feedback, and avoiding avoidable blocking.
- [[SoftwareVerification]] - tests, running the app, breakpoints, compile errors, warnings, and failures are treated as better bug-finding tools than diff reading alone.
- [[WorkplaceLearning]] - reviewers learn the codebase and coworkers' reasoning by predicting changes, visualizing call relationships, and testing their memory.
- [[HumanCodeResponsibility]] - reviewers should communicate approval limits and next steps clearly when they are not qualified to approve.

## Contradictions
- Partly qualifies [[PRReviewHygiene]] and [[SoftwareVerification]]: the article de-emphasizes code review as a primary bug-finding or style-enforcement mechanism, while still treating review as valuable for team knowledge, feedback, and local behavior checks.

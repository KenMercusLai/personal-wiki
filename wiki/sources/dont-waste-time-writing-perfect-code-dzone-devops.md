---
title: "Don't Waste Time Writing Perfect Code"
type: source
tags: [software-development, code-quality, refactoring, code-review]
date: 2014-11-05
source_file: "/mnt/ken_personal_wiki/Articles/Don't Waste Time Writing Perfect Code - DZone DevOps.md"
---

## Summary
[[JimBird]] argues that software quality should be judged by practical fitness rather than aesthetic perfection. Because code changes unevenly and may be replaced quickly, teams should preserve a baseline of correctness, understandability, safety, security, and debuggability while directing refactoring, review, and test effort toward the changes and risks that matter most.

## Key Claims
- Code lifetimes and change frequencies are uneven: much code is written once, while a small and important portion is repeatedly changed or rewritten.
- [[InternalSoftwareQuality]] should protect correctness, understandability, error handling, security, debuggability, and safe change rather than pursue subjective elegance for its own sake.
- Code that rarely changes still needs to be correct and readable, but speculative polishing and refactoring may have little return until a real change is required.
- Rapidly changing code also should not be perfected prematurely because learning may soon replace the current design.
- [[IterativeRefinement]] is most useful when it is opportunistic or preparatory: refactor enough to understand, clean up, or make the next change safer, then stop.
- [[CodeReviewPractice]] should prioritize correctness, defensive behavior, security, comprehension, and change safety while leaving formatting to tools and treating style as material only when it obstructs understanding.
- Tests should maximize confidence and useful information for important paths and exception cases rather than conform to one universal size or test-first sequence.

## Key Quotes
> "Code can always be better. But that’s not important." - on separating possible improvement from valuable improvement.

> "Do what needs to be done, and no more." - on proportionate engineering effort.

## Connections
- [[JimBird]] - author advocating practical, risk-sensitive software quality.
- [[DZone]] - publication venue for the captured article.
- [[InternalSoftwareQuality]] - quality is defined through operational and maintenance outcomes rather than perfection.
- [[IterativeRefinement]] - refinement should be bounded by the next useful change and a deliberate stopping rule.
- [[CodeReviewPractice]] - review attention should follow correctness, safety, security, and understandability.
- [[MartinFowler]] - cited for opportunistic and preparatory refactoring terminology.
- [[SoftwareVerification]] - important paths, exception cases, and failure behavior require confidence-producing tests.

## Contradictions
- Qualifies broad claims that more internal polish always reduces cost: the source argues that marginal refinement has uneven value when code is stable, temporary, or likely to be replaced.
- Qualifies open-ended [[IterativeRefinement]] by making practical need, risk, and the next intended change part of the stopping rule.

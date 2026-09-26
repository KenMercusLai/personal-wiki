---
title: "10 Tips To Write Better Functions In Python"
type: source
tags: [python, functions, code-quality]
date: 2022-01-19
source_file: /mnt/ken_personal_wiki/Articles/Bob Belderbos - 10 Tips To Write Better Functions In Python.md
---

## Summary
[[BobBelderbos]] argues that functions are Python's primary modularity unit and that better functions come from clear naming, narrow responsibility, small interfaces, early validation, close variable placement, argument discipline, type hints, consistent returns, purity, and safe defaults. The article connects function design to [[InternalSoftwareQuality]] because small, readable, testable functions make code easier to reason about, reuse, and maintain. The source has no image references to inspect.

## Key Claims
- [[FunctionDesign]] improves when names describe behavior without encoding incidental type details.
- Functions should usually do one thing, keep interfaces small, validate inputs early, and avoid excessive nesting.
- Python function APIs can become clearer through keyword-only or positional-only arguments, type hints, and consistent return types.
- Avoiding global mutation and mutable default arguments reduces hidden state and surprising cross-call behavior.
- Better functions support [[SoftwareVerification]] by making behavior easier to isolate and test.

## Key Quotes
> "Every function name is an opportunity to self document your code." - naming guidance.

> "Flat is better than nested" - Zen of Python principle used to motivate early validation.

## Connections
- [[BobBelderbos]] - author of the article.
- [[PyBites]] - publication and coaching context for the article.
- [[Python]] - programming language context for the function-design advice.
- [[FunctionDesign]] - main programming practice covered by the article.
- [[InternalSoftwareQuality]] - function structure is framed as a way to improve readability, reuse, testability, and maintenance.
- [[SoftwareVerification]] - small, isolated functions are easier to test.

## Contradictions
- No direct contradictions found. The article is practical guidance rather than an empirical study, so line-count and design-rule claims should be treated as heuristics.

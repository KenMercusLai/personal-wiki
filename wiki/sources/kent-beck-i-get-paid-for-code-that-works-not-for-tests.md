---
title: "Kent Beck: I get paid for code that works, not for tests"
type: source
tags: [software-testing, tdd, test-coverage, software-quality]
date: 2013-09-17
source_file: "/mnt/ken_personal_wiki/Articles/Kent Beck - “I get paid for code that works, not for tests” – Another blog lost in the interweb….md"
---

## Summary
This saved blog-and-comments thread centers on [[KentBeck]]'s proposal to write the least testing needed for a chosen level of confidence, concentrating effort on mistakes an individual or team is likely to make. The discussion develops [[ConfidenceBasedTesting]] through competing concerns about maintenance, test cost, coverage targets, integration and smoke testing, static types, and customer outcomes, but supplies practitioner opinions rather than comparative evidence for one universal test mix.

## Key Claims
- [[KentBeck]] frames test selection as a confidence decision: test recurring individual or team error patterns more heavily and experiment because no universal theory yet identifies every worthwhile test.
- Raw test quantity and fixed coverage targets can reward low-information tests without proving software quality or customer value.
- Tests have implementation, execution, diagnosis, and maintenance costs, so their value depends on the risk they cover and the confidence they add.
- One commenter argues that this mistake-focused strategy can undervalue regression protection and long-term maintainability, especially in enduring multi-developer or open-source systems.
- Other commenters propose smoke tests, integration tests, and strong static types as ways to replace some low-value unit checks, but provide no comparative results establishing when those substitutions preserve confidence.
- The thread's durable question is why a test is needed, not merely how to write it or how many tests a suite contains.

## Key Quotes
> "test as little as possible to reach a given level of confidence" - Beck's allocation rule.

> "We should ask WHY before writing a test case" - a comment rejecting test production as an end in itself.

## Connections
- [[KentBeck]] - supplies the central confidence-based testing philosophy quoted by the article.
- [[ConfidenceBasedTesting]] - testing strategy synthesized from the thread's risk, confidence, cost, and maintenance debate.
- [[SoftwareVerification]] - broader practice to which selective automated tests, static checks, and smoke or integration tests contribute.
- [[TestPyramid]] - related test-portfolio strategy; the thread contains an opposing preference for fewer unit tests and more smoke or integration testing.
- [[InternalSoftwareQuality]] - maintainability and regression protection qualify any attempt to minimize testing effort.
- [[ExtremeProgramming]] - Beck's wider practice context, although the thread does not explain XP as a system.

## Contradictions
- The preference expressed by one commenter for replacing many unit tests with smoke or integration tests conflicts with [[TestPyramid]]'s general preference for broad fast unit coverage and fewer higher-level tests. Neither source supplies comparative outcome evidence sufficient to settle the appropriate mix across systems.
- The critique that Beck's rule mainly suits short-lived, small-team work is in tension with Beck's explicit statement that team error patterns should change the strategy. The thread does not resolve whether that adaptation adequately covers long-term regression and maintainer turnover.

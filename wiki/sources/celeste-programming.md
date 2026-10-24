---
title: "游戏《蔚蓝山》教我的编程道理"
type: source
tags: [software-engineering, testing, feedback-loops, game-design]
date: 2020-02-23
source_file: "/mnt/ken_personal_wiki/Articles/celeste-programming.md"
---

## Summary
[[Piglei]] uses [[Celeste]]'s frequent deaths and near-immediate room-level restart to explain why iteration cost matters in programming. The article contrasts a browser-driven permissions workflow that takes more than 30 seconds per attempt with focused automated tests that exercise role behavior in under a second, arguing that [[SoftwareVerification]] improves development not only by catching regressions but by making experimentation fluid. Its Django example also reframes DRY as avoiding repeated manual verification, while remaining a practitioner analogy rather than comparative evidence about defect rates or total test-maintenance cost.

![Madeline stands beside a waterfall in Celeste's pixel-art mountain environment](../../wiki-assets/celeste-programming/celeste-gameplay.jpg)

## Key Claims
- [[DeveloperFeedbackLoop]] quality depends partly on the time and effort between a change, behavioral evidence, and the next attempt.
- [[Celeste]] lowers failure cost by restarting Madeline at the current room entrance in roughly three seconds, allowing repeated adjustment without replaying the whole chapter.

![Celeste room attempt ends on spikes and restarts at the room entrance in about three seconds](../../wiki-assets/celeste-programming/fast-room-retry.gif)

- Manual browser checks make permission work expensive when every code change requires a server reload, navigation, setup, and repeated checks across roles and endpoints.
- Focused automated tests can exercise permitted and forbidden API behavior directly, turning a 60-case role-and-feature matrix from repeated human interaction into a repeatable suite.
- [[SoftwareVerification]] supports learning during implementation: fast failures make it easier to adjust code immediately, while the saved suite also protects later refactoring.
- Test automation extends the DRY principle from repeated code to repeated checking, although some exploratory, integration, usability, and production-dependent behavior still requires other forms of verification.

## Key Quotes
> “写代码，其实就是一个在不断重复 ‘开发’ - ‘试错’ - ‘修改’ 的过程” - on programming as an iterative feedback process.

> “不要重复手工测试已经测过的东西” - on treating repeatable manual checks as candidates for automation.

> “失败后就马上重试” - on the felt benefit of a short test loop.

## Connections
- [[Piglei]] - author who draws the programming lesson from Celeste's retry design.
- [[Celeste]] - game whose room-level respawn supplies the central low-cost-failure analogy.
- [[DeveloperFeedbackLoop]] - central concept linking change latency, behavioral evidence, and retry cost.
- [[SoftwareVerification]] - automated API tests replace repeated browser interaction and preserve regression coverage.
- [[TestPyramid]] - focused lower-level tests usually give faster and more localized feedback than repeated UI checks.
- [[ContinuousDelivery]] - extends short feedback from local development into integration and release flow.

## Contradictions
- No direct contradiction was found. The article complements [[TestPyramid]] and [[SoftwareVerification]] by emphasizing feedback latency and developer experience rather than proposing a complete testing strategy.
- The numerical comparison is illustrative and source-specific: the article reports one manual loop taking more than 30 seconds, one five-test run taking 0.72 seconds, and a hypothetical 60-check matrix taking 20 minutes. It supplies no controlled defect, maintenance, flakiness, or long-run productivity study.

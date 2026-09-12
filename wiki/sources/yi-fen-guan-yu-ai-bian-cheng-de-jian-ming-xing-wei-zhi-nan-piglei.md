---
title: "一份关于 AI 编程的简明行为指南 | Piglei"
type: source
tags: [ai, software-engineering, coding-practice]
date: 2026-04-17
source_file: /mnt/ken_personal_wiki/Articles/一份关于 AI 编程的简明行为指南 Piglei.md
---

## Summary
Piglei presents a team-oriented guide for practicing [[AICodingPractice]] with AI coding agents. The article argues that engineers remain responsible for code quality, maintainability, reviewability, and verification even when an agent generates much of the implementation. It also gives junior engineers a stricter learning-oriented stance: use agents as collaborators, not as unsupervised substitutes for debugging, design thinking, documentation reading, or architectural growth.

## Key Claims
- [[HumanCodeResponsibility]] remains central because AI agents expand developer capability but do not own code quality, maintenance, or production risk.
- [[AIAgentCollaboration]] is preferable to pure delegation: engineers should explore design, implementation structure, and tradeoffs with the agent instead of only requesting outputs.
- [[PRReviewHygiene]] matters more when AI makes large code changes easy; small PRs, design notes for large changes, and pre-PR AI review help preserve review quality.
- [[SoftwareVerification]] must accompany AI-generated code through automated tests, self-checks, and verification-fix loops.
- [[JuniorEngineerLearning]] can suffer when junior engineers outsource too much; slower manual debugging, prior thinking, official documentation, and architecture study may be better long-term investments.

## Key Quotes
> "AI Agent 拓展了人的能力，是一种“分身”" - on agents as capability extensions, not accountable authors.

> "多把 Agent 作为协作者来共同工作" - on collaboration as the preferred working model.

> "正确的判断无价" - on why human understanding remains decisive.

## Connections
- [[Piglei]] - author/source site for the AI coding behavior guide.
- [[AICodingPractice]] - central subject of the article.
- [[HumanCodeResponsibility]] - the article's strongest repeated warning.
- [[AIAgentCollaboration]] - primary recommended mental model for working with coding agents.
- [[PRReviewHygiene]] - practical workflow advice for AI-heavy code changes.
- [[SoftwareVerification]] - the article insists that AI-generated code should be tested and self-verified.
- [[JuniorEngineerLearning]] - the article gives special guidance for early-career engineers.
- [[FeynmanTechnique]] - used as a test for whether engineers truly understand generated code or a requirement.

## Contradictions
- No direct contradictions with existing wiki content. This source qualifies the wiki's optimistic AI-tooling material by emphasizing accountability, maintainability, verification, and learning cost.

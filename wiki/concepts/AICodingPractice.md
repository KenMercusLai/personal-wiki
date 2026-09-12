---
title: "AI Coding Practice"
type: concept
tags: [ai, software-engineering, developer-tools]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AICodingPractice]] is the set of engineering behaviors, team norms, and review habits used when software developers work with AI coding agents.

## Current Synthesis
The source frames AI coding practice as a sociotechnical discipline rather than a prompt library. Coding agents can increase implementation speed and expand what one engineer can attempt, but the useful practice pattern is bounded by human responsibility: understand generated code, shape the design, control review size, prefer stable libraries for mature problems, verify behavior, and keep learning rather than merely accepting outputs.

## Key Claims
- AI coding practice requires shared team expectations because inconsistent agent-use habits can create collaboration friction.
- Engineers remain responsible for generated code, maintainability, and final judgment.
- Collaboration with agents should include design exploration and implementation reasoning, not only natural-language task assignment.
- Fast AI output increases the need for small PRs, review aids, and pre-PR self-review.
- Verification through tests and self-checks is part of the workflow, not a later review responsibility.
- Junior engineers need AI practices that protect learning quality rather than optimize only for speed.

## Evidence
- Team norm: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] warns that teammates without shared assumptions about AI coding can create project friction.
- Responsibility: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says engineers should review, understand, and own AI-generated code.
- Collaboration: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] contrasts collaboration with delegation and urges engineers to explore design and structure with agents.
- Reviewability: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends controlling PR size and adding design notes when a large PR cannot be split.
- Verification: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests, self-testing, and agent-verifiable loops.
- Learning stage: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] gives junior engineers stricter advice on debugging, independent design, documentation, and architecture learning.

## Counterevidence & Qualifications
The article is a practitioner guide grounded in the author's work environment, not a controlled comparison of AI coding workflows. Its advice may need adaptation for teams with different risk tolerance, review culture, deadlines, tooling, or regulatory constraints.

## What Changed
- Created the concept page for AI coding practice as a human-centered engineering workflow around coding agents.

## Related Concepts
- [[HumanCodeResponsibility]] - accountability is the foundation of the article's practice model.
- [[AIAgentCollaboration]] - collaboration is the recommended interaction pattern within AI coding practice.
- [[PRReviewHygiene]] - reviewability becomes a central operational control for AI-heavy changes.
- [[SoftwareVerification]] - tests and self-checks are required to make agent output trustworthy.
- [[JuniorEngineerLearning]] - junior engineers need AI practices that protect skill formation.
- [[AIApplicationFramework]] - both concern AI developer tooling, but this page focuses on behavior around coding agents rather than application frameworks.

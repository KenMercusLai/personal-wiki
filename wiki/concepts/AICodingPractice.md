---
title: "AI Coding Practice"
type: concept
tags: [ai, software-engineering, developer-tools]
sources:
  - yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei
  - wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo
  - yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Definition
[[AICodingPractice]] is the set of engineering behaviors, team norms, and review habits used when software developers work with AI coding agents.

## Current Synthesis
The sources frame AI coding practice as a sociotechnical discipline rather than a prompt library. Piglei emphasizes the individual and team practice layer: understand generated code, shape the design, control review size, prefer stable libraries for mature problems, verify behavior, and protect learning. The AI-first source expands the frame to organization-level workflow design: agents become useful at production speed only when surrounded by tests, CI/CD, monitoring, task management, architecture, feature flags, and human strategic review. Onevcat adds a practitioner workflow view from intensive [[ClaudeCode]] use: fast [[VibeCoding]] works best when tasks are planned or prototyped deliberately, kept small enough to understand, verified continuously, and paced so the tool does not dictate the human tempo.

## Key Claims
- AI coding practice requires shared team expectations because inconsistent agent-use habits can create collaboration friction.
- Engineers remain responsible for generated code, maintainability, and final judgment.
- Collaboration with agents should include design exploration and implementation reasoning, not only natural-language task assignment.
- Fast AI output increases the need for small PRs, review aids, and pre-PR self-review.
- Verification through tests and self-checks is part of the workflow, not a later review responsibility.
- Junior engineers and intensive coding-agent users need practices that protect learning, human pace, and task control rather than optimize only for speed.
- AI-first coding practice depends on engineering systems that let agent output be checked, shipped, observed, and rolled back quickly.

## Evidence
- Team norm: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] warns that teammates without shared assumptions about AI coding can create project friction.
- Responsibility: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] says engineers should review, understand, and own AI-generated code.
- Collaboration: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] contrasts collaboration with delegation and urges engineers to explore design and structure with agents.
- Reviewability: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends controlling PR size and adding design notes when a large PR cannot be split.
- Verification: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] recommends automated tests, self-testing, and agent-verifiable loops.
- Learning stage: [[yi-fen-guan-yu-ai-bian-cheng-de-jian-ming-xing-wei-zhi-nan-piglei]] gives junior engineers stricter advice on debugging, independent design, documentation, and architecture learning.
- Production harness: [[wei-shen-me-ni-de-ai-you-xian-zhan-lue-ke-neng-da-cuo-te-cuo]] argues that AI coding speed only helps when automated tests, CI/CD, feature flags, monitoring, task decomposition, and architecture are already strong.
- Task boundary and pace: [[yi-ge-ban-yue-gao-qiang-du-claude-code-shi-yong-hou-gan-shou]] recommends small iterations, version-control safety, modular work, and remembering that faster tools still need human thinking time and life space.

## Counterevidence & Qualifications
The sources are practitioner essays rather than controlled comparisons of AI coding workflows. They also pull in different directions: Piglei stresses collaboration, understanding, and learning protection; the AI-first case study stresses automation, role redesign, and removing human bottlenecks; Onevcat stresses direct tool experience, small steps, context limits, and humane pacing. The right practice depends on codebase risk, UI complexity, product expectations, safety requirements, team maturity, model/tool quality, and the strength of the surrounding verification harness.

## What Changed
- Added the AI-first source's organization-level workflow view while preserving Piglei's responsibility, reviewability, and learning constraints.
- Added the Claude Code source's practitioner emphasis on small iterations, context-aware task boundaries, and human pace.

## Related Concepts
- [[HumanCodeResponsibility]] - accountability is the foundation of the article's practice model.
- [[AIAgentCollaboration]] - collaboration is the recommended interaction pattern within AI coding practice.
- [[PRReviewHygiene]] - reviewability becomes a central operational control for AI-heavy changes.
- [[SoftwareVerification]] - tests and self-checks are required to make agent output trustworthy.
- [[JuniorEngineerLearning]] - junior engineers need AI practices that protect skill formation.
- [[AIFirstEngineering]] - expands AI coding practice into a company operating model.
- [[HarnessEngineering]] - supplies the tests, constraints, and feedback loops that make agent output usable.
- [[AIApplicationFramework]] - both concern AI developer tooling, but this page focuses on behavior around coding agents rather than application frameworks.
- [[VibeCoding]] - names the speed-amplified workflow where these practices become especially important.

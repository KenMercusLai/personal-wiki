---
title: "Don't fall into the anti-AI hype"
type: source
tags: [ai, programming, career]
date: 2026-01-11
source_file: "/mnt/ken_personal_wiki/Articles/Blog - antirez - Don't fall into the anti-AI hype.md"
---

## Summary
[[Antirez]] argues that programmers should not let dislike of AI hype, corporate behavior, or economic anxiety obscure the practical fact that LLMs are rapidly changing software work. The essay treats AI coding as a shift from line-by-line implementation toward problem framing, specification, review, and tool-guided building, while still warning about centralization and job loss. It is optimistic about small-team leverage and open-source renewal, but politically concerned about workers displaced by automation.

## Key Claims
- State-of-the-art LLMs can already complete large subtasks or medium projects with limited human guidance, especially when the work is isolated and textually representable.
- [[AICodingPractice]] is shifting from writing every line to deciding what to build, representing the problem clearly, prompting, inspecting, and guiding generated work.
- Concrete [[ClaudeCode]] examples include adding UTF-8 and terminal-cell tests to linenoise, debugging Redis test flakes, generating a pure C BERT-like embedding inference library, and reproducing Redis Streams internal changes from a design document.
- [[PracticalLLMUse]] should not be dismissed because of AI-company economics, off-putting executives, or anti-hype identity; programmers should test tools seriously over weeks and revisit them periodically.
- AI coding may democratize software creation like open source did, giving small teams more leverage, but centralization of frontier AI capability remains a serious risk.
- Job displacement and non-programming automation need political responses, including support for people who lose work, rather than denial that innovation is happening.
- The motivating core of programming can remain building, even if the fun moves away from hand-writing every line.

## Key Quotes
> "facts are facts, and AI is going to change programming forever." - on separating preferences from observed capability.

> "Writing code is no longer needed for the most part." - on the author's strongest programming-work claim.

> "Skipping AI is not going to help you or your career." - on the author's practical advice to programmers.

## Connections
- [[Antirez]] - author of the essay and Redis creator writing from a systems-programming perspective.
- [[AICodingPractice]] - central practice shift from manual coding toward problem framing, prompting, inspection, and guidance.
- [[ClaudeCode]] - tool used in the author's concrete coding examples.
- [[Redis]] - project context for test-failure debugging and Redis Streams internal-change reproduction.
- [[PracticalLLMUse]] - the essay provides a strongly optimistic practitioner case for bounded but powerful LLM use.
- [[HumanCodeResponsibility]] - the examples still depend on human inspection, design documents, and authorization of tool actions.
- [[AIDependencySkillAtrophy]] - the essay partially tensions manual-craft preservation by arguing that writing code oneself is increasingly optional unless done for fun.

## Contradictions
- Partly tensions [[AIDependencySkillAtrophy]] and manual-coding arguments: Spati warns that AI substitution can erode craft and thinking, while Antirez argues programmers should accept that much code no longer needs to be written manually and redirect effort toward building.

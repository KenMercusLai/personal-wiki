---
title: "Thoughts on slowing the fuck down"
type: source
tags: [ai, software-engineering, coding-agents, code-quality]
date: 2026-03-25
source_file: "/mnt/ken_personal_wiki/Articles/Thoughts on slowing the fuck down.md"
---

## Summary
[[MarioZechner]] argues that coding-agent output can exceed a team's capacity to understand, review, and maintain it, allowing small local errors and unnecessary abstractions to compound into brittle production systems. He recommends using agents for bounded, verifiable, non-critical, or exploratory work while humans retain architecture, API, product-scope, and final quality decisions. The essay links [[BottleneckAwareAICoding]], [[HumanCodeResponsibility]], and [[AgenticCodeSearchRecall]]: deliberate friction can preserve learning and system understanding, while unchecked codebase growth makes later agent retrieval less complete and further increases duplication and inconsistency.

## Key Claims
- Coding-agent speed is not evidence of production quality; unreviewed output can accumulate defects, code smells, redundant features, and architectural inconsistency faster than people can notice or repair them.
- Humans provide a natural throughput and pain-feedback bottleneck: limited implementation and review capacity slows error accumulation and exposes maintainability costs before they become systemic.
- Agent instructions and memory can reduce repeated known mistakes only after someone observes and records them; they do not remove the need for human inspection and learning.
- Local agent decisions compound into global complexity because separate runs lack complete codebase and decision history, encouraging duplication and cargo-cult abstraction.
- [[AgenticCodeSearchRecall]] tends to decline as a codebase grows, regardless of whether the agent uses grep, indexes, language servers, or vector retrieval, so relevant reuse and change sites can be missed.
- Good agent tasks are bounded, independently evaluable, and low-consequence, with a human as the final quality gate; narrow optimization functions do not capture omitted dimensions such as maintainability or correctness.
- Architecture, APIs, and other system-defining decisions benefit from deliberate human involvement, paced generation, and enough friction to preserve understanding, taste, learning, and the ability to recover from failures.

## Key Quotes
> "Set yourself limits on how much code you let the clanker generate per day, in line with your ability to actually review the code." - on matching generated output to human review capacity.

> "Anything that defines the gestalt of your system, that is architecture, API, and so on, write it by hand." - on retaining human control of system-defining decisions.

## Connections
- [[MarioZechner]] - author presenting a production-oriented critique of high-autonomy agent coding.
- [[AICodingPractice]] - recommends bounded tasks, closed evaluation loops, paced generation, and human final review.
- [[BottleneckAwareAICoding]] - treats human comprehension and review capacity as necessary constraints rather than inefficiencies to eliminate.
- [[HumanCodeResponsibility]] - keeps people responsible for architecture, acceptance, maintainability, and recovery.
- [[AgenticCodeSearchRecall]] - names incomplete discovery of relevant and reusable code as a mechanism behind duplication and inconsistent change.
- [[InternalSoftwareQuality]] - unchecked local mistakes and abstractions can erode changeability and trust in both code and tests.
- [[SoftwareVerification]] - narrow automated evaluation is useful but cannot establish qualities omitted from its objective.
- [[AIDependencySkillAtrophy]] - deliberate friction and hands-on implementation preserve learning, taste, and system understanding.

## Contradictions
- The essay tensions high-autonomy and parallel-agent accounts such as [[hu-yuan-ming-wo-gei-10-ge-claude-code-da-gong]] by arguing that removing human review and implementation bottlenecks can hide rather than eliminate downstream quality work.
- It qualifies [[control-the-ideas-not-the-code]] and [[ye-tian-zhi-shu-121-when-code-is-cheap]]: design and behavioral control can sometimes replace exhaustive line review, but Zechner argues that people must remain close enough to the implementation to understand the system and detect compounding local errors.
- The reliability decline, company anecdotes, and claims about agent search recall are practitioner observations rather than controlled measurements. The source gives no defect rates, codebase-size thresholds, comparative retrieval evaluation, or longitudinal maintenance data.
- The sole remote image was opened and omitted as a decorative tortoise-and-hare illustration without independent evidence.

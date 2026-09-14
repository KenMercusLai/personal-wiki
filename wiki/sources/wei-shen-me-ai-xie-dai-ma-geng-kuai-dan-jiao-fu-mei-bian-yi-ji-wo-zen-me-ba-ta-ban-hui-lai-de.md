---
title: "为什么 AI 写代码更快但交付没变，以及我怎么把它扳回来的"
type: source
tags: [ai, software-engineering, ai-coding, workflow]
date: 2026-03-03
source_file: /mnt/ken_personal_wiki/Articles/为什么 AI 写代码更快但交付没变，以及我怎么把它扳回来的.md
---

## Summary
This article argues that AI coding often improves local code-production speed without improving delivery because the bottleneck has moved to requirements, review, verification, context management, and organizational flow. It connects [[BottleneckAwareAICoding]] with [[AICodingPractice]], [[SpecDrivenAgentDevelopment]], [[LLMToolingSkills]], [[SoftwareVerification]], and [[CodeReviewPractice]]: specs make implicit design thinking explicit, skills should be loaded on demand, verification creates an "andon" stop loop, and parallel agent work only helps when WIP and review queues stay bounded.

## Key Claims
- [[BottleneckAwareAICoding]] explains the AI coding delivery paradox: speeding a non-bottleneck coding step can inflate PR size, review time, WIP, and rework without improving organizational throughput.
- AI coding frameworks such as OpenSpec, Superpowers, BMAD, and Spec Kit mostly converge on reusable workflow skills for exploration, design, implementation, and verification, so teams should understand the underlying workflow rather than chase framework novelty.
- [[SpecDrivenAgentDevelopment]] works because specs preserve current business state, compatibility constraints, expected behavior, invariants, and edge cases as reusable files instead of leaving plan-mode reasoning trapped inside one conversation.
- [[LLMToolingSkills]] should be distinguished from rules and specs by loading mechanism: rules are short always-on constraints, specs are business-state inputs, and skills are on-demand workflows with SOPs, examples, and optional scripts.
- [[SoftwareVerification]] is the trust boundary for AI-generated code: lint, unit tests, E2E tests, logs, review, and QA act as layered "andon" and Swiss-cheese defenses that stop bad output before it travels downstream.
- Parallel AI sessions can improve total throughput even when a single task is slower under full SDLC discipline, but only if verification makes unattended work judgeable and WIP limits prevent review queues from exploding.
- AI's highest leverage is not doing the same coding work faster; it is using automation to remove repetitive toil and invest human attention in higher-order capability building such as broad report analysis, architecture judgment, and learning.

## Key Quotes
> "AI 就是今天的 NCX-10。" - on non-bottleneck acceleration creating downstream accumulation.

> "区别不在语义标签，在加载机制。" - on why Spec, Rule, and Skill are different.

> "你不需要更聪明的 AI，你需要一根能让它自己停下来的绳子。" - on verification as an andon loop.

> "洗衣机洗衣服，你去读书。" - on turning automation gains into capability growth rather than more throughput pressure.

## Connections
- [[BottleneckAwareAICoding]] - central throughput model linking AI coding speed to SDLC bottlenecks, review queues, WIP, and parallelism.
- [[AICodingPractice]] - the article turns AI coding practice into a full-SDLC discipline rather than a prompt or tool choice.
- [[SpecDrivenAgentDevelopment]] - specs are presented as lightweight persistent design context for existing systems, compatibility analysis, and edge cases.
- [[LLMToolingSkills]] - the article defines skills as on-demand workflow bundles distinct from always-loaded rules and business-state specs.
- [[SoftwareVerification]] - lint, tests, E2E, logs, QA, review, and automated fix loops are the article's trust machinery.
- [[CodeReviewPractice]] - the article treats PR size and reviewer bandwidth as the practical downstream bottleneck exposed by AI coding.
- [[AgenticWorkflowPatterns]] - parallel agent work, multi-agent report analysis, and generate-verify-fix loops appear as reusable workflow patterns.
- [[AIDependencySkillAtrophy]] - the article warns that AI can solve immediate problems while reducing the practice of reading source code and building durable understanding.

## Contradictions
- Qualifies optimistic [[AIFirstEngineering]] and [[VibeCoding]] claims by arguing that faster code generation does not improve delivery unless the actual bottleneck, verification loop, and WIP limits are addressed.
- Partly qualifies [[LLMToolingSkills]] as merely probabilistic prompt guidance: the article argues that skill compliance improves materially when skills are narrow, high-signal, and loaded near the generation point.

## Image Evidence
- The inspected diagrams show the subjective/objective speed paradox, AI coding as an NCX-10-like non-bottleneck, framework convergence around reusable skills, prompt load types, and context-position effects.
- The verification diagrams show checklist-style error reduction, plan/spec persistence versus transient plan mode, Toyota-style andon stopping, generate-verify-fix loops, and Swiss-cheese layered defenses across spec, check, test, and review.
- The flow diagrams show slower individual vessels improving network throughput, five concurrent agent workstreams converging at a review gate, positive throughput only when concurrency offsets slower full-SDLC tasks, and WIP overflow recreating the bottleneck.
- The later diagrams show automation increasing demand like a washing machine, multi-agent report analysis as capability expansion, risk-tiered automation modes, tool-return tables favoring document and research tasks, business-risk levels, and automation of routine updates to free learning time.

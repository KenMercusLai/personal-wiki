---
title: "为什么你的\"AI 优先\"战略可能大错特错？"
type: source
tags: [ai, software-engineering, ai-first]
date: 2026-04-21
source_file: /mnt/ken_personal_wiki/Articles/为什么你的AI 优先战略可能大错特错？.md
---

## Summary
This article frames "AI-first" software strategy as an engineering-systems problem rather than a tool-adoption slogan. The author's commentary argues that teams need strong [[SoftwareVerification]], CI/CD, monitoring, task management, and architecture before AI speed becomes useful, while the translated [[PeterPang]] essay describes [[CREAO]] rebuilding its workflow around AI agents, automated tests, deployment gates, feature flags, observability, and human strategic review.

## Key Claims
- [[AIFirstEngineering]] is not simply using coding assistants; it means redesigning planning, implementation, testing, deployment, monitoring, and organization around AI as a primary builder.
- The practical prerequisite for AI-first work is "software engineering first": automated tests, CI/CD, feature flags, observability, task granularity, and maintainable architecture.
- [[HarnessEngineering]] shifts engineering attention from writing every line of code to building the scaffolds, constraints, signals, and validation loops that let agents work safely.
- AI-first workflows fit backend-heavy, data-measurable, early-stage, or internal-tool contexts better than UI-dense, safety-critical, or high-quality-sensitive products.
- [[SoftwareVerification]] must move at AI speed through deterministic pipelines, AI review, end-to-end tests, deployment gates, production monitoring, automatic rollback, and self-healing triage.
- The article partly tensions [[JuniorEngineerLearning]]: [[PeterPang]] claims juniors adapted faster to AI-native workflows, while the commentary still emphasizes architecture and judgment as hard constraints.

## Key Quotes
> "与其说 AI First，不如说软件工程 First。" - on the source author's main qualification.

> "测试、CI/CD、监控、架构、任务管理，这些做扎实了，AI 的能力自然能释放出来。" - on the prerequisite stack.

> "真正的竞争优势，在于你下定决心要围绕这些工具彻底重塑一切。" - on workflow redesign rather than tool access.

## Connections
- [[AIFirstEngineering]] - central strategy model analyzed and qualified by the source.
- [[HarnessEngineering]] - named operating philosophy for making AI agents effective through scaffolds and constraints.
- [[AICodingPractice]] - the source expands AI coding practice from individual habits into organization-level automation.
- [[SoftwareVerification]] - the source treats validation speed and determinism as the gate on AI-generated output.
- [[AIAgentCollaboration]] - humans still direct, review, and judge, but the article is more automation-first than collaboration-first.
- [[HumanCodeResponsibility]] - the source shifts responsibility toward strategic risk review and scaffold design.
- [[JuniorEngineerLearning]] - the source offers a different observation about junior engineers adapting quickly to AI-native workflows.
- [[CREAO]] - company case study in the translated essay.
- [[PeterPang]] - author of the translated AI-first case study.
- [[Claude]] - AI reviewer and triage agent used in the described workflow.
- [[OpenAI]] - named as a source of the "Harness Engineering" label in the article.
- [[Anthropic]] - referenced through Claude and as an example company unlikely to fully automate core-product iteration without quality controls.

## Contradictions
- Partly qualifies [[AIAgentCollaboration]] and [[HumanCodeResponsibility]]: Piglei emphasizes engineer-agent collaboration and individual code ownership, while this source describes a more system-level model where AI writes, reviews, tests, deploys, monitors, and triages while humans focus on strategic risk and scaffold design.
- Partly tensions [[JuniorEngineerLearning]]: Piglei warns that junior engineers can lose learning opportunities by outsourcing debugging and design, while [[PeterPang]] reports that juniors adapted fastest because they had fewer legacy habits.

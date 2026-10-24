---
title: "一天几百个 PR 有什么意义？我照着 SpaceXAI 工程师 Lauren（@poteto）的九类清单，把自己的活拆了一遍"
type: source
tags: [ai, agents, software-engineering, code-review, workflow]
date: 2026-10-09
source_file: "/mnt/ken_personal_wiki/Articles/hundreds-of-prs-a-day-nine-work-lines.md"
---

## Summary
[[MaiYang]] uses [[LaurenTan]]'s nine reported work lines to argue that very high pull-request volume is an output of parallel, demand-backed work plus risk-tiered review and verification, not a useful target by itself. The article contrasts Tan's reported 2,500 production PRs in one month and Jacob Gold's nearly 250 daily merges with Mai Yang's [[ContextEcho]] record of 1,020 commits but only 18 pull-request merges from April to early October. Its durable contribution is a [[VerificationDrivenAgentDelegation]] rule: classify work, define input and output checks, automate low- and medium-risk validation, and reserve human judgment for direction, standards, experience, and consequential uncertainty.

## Key Claims
- Tan's nine concurrent work lines cover performance, user-reported bugs, agent-friendly refactoring, Skills, features, UI polish, harness work, developer tooling and release observability, and personal projects.
- Her reported review model runs agentic code review and risk assessment on every pull request, allows low- and medium-risk changes to merge without human review, and uses Bugbot as another check.
- The article attributes Tan's September output of 2,500 production PRs to parallel work, verification, and accumulated trust rather than treating the number alone as proof of value.
- Jacob Gold reportedly added a check that compares each diff with all prompts issued for that pull request and escalates any possible intent mismatch to a human decision tool; he still describes PR count as practice for building a software production system rather than business value.
- Mai Yang reports 1,020 [[ContextEcho]] commits from April to early October, including 17 days with at least 20 commits and a maximum of 54, but only 18 pull-request merges because the project has one developer and a smaller impact surface.
- The author's own work spans eleven product, content, community, Skill-maintenance, and running-analysis lines; this breadth differs from Tan's concentration around one growing product and several connected codebase concerns.
- High output is meaningful only when real users, bugs, performance problems, and features supply demand; otherwise PR volume can become expensive make-work and a vanity metric.

## Key Quotes
> “需求是真的，量才有意义。” — Mai Yang's boundary on treating volume as valuable.

> “定方向，定标准，看结果，自己用一遍看体验。” — the human judgment Mai Yang retains while delegating line-level code review.

## Connections
- [[MaiYang]] - author comparing her own product and content workflow with Tan's production-coding workflow.
- [[LaurenTan]] - source of the nine work lines, risk-tiered review account, and trust-before-volume argument.
- [[ContextEcho]] - solo project whose commit and pull-request history provides the author's contrasting case.
- [[VerificationDrivenAgentDelegation]] - trust grows through checks, risk classification, and escalation rather than raw agent count.
- [[BottleneckAwareAICoding]] - separates generated and merged volume from demand, delivered value, review capacity, and human attention.
- [[CodeReviewPractice]] - supports review depth and human involvement that vary with risk and impact.
- [[HarnessEngineering]] - lint rules, compilers, tests, observability, Skills, and review agents make broader delegation possible.
- [[GrokBot]] - executes many of Mai Yang's non-code work lines and is also part of Tan's reported engineering work.

## Contradictions
- The reported 2,500 monthly and nearly 250 daily pull-request figures come from social posts summarized by the author. The article provides no repository audit, PR-size distribution, defect or rollback rate, review false-negative rate, production-incident rate, user-outcome measure, token cost, or baseline.
- The article strengthens the case for risk-tiered review but does not specify the classifier, risk thresholds, validation suite, exception rate, or evidence that low- and medium-risk automatic merges are correctly categorized.
- Mai Yang's 1,020 commits and 18 pull-request merges are not directly comparable with Tan's or Gold's PR counts because project scope, team structure, merge policy, unit size, demand, and measurement window differ.
- The author reports reduced concentration and severe fragmentation as a cost of many parallel work lines, so greater breadth does not imply greater sustainable output or wellbeing.
- The sole local image was opened and classified as a redundant text-bearing lead graphic: its 2,500-versus-18 contrast is fully repeated and better qualified in the prose. It was omitted, so no asset manifest was required.

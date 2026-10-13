---
title: "0% 是机会，20% 是陷阱：Jeff Dean 离职前那场 YC 访谈里，我抄走了三条判断"
type: source
tags: [ai, startups, agents, judgment]
date: 2026-08-11
source_file: "/mnt/ken_personal_wiki/Articles/0% 是机会，20% 是陷阱：Jeff Dean 离职前那场 YC 访谈里，我抄走了三条判断.md"
---

## Summary
Mai Yang extracts three operating judgments from a 2026 YC interview with [[JeffDean]]: seek useful problems where general models currently succeed almost never rather than partially capable tasks likely to be absorbed by the next model generation; train [[TasteAsProblemSense|taste]] by recording and later scoring forecasts; and make specifications more explicit as agents become more capable. The essay connects those judgments to [[DiscoveryLoop]], reusable [[LLMToolingSkills|Skills]], parallel experimentation, and first-principles performance reasoning, while adding two important limits: capability failure is only a second-stage filter after user value, and a model's current success rate says little about how fast that rate will rise.

## Key Claims
- [[StartupOpportunitySelection]] can use general-model task success as a competitive-frontier signal: roughly 20% success may mean a capability is already emerging and likely to commoditize a wrapper, while a near-zero result can indicate room for proprietary data or a narrow specialist model.
- Near-zero model performance does not establish demand; founders must first identify a useful problem they care about, then distinguish “hard and wanted” from “nobody wants it.”
- A static success rate is insufficient because model frontiers move. Re-running the same real task suite across releases can at least produce a local capability curve, although the source offers no validated forecasting method.
- [[TasteAsProblemSense]] can be trained by writing five to ten predictions about what will matter over the next year, choosing among them, and later scoring what became important, what others built, and what never happened.
- Agent capability raises the value of [[SpecDrivenAgentDevelopment|explicit specifications]] because long autonomous trajectories need durable descriptions of desired behavior, tests, constraints, and equivalence rather than relying on a collaborator's unstated context.
- [[LLMToolingSkills]] can package a repeated expert workflow for an agent; Dean's example turns measurement, modification, re-benchmarking, and cache-footprint analysis into an iterative performance-optimization Skill.
- Automated scientific and engineering work can decompose a problem into subproblems, run many experimental loops in parallel, evaluate candidate paths, and recombine results; the author interprets this interview prediction as a preview of [[DiscoveryLoop]].

## Key Quotes
> "So look for something where the model succeeds 0% or 1% of the time, not 20%." — Dean's task-selection heuristic as quoted by the source.

> "The most important thing is to pick something you’re super excited about and want to build and you think would be useful in the world." — the value filter the author argues must precede the capability-gap filter.

> "It really just is us giving the approach we would use as people to the model in a form that it could use." — Dean's description of encoding an expert optimization process as a Skill.

## Connections
- [[MaiYang]] - author interpreting and qualifying the YC interview.
- [[JeffDean]] - interview subject and source of the capability-gap, taste, specification, experimentation, and performance examples.
- [[DianaHu]] - interviewer whose questions repeatedly translate past technical episodes into present-day actions.
- [[DiscoveryLoop]] - company the author connects to Dean's prediction about AI-run experimental loops.
- [[StartupOpportunitySelection]] - receives the two-stage “useful first, capability gap second” opportunity screen.
- [[TasteAsProblemSense]] - judgment is treated as a trainable record of settled predictions rather than an ineffable gift.
- [[SpecDrivenAgentDevelopment]] - stronger agents increase the need for explicit behavior, constraints, and tests.
- [[LLMToolingSkills]] - repeated expert procedures can be encoded for agents to execute and iterate.
- [[BackOfEnvelopeEstimation]] - napkin calculations and first-principles bottleneck analysis guide high-leverage technical bets.
- [[LatencyHierarchy]] - memory, compute, interconnect, and data-movement costs remain central to AI-system performance judgment.

## Contradictions
- The “0% or 1%, not 20%” rule is an attributed practitioner heuristic, not a validated threshold. The essay itself rejects using it as a first-stage demand test and supplies no evidence that 20% capability reliably predicts rapid commoditization.
- The proposed 20–30 example test set can support local comparison but may be too small or unrepresentative to estimate a product's real task distribution, reliability, or future model trajectory.
- The author explicitly did not independently verify several biographical, market, and technical figures reported in the interview, including employee counts, stock movement, hardware improvements, energy ratios, and scientific-simulation speedups.
- The claimed five-day line from interview prediction to Discovery Loop's announcement is the author's interpretation of thematic continuity, not evidence that the interview disclosed a complete company plan.

---
title: "Software Estimation"
type: concept
tags: [software-engineering, planning, estimation, product-management]
sources:
  - estimating-work-a-software-development-superpower-hackernoon-com-medium
  - estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
[[SoftwareEstimation]] is the practice of forecasting the engineering effort or elapsed time required for software work by making its constituent work, assumptions, dependencies, and uncertainty discussable before delivery.

## Current Synthesis
Estimation is both an engineering skill and a resource-allocation input. A large, undifferentiated duration guess hides how the work will proceed and makes errors expensive in salary cost, opportunity cost, and delayed access to the intended product value. One remedy is to divide the project into phases, estimate the phases separately, and let several engineers who know the codebase challenge the plan.

The review is meant to reveal omitted work, likely stalls, and help needs rather than manufacture certainty. Two complementary techniques make uncertainty visible: optimistic, realistic, and pessimistic scenarios expose the conditions hidden by a single number, while simultaneous team estimates expose differences in understanding. Large differences should trigger investigation of assumptions and risks, not merely arithmetic reconciliation.

For product managers and non-technical founders, listening to estimation discussion provides a way to understand delivery risk without claiming implementation expertise. Repetition may improve judgment, but the resulting timeline remains a pre-development forecast rather than a guarantee.

## Key Claims
- A project-sized duration guess is less inspectable and more fragile than estimates grounded in smaller phases.
- Estimation error consumes labor budget and prevents the same engineering capacity from serving other priorities.
- Decomposition improves an estimate by making components, blockers, and help needs explicit enough to challenge.
- Review by multiple codebase-familiar engineers can expose assumptions that one estimator misses.
- Product decision makers should use estimates as inputs to cost and priority judgments, not as contractual certainty.
- Three-scenario estimates make favorable, ordinary, and adverse conditions explicit and can reveal blockers hidden by one most-likely duration.
- Independent estimates revealed simultaneously can reduce domination and turn disagreement into evidence about confidence and assumptions.

## Evidence
- Decomposition and inspectability: [[estimating-work-a-software-development-superpower-hackernoon-com-medium]] contrasts one six-month estimate with separately estimated project phases.
- Economic consequence: [[estimating-work-a-software-development-superpower-hackernoon-com-medium]] illustrates how a two-month miss adds salary cost and delays alternative work.
- Peer review: [[estimating-work-a-software-development-superpower-hackernoon-com-medium]] recommends reviewing phases and estimates with several engineers familiar with the codebase, then using an open-ended prompt to elicit discussion.
- Anticipated impediments: [[estimating-work-a-software-development-superpower-hackernoon-com-medium]] associates better estimating with recognizing likely stalls and communicating help needs in advance.
- Product judgment: [[estimating-work-a-software-development-superpower-hackernoon-com-medium]] argues that repeated participation helps non-technical product leaders develop better intuition about delivery time.
- Scenario range: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] asks for optimistic, realistic, and pessimistic estimates rather than one idealized duration.
- Confidence and risk: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] treats the pessimistic case and standard deviation as prompts to expose blockers and confidence.
- Independent team input: [[estimation-for-fun-and-profit-but-mostly-for-sanity-8th-light]] recommends individual reflection followed by simultaneous reveal so one voice is less likely to dominate.

## Counterevidence & Qualifications
The evidence consists of two short practitioner essays without observed projects, forecast-versus-actual results, comparison groups, or accuracy measures. Decomposition can reveal work while still producing a wrong sum; correlated risks, integration overhead, queues, interruptions, unfamiliar systems, and unknown unknowns may remain hidden. Three scenarios do not become calibrated probabilities merely because a calculator combines them, and the 8th Light source does not specify its formula or distributional assumptions. Simultaneous reveal can reduce public anchoring, but prior discussion can still anchor the group; averaging divergent estimates may also hide rather than resolve important uncertainty. The salary example assumes time maps directly to cost, and neither source establishes that repeated exposure produces calibrated intuition.

## What Changed
- Created a delivery-estimation concept centered on phase decomposition, codebase-informed peer review, and explicit resource trade-offs.
- Added optimistic, realistic, and pessimistic scenarios as a way to expose schedule conditions and risk.
- Added simultaneous team estimation while preserving disagreement as evidence rather than treating an average as certainty.

## Related Concepts
- [[ProductIdeaPrioritization]] - uses engineering effort as one input when comparing candidate product work.
- [[ProductManagement]] - translates delivery forecasts into cost, sequencing, and opportunity decisions.
- [[CrossFunctionalProductTeams]] - supplies the engineering and product perspectives needed to review assumptions together.
- [[BackOfEnvelopeEstimation]] - uses decomposition for technical performance plausibility rather than project duration.
- [[AgileSoftwareDevelopment]] - adapts plans as evidence and requirements change during delivery.
- [[PERTEstimation]] - structures one estimate around favorable, ordinary, and adverse scenarios.
- [[UserStories]] - provides the small user-visible work unit estimated in the 8th Light example.

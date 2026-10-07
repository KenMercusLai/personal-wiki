---
title: "Bayesian Updating"
type: concept
tags: [probability, decision-making, evidence, investing, uncertainty]
sources:
  - serenity-qi-shi-lu
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[BayesianUpdating]] is the revision of confidence in a hypothesis by combining an initial probability with evidence whose likelihood differs depending on whether the hypothesis is true.

## Current Synthesis
In the wiki's current source, 王翼之 uses Bayesian updating as an analogy for investment research. A supply-chain model establishes an initial belief that a company controls a future bottleneck; patents, contracts, yields, substitution threats, customer insourcing, and management conduct then strengthen or weaken that belief. The practical discipline is valuable: name the thesis, identify evidence that could change it, and update on causal facts rather than price movement alone.

The analogy becomes a formal Bayesian method only when the investor defines hypotheses, base rates or priors, evidence likelihoods, and an updating rule. Even a well-calibrated posterior probability does not select a trade by itself. Decision quality also depends on payoffs, valuation, loss severity, position size, liquidity, correlation, and opportunity cost. The source invokes expected value but does not calculate it or show that different bottleneck hypotheses are calibrated on a common scale.

## Key Claims
- An explicit prior makes the starting belief inspectable and separates structural research from intuition disguised as certainty.
- Evidence is informative when its probability differs materially between the hypothesis and plausible alternatives.
- Positive and negative thesis evidence should both change conviction; price movement is not a substitute for causal evidence.
- A posterior from one round of evidence can become the prior for later evidence, enabling sequential revision.
- Comparing posterior probabilities across opportunities is insufficient when payoff distributions, prices, correlations, and losses differ.
- Qualitative Bayesian language can improve reasoning while still falling short of a calibrated statistical model.

## Evidence
- Prior formation: [[serenity-qi-shi-lu]] maps papers, bills of materials, and supply-chain structure to an initial belief about bottleneck status.
- Likelihood-bearing evidence: [[serenity-qi-shi-lu]] contrasts patents, contracts, and yields with substitution, insourcing, and management-integrity concerns.
- Sequential revision: [[serenity-qi-shi-lu]] says continuing diligence should update the original thesis and that the resulting posterior becomes input to the next assessment.
- Decision analogy: [[serenity-qi-shi-lu]] connects updated conviction to adding, reducing, exiting, or rotating positions, but provides no numerical implementation.

## Counterevidence & Qualifications
The source repeats probability notation but supplies no values, base-rate class, likelihood ratios, mutually exclusive hypotheses, calibration test, or posterior calculation. Deep research can improve inputs without eliminating motivated reasoning, selection bias, overconfidence, or model misspecification. Evidence items may be dependent, already priced, stale, strategically disclosed, or consequences rather than causes. A high probability of bottleneck status can coexist with a poor investment when valuation is excessive or downside is asymmetric. The source's “highest posterior” rotation rule therefore should not be equated with maximum expected utility.

## What Changed
- Created the concept around explicit priors, thesis-relevant evidence, and sequential belief revision.
- Distinguished a useful qualitative discipline from a calibrated Bayesian model.
- Separated posterior confidence from valuation, payoff, portfolio, and expected-utility decisions.

## Related Concepts
- [[ChokepointInvesting]] - source-specific investment workflow interpreted through sequential belief revision.
- [[DecisionQuality]] - separates sound updating from outcome bias after a trade succeeds or fails.
- [[StartupHypothesisTesting]] - applies a related hypothesis-evidence-revision loop to uncertain company and product assumptions.
- [[InvestmentRiskDiscipline]] - converts revised conviction and invalidation evidence into bounded exposure decisions.
- [[MarketTiming]] - a correct posterior does not remove uncertainty about when price and fundamentals converge.
- [[CompetitiveIntelligence]] - supplies evidence whose reliability and dependence must be assessed before updating.

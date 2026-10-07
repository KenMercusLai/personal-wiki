---
title: "Relevance-Constrained Ranking"
type: concept
tags: [search, advertising, ranking, constrained-optimization, control-systems]
sources:
  - search-relevance-from-modeling-to-ranking-mechanism
  - user-experience-optimization-from-heuristic-intervention-to-unified-value-modeling
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[RelevanceConstrainedRanking]] selects and orders results to maximize a business or utility objective while keeping estimated search relevance at or above an explicit target.

## Current Synthesis
The source models search-ad ranking as constrained optimization: choose one candidate per request to maximize eCPM while meeting a global mean-relevance target. Lagrangian relaxation converts the constraint into a shadow price on relevance, giving each request a local linear score that combines candidate value and relevance. Under full information, one global multiplier can be searched by replaying all requests and candidates until the selected mean reaches the target.

Production control does not have that omniscience. Historical replay assumes the next interval resembles the last and that changing winners does not alter the environment. A PID-like controller can track mean relevance online, but a controller blind to traffic value may overpay for relevance in valuable intervals and compensate when little value remains. The search source therefore proposes perturbing the common coefficient by value/relevance tier while retaining an overall pacing control. This is a heuristic approximation whose validity depends on recoverable relevance slack and different marginal relevance costs across tiers.

The experience-value source generalizes the same pattern from query relevance to short-window retention. It treats LT as an aggregate experience constraint, proposes listwise reranking because a sequence can affect retention differently from isolated items, and uses a shadow price to compare predicted LT with eCPM. The analogy clarifies the architecture but not the measurement: relevance and retention use different labels, time horizons, counterfactual requirements, and proxy risks.

## Key Claims
- A hard relevance threshold removes unacceptable candidates, while a relevance-weighted score manages the remaining value-quality tradeoff.
- Lagrangian relaxation turns a global mean-relevance constraint into a per-request value-plus-relevance ranking score.
- The relevance coefficient is a shadow price: it represents the marginal business cost of tightening the relevance target.
- Full-traffic replay and binary search can estimate the coefficient only when traffic and candidate distributions are sufficiently stable.
- Relevance-only feedback control can be economically inefficient because it does not know when business value is unusually high or low.
- Value-aware coefficient perturbations may improve the tradeoff, but only if lost relevance can be recovered elsewhere and marginal exchange costs differ across traffic tiers.
- The same shadow-price decomposition can internalize a retention constraint, but transferring the mechanism does not make relevance and retention interchangeable signals.

## Evidence
- Constraint application: [[search-relevance-from-modeling-to-ranking-mechanism]] distinguishes fixed low-relevance filtering from a dynamically weighted relevance term.
- Shadow-price derivation: [[search-relevance-from-modeling-to-ranking-mechanism]] applies Lagrangian relaxation and decomposes the global objective into independent per-request maximization.
- Offline solution: [[search-relevance-from-modeling-to-ranking-mechanism]] proposes binary search over replayed traffic because selected mean relevance rises monotonically with the multiplier.
- Online-control limitation: [[search-relevance-from-modeling-to-ranking-mechanism]] gives a two-interval example where relevance-only feedback suppresses high-value candidates and relaxes only after that value disappears.
- Value-aware heuristic: [[search-relevance-from-modeling-to-ranking-mechanism]] divides traffic into value/relevance quadrants and assigns different coefficient directions while preserving a unified control baseline.
- Feasibility assumptions: [[search-relevance-from-modeling-to-ranking-mechanism]] requires recoverable relevance and a lower marginal cost of buying relevance in low-value traffic.
- Retention generalization: [[user-experience-optimization-from-heuristic-intervention-to-unified-value-modeling]] places predicted LT in a listwise ranking objective and proposes replay or PID adjustment of its exchange coefficient against eCPM.

## Counterevidence & Qualifications
Both supplied Markdown files omit the mathematical symbols and formulas needed to reproduce their derivations. Neither source reports a simulation, production experiment, calibration analysis, controller-stability result, or sensitivity test. A mean constraint can be met while specific queries, categories, or users receive poor results, and an estimated mean has the intended physical interpretation only when the modeled signal is calibrated. Traffic-tier perturbation intentionally departs from the single-multiplier full-information optimum, so it should be evaluated as an online approximation rather than described as theoretically equivalent. Retention adds sparse delayed labels, policy-dependent proxies, and costly counterfactual exploration that are not resolved by borrowing the relevance formulation.

## What Changed
- Generalized the shadow-price pattern from relevance to short-window retention while preserving their different measurement and causal requirements.
- Added listwise sequence effects, delayed labels, proxy validity, and counterfactual exploration as constraints on experience-aware ranking.

## Related Concepts
- [[SearchRelevance]] - supplies the modeled quality constraint and its measurement boundary.
- [[MixedRankingGovernance]] - addresses system-wide coupling and stability when local ranking controls share traffic.
- [[ScoreShading]] - similarly adjusts score coefficients to satisfy aggregate delivery or experience targets.
- [[AdloadConstrainedMixedRanking]] - uses a global capacity price to make a cross-request allocation locally computable.
- [[ProgrammaticAdvertising]] - provides the eCPM objective and auction context for search-ad selection.
- [[ExperienceValueModeling]] - applies constrained ranking to retention and user-experience signals rather than query relevance alone.

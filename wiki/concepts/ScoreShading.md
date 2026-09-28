---
title: "Score Shading"
type: concept
tags: [ranking-systems, auction-theory, constrained-optimization, control-systems]
sources:
  - from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[ScoreShading]] is a proposed method for dynamically changing a business line's mixed-ranking score as though it were an auction bid, so the line can optimize exposure utility subject to platform constraints on load or score cost.

## Current Synthesis
The source maps first-price bid shading onto a feed in which formats submit PK scores for shared exposure opportunities. Its two formulations reverse the constrained objective: one maximizes expected utility under a budget for the winning score, while the other minimizes score cost under a target win rate. Lagrangian duality supplies a per-request objective and a pacing multiplier; a PID controller updates that multiplier from aggregate error. The framework is conceptually coherent, but the available article is a proposal rather than validated production evidence, and its extracted equations are absent.

Win-rate estimation is the decision layer. Binary replay and monotone curve fitting estimate success at a proposed score, whereas distribution modeling estimates the highest competing score and derives a response curve from its CDF. The latter can represent near losses, severe losses, and uncertainty more richly, but only if the observation process, censoring treatment, and distribution family are credible. An unshaded exploration bucket is needed because a policy trained only on its own shaded outcomes can reinforce downward bias. Even a sound local optimizer is incomplete without [[MixedRankingGovernance]], since multiple independent controllers change one another's environments.

## Key Claims
- PK scores can be modeled as implicit bids when multiple business lines compete for the same exposure.
- Dual optimization separates per-request score choice from aggregate load or score-cost control.
- PID-updated pacing multipliers translate target error into stronger or weaker bidding pressure.
- Distribution estimation can provide an entire score-to-win-rate landscape and an uncertainty measure from one inference.
- Exploration traffic is required to reduce policy-induced feedback bias in observed competition.
- Local optimization does not guarantee platform welfare when independently controlled formats share a traffic pool.

## Evidence
- Optimization structure: [[from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems]] formulates penetration growth under a winning-score constraint and score reduction under a win-rate constraint.
- Control mechanism: [[from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems]] assigns the dual multiplier to a PID controller that responds to aggregate constraint error.
- Competition modeling: [[from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems]] contrasts binary win prediction, monotone curve fitting, and distribution estimation of the highest competing score.
- Feedback correction: [[from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems]] proposes a small unshaded epsilon-greedy bucket for less policy-biased observations.
- System boundary: [[from-bid-shading-to-score-shadingdual-optimization-and-game-governance-in-mixed-ranking-systems]] describes score deflation and coupled PID oscillation when every format shades independently.

## Counterevidence & Qualifications
The sole source gives no production experiment, offline evaluation, baseline comparison, controller parameters, calibration results, or causal evidence that score shading improves long-term platform value. Its displayed formulas and variable names are missing from the extracted Markdown, preventing independent verification of the derivations. Distribution estimation still depends on correct censoring, observability, calibration, and distributional assumptions; variance does not by itself guarantee conservative decisions unless the objective explicitly prices uncertainty. Mean-score and load proxies may also diverge from user welfare or [[CustomerLifetimeValue]].

## What Changed
- Created the concept as a dual-control framework rather than a generic score-rescaling technique.
- Separated local decision quality from the platform-governance conditions required for safe deployment.

## Related Concepts
- [[MixedRankingGovernance]] - supplies system-level constraints when multiple score-shading controllers compete in one feed.
- [[ProgrammaticAdvertising]] - first-price bid shading provides the auction analogy and optimization baseline.
- [[DataExploration]] - an unshaded bucket collects less policy-biased competition observations.
- [[CustomerLifetimeValue]] - desired long-horizon outcome that the source replaces with faster score and load proxies.
- [[ReinforcementLearning]] - possible future approach for sequential, delayed constraints rather than evidence for the current method.

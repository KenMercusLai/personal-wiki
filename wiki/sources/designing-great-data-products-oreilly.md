---
title: "Designing Great Data Products"
type: source
tags: [data-products, data-science, optimization, decision-making]
date: 2012-03-28
source_file: "/mnt/ken_personal_wiki/Articles/Designing great data products – O’Reilly.md"
---

## Summary
[[JeremyHoward]], [[MargitZwemer]], and [[MikeLoukides]] present the [[DrivetrainApproach]], a four-step method that starts with an objective, identifies controllable levers, determines required data, and only then builds models. Through search, insurance pricing, recommendations, marketing, systems engineering, and self-driving examples, they argue that predictions become useful products only when simulation and optimization connect them to implementable decisions. The article is a conceptual and practitioner account rather than a comparative evaluation, and its sole embedded mechanical-drivetrain illustration is decorative.

## Key Claims
- [[DrivetrainApproach]] reverses model-first development: define the desired outcome, controllable levers, and needed data before choosing predictive models.
- A Model Assembly Line joins component models in a simulator, searches possible input combinations, and uses an optimizer to select desirable outcomes while exposing catastrophic ones.
- [[OptimalDecisionsGroup]] applied this pattern to insurance pricing by combining acceptance probability, conditional profit, retention, constraints, and multi-year simulation rather than pricing from accident-risk prediction alone.
- Recommendation ranking should optimize incremental purchases caused by exposure, not merely the probability that a customer will like or buy an item anyway.
- Randomized interventions are often necessary because observational purchase or pricing data do not reveal how customer behavior changes under alternative recommendations or prices.
- Marketing optimization must include long-term effects such as margins, customer patience, retention, purchase sequences, and lifetime value rather than only immediate conversion.
- In safety- and mission-critical settings, a useful data product must turn prediction into a concrete action that respects constraints and downside risk.

## Key Quotes
> "What choice are we actually helping him or her make?" - the authors' test for whether an objective function represents a useful product decision.

> "Prediction only tells us that there is going to be an accident. An optimizer tells us how to avoid accidents." - the self-driving example's distinction between forecasting and action selection.

## Connections
- [[JeremyHoward]] - coauthor and founder of Optimal Decisions Group.
- [[MargitZwemer]] - coauthor of the four-step data-product framework.
- [[MikeLoukides]] - coauthor and O'Reilly editor associated with the article.
- [[OptimalDecisionsGroup]] - insurance-pricing case used to develop the modeler-simulator-optimizer pattern.
- [[DrivetrainApproach]] - central objective-to-action framework proposed by the article.
- [[IndustryDataScience]] - broader practice that must connect models and intrinsic metrics to operational impact.
- [[Google]] - search-ranking example in which relevance, link data, and PageRank follow from a user objective and ranking lever.
- [[Amazon]] - recommendation example used to distinguish predicted affinity from incremental purchasing caused by a recommendation.
- [[CustomerLifetimeValue]] - long-horizon objective proposed for pricing and marketing decisions.
- [[DataExploration]] - randomized exposure is needed to learn responses to recommendations and price changes.

## Contradictions
- The article challenges model-centric interpretations of [[IndustryDataScience]] and affinity-based recommendation quality, but it does not contradict the wiki's existing synthesis, which already treats business impact, experimentation, interpretation, and operationalization as central.
- Its strongest insurance gains are company- and founder-reported without independent evaluation, while the proposed recommendation and marketing systems are designs rather than reported controlled outcomes.

---
title: "Artwork Personalization at Netflix"
type: source
tags: [machine-learning, personalization, recommendations, experimentation]
date: 2017-12-07
source_file: /mnt/ken_personal_wiki/Articles/Artwork Personalization at Netflix - Netflix TechBlog - Medium.md
---

## Summary
Ashok Chandrashekar, Fernando Amat, Justin Basilico, and Tony Jebara describe how [[Netflix]] moved from choosing one best title image for everyone to selecting personalized artwork for each member context. The article frames [[ArtworkPersonalization]] as part of recommendation quality: not only which title is recommended, but how the title is visually presented, can affect discovery. The system uses [[ContextualBandits]], controlled [[DataExploration]], and [[OfflinePolicyReplay]] to learn from logged impressions while limiting regret, avoiding clickbait labels, and handling scale, cold start, and recognizability constraints.

## Key Claims
- [[ArtworkPersonalization]] can improve discovery because different members may respond to different actors, genres, moods, aesthetics, or story signals for the same title.
- Image choice creates attribution and closed-loop learning problems because the member can only react to the one artwork that was shown.
- [[ContextualBandits]] fit artwork selection because they combine online learning, exploration, regret minimization, and context-aware image ranking.
- [[DataExploration]] must log randomization propensities so later evaluation can correct for skewed image exposure.
- [[OfflinePolicyReplay]] can use logged randomized data to estimate how a new artwork-selection policy would have performed before online launch.
- Artwork systems need creative asset diversity, page-level visual diversity, low-latency serving, cold-start adaptation, and labels based on quality engagement rather than mere clicks.

## Key Quotes
> "we don't have one product but over a 100 million different products" - on member-specific recommendations and visuals.

> "personalizing not just what we recommend but also how we recommend" - on the project expanding recommendation beyond title ranking.

## Connections
- [[Netflix]] - company context for large-scale visual recommendation and experimentation infrastructure.
- [[ArtworkPersonalization]] - source's central design and machine-learning problem.
- [[ContextualBandits]] - online-learning approach used for personalized image selection.
- [[DataExploration]] - controlled randomization and propensity logging needed for learning and evaluation.
- [[OfflinePolicyReplay]] - counterfactual evaluation method used before online A/B testing.
- [[BehavioralData]] - impressions, plays, quality engagement, member attributes, and recommendation signals feed model training.
- [[ProductMetricLadder]] - take fraction and quality engagement act as short-cycle metrics tied to long-term discovery and member experience.
- [[ConversionRateOptimization]] - related experimentation pattern, qualified here by downstream engagement quality and recommendation attribution.

## Contradictions
- No direct contradictions found. The source extends existing experimentation and personalization material by making visual presentation a recommendation decision rather than a fixed content asset.

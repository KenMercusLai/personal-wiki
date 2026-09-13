---
title: "Data Exploration"
type: concept
tags: [machine-learning, experimentation, data, recommendations]
sources:
  - artwork-personalization-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[DataExploration]] is the deliberate injection of controlled randomness into a decision system so it can observe outcomes for alternatives it might not otherwise choose.

## Current Synthesis
The Netflix source frames exploration as the data-generation side of online personalization. If the system always shows the currently predicted best artwork, it cannot learn enough about other candidate images or correct for the fact that exposure was already biased by earlier decisions. Controlled randomization creates logged impressions across member, title, and image tuples, while propensity logging records how likely each image was to be selected. That evidence supports later model training and [[OfflinePolicyReplay]], but it must be constrained so artwork does not change too often or damage the member experience.

## Key Claims
- Exploration produces training data for alternatives that exploitation-only systems would rarely show.
- Randomization schemes can range from uniform epsilon-greedy choices to adaptive schemes based on model uncertainty.
- Logging selection propensities is necessary to correct skewed exposure during offline evaluation.
- Exploration creates regret because some sessions show an image that is not predicted to be best.
- Large populations can make the individual cost of exploration small when the per-session downside is limited.
- Exploration design can also stabilize attribution by controlling how often artwork changes.

## Evidence
- Randomized exposure: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says training data comes from controlled randomization in model predictions.
- Scheme range: [[artwork-personalization-at-netflix-netflix-techblog-medium]] contrasts simple epsilon-greedy randomness with closed-loop uncertainty-based randomization.
- Propensity logging: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says randomization information must be logged for each artwork selection to support unbiased offline evaluation.
- Regret cost: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says exploration can show a non-best predicted image and therefore has member-experience cost.
- Scale amortization: [[artwork-personalization-at-netflix-netflix-techblog-medium]] argues that Netflix's large member base makes exploration cost per member negligible.
- Attribution stability: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says exploration can be controlled so artwork selections do not change too often.

## Counterevidence & Qualifications
Exploration is not automatically appropriate. The Netflix source itself notes that contextual-bandit randomization would be less suitable if exploration cost were high. Exploration also depends on correct instrumentation; missing propensities, poor labels, or excessive image churn can make learning unreliable or harmful.

## What Changed
- Created the concept for controlled randomization and propensity logging in online recommendation systems.

## Related Concepts
- [[ContextualBandits]] - use exploration to balance learning and exploitation.
- [[OfflinePolicyReplay]] - depends on logged randomized selections and propensities.
- [[ArtworkPersonalization]] - is the concrete Netflix use case for exploration.
- [[BehavioralData]] - exploration changes which behavior data the system observes.
- [[ConversionRateOptimization]] - shares experimentation logic but often uses coarser treatment groups.

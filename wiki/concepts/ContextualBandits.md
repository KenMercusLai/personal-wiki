---
title: "Contextual Bandits"
type: concept
tags: [machine-learning, recommendations, experimentation, online-learning]
sources:
  - artwork-personalization-at-netflix-netflix-techblog-medium
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[ContextualBandits]] are online-learning algorithms that choose actions for a given context while balancing exploitation of the currently best prediction with exploration needed to improve future decisions.

## Current Synthesis
The Netflix source presents contextual bandits as a bridge between batch recommendation experiments and continuously adapting personalization. Traditional batch learning plus A/B testing can incur regret because many members wait while data is collected, models are trained, and experiments conclude. For artwork, the member and session context become the input; the algorithm ranks candidate images by predicted probability of quality engagement and chooses the top image while injecting controlled randomization where learning is still needed. This makes the approach especially suitable when exploration cost is small per user and large populations can amortize learning across a catalog.

## Key Claims
- Contextual bandits reduce regret compared with slower batch-learning and delayed A/B-test cycles.
- The context can include member history, title interaction, country, language, device, time, day, and recommendation-model signals.
- The action is the image selected from a title's candidate artwork pool.
- Exploration is necessary to collect less biased training data, but it imposes some member-experience cost.
- Model variants can include supervised ranking simplifications or bandit methods such as Thompson Sampling, LinUCB, and Bayesian approaches.
- Contextual bandits are most appropriate when exploration costs are low enough to be amortized across a large population.

## Evidence
- Batch regret: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says collecting data, training a batch model, and waiting for an A/B test means many members do not benefit during the delay.
- Context definition: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says personalization treats the member as context because different members respond differently to images.
- Feature signals: [[artwork-personalization-at-netflix-netflix-techblog-medium]] lists viewing history, genres, country, language, device, time, day, and recommendation scores as candidate features.
- Action space: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says titles typically have up to a few dozen candidate images and the model ranks them for each context.
- Exploration tradeoff: [[artwork-personalization-at-netflix-netflix-techblog-medium]] says exploration has regret, but Netflix's large member base makes the per-member cost small.
- Algorithm families: [[artwork-personalization-at-netflix-netflix-techblog-medium]] mentions Thompson Sampling, LinUCB, Bayesian methods, and simpler supervised-learning formulations.

## Counterevidence & Qualifications
The source is a practitioner case study rather than a general technical survey. It does not specify the exact production algorithm, feature transformations, calibration method, confidence bounds, or privacy controls. Contextual bandits also require reliable logging and suitable outcome labels; if the reward is badly chosen, the learner can optimize clicks or novelty at the expense of member satisfaction.

## What Changed
- Created the concept from Netflix's artwork-personalization case.

## Related Concepts
- [[ArtworkPersonalization]] - provides the source's concrete action-selection problem.
- [[DataExploration]] - supplies the randomized data contextual bandits need.
- [[OfflinePolicyReplay]] - evaluates candidate contextual-bandit policies before online launch.
- [[ReinforcementLearning]] - related family of learning from actions and rewards, though contextual bandits are a simpler one-step setting.
- [[BehavioralData]] - provides the actions and outcomes used to train and evaluate policies.
- [[ProductMetricLadder]] - reward design links immediate take fraction to broader quality engagement.

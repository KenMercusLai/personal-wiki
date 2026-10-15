---
title: "Computational Humor"
type: concept
tags: [artificial-intelligence, humor, cognitive-modeling, language]
sources:
  - "2309.02009"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[ComputationalHumor]] uses computational or formal models to represent, analyze, recognize, interpret, or generate humorous material and the cognitive or social processes around it.

## Current Synthesis
The current source models one listener's interpretation of a context-punchline statement. A setup prompts a defeasible expectation; a potentially funny punchline overturns the resulting preferred belief state while also making the setup intelligible. [[IncongruityResolution]] adds a second path in which the story violates a strict or default norm, yet becomes revealing when reasoning proceeds in disregard of that norm.

The framework is deliberately componential. Surprise, revelation, and incongruity can help explain why some narrative jokes work, but none uniquely identifies humor: detective stories also surprise and reveal, and incongruity can evoke wonder. Superiority, teller-listener coordination, delivery, compassion, taboo strength, cultural background, emotion, identification, and physiology remain additional variables.

## Key Claims
- Joke comprehension can be represented as sequential belief change over context and punchline.
- A useful punchline both defeats an induced expectation and explains the setup after reinterpretation.
- Potential funniness is relative to the listener's knowledge and revision policy.
- Narrative order, context length, punchline specificity, and plausibility distance can affect the modeled result or intensity.
- A complete humor model needs more than surprise, revelation, and norm violation.

## Evidence
- Core formalization: [[2309.02009]] defines surprising, revealing, and potentially funny statements and illustrates them with ranked models.
- Structural properties: [[2309.02009]] proves that revealing punchlines lose surprise when placed first and gives counterexamples showing that added setup material can destroy surprise or revelation.
- Graduality and scope: [[2309.02009]] proposes possibility-based surprise and revelation levels while listing unmodeled cognitive, social, cultural, and performance factors.

## Counterevidence & Qualifications
The paper analyzes hand-encoded propositional examples rather than measuring joke comprehension, laughter, or model performance on a corpus. Its definitions identify conditions for “potentially funny” statements, not sufficient or necessary conditions for human humor. The natural-language-to-logic step is explicitly omitted, and the account centers the listener while leaving teller strategy and multi-agent beliefs largely open. Some cited psychological and philosophical claims are background motivation rather than new empirical evidence.

## What Changed
- Created the concept from a formal listener-centered model of narrative jokes.
- Separated modeled ingredients from a sufficient theory of laughter.
- Recorded narrative, listener, and representation dependencies.

## Related Concepts
- [[BeliefRevision]] - formalizes integration of setup and punchline.
- [[NonmonotonicReasoning]] - produces the defeasible expectation that a punchline can overturn.
- [[IncongruityResolution]] - represents humorous norm violation and retrospective explanation.
- [[BayesianUpdating]] - adjacent belief-change framework not used as the paper's core semantics.

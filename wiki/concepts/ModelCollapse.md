---
title: "Model Collapse"
type: concept
tags: [ai, training-data, synthetic-data, model-quality]
sources:
  - yu-yan-de-bian-jie-jiu-shi-si-wei-de-bian-jie
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[ModelCollapse]] is degradation or distributional narrowing attributed to training successive models on recursively generated model outputs, especially when synthetic material displaces diverse, high-quality real data or preserves earlier errors.

## Current Synthesis
The source presents a simple feedback-loop account: temperature makes generated token sequences noisy, feeding those sequences into later training rounds increases disorder, and repeated rounds eventually reduce model quality. Its broader warning is useful because generated data can reproduce errors and overrepresent already probable patterns, turning a model's outputs into a progressively narrower substitute for the distribution it was meant to learn.

The proposed entropy mechanism is not established by the supplied evidence. Sampling can increase output diversity, but recursive training can also lose rare modes, making some measures of diversity decline rather than rise. Outcomes depend on what synthetic data is generated, how it is filtered or labeled, the amount and quality of real data retained, model and objective changes, and the evaluated task. The present wiki evidence therefore supports a risk hypothesis, not inevitability or a universal direction of entropy change.

## Key Claims
- Recursive use of model-generated training data can reproduce mistakes and overrepresent high-probability patterns.
- Degradation is better framed as a data-distribution and quality-control risk than as a consequence of temperature alone.
- Entropy is not a single sufficient diagnosis: some feedback loops may add noise while others erase rare modes and narrow the distribution.
- Real-data mixture, provenance, filtering, task design, training objective, and evaluation determine whether synthetic data helps or harms.

## Evidence
- Feedback-loop claim: [[yu-yan-de-bian-jie-jiu-shi-si-wei-de-bian-jie]] reports that repeatedly training on model-generated text causes performance to regress.
- Proposed mechanism: [[yu-yan-de-bian-jie-jiu-shi-si-wei-de-bian-jie]] attributes the regression to temperature-based randomness and increasing entropy across iterations.
- Evidentiary gap: [[yu-yan-de-bian-jie-jiu-shi-si-wei-de-bian-jie]] names no paper, experiment, model, task, data mixture, metric, or number of recursive rounds.

## Counterevidence & Qualifications
This page currently rests on one secondary, uncited description rather than an inspected study. The source moves from stochastic generation to inevitable degradation without showing the intermediate causal steps. Carefully generated, verified, or task-targeted synthetic data may differ materially from unfiltered self-consumption, and retaining sufficient real data can change the outcome. “Model collapse” should therefore not be used as a blanket claim that all synthetic data is harmful or that every recursive pipeline converges to meaningless text.

## What Changed
- Created the concept as a qualified recursive-training risk.
- Replaced the source's temperature-only explanation with an explicit multi-variable evidence boundary.

## Related Concepts
- [[LanguageModeling]] - model collapse concerns how the learned sequence distribution changes with the training corpus.
- [[TextGenerationSampling]] - sampling controls generated examples but does not by itself determine later training outcomes.
- [[SemanticAblation]] - both concepts describe possible distributional flattening, though one concerns training feedback and the other rewriting.
- [[MachineLearningDataMoats]] - synthetic data changes the value and risk profile of task-relevant training data.

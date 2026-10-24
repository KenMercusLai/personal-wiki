---
title: "Model Collapse"
type: concept
tags: [ai, training-data, synthetic-data, model-quality]
sources:
  - yu-yan-de-bian-jie-jiu-shi-si-wei-de-bian-jie
  - sspai-110102
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Definition
[[ModelCollapse]] is degradation or distributional narrowing attributed to training successive models on recursively generated model outputs, especially when synthetic material displaces diverse, high-quality real data or preserves earlier errors.

## Current Synthesis
The sources present related feedback-loop warnings: generated data can reproduce errors, overrepresent probable patterns, and turn a model's own stylistic defaults into a progressively narrower substitute for the distribution it was meant to learn. One source proposes a temperature-driven entropy mechanism; Losses Don instead connects AI-heavy web text, synthetic generation, cross-model distillation, and repeated reuse of homogenized outputs to declining usability despite better benchmark scores.

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
- Web-mixture warning: [[sspai-110102]] cites an Ahrefs detector study reporting that 74.2% of 900,000 newly found English webpages contained some AI-generated content, including 71.7% human-AI mixtures, then argues that such material may enter later training corpora.
- Recursive-style warning: [[sspai-110102]] argues that heavily post-trained, homogenized output can be generated, distilled, and consumed again, but supplies no corpus provenance, training run, ablation, or downstream quality measure establishing that chain.

## Counterevidence & Qualifications
This page rests on two secondary practitioner descriptions rather than an inspected recursive-training study. The sources move from sampling, AI-content prevalence, stylistic homogeneity, or suspected distillation to inevitable degradation without demonstrating the intermediate causal chain. The Ahrefs figures concern detector classifications of sampled webpages, not training-corpus inclusion or model outcomes, and detector error and sampling design are not examined here. Carefully generated, verified, or task-targeted synthetic data may differ materially from unfiltered self-consumption, and retaining sufficient real data can change the outcome. “Model collapse” should therefore not be used as a blanket claim that all synthetic data is harmful or that every recursive pipeline converges to meaningless text.

## What Changed
- Added web-content prevalence and cross-model reuse as possible exposure paths without treating either as proof of collapse.
- Strengthened the boundary between measured AI-content detection and unmeasured training-corpus or model-quality effects.

## Related Concepts
- [[LanguageModeling]] - model collapse concerns how the learned sequence distribution changes with the training corpus.
- [[TextGenerationSampling]] - sampling controls generated examples but does not by itself determine later training outcomes.
- [[SemanticAblation]] - both concepts describe possible distributional flattening, though one concerns training feedback and the other rewriting.
- [[MachineLearningDataMoats]] - synthetic data changes the value and risk profile of task-relevant training data.

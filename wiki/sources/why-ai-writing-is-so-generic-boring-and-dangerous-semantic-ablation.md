---
title: "Why AI writing is so generic, boring, and dangerous: Semantic ablation"
type: source
tags: [ai, writing, language-models, opinion]
date: 2026-02-16
source_file: "/mnt/ken_personal_wiki/Articles/Why AI writing is so generic, boring, and dangerous Semantic ablation.md"
---

## Summary
This Register opinion article proposes [[SemanticAblation]] as the subtractive counterpart to hallucination: instead of adding false material, AI rewriting removes rare vocabulary, precise technical distinctions, unconventional metaphors, subtext, and non-linear structure. It argues that repeated "refinement" pushes writing toward probable, low-friction language, describes metaphoric cleansing, lexical flattening, and structural collapse as three stages of that loss, and calls the result a "JPEG of thought." The article links the tendency to greedy decoding and reinforcement learning from human feedback, but offers the mechanism and entropy-decay test as a thesis rather than reporting an experiment or measurements.

## Key Claims
- [[SemanticAblation]] names the loss of distinctive meaning during AI rewriting, complementing hallucination's better-known addition of unsupported content.
- AI "polishing" can replace rare, exact, domain-specific, or emotionally vivid language with common and generic alternatives, making prose smoother while reducing semantic density.
- The proposed loss unfolds through three stages: unconventional imagery becomes cliché, precise terminology becomes broad vocabulary, and complex reasoning becomes a predictable template.
- Repeated refinement should be measurable as entropy decay, with vocabulary diversity such as type-token ratio falling over successive passes.
- The article attributes the tendency to probability-maximizing decoding and reinforcement learning from human feedback that rewards safe, helpful, low-friction outputs.
- Accepting flattened output at scale risks a broader "race to the middle" in which standardized fluency displaces difficult, idiosyncratic, or high-information thought.

## Key Quotes
> "JPEG of thought" - the article's metaphor for text that remains coherent on the surface after losing much of its original information density.

> "If 'hallucination' describes the AI seeing what isn't there, semantic ablation describes the AI destroying what is." - the proposed contrast between additive and subtractive model failure.

## Connections
- [[SemanticAblation]] - central term for the claimed erosion of rare, precise, and structurally complex information.
- [[AIAssistedWriting]] - AI revision needs a fidelity check for meaning, voice, specificity, and argument structure, not only fluency.
- [[TextGenerationSampling]] - the article attributes flattening partly to probability-maximizing token selection.
- [[NaturalLanguageGeneration]] - fluent continuation can remain locally coherent while drifting toward statistically common language.
- [[AIEraCreativeStandards]] - cheap smooth prose raises the value of distinctive material, taste, and deliberate preservation of specificity.
- [[AIDependencySkillAtrophy]] - repeated acceptance of generic rewrites may weaken the writer's exercise of voice and editorial judgment.

## Contradictions
- No direct contradiction with the wiki's existing generation material: [[what-is-chatgpt-doing-and-why-does-it-work]] also shows that always choosing the highest-probability token produces flat, repetitive text.
- The article nevertheless overstates mechanism relative to its evidence. It does not report the model, prompts, decoding settings, number of passes, type-token-ratio results, comparison texts, or controls needed to show that greedy decoding or reinforcement learning from human feedback caused the proposed three-stage pattern.
- Vocabulary diversity is only a proxy for retained meaning: a lower type-token ratio can reflect legitimate clarification or compression, while ornate or rare wording can preserve voice without improving truth or reasoning.

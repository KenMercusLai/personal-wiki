---
title: "GPT-2"
type: entity
tags: [ai, nlp, transformer]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Overview
[[GPT2]] is the pretrained transformer language model the wiki's sources use as their runnable large-model example: small enough to load and inspect on a desktop, and large enough to show the shift from tutorial-scale models to pretrained generation.

## Current Profile
The tutorial treats GPT-2 as the destination of its language-modeling ladder. It says OpenAI released GPT-2 in February 2019, describes it as trained on 40GB of curated internet text, and loads its tokenizer and language-model head through PyTorch-Transformers for next-word prediction and longer conditional generation.

The Wolfram essay uses the same model for a different purpose: it is the reference system whose insides can actually be examined. There, GPT-2's embedding module adds a 768-number token embedding to a 768-number position embedding; it has 12 attention blocks of 12 heads each and a ~50,257-token vocabulary; and the essay plots its attention-head recombination weights, its 768-by-768 fully connected weight matrices, and their moving averages. It is also the model that tests the sample-generation comparison, the embedding projections, and the parenthesis-language experiment, in which a two-block transformer converges after about ten million examples and still fails on longer balanced sequences. The essay is clear that GPT-2's outputs are weaker than GPT-3's, which is exactly why it can be run and inspected.

## Key Characteristics
- Serves as the sources' example of a large pretrained transformer language model.
- Is credited to OpenAI and described as released in February 2019 and trained on 40GB of curated internet text.
- Is loaded through PyTorch-Transformers in one source and through Wolfram's model repository in the other.
- Uses a 768-number embedding width, 12 attention blocks, 12 heads per block, and roughly 50,257 tokens in the essay's account.
- Computes token and position embeddings separately and adds them to form the input representation, which makes it inspectable in practice: its next-token probabilities, attention weights, and weight matrices are all plotted in the source.
- Produces visibly weaker continuations than the largest GPT-3 model on the same prompt, which the essay uses as its scale comparison.
- Successfully completes "What is the fastest car in the" with "world" in the tutorial, and generates a poem-like continuation from a Robert Frost prompt.

## Evidence
- Model description: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] calls GPT-2 a transformer-based generative language model trained on 40GB of curated internet text.
- OpenAI connection: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] says OpenAI released GPT-2 in February 2019.
- Library use: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] loads `GPT2Tokenizer` and `GPT2LMHeadModel` from PyTorch-Transformers.
- Completion screenshot: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] shows GPT-2 predicting "world" for the car prompt.
- Conditional generation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses the PyTorch-Transformers generation script to continue "The Road Not Taken".
- Architecture numbers: [[what-is-chatgpt-doing-and-why-does-it-work]] gives GPT-2 12 attention blocks, 12 heads, and 768-number embeddings, and contrasts them with GPT-3's 96/96/12,288.
- Embedding module: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the token embedding and position embedding being added, with an input port of n indices ranging over about 50,257 tokens.
- Inspected internals: [[what-is-chatgpt-doing-and-why-does-it-work]] plots the twelve heads' look-back patterns for a fixed string, the 768-by-768 weight matrix, and its moving average.
- Scale comparison: [[what-is-chatgpt-doing-and-why-does-it-work]] says the same prompt continued with the largest GPT-3 model gives better results than GPT-2.
- Experiment platform: [[what-is-chatgpt-doing-and-why-does-it-work]] uses a two-block transformer with 8 heads and 128-wide features for the parenthesis-language experiment, and notes that the full system also struggles with long parenthesis matching.

## Qualifications
The sources describe GPT-2 from a 2019 tutorial and an early-2023 essay. They do not cover its full release history, model sizes, licensing, current hosting, or safety research, and the architecture numbers are from the essay's reference implementation rather than official documentation. The parenthesis experiment uses a small custom transformer rather than GPT-2 itself.

## What Changed
- Created an entity profile for GPT-2 as used in the tutorial.
- Added the inspection role: embedding widths, block and head counts, attention and weight-matrix visualizations, and the scale comparison with GPT-3.

## Relationships
- [[OpenAI]] - credited source of GPT-2 in both sources.
- [[PyTorchTransformers]] - library used to run GPT-2 examples in the tutorial.
- [[WolframLanguage]] - environment used to run and inspect GPT-2 in the essay.
- [[NeuralLanguageModel]] - GPT-2 is presented as a large neural language model.
- [[TransformerArchitecture]] - the architecture whose internals the essay plots on this model.
- [[AttentionMechanism]] - GPT-2's heads supply the inspected look-back patterns.
- [[Embeddings]] - the token and position vectors the model adds together.
- [[NaturalLanguageGeneration]] - GPT-2 performs sentence completion and conditional text generation.

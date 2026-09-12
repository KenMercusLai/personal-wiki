---
title: "GPT-2"
type: entity
tags: [ai, nlp, transformer]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[GPT2]] is the pretrained transformer-based generative language model used in the tutorial's sentence-completion and conditional-generation examples.

## Current Profile
In the source, GPT-2 represents the shift from small tutorial-trained models to large pretrained language models. The article says OpenAI released GPT-2 in February 2019, describes it as trained on 40GB of curated internet text, and uses PyTorch-Transformers to load its tokenizer and language-model head for next-word prediction and longer generation.

## Key Characteristics
- Serves as the tutorial's example of a large pretrained transformer language model.
- Is credited to OpenAI in the source.
- Is loaded through PyTorch-Transformers for local inference examples.
- Successfully completes the prompt "What is the fastest car in the" with "world" in the tutorial.
- Generates a poem-like continuation from a Robert Frost prompt in the conditional-generation example.

## Evidence
- Model description: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] calls GPT-2 a transformer-based generative language model trained on 40GB of curated internet text.
- OpenAI connection: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] says OpenAI released GPT-2 in February 2019.
- Library use: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] loads `GPT2Tokenizer` and `GPT2LMHeadModel` from PyTorch-Transformers.
- Completion screenshot: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] shows GPT-2 predicting "world" for the car prompt.
- Conditional generation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses the PyTorch-Transformers generation script to continue "The Road Not Taken".

## Qualifications
This page reflects the tutorial's 2019 description and does not cover GPT-2's full release history, model sizes, license terms, current hosting, safety research, or modern successor models.

## What Changed
- Created an entity profile for GPT-2 as used in the tutorial.

## Relationships
- [[OpenAI]] - credited source of GPT-2 in the article.
- [[PyTorchTransformers]] - library used to run GPT-2 examples.
- [[NeuralLanguageModel]] - GPT-2 is presented as a large neural language model.
- [[NaturalLanguageGeneration]] - GPT-2 performs sentence completion and conditional text generation.

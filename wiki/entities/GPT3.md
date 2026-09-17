---
title: "GPT-3"
type: entity
tags: [ai, llm, transformer, model]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Overview
[[GPT3]] is the large transformer language model the source identifies as the network behind ChatGPT: about 175 billion weights, trained on a few hundred billion words, and large enough that its generated text improves visibly over the smaller models the essay uses for runnable examples.

## Current Profile
The source positions GPT-3 as the scale step that makes the essay's ideas about language plausible. Alongside the runnable [[GPT2]] experiments, it shows zero-temperature and temperature-0.8 continuations from the largest GPT-3 model and reports that they are better than the GPT-2 equivalents. Architecturally the essay describes ChatGPT's network as a GPT-3 variant with 96 attention blocks of 96 heads each and embedding vectors of 12,288 numbers, compared with GPT-2's 12 blocks, 12 heads, and 768 numbers. It also reports the odd ratio that matters for the essay's information argument: the network has roughly as many weights as the training corpus has words, with a few hundred billion of each, and about 3,000 of the ~50,000 tokens are whole words while the rest are fragments.

## Key Characteristics
- About 175 billion weights, described as comparable in number to the words of training text.
- 96 attention blocks with 96 attention heads each, and embedding vectors of 12,288 numbers in ChatGPT's version.
- Produces noticeably better continuations than GPT-2 on the same prompts, which the source uses as its scale comparison.
- Trained on a few hundred billion words, some seen once and some repeatedly.
- Uses roughly 50,000 tokens, of which only about 3,000 are whole words.
- Represented by the source as the base network that human feedback then tunes into a usable assistant.

## Evidence
- Scale and quality comparison: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the same prompt continued by the biggest GPT-3 model at zero temperature and at temperature 0.8, and says the results are better than GPT-2's.
- Weight count: [[what-is-chatgpt-doing-and-why-does-it-work]] states the network is a version of GPT-3 with 175 billion weights.
- Architecture numbers: [[what-is-chatgpt-doing-and-why-does-it-work]] contrasts GPT-3's 96 attention blocks, 96 heads, and 12,288-number embeddings with GPT-2's 12 blocks, 12 heads, and 768 numbers.
- Training data: [[what-is-chatgpt-doing-and-why-does-it-work]] says ChatGPT was successfully trained on a few hundred billion words, with some text fed more than once.
- Token inventory: [[what-is-chatgpt-doing-and-why-does-it-work]] says about 50,000 tokens are used, only about 3,000 of them whole words.
- Feedback stage: [[what-is-chatgpt-doing-and-why-does-it-work]] describes an additional human-feedback step after raw training that tunes the network towards being a good chatbot.

## Qualifications
All GPT-3 figures come from a single 2023 essay and describe the model family behind ChatGPT at that time. The wiki should not treat them as current OpenAI documentation, and the essay itself says there is no theory explaining why this scale of network works as well as it does.

## What Changed
- Created the entity page for GPT-3 as the network the source identifies behind ChatGPT.

## Relationships
- [[ChatGPT]] - the assistant built on this network.
- [[GPT2]] - the smaller model used in the same essay for runnable examples and scale comparison.
- [[OpenAI]] - the lab credited with the model in the source.
- [[TransformerArchitecture]] - the architecture both GPT-2 and GPT-3 instantiate at different scales.
- [[NeuralNetworkTraining]] - training on a few hundred billion words is the process that sets the weights.
- [[Embeddings]] - GPT-3's 12,288-number vectors represent tokens and positions.

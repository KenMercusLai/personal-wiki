---
title: "Transformer Architecture"
type: concept
tags: [ai, neural-networks, language, architecture]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[TransformerArchitecture]] is the neural-network layout used by GPT-style language models: an embedding module that turns tokens and their positions into vectors, a stack of identical attention blocks that repeatedly recombine those vectors, and a final decode step that turns the last vector into probabilities over the next token.

## Current Synthesis
The source describes the transformer as a sequence-specific alternative to fully connected or convolutional layouts. Instead of restricting connections to a fixed local window, each attention block lets the model look back over the whole sequence so far and decide which earlier tokens matter for the next one - the mechanism the source credits with capturing the nested, tree-like structure of language. The pipeline has three stages: embed the token sequence, run it through the attention blocks, then take the last embedding and decode it into roughly 50,000 token probabilities. Everything except the overall architecture is learned end-to-end, so the essay treats the specific choices inside the blocks as engineering lore rather than derived design.

The concrete figures the source inspects for [[GPT2]] make the shape of the architecture visible: an embedding module that adds a token-value embedding to a position embedding to produce one 768-number vector per token, 12 attention blocks each containing 12 attention heads, and within each block a fully connected path that expands the 768-number vector to 3,072 and back with normalization and residual additions. Scaling this to ChatGPT's [[GPT3]] means 12,288-number embeddings and 96 blocks with 96 heads each. Looking inside, the essay finds that different blocks' weight matrices look superficially similar but have different weight-size distributions, and that the learned structure is real but not human-readable.

## Key Claims
- The transformer replaces fixed local connectivity with attention, letting each token draw on any earlier token in the sequence.
- The pipeline is embedding, then repeated attention blocks, then decoding the final embedding into next-token probabilities.
- Token embeddings and position embeddings are computed separately and simply added together; the source reports no theory for why addition works, only that it does.
- Each attention block contains multiple independently operating heads that split the embedding vector into chunks, plus a fully connected path, normalization, and residual additions.
- Scale is expressed in the same three numbers: embedding width, block count, and head count - 768/12/12 for GPT-2 and 12,288/96/96 for ChatGPT's GPT-3.
- The architecture was found empirically rather than derived, and the essay describes its internal choices as arbitrary-looking engineering decisions validated by training.
- Interpretability is limited: block weight matrices can be visualized and moving-averaged, but what features they encode remains unknown.

## Evidence
- Purpose of attention: [[what-is-chatgpt-doing-and-why-does-it-work]] contrasts transformers with convolutional nets and says attention lets a model attend to much earlier words, such as a verb referring to a noun many words back.
- Pipeline stages: [[what-is-chatgpt-doing-and-why-does-it-work]] describes embedding the tokens so far, passing the embedding through successive layers, then producing ~50,000 next-token values.
- Embedding module: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the GPT-2 graph in which token embeddings and position embeddings are added to give an n-by-768 output, with an input port of n indices in the range 1 to 50257.
- Attention block internals: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the GPT-2 block graph with 12 heads of width 64, a 768-to-3072-to-768 fully connected path, normalization, and residual additions.
- Scaling numbers: [[what-is-chatgpt-doing-and-why-does-it-work]] pairs GPT-2's 12 blocks, 12 heads, and 768-number vectors with GPT-3's 96 blocks, 96 heads, and 12,288-number vectors.
- Learned but unreadable structure: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a 768-by-768 weight matrix with no visible structure and a 64-by-64 moving average with random-walk-like structure, and reports that the features being encoded are unknown.
- Block-to-block variation: [[what-is-chatgpt-doing-and-why-does-it-work]] shows that the weight matrices of different attention blocks look similar while their weight-size distributions differ.
- No internal looping: [[what-is-chatgpt-doing-and-why-does-it-work]] notes that generating one token pushes data once through the network with no looping, so there is only an outer loop over generated tokens.

## Counterevidence & Qualifications
The source is a printed explanation of a 2023 GPT-3-class model, not an architecture specification: it names layers and sizes without hyperparameter, initialization, or training details, and it repeatedly says the design choices lack theory. The "why addition works" and "why heads split the vector" questions are explicitly left open, and later transformer variants, tool use, retrieval, or multimodal inputs are outside the source's scope.

## What Changed
- Created the concept page for the transformer layout used by GPT-style language models.

## Related Concepts
- [[AttentionMechanism]] - the look-back recombination performed inside every block.
- [[Embeddings]] - the vectors the embedding module produces, including the position pathway.
- [[NeuralNetwork]] - the general model class this architecture is an instance of.
- [[NeuralNetworkTraining]] - the process that determines all the weights in the layout.
- [[NaturalLanguageGeneration]] - the decoding step that turns the final embedding into the next token.
- [[MeaningSpace]] - the geometry of the embedding vectors the blocks transform.

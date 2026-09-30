---
title: "Positional Encoding"
type: concept
tags: [ai, transformers, sequence-modeling, embeddings]
sources:
  - jay-alammar-the-illustrated-transformer
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[PositionalEncoding]] is an explicit vector signal combined with token embeddings so an attention-based model can distinguish sequence positions and use token order.

## Current Synthesis
Self-attention compares vector content but does not inherently know whether one token came first, second, or later. The original Transformer addresses this by adding a deterministic position vector to every token embedding before the first encoder or decoder layer. Because addition preserves the model width, all later query, key, and value projections receive a representation containing both token and position information.

The illustrated base model uses sine and cosine functions at different frequencies across dimensions, producing a structured pattern bounded between -1 and 1. The article initially shows a Tensor2Tensor implementation with sine values in one half of the vector and cosine values in the other; its 2020 correction distinguishes the paper's interleaved even and odd sine/cosine dimensions. The sinusoidal construction is presented as able to extend to sequence lengths not seen in training, but the source does not compare it with learned positions or later relative and rotary schemes.

## Key Claims
- Attention needs an explicit order signal because content-only comparisons are permutation-insensitive.
- The original Transformer adds, rather than concatenates, one position vector to each token embedding.
- Sine and cosine waves at different frequencies give each position a structured multi-dimensional signature.
- The paper interleaves sine and cosine dimensions, while the older Tensor2Tensor visualization concatenates two halves.
- Deterministic sinusoidal positions can be evaluated beyond the maximum sequence length observed during training.

## Evidence
- Placement in the model: [[jay-alammar-the-illustrated-transformer]] diagrams a position vector added to each word embedding before the encoder stack and again for decoder inputs.
- Toy values: [[jay-alammar-the-illustrated-transformer]] shows three four-dimensional position vectors added to the embeddings for “Je suis étudiant.”
- Frequency structure: [[jay-alammar-the-illustrated-transformer]] includes heatmaps whose rows are token positions and columns are embedding dimensions, making the slow and fast periodic components visible.
- Implementation distinction: [[jay-alammar-the-illustrated-transformer]] explicitly corrects the original concatenated Tensor2Tensor illustration with a heatmap of the paper's interleaved sine/cosine formulation.

## Counterevidence & Qualifications
The source explains one absolute sinusoidal method and does not compare learned absolute positions, relative position biases, rotary position embeddings, or their length-generalization behavior. Adding a position signal makes order available to the network but does not guarantee that it will learn every ordering relation. The claim about extrapolating to unseen lengths is architectural intuition in this source rather than an evaluated benchmark.

## What Changed
- Created the concept with the original Transformer's additive sinusoidal position signal.
- Preserved the source's correction between concatenated implementation output and interleaved paper formulation.

## Related Concepts
- [[TransformerArchitecture]] - consumes position-enriched token embeddings at the bottom of its stacks.
- [[AttentionMechanism]] - requires an added signal to distinguish ordering that content similarity alone omits.
- [[Embeddings]] - token and position vectors share a width and are combined by addition.
- [[NaturalLanguageProcessing]] - word order materially affects translation and other language tasks.

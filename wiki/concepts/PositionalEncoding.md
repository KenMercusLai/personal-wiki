---
title: "Positional Encoding"
type: concept
tags: [ai, transformers, sequence-modeling, embeddings]
sources:
  - jay-alammar-the-illustrated-transformer
  - designing-positional-encoding
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[PositionalEncoding]] is a deterministic or learned mechanism that makes sequence or spatial position available to an attention-based model, whether by adding a position vector to token embeddings or by changing query-key interactions directly.

## Current Synthesis
Self-attention compares vector content but does not inherently know whether one token came first, second, or later. More precisely, content-only self-attention is permutation equivariant: permuting the inputs permutes the outputs, and repeated identical inputs cannot be distinguished by index alone. The original Transformer addresses this by adding a deterministic position vector to every token embedding before the first encoder or decoder layer. Because addition preserves the model width, all later query, key, and value projections receive a representation containing both token and position information.

The illustrated base model uses sine and cosine functions at different frequencies across dimensions, producing a structured pattern bounded between -1 and 1. The article initially shows a Tensor2Tensor implementation with sine values in one half of the vector and cosine values in the other; its 2020 correction distinguishes the paper's interleaved even and odd sine/cosine dimensions. A second source explains why pairing sine with cosine matters: advancing a pair by a fixed offset is exactly a two-dimensional rotation, so relative displacement has a simple linear representation.

That rotation perspective leads to [[RotaryPositionalEncoding]]. Instead of adding an absolute position vector before projection, RoPE rotates paired coordinates of queries and keys before their dot product. Rotation preserves their norms while changing their relative angle, allowing position to modulate attention scores directly. This clean semantic-versus-positional separation is a useful geometric account, not proof that RoPE extrapolates without limit: the source cites evidence that models may underuse parts of its frequency spectrum and that removing the lowest frequencies improved one evaluated Gemma 2B setting. For multiple spatial dimensions, separate feature pairs can encode each axis independently rather than mixing horizontal and vertical offsets.

## Key Claims
- Attention needs an explicit order signal because content-only comparisons are permutation-insensitive.
- The original Transformer adds, rather than concatenates, one position vector to each token embedding.
- Sine and cosine waves at different frequencies give each position a structured multi-dimensional signature.
- Paired sine and cosine values turn a fixed position offset into a linear rotation.
- RoPE moves position into query-key geometry, preserving vector norms while making attention depend on relative displacement.
- Multidimensional rotary schemes should allocate independent feature pairs to each coordinate axis.
- Deterministic formulas permit evaluation beyond trained sequence lengths, but architectural availability does not guarantee reliable extrapolation.

## Evidence
- Placement in the model: [[jay-alammar-the-illustrated-transformer]] diagrams a position vector added to each word embedding before the encoder stack and again for decoder inputs.
- Toy values: [[jay-alammar-the-illustrated-transformer]] shows three four-dimensional position vectors added to the embeddings for “Je suis étudiant.”
- Frequency structure and implementation: [[jay-alammar-the-illustrated-transformer]] shows slow and fast periodic components and corrects its older concatenated Tensor2Tensor visualization against the paper's interleaved sine/cosine formulation; [[designing-positional-encoding]] derives the paired functions as offset-dependent rotation matrices.
- Design progression: [[designing-positional-encoding]] compares raw integer, length-normalized, binary, sinusoidal, and rotary approaches against consistency, smoothness, extrapolation, and dimensional-extension goals.
- Attention integration: [[designing-positional-encoding]] applies rotations to paired query and key coordinates before their dot product, rather than adding another vector to token embeddings.
- Multiple dimensions: [[designing-positional-encoding]] assigns independent rotations to feature pairs for each spatial axis so relative offsets remain separated.

## Counterevidence & Qualifications
The sources do not compare learned absolute positions, relative attention biases, or the broader family of long-context extensions under a shared benchmark. Adding a position signal makes order available to the network but does not guarantee that it will learn every ordering relation. Deterministic formulas can be evaluated at unseen indices, yet useful length extrapolation remains empirical and may fail when frequency use, training distribution, precision, or attention behavior changes. The RoPE source cites external performance evidence rather than reproducing experiments, and its five desirable properties are design criteria rather than a proof of universal optimality. Its repeated-token demonstration applies to identical position-free inputs; contextualized occurrences need not remain identical after earlier layers.

## What Changed
- Broadened the concept from additive vectors to mechanisms that alter query-key interactions directly.
- Added the rotation derivation that makes sinusoidal offsets linear and motivates RoPE.
- Added norm-preserving relative encoding, multidimensional axis separation, and explicit extrapolation limits.

## Related Concepts
- [[TransformerArchitecture]] - consumes position-enriched token embeddings at the bottom of its stacks.
- [[AttentionMechanism]] - requires an added signal to distinguish ordering that content similarity alone omits.
- [[RotaryPositionalEncoding]] - injects relative position by rotating queries and keys instead of adding an absolute vector.
- [[Embeddings]] - token and position vectors share a width and are combined by addition.
- [[NaturalLanguageProcessing]] - word order materially affects translation and other language tasks.

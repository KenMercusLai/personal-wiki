---
title: "You could have designed state of the art positional encoding"
type: source
tags: [transformers, positional-encoding, rope, self-attention, multimodal]
date: 2024-11-25
source_file: "/mnt/ken_personal_wiki/Articles/designing-positional-encoding.md"
---

## Summary
FL33TW00D-HF develops [[PositionalEncoding]] as an iterative design problem, moving from integer and binary codes through the original Transformer's additive sinusoids to [[RotaryPositionalEncoding]] applied multiplicatively to queries and keys. The derivation connects paired sine and cosine coordinates to rotation matrices, then shows why rotating query-key pairs makes attention scores depend on relative position without changing vector norms. The article also sketches independent per-axis rotations for multidimensional inputs and notes that RoPE still has frequency-use and length-generalization limits.

## Key Claims
- Content-only [[AttentionMechanism|self-attention]] is permutation equivariant: identical token embeddings in different positions produce identical outputs unless some position-dependent signal distinguishes them.
- A useful position scheme should be sequence-length-independent, relate positions through a simple transformation, extrapolate beyond training lengths, arise deterministically, and extend to multiple spatial dimensions.
- Adding raw integer positions overwhelms small embedding coordinates, while normalized integers become sequence-length-dependent and binary codes change discontinuously.
- Paired sine and cosine coordinates provide bounded, smooth signals whose value at an offset can be obtained by a two-dimensional rotation matrix.
- Absolute position is often less useful than the displacement between tokens, and additive position vectors mix semantic and positional information before query, key, and value projection.
- [[RotaryPositionalEncoding]] rotates two-coordinate chunks of queries and keys before their dot product, preserving each vector's norm while making the score depend on relative position.
- For multidimensional inputs, coordinates from each axis should rotate separate feature pairs so horizontal, vertical, and higher-dimensional offsets do not become intermixed.

## Key Quotes
> “what matters is how words relate to each other” — on preferring relative relationships to absolute indices.

> “Shifting to multiplicative is the key.” — on moving the position operation into query-key geometry.

## Connections
- [[PositionalEncoding]] — the broader design problem and the progression from additive absolute codes to relative methods.
- [[RotaryPositionalEncoding]] — the principal method derived from sinusoidal rotations and attention dot products.
- [[AttentionMechanism]] — the position signal is needed because content-only self-attention does not distinguish permutations.
- [[Embeddings]] — integer and additive encodings are evaluated partly by how they affect the scale and semantic content of token vectors.
- [[TransformerArchitecture]] — the model family in which the compared position schemes operate.

## Contradictions
- The article calls RoPE state of the art and cites its use in Llama 3.2, but it also cites later analysis showing that standard RoPE is not final: models may underuse some frequencies, and removing the lowest frequencies reportedly improves one Gemma 2B setting.
- The five desirable properties are design criteria proposed by the author, not a benchmark proving that RoPE satisfies every property under arbitrary context lengths, dimensions, or low-precision deployment.
- The motivating PyTorch demonstration establishes symmetry for repeated, position-free token inputs in that construction; it does not show that two occurrences of the same token remain identical once their surrounding hidden states have already become contextualized.
- The article attributes empirical gains to RoPE through a linked external post rather than reproducing comparative experiments, datasets, metrics, or implementation controls.
- The embedded animations illustrate integer, binary, sinusoidal, and rotary behavior, but they are externally hosted videos rather than local image references; their substantive claims are also described in the prose and equations.

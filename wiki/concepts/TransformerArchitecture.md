---
title: "Transformer Architecture"
type: concept
tags: [ai, neural-networks, language, architecture]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
  - jay-alammar-the-illustrated-transformer
  - transformer-jia-gou-bian-hua-rmsnorm-zhi-nan
  - transformer-architectures
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[TransformerArchitecture]] is a neural-network architecture for sequences that combines vector embeddings, repeated attention and positionwise feed-forward layers, residual pathways, normalization, and output projection; encoder-decoder, encoder-only, and decoder-only systems select different parts and masks from that family.

## Current Synthesis
The original machine-translation Transformer has two stacks. A six-layer encoder contextualizes all input positions through self-attention and positionwise feed-forward networks. A six-layer autoregressive decoder uses masked self-attention over the output generated so far, cross-attention over the top encoder representation, and a final linear-plus-softmax stage that produces the next output token. Every sublayer has a residual path and [[LayerNormalization]], while token embeddings receive an added position signal because attention itself is order-agnostic. The encoder can process token paths in parallel, and training can score all known target positions together even though inference emits one token at a time.

GPT-style language models use the decoder-only branch of this design. In the inspected [[GPT2]] configuration, token and learned position embeddings produce 768-number states, followed by 12 blocks with 12 heads; the feed-forward path expands each state to 3,072 and contracts it again. The Wolfram source attributes 12,288-wide states, 96 blocks, and 96 heads to [[GPT3]]. The two sources therefore describe related but non-identical architectures: Alammar exposes the original encoder-decoder dataflow, while Wolfram follows causal next-token generation. Both agree that most internal transformations are learned end-to-end and that visualizing weights or attention does not by itself reveal the features represented.

The 2017 block skeleton persisted while many implementation choices changed. A 53-model survey describes a shift from post-norm, sinusoidal positions, ReLU, separate KV heads, and four-times-wide FFNs toward pre-normalization with [[RMSNorm]], [[RotaryPositionalEncoding]], [[SwiGLU]], [[GroupedQueryAttention]] or related KV sharing, and fewer biases. [[TransformerArchitecturalConvergence]] names this as a strong dense decoder-only default under current quality, stability, accelerator, and inference constraints—not a fixed definition or proof of global optimality. Sparse expert routing, long-context attention, and interventions such as [[QueryKeyNormalization]] remain less settled.

## Key Claims
- The architecture's reusable core is embedding plus repeated attention, feed-forward transformation, residual connection, and configurable normalization such as LayerNorm or RMSNorm, followed by task-specific output projection.
- The original Transformer separates a bidirectional encoder stack from an autoregressive decoder stack connected by cross-attention.
- Decoder-only GPT models retain causal self-attention and next-token decoding while omitting the separate encoder and its cross-attention path.
- Parallelism comes from removing recurrent state: encoder positions and training-time target positions can be computed together subject to masks, although inference remains sequential across generated tokens.
- Sequence order must be supplied explicitly, but the mechanism may add position vectors to embeddings or alter query-key interactions directly.
- Architectural scale can be summarized by state width, block count, and head count, but specific values such as 512/6/8 or 768/12/12 belong to particular model configurations.
- Modern dense decoder-only blocks have converged on a strong default bundle, while sparse routing, long-context attention, and stability controls remain active design variables.

## Evidence
- Original encoder-decoder flow: [[jay-alammar-the-illustrated-transformer]] diagrams the input-to-encoder, encoder-to-every-decoder, and decoder-to-vocabulary paths in both stacked and two-layer views.
- Repeating layer structure: [[jay-alammar-the-illustrated-transformer]] shows encoder self-attention plus feed-forward sublayers, decoder masked self-attention plus cross-attention and feed-forward sublayers, and residual add-and-normalize paths around each.
- Parallel token processing: [[jay-alammar-the-illustrated-transformer]] shows self-attention coupling positions followed by the same feed-forward network applied independently to each position.
- Position and output stages: [[jay-alammar-the-illustrated-transformer]] adds sinusoidal position vectors to embeddings and projects decoder outputs through a linear layer and softmax over the output vocabulary.
- GPT pipeline: [[what-is-chatgpt-doing-and-why-does-it-work]] describes embedding the tokens so far, passing them through successive causal attention blocks, and decoding the last representation into roughly 50,000 next-token values.
- GPT-2 and GPT-3 scale: [[what-is-chatgpt-doing-and-why-does-it-work]] pairs GPT-2's 768-number vectors, 12 blocks, and 12 heads with GPT-3's 12,288-number vectors, 96 blocks, and 96 heads.
- Interpretability boundary: [[what-is-chatgpt-doing-and-why-does-it-work]] visualizes block weights but says their encoded features remain unknown; [[jay-alammar-the-illustrated-transformer]] shows that many simultaneous head patterns quickly become difficult to read.
- Normalization evolution: [[jay-alammar-the-illustrated-transformer]] shows LayerNorm after residual additions in the original architecture; [[transformer-jia-gou-bian-hua-rmsnorm-zhi-nan]] explains RMSNorm's removal of mean subtraction and affine bias and reports growing use in later large models without quantifying adoption.
- Modern bundle: [[transformer-architectures]] reports RMSNorm, RoPE, GLU-family MLPs, and GQA becoming common across its selected 2017–2025 model sequence and identifies LLaMA as an influential integration point.
- Co-evolution boundary: [[transformer-architectures]] connects architecture choices to fused kernels, accelerator tile shapes, KV-cache memory, model-family copying, and reference implementations.

## Counterevidence & Qualifications
The Alammar source is a pedagogical account of the 2017 base Transformer, not a specification for every later variant; its six layers, eight heads, 512-wide states, post-sublayer normalization, and sinusoidal positions are configuration choices rather than defining invariants. The Wolfram source is a 2023 printed explanation that focuses on decoder-only GPT systems and leaves later attention, position, retrieval, tool-use, and multimodal variants outside scope. The RMSNorm guide is also explanatory: it delegates quality evidence to the original paper, and its handwritten multi-axis interface normalizes only the final axis. The architecture survey supplies adoption evidence but not controlled ablations: it favors publicly documented influential models, counts related family versions separately, and bundles quality, stability, hardware, inference economics, and path dependence. None of the sources isolates which component causes downstream capability, and readable diagrams or adoption charts should not be confused with full mechanistic or causal explanation.

## What Changed
- Recast post-norm, sinusoidal positions, ReLU, and four-times-wide FFNs as the original configuration rather than permanent invariants.
- Added the modern pre-RMSNorm, RoPE, SwiGLU, KV-sharing, and reduced-bias default bundle.
- Separated dense-model convergence from unsettled MoE, long-context, and stability choices.
- Added hardware, inference economics, and ecosystem path dependence as adoption forces.

## Related Concepts
- [[AttentionMechanism]] - supplies self-attention and encoder-decoder cross-attention inside the stacks.
- [[PositionalEncoding]] - injects sequence order into otherwise order-agnostic attention inputs.
- [[Embeddings]] - provides the token vectors transformed by the network.
- [[NeuralNetwork]] - the general learned function class instantiated by the architecture.
- [[NeuralNetworkTraining]] - adjusts projections, sublayers, and output probabilities end-to-end.
- [[NaturalLanguageGeneration]] - consumes the decoder's next-token probability distributions.
- [[NaturalLanguageProcessing]] - includes translation and language modeling applications built with Transformers.
- [[LayerNormalization]] - supplies mean-centering and variance scaling in the original illustrated architecture.
- [[RMSNorm]] - later normalization variant that keeps magnitude scaling while removing mean subtraction and affine bias.
- [[TransformerArchitecturalConvergence]] - describes concentration around a modern dense decoder-only recipe.
- [[SwiGLU]] - supplies the gated feed-forward sublayer common in the modern recipe.
- [[GroupedQueryAttention]] - reduces decoder KV-cache state through shared key-value heads.
- [[QueryKeyNormalization]] - controls attention-logit growth in some newer large models.

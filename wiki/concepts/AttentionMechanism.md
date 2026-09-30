---
title: "Attention Mechanism"
type: concept
tags: [ai, neural-networks, language, mechanism]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
  - jay-alammar-the-illustrated-transformer
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Definition
[[AttentionMechanism]] maps queries against keys to normalized relevance weights and uses those weights to combine values, letting each sequence position build a context-dependent representation from selected positions in the same or another sequence.

## Current Synthesis
Scaled dot-product attention makes the mechanism explicit. Learned matrices project input states into queries, keys, and values; query-key dot products measure compatibility, division by the square root of key width stabilizes their scale, softmax turns them into weights, and the weighted values are summed. Self-attention draws all three projections from one sequence. Encoder-decoder cross-attention draws queries from the decoder but keys and values from the encoder. A causal mask prevents decoder self-attention from reading future output positions.

Multi-head attention performs this calculation through several independent projection sets, concatenates the resulting matrices, and applies another learned output projection. This gives the layer several representation subspaces rather than one compulsory mixture. The visual examples show one head linking “it” to “animal” and another to “tired,” but all heads overlaid are harder to interpret; attention weights expose routing patterns, not a complete causal explanation of model behavior.

The broader evidence preserves a competence boundary. In Wolfram's balanced-parentheses experiment, a two-block model learns useful nested-sequence regularities after roughly ten million examples but still assigns probability to impossible continuations and degrades at longer lengths. Attention therefore expands context beyond fixed n-gram windows and can approximate structured dependencies, yet it does not automatically implement exact symbolic counting.

## Key Claims
- Attention computes a context-sensitive weighted sum of value vectors from query-key compatibility scores.
- Scaling scores by the square root of key width before softmax improves numerical and gradient stability in the illustrated formulation.
- Self-attention relates positions within one sequence, cross-attention connects decoder states to encoded input, and causal masking restricts access to future outputs.
- Multi-head attention uses independent learned projections, then concatenates and projects their outputs into one representation.
- Attention removes the fixed context window of an n-gram and lets positions directly use distant sequence information.
- Attention maps are inspectable but do not, by themselves, establish stable linguistic roles or explain the model's final decision.
- Learned attention can approximate nested dependencies while still failing exact algorithmic constraints at longer lengths.

## Evidence
- Query-key-value calculation: [[jay-alammar-the-illustrated-transformer]] walks from per-token projections and dot products through scaling, softmax, weighted values, and the compact matrix formula `softmax(QKᵀ / √dₖ)V`.
- Attention variants: [[jay-alammar-the-illustrated-transformer]] distinguishes encoder self-attention, masked decoder self-attention, and encoder-decoder attention whose queries come from the decoder while keys and values come from the encoder.
- Multiple heads: [[jay-alammar-the-illustrated-transformer]] shows eight independent projection sets, eight outputs, concatenation, and the learned output matrix, then visualizes different heads emphasizing “animal” and “tired.”
- Long-range context: [[what-is-chatgpt-doing-and-why-does-it-work]] contrasts attention with bigram prediction and describes heads as packaging the past for next-token prediction.
- Inspected GPT patterns: [[what-is-chatgpt-doing-and-why-does-it-work]] plots GPT-2 attention weights across heads and blocks, revealing structured causal look-back patterns.
- Nested-sequence test: [[what-is-chatgpt-doing-and-why-does-it-work]] reports that one attention block learns little on balanced parentheses, while two blocks converge but retain invalid continuation probability and fail as sequences lengthen.

## Counterevidence & Qualifications
The pronoun diagrams are individual visualizations, not evidence that heads always implement a fixed grammatical function; attention weights can be distributed, layer-dependent, and insufficient as a causal explanation. The original article's dimensions and eight-head configuration describe one model, not requirements of attention generally. Wolfram's parenthesis experiment is a small constructed task rather than a general benchmark, and its negative result bounds one trained configuration rather than proving that every attention-based system cannot count.

## What Changed
- Added the scaled query-key-value computation and matrix formulation.
- Distinguished self-attention, causal masked attention, and encoder-decoder cross-attention.
- Reframed head visualizations as useful routing evidence with an explicit interpretability limit.

## Related Concepts
- [[TransformerArchitecture]] - organizes attention into encoder, decoder, or decoder-only blocks.
- [[PositionalEncoding]] - supplies order information that attention scores do not contain on their own.
- [[Embeddings]] - provides the vectors projected into queries, keys, and values.
- [[NGramLanguageModel]] - fixed local context is the baseline that attention generalizes.
- [[ComputationalIrreducibility]] - helps frame why approximate sequence weighting need not perform exact computation.
- [[NeuralNetworkTraining]] - learns every projection and output matrix used by attention.

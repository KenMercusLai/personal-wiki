---
title: "让研究人员绞尽脑汁的 Transformer 位置编码"
type: source
tags: [transformers, positional-encoding, attention, sequence-modeling]
date: 2021-03-23
source_file: "/mnt/ken_personal_wiki/Articles/让研究人员绞尽脑汁的Transformer位置编码 - 科学空间|Scientific Spaces.md"
---

## Summary
This Scientific Spaces survey organizes [[PositionalEncoding]] into absolute methods that alter token inputs, relative methods that alter [[AttentionMechanism|attention]] interactions, and less conventional mechanisms that expose position through recurrence, padding boundaries, or complex-valued geometry. It compares learned, sinusoidal, recurrent, multiplicative, clipped, bucketed, Transformer-XL, T5, DeBERTa, CNN, and complex formulations, then derives a paired-coordinate rotation that anticipates the core query-key geometry of [[RotaryPositionalEncoding]]. The article is strongest as a mathematical taxonomy; several performance and extrapolation claims are preliminary, cited secondhand, or not tested under a common benchmark.

## Key Claims
- Content-only self-attention cannot distinguish token order by itself, so a [[TransformerArchitecture|Transformer]] needs either position-dependent inputs or position-dependent attention interactions.
- Absolute encodings attach a vector determined by index to each token representation; learned tables are flexible but length-bounded by default, sinusoidal formulas are defined beyond the training range, and recurrent or ODE-generated codes trade parallelism for flexibility.
- Relative encodings make attention depend on displacement such as `i-j`; clipping allows a finite table to cover arbitrary distances, while Transformer-XL uses sinusoidal relative vectors and learned global biases.
- T5 reduces position to a trainable attention-logit bias and buckets increasingly distant offsets more coarsely, expressing the assumption that nearby differences deserve finer resolution.
- DeBERTa retains content-to-position and position-to-content interactions while dropping the position-to-position term, illustrating that relative schemes choose different parts of the expanded absolute-position attention score.
- CNN position awareness can arise partly from zero-padding boundaries and local propagation, a mechanism that does not transfer directly to globally connected attention.
- Rotating paired query and key coordinates by their absolute positions makes their inner product depend on the relative offset, combining an absolute operation with relative attention behavior while preserving real-valued implementation.

## Key Quotes
> “纯粹的Attention模块是无法捕捉输入顺序的” — on why Transformers require an order signal.

> “内积只依赖于相对位置” — on the paired-coordinate rotation derivation.

## Connections
- [[PositionalEncoding]] — the umbrella design problem surveyed across absolute, relative, recurrent, boundary-derived, and complex mechanisms.
- [[RotaryPositionalEncoding]] — the closing rotation derivation uses absolute phase operations to make query-key scores depend on relative displacement.
- [[AttentionMechanism]] — relative methods inject distance into logits, keys, values, or selected interaction terms.
- [[TransformerArchitecture]] — the architecture lacks a recurrent or convolutional order prior and therefore needs an explicit position mechanism.
- [[NeuralNetwork]] — recurrent ODEs, CNN padding, and complex-valued models offer alternative structural sources of position information.

## Contradictions
- The common claim that learned absolute position tables have no extrapolation is qualified within the article itself: hierarchical decomposition or newly initialized positions can extend range, although the cited result is not reproduced here.
- A formula being defined at unseen indices does not establish useful length extrapolation; the source supplies no shared benchmark comparing learned, sinusoidal, recurrent, bucketed, or rotary variants outside their training lengths.
- The reported advantage of multiplicative over additive absolute encoding comes from an external experiment the author says was not comprehensively checked.
- The proposed fused rotation is described as working in preliminary experiments without datasets, metrics, baselines, or robustness tests; its later importance should not be read back into this article as complete empirical validation.
- The CNN padding account identifies one source of absolute location leakage, not proof that padding is the only way convolutional models represent direction or relative position.

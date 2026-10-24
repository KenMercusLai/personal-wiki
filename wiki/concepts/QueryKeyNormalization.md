---
title: "Query-Key Normalization"
type: concept
tags: [transformers, attention, normalization, training-stability]
sources:
  - transformer-architectures
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Definition
[[QueryKeyNormalization]] normalizes attention query and key vectors before their dot product to control learned norm drift and reduce extreme or excessively sharp attention logits.

## Current Synthesis
The usual `1/√d` attention scaling controls dot-product variance under idealized initialization assumptions, but training can change query and key means, correlations, and norms. Growing norms then increase logit magnitude even at fixed head width, sharpening softmax distributions and raising numerical risk. QK normalization applies L2- or RMSNorm-style control before scoring; practical variants may retain learned scale parameters.

Strict unit-length vectors with fixed scaling bound their dot product, but that guarantee does not transfer unchanged to RMS-normalized implementations with learned scales. The more general interpretation is control of norm drift and pathological logit growth. The surveyed models use related mechanisms particularly at large depth, in MoE systems, and for long-context training, but the article reports adoption rather than a common controlled stability experiment.

## Key Claims
- Standard head-width scaling does not prevent query and key norms from drifting during training.
- Large query-key norms can produce overly sharp attention and numerical instability.
- Normalizing queries and keys directly controls a source of attention-logit growth.
- Practical QK-normalization variants differ in norm definition and learned scaling.
- The mechanism is a scale-specific stability control rather than a defining Transformer invariant.

## Evidence
Statistical motivation:
- [[transformer-architectures]] contrasts idealized dot-product variance at initialization with learned mean, correlation, and norm drift during training.

Implementation and use:
- [[transformer-architectures]] distinguishes strict L2 normalization from RMSNorm-style variants with learnable scales and lists use in several 2025 model families.

## Counterevidence & Qualifications
The source does not reproduce controlled runs isolating QK normalization across depth, MoE, or context length. Attention entropy can be task- and layer-dependent, so sharper distributions are not automatically failures. Learned scales weaken any absolute logit bound, and related techniques such as logit soft-capping or clipping intervene at different points. Reported model adoption may also reflect copied recipes rather than independently established necessity.

## What Changed
- Created the concept with the distinction between idealized variance scaling and learned norm drift.

## Related Concepts
- [[AttentionMechanism]] - produces the query-key logits controlled by the technique.
- [[RMSNorm]] - supplies one common normalization form used on queries and keys.
- [[TransformerArchitecture]] - contains the attention blocks whose stability is being managed.
- [[TransformerArchitecturalConvergence]] - places QK normalization among newer, less-settled scale interventions.

---
title: "TurboQuant"
type: concept
tags: [vector-quantization, kv-cache, approximate-nearest-neighbor-search]
sources:
  - 2604.19528
  - turboquant-and-rabitq
last_updated: 2026-10-19
knowledge_schema: synthesis-v1
---

## Definition
[[TurboQuant]] is a random-rotation vector-quantization method using distribution-fitted scalar centroids for reconstruction and an optional one-bit residual sketch for unbiased inner-product estimation.

## Current Synthesis
TurboQuant normalizes and rotates vectors, then maps coordinates to a Lloyd-Max or one-dimensional k-means codebook fitted to the rotated coordinate distribution. Its reconstruction variant stores centroid indices and the input norm. Its unbiased inner-product variant allocates `B-1` bits per coordinate to that reconstruction and one bit to the sign of a Gaussian projection of the residual, additionally storing the residual norm.

This structure distinguishes its two objectives. The reconstruction path minimizes MSE but does not guarantee unbiased inner products; the residual-corrected path restores unbiasedness while adding a second estimator term, scalar metadata, random projection, and centroid decoding. The current evidence is contested: RaBitQ-authored sources report weaker error concentration, recall, speed, and low-bit KV-cache quality in most tests, and allege that TurboQuant underdescribed the shared random-rotation preprocessing, mischaracterized RaBitQ's theory, and used an undisclosed asymmetric baseline. The March 2026 article establishes that these objections were made publicly before the later technical report, but does not independently resolve them.

## Key Claims
- TurboQuant builds a non-uniform scalar codebook from the distribution induced by normalizing and randomly rotating vectors.
- The reconstruction variant stores centroid indices plus vector norm and decodes through the codebook.
- The unbiased variant reserves one bit per coordinate for a QJL sign sketch of the reconstruction residual and stores an additional residual norm.
- The cited published theory controls estimator variance; converting that result to a failure-probability tail with Chebyshev gives `log(1/delta)` bit-width dependence.
- The reconstruction variant can outperform the unbiased variant on ANN recall even though inner-product ranking is the target task.
- Prior-work description, theoretical comparison, released-artifact reproducibility, and baseline symmetry are disputed by the RaBitQ authors.

## Evidence
Representation and objectives:
- [[2604.19528]] reconstructs the centroid quantizer, signed residual projection, stored norms, and combined estimator from the TurboQuant paper and code.

Theory:
- [[2604.19528]] contrasts TurboQuant's stated mean-squared-error or variance guarantee with RaBitQ's tail bound and derives a Chebyshev-based failure-probability dependence.

Empirical dispute:
- [[2604.19528]] reports wider unbiased error above one bit, lower Recall@1@k, and slower A100 quantization than matched RaBitQ implementations.
- [[2604.19528]] reports a 0.709 Needle-In-A-Haystack score at 2.5 bits versus 0.951 for RaBitQ, while the methods are closer at 3.5 bits.
- [[2604.19528]] says the released KV-cache code required repairs and an unpublished CUDA dependency, and that reported runtime and baseline settings were not reproducible or fully disclosed.

Public dispute chronology:
- [[turboquant-and-rabitq]] says the TurboQuant authors received the method, theory, and benchmark objections before ICLR submission; it also records the RaBitQ authors' OpenReview comment and conference complaints.
- [[turboquant-and-rabitq]] attributes to private correspondence the admission that RaBitQ ran on a single CPU core with multiprocessing disabled while TurboQuant ran on an A100 GPU.

## Counterevidence & Qualifications
All current page evidence comes through a competing method's authors, not a neutral reproduction or TurboQuant's own source note. The public article does not reproduce the complete correspondence or give TurboQuant's full response, so its claims about knowledge, refusal, and deliberate unfairness remain allegations. The comparison's repaired KV-cache framework and choice of the MSE variant are reasoned but depart from the unreleased or underspecified original evaluation. A variance theorem is not proof of heavy tails, and a looser published bound does not alone establish worse practical behavior. Optimized implementations, different codebooks, models, hardware, or reconstruction-oriented workloads may change the ranking.

## What Changed
- Created the method page separating reconstruction and unbiased residual-corrected variants.
- Recorded the disputed theory, performance, and reproducibility claims without treating them as independent adjudication.
- Added ANN and KV-cache results showing objective- and bit-width-dependent behavior.
- Added the earlier public chronology and prior-work-description dispute, with allegations of knowledge and intent kept qualified.

## Related Concepts
- [[VectorQuantization]] - broader compression framework used to compare TurboQuant with alternatives.
- [[RaBitQ]] - competing method sharing random-rotation preprocessing.
- [[ApproximateNearestNeighborSearch]] - downstream ranking task used in the recall comparison.
- [[KVCacheCompression]] - application emphasized by TurboQuant and tested in the rebuttal.
- [[BlockQuantization]] - adjacent design space for scaling grouped low-precision values.

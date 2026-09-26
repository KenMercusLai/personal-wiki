---
title: "SimplyRetrieve"
type: entity
tags: [ai, retrieval, rcg, research]
sources:
  - blog-intel-labs-knowledge-retrieval-takes-center-stage
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Overview
[[SimplyRetrieve]] is an open-source Kioxia research system cited as an early example of retrieval-centric generation that separates context interpretation from knowledge memorization.

## Current Profile
The Intel Labs source describes SimplyRetrieve as implemented on Wizard-Vicuna-13B and contrasts it with RAG and retrieval-off generation on a query about Kioxia factory locations. In the reproduced example, the RCG answer stays within the retrieved facts, while RAG blends them with model knowledge and introduces unsupported locations and the retrieval-off response gives an incorrect main location and unrelated product details.

The example makes the intended RCG boundary concrete: the model should interpret supplied evidence without supplementing it from parametric memory. It remains one query, and the source explicitly warns that RAG and retrieval-off generation may be correct in other cases.

## Key Characteristics
- Open-source research prototype attributed to Kioxia Corporation researchers.
- Separates context interpretation from knowledge memorization.
- Implemented in the cited work on Wizard-Vicuna-13B.
- Used to compare RCG, RAG, and retrieval-off answers on a factory-location query.

## Evidence
- Design: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] describes SimplyRetrieve as using an RCG architecture to separate interpretation from memorization.
- Example result: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] reproduces an answer table where SimplyRetrieve gives the three retrieved Japanese locations without the comparison systems' additions.
- Model base: [[blog-intel-labs-knowledge-retrieval-takes-center-stage]] names Wizard-Vicuna-13B as the implementation base.

## Qualifications
The source provides only one visible qualitative query and no aggregate accuracy, latency, cost, robustness, or source-attribution metrics. The example is evidence that parametric memory can conflict with retrieved facts, not proof that disabling or suppressing it always improves answers. Current repository status and reproducibility were not independently checked during this ingest.

## What Changed
- Added SimplyRetrieve as the source's principal concrete RCG comparison.

## Relationships
- [[RetrievalCentricGeneration]] - SimplyRetrieve is presented as an implementation of this architecture.
- [[RetrievalAugmentedGeneration]] - the cited example contrasts RCG with RAG's blending of retrieved and parametric knowledge.
- [[SchemaBasedReasoning]] - interpreting retrieved facts without memorization depends on recognizing their roles and relations.
- [[IntelLabs]] - Intel Labs uses SimplyRetrieve as supporting evidence for its RCG argument.

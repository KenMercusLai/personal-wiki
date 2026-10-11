---
title: "Unum"
type: entity
tags: [software-company, vector-search, multimodal-ai]
sources:
  - combinatorial-stable-marriages-for-dbms-semantic-joins
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[Unum]] is represented as Ash Vardanian's software company and the organizational home of the [[USearch]] vector-search library and UForm multimodal models.

## Current Profile
The source presents Unum as the infrastructure-focused successor to an abandoned dating application. Its work spans fast vector indexing and joining through USearch and compact multimodal representation learning through UForm. The article uses both projects to argue that database-scale semantic joins are computationally plausible but remain limited by representation alignment, especially across text and images.

## Key Characteristics
- Focuses on reusable search and representation infrastructure rather than one application vertical.
- Develops USearch for approximate vector search and join operations.
- Develops UForm multimodal models while openly reporting their alignment limitations.

## Evidence
- Organizational origin: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] says Vardanian left application development to focus on the underlying Unum framework.
- Search infrastructure: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] locates the semantic-join implementation in USearch.
- Multimodal work: [[combinatorial-stable-marriages-for-dbms-semantic-joins]] compares UForm's representation problem with CLIP and attributes some weakness to far less training data.

## Qualifications
The available evidence is first-party and does not independently verify the company's current organization, product status, adoption, or comparative performance. UForm's training-scale comparison and USearch's speed claims are source-scoped.

## What Changed
- Established Unum's relationship to USearch, UForm, and the Amare prototype.

## Relationships
- [[AshVardanian]] - founder and source author describing Unum's development.
- [[USearch]] - vector-search library developed in the Unum context.
- [[SemanticJoin]] - database operation implemented and benchmarked through USearch.
- [[Embeddings]] - shared-space representations whose quality constrains the company's proposed joins.

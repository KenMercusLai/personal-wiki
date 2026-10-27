---
title: "左巨"
type: entity
tags: [author, ai, search, databases]
sources:
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Overview
[[ZuoJu|左巨]] is a technical author and builder represented here through an analysis of personal-agent retrieval, memory-product boundaries, and object-storage-backed search.

## Current Profile
The source combines product reasoning with implementation experience. 左巨 argues that a retrieval service can return historical evidence and provenance, but the agent product must decide whether that evidence is current, relevant to the active task, and appropriate to place in context. The author also reports building [[Todaypuffer]], a small Turbopuffer-like implementation used to test BM25 index layout over object storage.

## Key Characteristics
- Analyzes personal-agent memory as a coupled product, model, and engineering problem.
- Distinguishes general search infrastructure from application-specific memory judgment.
- Uses direct prototype measurements to test object-storage-native indexing assumptions.
- Treats source documents, versions, timestamps, and provenance as evidence that should survive changing interpretations.

## Evidence
Product and architecture analysis:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] develops the distinction between retrieval, context selection, and user-belief interpretation.

Implementation work:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] reports Todaypuffer's monolithic-index failure and bucketed BM25 redesign.

## Qualifications
The profile is based on one first-person article. It establishes the authorship and reported prototype work but does not independently verify production scale, organizational role, benchmark methodology, or the current state of the implementation.

## What Changed
- Established the author's search-infrastructure thesis and reported Todaypuffer implementation work.

## Relationships
- [[Todaypuffer]] - prototype the author reports building and evaluating.
- [[Turbopuffer]] - principal system analyzed as an infrastructure and product case.
- [[AgentMemory]] - capability whose interpretation layer the author separates from retrieval.
- [[PersonalAgentRetrieval]] - workload model developed in the article.

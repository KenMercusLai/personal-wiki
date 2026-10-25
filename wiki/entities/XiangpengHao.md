---
title: "Xiangpeng Hao"
type: entity
tags: [researcher, database-systems, data-analytics]
sources:
  - p5662-hao-corrected
  - how-to-llm-inference
last_updated: 2026-10-25
knowledge_schema: synthesis-v1
---

## Overview
[[XiangpengHao]] is a University of Wisconsin-Madison systems researcher represented through the [[LiquidCache]] paper and a practitioner guide to building a local CPU [[LLMInferenceSystems|LLM inference system]].

## Current Profile
In the database source, Hao co-designs a pushdown cache and ephemeral columnar representation around the observation that Parquet decoding dominates predicate-evaluation cost. The paper also attributes upstream Apache Arrow, Parquet, and [[ApacheDataFusion]] engineering work, including StringView integration, to the LiquidCache effort.

The personal systems article applies the same data-movement emphasis to a dependency-free Rust engine for [[Qwen36_35BA3B]]. It explains GGUF parsing, tokenization, typed tensor shapes, block quantization, CPU integer-dot kernels, autoregressive state, SIMD, fusion, and threading, and reports near-bandwidth-ceiling decode kernels on the author's machine.

## Key Characteristics
- Lead author of the LiquidCache system paper.
- Affiliated with the University of Wisconsin-Madison in the source.
- Works at the intersection of analytical databases, caching, columnar encoding, and resource disaggregation.
- Coauthor of implementation work contributed to the Apache data ecosystem.
- Writes implementation-led systems explanations that connect compact representation, data movement, and hardware execution.

## Evidence
- Authorship and affiliation: [[p5662-hao-corrected]] lists Hao first and associates him with the University of Wisconsin-Madison.
- Research contribution: [[p5662-hao-corrected]] presents LiquidCache's architecture, Liquid representation, filter-aware decoding, and evaluation.
- Engineering contribution: [[p5662-hao-corrected]] reports roughly 5,000 lines contributed upstream across DataFusion, Arrow, and Parquet.
- Inference implementation: [[how-to-llm-inference]] presents Hao's model-specific Rust engine and its reported prefill, decode, and per-kernel measurements.

## Qualifications
The inference article is hosted on “Xiangpeng's blog” at `xiangpeng.systems`; treating its author as the same [[XiangpengHao]] is a strong identity inference rather than an explicit full-name byline in the saved Markdown. The profile does not establish Hao's full biography, current affiliation, role allocation among LiquidCache coauthors, or independent production deployment of either system. The inference measurements and correctness claims are self-reported and not independently reproduced.

## What Changed
- Added a model-specific CPU inference engine and systems-writing role to the existing database-research profile.
- Preserved the byline-identity and first-party benchmark qualifications.

## Relationships
- [[LiquidCache]] - system for which Hao is lead author.
- [[AndrewLamb]] - coauthor and InfluxData-affiliated collaborator.
- [[YiboWu]] - University of Wisconsin-Madison coauthor.
- [[AndreaArpaciDusseau]] - University of Wisconsin-Madison coauthor.
- [[RemziArpaciDusseau]] - University of Wisconsin-Madison coauthor.
- [[ApacheDataFusion]] - implementation substrate and upstream contribution target.
- [[LLMInferenceSystems]] - systems topic of the represented Rust implementation guide.
- [[Qwen36_35BA3B]] - model targeted by the represented inference engine.

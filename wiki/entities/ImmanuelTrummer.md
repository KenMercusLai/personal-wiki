---
title: "Immanuel Trummer"
type: entity
tags: [researcher, databases, cornell]
sources:
  - 2607.07696
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[ImmanuelTrummer]] is a Cornell University researcher and coauthor of the [[Jailbreak]] database-bypass paper.

## Current Profile
In the supplied source, Trummer works on applying LLM-assisted code synthesis to database systems engineering. Jailbreak uses storage documentation and source knowledge to generate or refine C++ readers, then checks their output with deterministic database-derived ground truth before exposing Arrow-compatible data to analytical engines.

## Key Characteristics
- Works on database systems, query processing, and generated systems code.
- Co-developed and evaluated PostgreSQL and MySQL direct storage readers.
- Frames storage decoding as a candidate for verified LLM-assisted synthesis rather than purely manual implementation.

## Evidence
- Affiliation and authorship: [[2607.07696]] lists Trummer as a Cornell University author.
- Systems contribution: [[2607.07696]] attributes the Jailbreak design, implementation, and evaluation to its two authors.
- Research context: [[2607.07696]] positions GenDB and Dingo alongside the new storage-ingestion work.

## Qualifications
This profile is bounded to one supplied paper. It does not establish Trummer's complete biography, current role beyond the stated affiliation, or individual contribution split between the two authors.

## What Changed
- Created a source-bounded researcher profile around database systems synthesis and storage bypass.

## Relationships
- [[VictorGiannakouris]] - coauthor of the Jailbreak paper.
- [[Jailbreak]] - database-bypass project described in the source.
- [[DatabaseBypass]] - principal data-access problem addressed by the paper.
- [[AgenticStorageReaderSynthesis]] - generation methodology developed in the work.

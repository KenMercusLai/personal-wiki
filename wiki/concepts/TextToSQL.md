---
title: "Text-to-SQL"
type: concept
tags: [ai, sql, databases, natural-language-interface]
sources:
  - blog-timescale-rag-is-more-than-just-vector-search
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[TextToSQL]] translates a natural-language analytical request into a SQL query against a known database schema, usually as one controlled step inside a larger application workflow.

## Current Synthesis
The Timescale tutorial treats text-to-SQL as a fallback for questions that specialized semantic-search tools cannot answer, especially aggregation and time-series analysis. Its prompt includes the user request, allowed repositories, table and column semantics, preferred Timescale functions, and warnings about unavailable metadata. The central design lesson is that schema-grounded specificity and explicit boundaries are more useful than a terse generic request to "write SQL."

The example remains incomplete as a safe execution design. Detailed prompts can reduce nonexistent columns and inappropriate functions, but they cannot guarantee valid, authorized, efficient, or read-only queries. Schema validation, constrained database roles, query inspection, resource limits, execution error handling, and result-grounding checks remain necessary outside the model prompt.

## Key Claims
- Text-to-SQL is most useful as a bounded analytical tool, not an unrestricted substitute for a database interface.
- Accurate generation depends on detailed table, column, relationship, type, and domain-function context.
- Explicit negative constraints can reduce hallucinated fields and inappropriate custom functions.
- Generated SQL still requires non-prompt controls for authorization, safety, cost, and correctness.

## Evidence
- Fallback role: [[blog-timescale-rag-is-more-than-just-vector-search]] routes time-series and analytical questions to SQL only when narrower retrieval tools are insufficient.
- Schema guidance: [[blog-timescale-rag-is-more-than-just-vector-search]] recommends detailed column descriptions and repository filters.
- Domain constraints: [[blog-timescale-rag-is-more-than-just-vector-search]] instructs the model to prefer Timescale's `time_bucket` and avoid empty metadata.
- Failure evidence: [[blog-timescale-rag-is-more-than-just-vector-search]] itself mixes the actual `label` column with an `issue_label` prompt reference, illustrating why prompt and schema drift need validation.

## Counterevidence & Qualifications
The source does not implement the SQL execution method, benchmark query accuracy, or describe database permissions and destructive-query controls. Its verbose-prompt recommendation is experience-based and may trade token cost and maintenance burden for accuracy. The internal column-name mismatch shows that more prompt detail can reproduce stale or inconsistent schema information rather than eliminate it.

## What Changed
- Established schema-rich prompting and explicit field boundaries as core text-to-SQL design inputs.
- Added schema drift and execution controls as necessary qualifications to prompt-based accuracy.

## Related Concepts
- [[NaturalLanguageInterface]] - text-to-SQL exposes structured data through natural-language requests.
- [[PostgreSQL]] - database platform targeted by the source's generated queries.
- [[RetrievalAugmentedGeneration]] - SQL supplies structured retrieval and aggregation beyond semantic similarity.
- [[EvalsDrivenAIDevelopment]] - query generation and execution need repeatable behavioral evaluation.

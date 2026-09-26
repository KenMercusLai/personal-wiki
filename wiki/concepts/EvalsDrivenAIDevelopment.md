---
title: "Evals-Driven AI Development"
type: concept
tags: [ai, evaluations, testing, tool-calling]
sources:
  - blog-timescale-rag-is-more-than-just-vector-search
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[EvalsDrivenAIDevelopment]] is the practice of specifying representative model behaviors and checking them repeatedly while an AI application is still being designed, so evidence about model performance shapes tools, prompts, data, and architecture.

## Current Synthesis
The Timescale example applies this practice narrowly to tool routing. Typed Pydantic schemas act as prospective tool contracts, test questions name the expected tool class, and assertions check whether the model selects raw issue search, summary search, or SQL analysis before every execution path is implemented. This makes routing behavior independently testable and lets the desired user workflow guide tool design.

The useful boundary is equally important: selecting the expected tool is not the same as completing the task correctly. A credible evaluation suite must eventually cover argument extraction, retrieval quality, generated SQL, execution safety, grounded synthesis, failure handling, and real user value. The source demonstrates an early unit-like layer, not a complete end-to-end evaluation program.

## Key Claims
- Typed tool schemas can serve as testable behavioral contracts before their implementations are complete.
- Representative user questions can expose missing tools, metadata, and routing rules early in development.
- Tool-selection evaluation separates orchestration failures from retrieval or execution failures.
- Unit-like routing checks should be extended into end-to-end task and safety evaluations before production use.

## Evidence
- Typed routing contracts: [[blog-timescale-rag-is-more-than-just-vector-search]] defines three Pydantic tool types and asserts the expected type for representative GitHub-issue questions.
- Design-before-implementation: [[blog-timescale-rag-is-more-than-just-vector-search]] tests selection of the SQL tool while its `execute` method is still a placeholder.
- Separation of concerns: [[blog-timescale-rag-is-more-than-just-vector-search]] explicitly evaluates tool choice separately from tool implementation.

## Counterevidence & Qualifications
The source provides three illustrative assertions rather than a measured evaluation set. It does not test ambiguous questions, multiple correct tool plans, argument quality, SQL validity, retrieved evidence, final-answer faithfulness, cost, latency, regressions across model versions, or adversarial inputs. Its analogy to unit testing is useful for decomposition but should not imply deterministic coverage of a probabilistic end-to-end system.

## What Changed
- Established tool-routing tests as a narrow, early layer of eval-driven AI development.
- Distinguished routing accuracy from full task correctness and safety.

## Related Concepts
- [[SoftwareVerification]] - evals extend repeatable checking to probabilistic model behavior.
- [[AgenticWorkflowPatterns]] - tool-routing evaluations test which workflow branch a model chooses.
- [[RetrievalAugmentedGeneration]] - retrieval applications need evaluation beyond vector-query latency.
- [[TextToSQL]] - generated queries require correctness and safety checks beyond choosing the SQL tool.

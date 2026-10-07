---
title: "OpenAI o1"
type: entity
tags: [ai, reasoning-model, openai]
sources:
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[OpenAIo1]] is a reasoning-focused language model presented in OpenAI's September 2024 report as improving through reinforcement learning and additional test-time reasoning compute.

## Current Profile
The source characterizes o1 as an early public demonstration of inference-time scaling: before answering, the system uses an internal reasoning process that can decompose problems, detect mistakes, and change approaches. Reproduced charts report gains over GPT-4o across mathematics, science, exam, and MMLU benchmarks and rising AIME accuracy with both training and test-time compute, but the report withholds implementation details and exposes only summaries rather than the underlying chain of thought.

## Key Characteristics
- Uses additional internal reasoning before producing a final answer.
- Is reported to improve with both reinforcement-learning compute and test-time compute.
- Substantially outperforms GPT-4o on several reproduced reasoning benchmarks, with uneven gains across domains.
- Keeps raw reasoning traces hidden while presenting summaries.
- Has an implementation that the source cannot reconstruct from the short public report.

## Evidence
- Benchmark profile: [[large-language-model-technical-reports-overview]] reproduces o1-versus-GPT-4o results across MATH, science, exams, and MMLU categories.
- Scaling behavior: [[large-language-model-technical-reports-overview]] reproduces plots relating AIME pass@1 accuracy to logarithmic training and test-time compute.
- Reasoning behavior: [[large-language-model-technical-reports-overview]] quotes the report's claims about recognizing mistakes, decomposing difficult steps, and trying alternate approaches.
- Disclosure boundary: [[large-language-model-technical-reports-overview]] notes that the raw reasoning process and algorithmic details are not public.

## Qualifications
The wiki evidence is a secondary overview of a short vendor report, not an independent evaluation or implementation study. The plotted benchmarks do not establish equal gains on ordinary use, hidden reasoning cannot be audited from the source, and the article's speculation about process reward models is not confirmed as o1's actual training design.

## What Changed
- Created a source-bounded profile of o1's reported reasoning, scaling behavior, benchmark gains, and disclosure limits.

## Relationships
- [[OpenAI]] - developer of o1.
- [[ChainOfThoughtReasoning]] - o1 uses extended internal reasoning before its final response.
- [[ReinforcementLearning]] - the report attributes improved reasoning to reinforcement learning.
- [[DeepSeekR1]] - compared as a more openly documented reasoning-model program.
- [[KimiK15]] - compared as another reinforcement-learning-based reasoning model.

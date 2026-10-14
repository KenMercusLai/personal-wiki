---
title: "FuzzyBench"
type: entity
tags: [dataset, machine-learning, synthetic-data, evaluation]
sources:
  - 2607.02512
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[FuzzyBench]] is a 10M-example synthetic dataset introduced to train and evaluate compilers that map natural-language [[FuzzyFunctions|fuzzy-function]] specifications to executable neural adaptations.

## Current Profile
Each example is a specification-input-output triple. The authors use gpt-5.2 first to generate task specifications and then to generate eight input-output pairs per specification. Specifications—not individual examples—are divided 80/10/10 into train, validation, and test splits, and a verified test subset retains targets on which gpt-5.2 and gpt-5-mini agree.

The corpus grew through 29 thematic versions spanning more than 800 subcategories. The displayed high-level distribution is 30% core text processing and NLP, 18% search and web intelligence, 15% custom classification and filtering, 12% code and natural-language commands, 12% safety and domain knowledge, 8% agentic tool use, and 5% format repair and validation. Eight noise axes with three intensities support specification-robustness tests.

## Key Characteristics
- Contains 10 million synthetic specification-input-output examples.
- Splits by specification so test functions are unseen during training.
- Uses a model-agreement filter to remove some ambiguous evaluation targets.
- Covers 29 incremental thematic versions and more than 800 subcategories.
- Includes typo, grammar, ambiguity, formatting, combined-noise, terse, casual, and paraphrase perturbations.
- Uses exact match for the principal benchmark despite heterogeneous task families.

## Evidence
- Generation pipeline: [[2607.02512]] documents separate gpt-5.2 prompts for specification generation and conditioned input-output generation.
- Split and verification: [[2607.02512]] states that splits are specification-level and the verified test set requires agreement between gpt-5.2 and gpt-5-mini.
- Coverage: [[2607.02512]] supplies the 29-version timeline, more than 800 subcategories, and the seven-family distribution retained in the source note.
- Ceiling estimates: [[2607.02512]] reports 96.09% for the data-generating gpt-5.2 model and 91.87% for gpt-5-mini on the verified evaluation.
- Robustness suite: [[2607.02512]] describes eight specification perturbation axes at light, medium, and heavy intensity.

## Qualifications
The dataset is generated rather than collected from real developer workloads, and agreement between two related evaluator models filters ambiguity without proving ground truth. Exact match can under-credit semantically equivalent outputs and overstate reliability on tasks where calibration or partial correctness matters. Category prompts, synthetic style, model biases, data leakage, duplicate structure, and the representativeness of the 800-plus subcategories are not independently audited in this source.

## What Changed
- Created the dataset profile with generation, split, verification, and coverage details.
- Added the seven-family distribution and noise-robustness suite.
- Preserved synthetic-data and evaluator-agreement limits on the reported ceiling.

## Relationships
- [[ProgramAsWeights]] - FuzzyBench trains and evaluates its task-conditioned compiler.
- [[FuzzyFunctions]] - each specification defines one fuzzy input-output behavior.
- [[ParameterEfficientFineTuning]] - the dataset supervises a compiler that emits PEFT parameters.
- [[NaturalLanguageProcessing]] - its largest task family covers core text processing and NLP.
- [[AgenticWorkflowPatterns]] - agentic and tool-use tasks form one bounded part of its coverage.

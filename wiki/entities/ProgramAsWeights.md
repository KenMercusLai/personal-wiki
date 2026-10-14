---
title: "Program-as-Weights"
type: entity
tags: [machine-learning, local-ai, programming, hypernetwork]
sources:
  - 2607.02512
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Overview
[[ProgramAsWeights]] (PAW) is a research system and programming paradigm that compiles a natural-language [[FuzzyFunctions|fuzzy-function]] specification into a reusable hybrid neural program for execution by a small frozen local language model.

## Current Profile
The system separates compilation from execution. An off-the-shelf 4B pseudo compiler produces a cleaned task description plus examples; a trained 4B PEFT compiler turns the specification and pseudo-program into a task-specific LoRA or attention prefix. A frozen Qwen3-0.6B interpreter then executes new inputs with the discrete pseudo-program prepended and the continuous module attached.

The authors expose compilation and loading through Python, JavaScript, and a hosted web interface. The intended artifact can be cached, version-controlled, distributed, and run offline after the base model is installed. The paper reports strong synthetic-benchmark and on-device results, but the compiler remains cloud/GPU-oriented, each compiler is tied to an interpreter family, and the learned portion is opaque.

## Key Characteristics
- Uses a two-stage compiler: specification cleanup followed by task-conditioned PEFT generation.
- Packages discrete instructions and examples together with a continuous adapter.
- Keeps the interpreter frozen and hot-swaps one adapter per fuzzy function.
- Targets compile-once, repeated local execution rather than a large-model API call per input.
- Supports text and image-conditioned compilation while retaining a text-only local interpreter.
- Provides a single-file program abstraction and small callable developer API.
- Is trained on the synthetic 10M-example [[FuzzyBench]] corpus.

## Evidence
- Architecture: [[2607.02512]] documents the pseudo compiler, LoRA compiler, shared-basis mapper, and frozen interpreter data flow.
- Benchmark: [[2607.02512]] reports 73.78% FuzzyBench exact match for Qwen3-0.6B PAW versus 68.70% for direct Qwen3-32B prompting.
- Local execution: [[2607.02512]] reports about 31.6 tokens/s and 0.48-second cold load on a MacBook M3 for a $Q5_K_M$ base plus $Q4_0$ adapter.
- Program library: [[2607.02512]] shows distinct email-triage, JSON-repair, and PII-redaction adapters served by one device-resident interpreter.
- Applied scope: [[2607.02512]] describes five first-party studies and a ten-function ToolCall-15 pipeline that scores 93%.

## Qualifications
The main benchmark is synthetic and the five applications are author-built demonstrations rather than independent production evaluations. PAW is evaluated only on single-step functions; composition happens in conventional code. Compiler and interpreter are coupled, continuous adapters are not meaningfully inspectable, compilation still requires a larger model and hosted or GPU-backed infrastructure, and the best PEFT varies by task. The paper does not report security isolation between untrusted programs, calibration, adversarial robustness, broad external validation, or long-horizon behavior.

## What Changed
- Created the project profile and separated compile-time and run-time responsibilities.
- Recorded the hybrid pseudo-program plus PEFT artifact and hot-swappable runtime model.
- Added benchmark, quantization, modality, and application boundaries.

## Relationships
- [[FuzzyFunctions]] - PAW is designed to implement functions whose semantics resist exhaustive symbolic rules.
- [[ParameterEfficientFineTuning]] - LoRA and prefix-tuning are the supported continuous program forms.
- [[FuzzyBench]] - supplies the synthetic training triples and verified held-out evaluation.
- [[LocalFirstSoftware]] - local cached execution provides the project's deployment motivation.
- [[NaturalLanguageInterface]] - developers specify new behavior in prose and optional examples.
- [[QuantizationAwareTraining]] - adjacent low-precision methods may further shape deployable interpreters, although PAW reports post-training GGUF quantization.

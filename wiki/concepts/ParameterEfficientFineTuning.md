---
title: "Parameter-Efficient Fine-Tuning"
type: concept
tags: [machine-learning, neural-networks, lora, adapters]
sources:
  - 2607.02512
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[ParameterEfficientFineTuning]] adapts a pretrained model by changing or supplying a relatively small parameter module—such as a LoRA, adapter, soft prompt, or attention prefix—while leaving the base model frozen.

## Current Synthesis
The PAW source uses PEFT not merely as a cheaper way to train one task, but as a generated program representation. A task-conditioned compiler emits either LoRA matrices or prefix-tuning key-value states for a frozen interpreter. The strongest text configuration predicts layer- and module-specific mixtures over shared LoRA bases, so one resident base model can hot-swap many compact task artifacts without retraining at deployment time.

This extends the usual storage and training argument into a compiler abstraction, but it also exposes task dependence. LoRA is stronger in the paper's text and diagram-style experiments, whereas prefix-tuning performs better on long structured image-to-markup outputs. Quantizing each generated LoRA shrinks its shipping size, but generated weights remain opaque and coupled to the interpreter family used in training.

## Key Claims
- Freezing a shared base lets many task adaptations reuse the same expensive model parameters.
- A hypernetwork can generate a PEFT module directly from a natural-language task description instead of optimizing a new adapter for each task.
- Generated LoRA weights can be hot-swapped per call, making the adapter function like a compact executable artifact.
- Simpler shared-basis generation can outperform more expressive mapper architectures.
- PEFT choice is task-dependent; compactness alone does not determine accuracy or context behavior.
- Adapter quantization reduces per-program storage but adds another approximation boundary that must be evaluated.

## Evidence
- Generated LoRA design: [[2607.02512]] mean-pools compiler hidden states and predicts mixtures over 64 shared rank-64 bases for seven attention and MLP module types.
- Controlled PEFT comparison: [[2607.02512]] reports 50.4% exact match for prefix-tuning, 56.5% for size-matched rank-18 LoRA, and 65.7% for rank-64 LoRA at the comparison scale.
- Architectural simplicity: [[2607.02512]] reports 62.23% for the default shared-basis mapper versus 55.59–60.33% for per-position, per-layer, and combined LoRA-plus-prefix alternatives.
- Deployment footprint: [[2607.02512]] reports a 23 MB $Q4_0$ LoRA per Qwen3-0.6B program and a shared 430–484 MB four-bit base, with a modest measured accuracy change.
- Task dependence: [[2607.02512]] finds LoRA stronger on three diagram-understanding tasks while prefix-tuning is stronger on Im2LaTeX long-form generation.

## Counterevidence & Qualifications
The comparisons come from one compiler family, a small set of interpreter families, the authors' training recipe, and largely synthetic tasks. Per-program adapters are compact relative to the base but not free: the default LoRA represents about 38.5 million injected parameters before quantization. Switching interpreter families requires retraining the compiler, the continuous artifact is not human-inspectable, and the source offers no general criterion for selecting LoRA, prefix-tuning, or another PEFT for a new task.

## What Changed
- Created the concept around frozen-base adaptation and generated task modules.
- Added compiler-generated PEFT as distinct from per-task gradient optimization.
- Recorded the evidence that PEFT choice and pseudo-program length interact with task form.

## Related Concepts
- [[ProgramAsWeights]] - treats a generated PEFT module as the continuous half of a neural program.
- [[NeuralNetwork]] - provides the frozen backbone and target projections modified by the adapter.
- [[QuantizationAwareTraining]] - addresses low-precision behavior during training, complementary to PAW's reported post-training adapter quantization.
- [[BlockQuantization]] - explains how low-precision grouping choices can affect model and adapter fidelity.
- [[NeuralLanguageModel]] - supplies the compiler and interpreter architectures used in the reported instantiation.

---
title: "Software 2.0"
type: concept
tags: [software, machine-learning, neural-networks, programming-paradigms]
sources:
  - software-2-0
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Definition
[[Software20|Software 2.0]] is [[AndrejKarpathy]]'s term for software whose detailed behaviour is encoded in learned parameters: developers specify examples or another evaluation criterion, choose an architecture that bounds the possible programs, and use optimization to search for weights that work.

## Current Synthesis
The framing recasts a trained [[NeuralNetwork]] as executable code rather than merely a component selected from a machine-learning toolbox. Conventional programming directly places a human-written program in program space. Software 2.0 instead supplies a behavioural specification, commonly a labeled dataset, and a differentiable architecture; [[NeuralNetworkTraining]] searches the architecture's continuous parameter space and emits a trained model. Under this analogy, the dataset and architecture are source code, training is compilation, and the weights are the binary.

This changes the locus of development. Many improvements come from sourcing, labeling, cleaning, balancing, and inspecting examples instead of adding conditional branches. The required engineering ecosystem therefore includes dataset versioning, labeling interfaces, error and uncertainty analysis, model packaging, evaluation, deployment, and monitoring alongside conventional training infrastructure. The approach is most compelling when desired behaviour is easy to demonstrate or repeatedly score but difficult to state as rules.

The abstraction is useful but incomplete. A learned component remains surrounded by conventional software, and its apparent computational regularity does not guarantee simple end-to-end operations. Optimization can produce better benchmark behaviour while leaving mechanisms opaque, reproducing data bias, failing silently outside the training distribution, or admitting adversarial inputs. Software 2.0 is therefore a shift in where behaviour is specified and debugged, not an escape from software engineering, verification, governance, or explicit system boundaries.

## Key Claims
- Behaviour moves from explicit instructions into learned parameters found by optimizing an evaluation criterion within an architecture-defined search space.
- Datasets function as executable specifications, so curation, labeling, coverage, and versioning become core programming activities.
- Training resembles compilation: it transforms data, architecture, objectives, and compute into a deployable model artifact.
- The paradigm fits tasks whose outcomes can be demonstrated or scored more readily than their rules can be hand-coded.
- Learned computation can be homogeneous, portable, capacity-adjustable, and jointly optimized across differentiable module boundaries.
- Better task performance does not remove opacity, bias, silent failure, adversarial vulnerability, distribution shift, or total-system engineering costs.

## Evidence
- Representation and search: [[software-2-0]] contrasts a human-chosen Software 1.0 point in program space with optimization inside an architecture-bounded Software 2.0 region, and illustrates learned code as numerical network weights.
- Development workflow: [[software-2-0]] identifies the dataset and architecture as source code, training as compilation, and data collection, cleaning, labeling, and inspection as central development work.
- Applicability: [[software-2-0]] points to 2017 transitions in visual and speech recognition, speech synthesis, translation, Go, and learned database indexing where specifying examples or objectives proved more tractable than writing rules.
- Operational properties: [[software-2-0]] argues that common neural networks use a small set of computational primitives, can run across hardware targets, permit capacity-quality tradeoffs, and allow end-to-end optimization through learned modules.
- Tooling implications: [[software-2-0]] proposes dataset-focused IDEs, dataset-and-label version control, and model packaging and serving equivalents as missing infrastructure.
- Failure modes: [[software-2-0]] explicitly names interpretability loss, training-data bias, silent failures, and adversarial examples as costs of the learned stack.

## Counterevidence & Qualifications
The evidence is a 2017 conceptual practitioner essay, not a controlled comparison of programming paradigms. Its examples were early successes selected to support the thesis, and its learned-index speed and memory figures are inherited from a cited paper rather than independently evaluated. Claims of constant time, constant memory, exact speed-quality scaling, and computational homogeneity apply only to restricted model and serving designs; dynamic compute, sparse routing, retrieval, autoregressive decoding, data pipelines, and orchestration complicate them. An evaluation criterion can also be incomplete or gameable, and easy measurement does not guarantee alignment with the actual goal. The prediction that AGI will necessarily be Software 2.0 is speculative.

## What Changed
- Created the concept and separated the durable data-and-optimization programming model from the source's stronger universal forecasts.
- Made conventional software, evaluation quality, deployment overhead, and learned-system failure modes explicit parts of the paradigm.

## Related Concepts
- [[NeuralNetwork]] - parameterized program representation emphasized by the original essay.
- [[NeuralNetworkTraining]] - search and compilation process that produces the learned artifact.
- [[Backpropagation]] - credit-assignment mechanism enabling differentiable end-to-end optimization.
- [[StochasticGradientDescent]] - common procedure for searching parameter space.
- [[DeepLearning]] - layered learning practice through which much of the transition occurred.
- [[SoftwareEngineering]] - surrounding discipline that still supplies architecture, integration, testing, deployment, monitoring, and governance.
- [[MachineLearningResearchEngineering]] - builds the infrastructure and interfaces for fast learned-software experimentation.
- [[AlgorithmicDecisionOpacity]] - accountability risk created when learned behaviour cannot be explained.

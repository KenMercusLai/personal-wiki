---
title: "Andrej Karpathy"
type: entity
tags: [software, ai, education, cryptocurrency]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
  - on-technical-accessibility
  - software-2-0
last_updated: 2026-10-02
knowledge_schema: synthesis-v1
---

## Overview
[[AndrejKarpathy]] appears in this wiki as a technical educator and AI practitioner who uses from-scratch construction, explicit learning ramps, and memorable conceptual frames to make complex systems more approachable.

## Current Profile
The Bitcoin tutorial presents Karpathy as both learner and explainer: he starts from curiosity about blockchain as open software with shared state, then rebuilds the Bitcoin path from key generation to a testnet transaction in pure [[Python]]. His stance is explicitly educational rather than production-oriented, with warnings that the cryptographic code is for understanding rather than real use. The Micrograd post adds a meta-teaching layer: Karpathy argues that compact, commented, documented code may still fail to reach people until the creator builds an accessible ramp such as a from-scratch video walkthrough.

The 2017 Software 2.0 essay shows the same explanatory style at the level of a field. Karpathy reframes a [[NeuralNetwork]] as learned code, a dataset and architecture as source code, and [[NeuralNetworkTraining]] as compilation. This makes the industrial consequence legible: much development shifts from writing instructions to curating behavioural examples and building the infrastructure that turns them into reliable models. Unlike a purely promotional account, the essay also names opacity, bias, silent failure, and adversarial examples as costs of the paradigm.

## Key Characteristics
- Uses implementation as a learning method for understanding complex systems.
- Frames blockchain as a computing paradigm that extends open source code into open, shared state.
- Explains Bitcoin through concrete protocol artifacts: keys, addresses, hashes, scripts, serialized transactions, and testnet broadcasts.
- Keeps the tutorial candid about omitted production details and unsafe educational shortcuts.
- Connects the article to a cleaner reference implementation in [[Cryptos]].
- Treats accessibility as part of technical creation, not an optional polish step after publishing code.
- Uses compact analogies to reposition machine learning as a change in how software is specified, built, and debugged.

## Evidence
- Implementation-first learning: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] builds key generation, hashing, address derivation, transaction serialization, signing, and broadcasting in one walkthrough.
- Blockchain framing: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] presents Bitcoin as a seed example of open software plus shared running state.
- Safety boundaries: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] warns against using the educational cryptography in production and notes skipped standards such as RFC 6979.
- Reference-project link: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] points to [[Cryptos]] as a cleaner, separated, tested implementation.
- Accessibility lesson: [[on-technical-accessibility]] says [[Micrograd]] grew much more after Karpathy made a from-scratch video, even though the code itself did not change.
- Audience humility: [[on-technical-accessibility]] argues that technical creators often overestimate how self-explanatory code, comments, papers, and READMEs are.
- Paradigm framing: [[software-2-0]] maps datasets to source code, training to compilation, and learned weights to binaries while explicitly recording the stack's interpretability, bias, and adversarial risks.

## Qualifications
This profile is limited to three authored educational sources. The Software 2.0 claims are a 2017 practitioner thesis illustrated by selected successes, not a comparative study or a complete account of learned-system engineering. The profile does not summarize Karpathy's broader AI research, teaching, or industry work.

## What Changed
- Added Karpathy's explicit accessibility lesson from Micrograd: the explanatory ramp around a technical artifact can matter as much as the artifact's compactness.
- Added his Software 2.0 framing of learned models as programs and data work as software development, together with its stated failure modes.

## Relationships
- [[Bitcoin]] - Karpathy reconstructs Bitcoin's identity, transaction, and proof-of-work mechanisms.
- [[Python]] - tutorial implementation language.
- [[Cryptos]] - related reference codebase maintained by Karpathy.
- [[FromScratchProtocolLearning]] - learning mode exemplified by the article.
- [[Micrograd]] - educational autograd engine used in Karpathy's accessibility reflection.
- [[TechnicalAccessibility]] - Karpathy argues technical work needs ramps that lower the barrier to engagement.
- [[Software20]] - Karpathy's framing of neural-network optimization as a new programming paradigm.
- [[NeuralNetworkTraining]] - recast in his essay as compilation from behavioural specification to learned weights.

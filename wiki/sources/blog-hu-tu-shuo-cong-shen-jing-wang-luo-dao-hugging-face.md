---
title: "从神经网络到 Hugging Face"
type: source
tags: [ai, neural-networks, deep-learning, history, open-source]
date: 2024-03-17
source_file: "/mnt/ken_personal_wiki/Articles/Blog - 胡涂说 - 从神经网络到 Hugging Face.md"
---

## Summary
[[Hutusi]] gives a popular history of [[NeuralNetwork]] research from the M-P neuron and perceptron through [[GeoffreyHinton]], [[DeepLearning]], Transformer models, and [[HuggingFace]]. The article combines a simplified explanation of weighted layers and training with a larger argument: reusable pretrained models, open-source libraries, datasets, and hosted applications turn advances that once required specialist research teams into shared infrastructure for a wider developer community.

## Key Claims
- A neuron can be modeled as weighted inputs plus a threshold or bias and an activation function; layered networks learn parameters from examples rather than relying only on hand-written rules.
- The perceptron's inability to solve nonlinear problems such as XOR helped discredit connectionism, while hidden layers, backpropagation, greater compute, and later training techniques made deeper networks practical.
- [[GeoffreyHinton]] is presented as a central historical bridge from Boltzmann machines and backpropagation through deep belief networks and AlexNet.
- Deep-network training alternates forward prediction and loss measurement with backward gradient calculation and optimizer-driven parameter updates.
- Transformer models, pretraining plus task-specific fine-tuning, and human-feedback post-training are presented as steps toward modern large language models, although several details are simplified.
- [[HuggingFace]] pivoted from a consumer chatbot to open-source model tooling; its Transformers, Datasets, Tokenizers, Diffusers, and Hub products lowered the practical cost of reusing models, datasets, and demonstrations.
- The Hugging Face ecosystem extends the resource-sharing logic of pretraining and fine-tuning by making trained artifacts discoverable and reusable, supporting a qualified form of AI democratization.

## Key Quotes
> "Hugging Face也被称为是机器学习领域的GitHub。" - the article's summary of the Hub's ecosystem role.

> "大多数时候，他需要平躺以缓解疼痛" - biographical context for Hinton's long research career.

## Connections
- [[Hutusi]] - author of the historical and technical synthesis.
- [[NeuralNetwork]] - the model family whose historical development structures the article.
- [[DeepLearning]] - the layered representation-learning approach explained through parameters, loss, backpropagation, and optimization.
- [[GeoffreyHinton]] - the main person in the article's account of deep learning's revival.
- [[HuggingFace]] - the open-source tooling and hosted-artifact ecosystem at the endpoint of the history.
- [[TransformerArchitecture]] - the architecture linked to GPT and the modern Hugging Face ecosystem.
- [[Backpropagation]] - the mechanism used to send loss information backward through layers.
- [[NeuralNetworkTraining]] - the forward-pass, loss, gradient, optimizer, and update loop.

## Contradictions
- The article attributes backpropagation to Hinton in 1986, but the algorithm has a longer multi-author history; the source is best read as popular synthesis rather than definitive priority history.
- It calls image data "discrete" and contrasts it with sequential data too sharply; spatial pixels are also related, and Transformer naming is not simply derived from converting one sequence into another.
- It describes RLHF as part of "pretraining fine-tuning," although the listed supervised and reinforcement stages are post-training after base-model pretraining.
- Its claim that ChatGPT's multi-turn ability comes from prompt engineering compresses several layers of system behavior, including conversation serialization, context-window management, model training, and product orchestration.
- The reported GPT-4 parameter count, fixed Hub inventory totals, and broad scaling-law summary are unverified or time-bound claims from the article, not stable measurements.

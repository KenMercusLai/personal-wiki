---
title: "Backpropagation"
type: concept
tags: [machine-learning, neural-networks, optimization]
sources:
  - iamtrask-a-neural-network-in-11-lines-of-python-part-1
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[Backpropagation]] is the procedure that computes how output error is attributable to earlier neural-network units and weights by propagating error signals backward through the network.

## Current Synthesis
The tutorial makes backpropagation concrete in a two-weight-layer sigmoid network. The forward pass maps inputs through a hidden layer to an output. The backward pass first multiplies output error by the output sigmoid derivative, then sends that delta backward through the transpose of the downstream weight matrix. Multiplying the resulting hidden error by each hidden unit's sigmoid derivative produces the hidden delta used to update the first weight matrix.

This is best understood as contribution-sensitive credit assignment, not merely backward data flow. Downstream weights determine how strongly each hidden unit contributed to the output error, local derivatives determine sensitivity at the current activation, and matrix products aggregate the batch's input-delta contributions into weight changes.

## Key Claims
- Backpropagation separates the forward prediction pass from a backward error-assignment pass.
- Output delta combines prediction error with the activation function's local derivative.
- Hidden-layer error is the downstream delta projected backward through the downstream weights.
- Each weight update aggregates an upstream activation multiplied by the downstream delta across the batch.
- The procedure enables earlier layers to learn intermediate features that make a nonlinear mapping such as XOR separable at the output.

## Evidence
- Output delta: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] computes `(y - l2) * sigmoid_derivative(l2)` before changing the output weights.
- Hidden credit assignment: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] computes `l2_delta.dot(syn1.T)` and then scales it by the hidden-layer sigmoid derivative.
- Weight aggregation: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] uses transposed layer activations dotted with deltas, and its diagrams show one-example contributions expanding to a four-example full-batch update.
- Nonlinear representation: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] uses the added hidden layer to solve XOR, whose individual inputs have no direct correlation with the output.

## Counterevidence & Qualifications
The source is an intuition-building implementation, not a general derivation of reverse-mode automatic differentiation. Its sigmoid-specific derivative, omitted biases, absent explicit learning rate, full-batch updates, and additive update convention should not be mistaken for requirements of backpropagation itself. The tutorial's "confidence weighted error" phrase is also only a mnemonic: sigmoid saturation can suppress gradients even when a confident prediction is wrong.

## What Changed
- Created a dedicated concept page separating backward credit assignment from the broader training loop.

## Related Concepts
- [[NeuralNetworkTraining]] - uses backpropagated derivatives inside the iterative weight-fitting loop.
- [[NeuralNetwork]] - supplies the layered computation graph whose parameters receive credit or blame.
- [[DeepLearning]] - depends on assigning error through multiple learned representation layers.
- [[StochasticGradientDescent]] - applies gradient information to parameter updates, although the tutorial itself uses full-batch updates.

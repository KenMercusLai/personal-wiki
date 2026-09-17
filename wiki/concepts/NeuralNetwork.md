---
title: "Neural Network"
type: concept
tags: [ai, machine-learning, neural-networks, mathematics]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[NeuralNetwork]] is a connected collection of simple numerical units - often called neurons - arranged in layers, where each unit combines weighted inputs with a constant and applies an activation function, so that the whole network computes one mathematical function whose behaviour is set by its weights.

## Current Synthesis
The source presents neural networks as a way of turning a task into a fitted function without writing its rules. A network is only ever doing arithmetic: multiply inputs by weights, add, apply a threshold such as ReLU, and pass the result forward. What makes that useful is that the weights are learned, and that even small networks can approximate a target function once trained on enough examples. The essay's worked cases are deliberately small - a 17-neuron network that approximates "which of three points is nearest", a 2,190-neuron LeNet-style net that recognizes handwritten digits, and a 60,650-neuron net that separates cats from dogs - and the pattern is the same each time: bigger networks approximate better inside the training region, answers are exact in the middle of an attractor basin and messy at the boundaries, and once trained the network is a complete mathematical function that can be written out in principle.

The source also supplies the wiki's clearest statement of what such a network does not give you. Its internal features are usually nameless: the first layer of an image net produces interpretable maps such as outlines and background removal, but by the tenth layer the same inspection is unreadable, and the essay's message is that a working network is not the same as a theory of the task. Because networks with no hidden layer can only express essentially linear functions while a single hidden layer can approximate any function in principle, capacity, regularization, and training feasibility rather than expressiveness are the practical constraints.

## Key Claims
- A network is a mathematical function: weighted sums, biases, and activation functions composed across layers, with the weights chosen by training rather than by hand.
- Activation functions introduce the nonlinearity that makes non-trivial behaviour possible; the source's examples use ReLU (Ramp), and it notes that Tanh, Sigmoid, Mish, and Swish are common alternatives.
- Increasing capacity improves approximation inside the region covered by training examples, while behaviour at basin boundaries stays unreliable.
- A network with no intermediate layer can only learn essentially linear functions, while a single hidden layer can in principle approximate any function.
- A squeeze or bottleneck in the middle of a network is a recurring practical device, and the source reports that networks below a task-dependent size simply cannot fit the target function.
- Trained networks are not self-explaining: early image layers map to recognizable features, later layers do not, and the source can produce the function without being able to narrate what it is doing.
- Network capacity is task-dependent and hard to estimate for human-like tasks, because there may be shortcuts that are not visible from a mechanical description of the task.

## Evidence
- Mathematical form: [[what-is-chatgpt-doing-and-why-does-it-work]] writes each neuron as an activation applied to a weighted sum plus bias, and shows a small network's overall function as a nested formula of those terms.
- Function approximation: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a 17-neuron network approximating the nearest-of-three-points function, close to the exact answer but imperfect near boundaries.
- Digit recognition architecture: [[what-is-chatgpt-doing-and-why-does-it-work]] lists the LeNet-style chain - input 1x28x28, convolution to 20x24x24, pooling to 20x12x12, convolution to 50x8x8, pooling to 50x4x4, flatten to 800, linear to 500, linear to 10, softmax to class - as 11 layers with 2,190 neurons, and the cat/dog net as 60,650 neurons.
- Activation functions: [[what-is-chatgpt-doing-and-why-does-it-work]] uses Ramp/ReLU and illustrates ReLU, Tanh, Sigmoid, Mish, and Swish as the family of choices.
- Capacity and squeezing: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the best fit achievable with several small networks, reports that too small a net cannot reproduce the function, and notes the bottleneck trick.
- Expressiveness: [[what-is-chatgpt-doing-and-why-does-it-work]] says no-intermediate-layer perceptrons are essentially linear while a single intermediate layer makes arbitrarily good approximation possible in principle, subject to regularization or normalization for trainability.
- Feature opacity: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the first-layer feature maps for a cat photo alongside tenth-layer maps, and says the network is picking out features for which we mostly have no names.
- Attractors: [[what-is-chatgpt-doing-and-why-does-it-work]] explains recognition through attractor basins separated by watersheds, using a Voronoi diagram as the 2D analogy for a much higher-dimensional pixel space.

## Counterevidence & Qualifications
The source is an explanatory essay rather than a benchmark study: its network sizes, layer lists, and examples are pedagogical, and the claim that trained networks "capture a human-like way of doing things" is described by the author as an empirical fact in some domains rather than a derivable one. The universal-approximation point is about existence, not about whether a network of a practical size can be trained to it, and the essay's opacity claim is a statement about current interpretability rather than a proof that no explanation exists.

## What Changed
- Created the concept page for the general neural-network model class.

## Related Concepts
- [[NeuralNetworkTraining]] - the process that sets a network's weights.
- [[StochasticGradientDescent]] - the descent procedure used to fit them.
- [[TransformerArchitecture]] - the specific network layout used by GPT-2 and GPT-3.
- [[AttentionMechanism]] - the mechanism inside that layout which looks back over a sequence.
- [[Embeddings]] - networks operate on numbers, so text and images must be embedded first.
- [[DeepLearning]] - the broader practice of learning representations with layered models.
- [[AlgorithmicDecisionOpacity]] - a related but narrower accountability concern about systems that decide without giving reasons.

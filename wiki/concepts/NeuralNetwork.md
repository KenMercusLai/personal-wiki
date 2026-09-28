---
title: "Neural Network"
type: concept
tags: [ai, machine-learning, neural-networks, mathematics]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
  - iamtrask-a-neural-network-in-11-lines-of-python-part-1
  - from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune
last_updated: 2026-09-28
knowledge_schema: synthesis-v1
---

## Definition
[[NeuralNetwork]] is a connected collection of simple numerical units - often called neurons - arranged in layers, where each unit combines weighted inputs with a constant and applies an activation function, so that the whole network computes one mathematical function whose behaviour is set by its weights.

## Current Synthesis
The sources present neural networks as a way of turning a task into a fitted function without writing its rules. A network is only ever doing arithmetic: multiply inputs by weights, apply an activation function, and pass the result forward. What makes that useful is that the weights are learned. The NumPy tutorial gives the smallest working case: a single weight matrix learns the input directly correlated with an output, while adding a four-unit hidden layer lets the same machinery solve XOR by constructing intermediate combinations. The larger essay extends that account through a 17-neuron nearest-point approximator, a 2,190-neuron LeNet-style digit recognizer, and a 60,650-neuron cat/dog classifier.

Together they distinguish stored parameters from transient activations: the toy tutorial says the learned network is its weight matrices, while layer values are recalculated from each batch. They also explain why depth matters. A no-hidden-layer model can only express essentially linear structure, while hidden units can encode combinations of inputs and a single hidden layer can approximate any function in principle. The 2016 history supplies a concrete visual hierarchy: lower layers detect edges, intermediate layers corners and parts such as beaks or heads, and higher layers recurring configurations associated with a bird. Capacity, regularization, data, compute, and training feasibility rather than expressiveness are therefore the practical constraints. None of this makes a trained network self-explaining: some features remain recognizable, but many deeper or unsupervised units are nameless and a working function is not yet a theory of the task.

## Key Claims
- A network is a mathematical function: weighted sums, optional biases, and activation functions composed across layers, with learned weight matrices storing the fitted behaviour while activations remain transient.
- Activation functions introduce the nonlinearity that makes non-trivial behaviour possible; the source's examples use ReLU (Ramp), and it notes that Tanh, Sigmoid, Mish, and Swish are common alternatives.
- Increasing capacity improves approximation inside the region covered by training examples, while behaviour at basin boundaries stays unreliable.
- A network with no intermediate layer can only learn essentially linear functions, while a single hidden layer can in principle approximate any function.
- A squeeze or bottleneck in the middle of a network is a recurring practical device, while minimum useful capacity is task-dependent and hard to estimate for human-like problems.
- Trained networks are not self-explaining: early image layers map to recognizable features, later layers do not, and the source can produce the function without being able to narrate what it is doing.
- Hierarchical features can progress from local visual contrasts to object parts and configurations, but this pattern recognition does not by itself supply broad reasoning.

## Evidence
- Mathematical form: [[what-is-chatgpt-doing-and-why-does-it-work]] writes each neuron as an activation applied to a weighted sum plus bias, and shows a small network's overall function as a nested formula of those terms.
- Function approximation: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a 17-neuron network approximating the nearest-of-three-points function, close to the exact answer but imperfect near boundaries.
- Digit recognition architecture: [[what-is-chatgpt-doing-and-why-does-it-work]] lists the LeNet-style chain - input 1x28x28, convolution to 20x24x24, pooling to 20x12x12, convolution to 50x8x8, pooling to 50x4x4, flatten to 800, linear to 500, linear to 10, softmax to class - as 11 layers with 2,190 neurons, and the cat/dog net as 60,650 neurons.
- Activation functions: [[what-is-chatgpt-doing-and-why-does-it-work]] uses Ramp/ReLU and illustrates ReLU, Tanh, Sigmoid, Mish, and Swish as the family of choices.
- Capacity and squeezing: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the best fit achievable with several small networks, reports that too small a net cannot reproduce the function, and notes the bottleneck trick.
- Expressiveness: [[what-is-chatgpt-doing-and-why-does-it-work]] says no-intermediate-layer perceptrons are essentially linear while a single intermediate layer makes arbitrarily good approximation possible in principle, subject to regularization or normalization for trainability.
- Feature opacity: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the first-layer feature maps for a cat photo alongside tenth-layer maps, and says the network is picking out features for which we mostly have no names.
- Attractors: [[what-is-chatgpt-doing-and-why-does-it-work]] explains recognition through attractor basins separated by watersheds, using a Voronoi diagram as the 2D analogy for a much higher-dimensional pixel space.
- Minimal mechanics: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] shows a `(3,1)` weight matrix learning a directly correlated feature and a `(3,4)` plus `(4,1)` pair solving XOR through hidden combinations.
- Stored versus transient state: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] identifies the weight matrices as the learned network and the layer values as per-batch computations.
- Visual intuition: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] uses bicycle and pipe examples to show why no single pixel must correlate with an object even when combinations of pixels do.
- Hierarchical vision: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] describes successive units responding to edges, corners, beak-like angles, head-like circles, and bird-level configurations.
- Pattern boundary: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] explicitly distinguishes strong pattern recognition from general reasoning and notes that many units in the unlabeled-image experiment resisted ordinary-language interpretation.

## Counterevidence & Qualifications
All three sources are explanatory rather than controlled benchmark studies. Their sizes, layer lists, and examples are pedagogical, and the claim that trained networks "capture a human-like way of doing things" is presented as an empirical observation rather than a derivable fact. The NumPy tutorial omits biases and an explicit learning rate, calls bounded sigmoid outputs probabilities without discussing calibration, and uses XOR only as a demonstration of hidden combinations. Fortune's edge-to-bird hierarchy is an intuition, not proof that every network learns the same human-readable decomposition. The universal-approximation point is about existence, not whether a practical network can be trained, and opacity is a current interpretability limit rather than proof that no explanation exists.

## What Changed
- Added a minimal executable account of learned weights, transient activations, and hidden combinations that solve XOR.
- Created the concept page for the general neural-network model class.
- Added the edge-to-part-to-object hierarchy while preserving the boundary between pattern recognition and reasoning.

## Related Concepts
- [[NeuralNetworkTraining]] - the process that sets a network's weights.
- [[Backpropagation]] - assigns output error to earlier layers and weights.
- [[StochasticGradientDescent]] - the descent procedure used to fit them.
- [[TransformerArchitecture]] - the specific network layout used by GPT-2 and GPT-3.
- [[AttentionMechanism]] - the mechanism inside that layout which looks back over a sequence.
- [[Embeddings]] - networks operate on numbers, so text and images must be embedded first.
- [[DeepLearning]] - the broader practice of learning representations with layered models.
- [[UnsupervisedLearning]] - can produce selective internal units without explicit category labels, while leaving much of the representation opaque.
- [[AlgorithmicDecisionOpacity]] - a related but narrower accountability concern about systems that decide without giving reasons.

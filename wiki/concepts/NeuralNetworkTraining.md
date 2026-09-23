---
title: "Neural Network Training"
type: concept
tags: [ai, machine-learning, optimization, data]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
  - iamtrask-a-neural-network-in-11-lines-of-python-part-1
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[NeuralNetworkTraining]] is the process of finding the weights that make a network reproduce the examples it is given, by repeatedly measuring the error on a batch of examples and adjusting every weight to reduce it.

## Current Synthesis
The sources treat training as the difference between a network that could compute anything and one that does the job. The loop is simple to state: supply input-output examples, compute prediction error or a loss, work out how it changes with respect to each weight, and move the weights to reduce it. The NumPy tutorial exposes that loop in matrix form: a full batch moves forward through sigmoid activations, output error is scaled by local slope, [[Backpropagation]] assigns contribution-weighted error to the hidden layer, and transposed activations aggregate the weight updates. Its error falls from about 0.496 to 0.0035 on XOR across 60,000 iterations.

The broader essay adds the practical effort absent from the toy example. Small functions still need enough examples and iterations, loss curves flatten, and network size determines whether a fit is possible. Architecture choice, data acquisition, transfer learning, epochs, augmentation, loss choice, optimization method, and batch size are described as an art built by trial and error. At large scale, sequential weight updates make GPU availability a constraint, with approximate power-law relationships between loss, model size, and data quantity. Language is easier to feed than supervised image work because masking text makes the text itself supply a target.

## Key Claims
- Training means choosing weights that reproduce given examples, and relying on the network to interpolate reasonably between them.
- Error or a loss defines what training reduces; calculus and the chain rule supply gradients through successive layers, while activation derivatives and downstream weights determine the toy network's layer deltas.
- Descent is not guaranteed to reach a global minimum: it can end in a local minimum or "mountain lake", and the essay reports that having many weights can make approximate minimization easier rather than harder.
- Many different weight settings give equivalent performance, so training is not a unique answer; different solutions can diverge sharply on cases outside the training region.
- Data is a first-class constraint: supervised work needs tagged examples, transfer learning reduces the requirement, and useful tags are often inherited from existing metadata such as alt text or captions.
- Repetition and variation matter - examples are typically shown many times in epochs, and simple augmentations or simulated environments are treated as good enough to add variation.
- Training is compute-bound and largely sequential in its weight updates, which is why GPU supply limits progress, and its scaling follows approximate power laws rather than a first-principles theory.

## Evidence
- Basic loop: [[what-is-chatgpt-doing-and-why-does-it-work]] presents training as supplying input-output examples and trying to find weights that reproduce them.
- Loss function: [[what-is-chatgpt-doing-and-why-does-it-work]] uses an L2 sum-of-squares loss and shows the loss curve falling as training progresses.
- Gradient route: [[what-is-chatgpt-doing-and-why-does-it-work]] says the chain rule lets the operations of successive layers be unravelled so weights can be progressively adjusted.
- Local minima and high dimensions: [[what-is-chatgpt-doing-and-why-does-it-work]] describes descent ending in a local minimum and argues the 2011 deep-learning breakthrough was associated with the discovery that many weights can make approximate minimization easier.
- Equivalent solutions: [[what-is-chatgpt-doing-and-why-does-it-work]] shows several differently trained networks with similar performance but visibly different extrapolation behaviour.
- Data acquisition and transfer: [[what-is-chatgpt-doing-and-why-does-it-work]] describes piggybacking on alt tags, closed captions, and parallel documents, and says transfer learning can greatly reduce data requirements.
- Epochs and augmentation: [[what-is-chatgpt-doing-and-why-does-it-work]] says showing all examples repeatedly in epochs is standard and that slight image modifications or simulated driving data are useful variation.
- Self-supervised language training: [[what-is-chatgpt-doing-and-why-does-it-work]] says masking the end of a text and using the full text as the target means no explicit tagging is needed.
- Scale and compute: [[what-is-chatgpt-doing-and-why-does-it-work]] reports a few hundred billion training words for ChatGPT, notes the network's weight count is comparable to the number of training words, and concludes that training costs roughly the square of that number of operations.
- Training progress and hyperparameters: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a Wolfram Language training-progress monitor reporting an ADAM optimizer, batch size 64, GPU execution, a 1e-3 learning rate, and training loss flattening near 1e-2 while validation loss sits higher.
- Full-batch mechanics: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] processes four examples together, computes input-transpose-by-delta products, and illustrates how per-example contributions sum into shared weight updates.
- Hidden-layer error: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] projects output delta backward through `syn1.T` and scales it by the hidden sigmoid derivative before updating `syn0`.
- Convergence example: [[iamtrask-a-neural-network-in-11-lines-of-python-part-1]] reports mean absolute XOR error falling from about 0.496 to 0.0035 over 60,000 iterations.

## Counterevidence & Qualifications
The sources are conceptual walkthroughs, not complete training guides. The 2015 toy code omits biases and an explicit learning rate, performs additive full-batch updates without averaging, uses sigmoid saturation as a confidence mnemonic, and gives only training-set error. The broader essay names hyperparameters and lore without recipes, does not discuss regularization in depth, and gives no benchmarks. Its power-law and cost statements are rough and describe early-2023 systems; the claim that more parameters can ease training is an empirical observation, not a theorem.

## What Changed
- Added an executable full-batch example of forward prediction, backward delta assignment, and aggregated matrix weight updates.
- Created the concept page for the training loop that turns a network architecture into a working model.

## Related Concepts
- [[StochasticGradientDescent]] - the descent procedure whose loss-landscape behaviour this page depends on.
- [[Backpropagation]] - computes the earlier-layer error and derivatives used for weight changes.
- [[NeuralNetwork]] - the model class being fitted.
- [[TransformerArchitecture]] - the architecture used by the language models in the source.
- [[DeepLearningScaling]] - the contested claim that more compute, data, and parameters produce more capability.
- [[NaturalLanguageGeneration]] - the behaviour that trained language models then exhibit.

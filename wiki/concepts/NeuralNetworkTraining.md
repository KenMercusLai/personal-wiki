---
title: "Neural Network Training"
type: concept
tags: [ai, machine-learning, optimization, data]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[NeuralNetworkTraining]] is the process of finding the weights that make a network reproduce the examples it is given, by repeatedly measuring the error on a batch of examples and adjusting every weight to reduce it.

## Current Synthesis
The source treats training as the difference between a network that could compute anything and a network that actually does the job. The loop is simple to state: supply input-output examples, compute a loss such as the sum of squared differences, work out how the loss changes with respect to each weight, and move the weights to reduce it. What the essay adds is a practical picture of the effort involved. Small numerical functions still needed many examples to fit from scratch, loss curves fall and then flatten, and the size of the network relative to the task determines whether a fit is possible at all.

The training material is also where the essay is most explicit that practice outruns theory. Architecture choice, data acquisition, transfer learning, repetition across epochs, data augmentation, loss-function choice, loss-minimization method, and batch size are described as an art built by trial and error. The constraint that matters for large models is that weight updates are fundamentally sequential even though the forward pass parallelizes well, so training is bound by GPU availability, and the essay reports approximate power-law relationships between training loss, model size, and data quantity. For language specifically, training is easier to feed than image work because the objective is self-supervised: mask the end of a piece of text, and the text itself supplies the target.

## Key Claims
- Training means choosing weights that reproduce given examples, and relying on the network to interpolate reasonably between them.
- The loss function defines the distance to be minimized - the essay's example is a sum-of-squares (L2) loss - and minimization descends that surface, with calculus supplying the gradient through the chain rule so weights in successive layers can be adjusted.
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

## Counterevidence & Qualifications
The essay is a conceptual walkthrough, not a training guide: it names hyperparameters and lore without recipes, does not discuss regularization in depth, and gives no benchmarks. Its power-law and cost statements are rough, and the reported figures describe early-2023 systems. The claim that training can be easier with more parameters is presented as an empirical observation with a rough explanation, not as a theorem.

## What Changed
- Created the concept page for the training loop that turns a network architecture into a working model.

## Related Concepts
- [[StochasticGradientDescent]] - the descent procedure whose loss-landscape behaviour this page depends on.
- [[NeuralNetwork]] - the model class being fitted.
- [[TransformerArchitecture]] - the architecture used by the language models in the source.
- [[DeepLearningScaling]] - the contested claim that more compute, data, and parameters produce more capability.
- [[NaturalLanguageGeneration]] - the behaviour that trained language models then exhibit.

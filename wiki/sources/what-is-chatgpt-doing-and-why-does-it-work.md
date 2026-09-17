---
title: "What Is ChatGPT Doing … and Why Does It Work?"
type: source
tags: [ai, llm, neural-networks, transformers, language, machine-learning]
date: 2023-02-14
source_file: "/mnt/ken_personal_wiki/Articles/What Is ChatGPT Doing … and Why Does It Work.md"
---

## Summary
[[StephenWolfram]] gives a first-principles account of [[ChatGPT]] as a next-token machine: at every step it asks what token should follow the text so far, picks one from a ranked probability list produced by a [[NeuralNetwork]], and repeats. The essay climbs from letter-level and word-level [[NGramLanguageModel|n-gram]] generation, through the data-sparsity argument that counting can never estimate essay-length sequence probabilities, then builds up human-like task models, attractor basins, [[NeuralNetworkTraining|training]] with a loss function and gradient descent, [[Embeddings]] and meaning space, the [[TransformerArchitecture]] with its [[AttentionMechanism|attention]] blocks, and the human-feedback stage that turns a raw text predictor into a usable assistant. Its scientific conclusion is that ChatGPT's success is evidence that ordinary language and the thinking behind it are computationally "shallower" and more law-like than assumed, that those regularities might eventually be written down explicitly in [[SemanticGrammar]] and [[ComputationalLanguage]], and that [[ComputationalIrreducibility]] still limits what a feed-forward network can do without reaching for outside computational tools. The 93 embedded figures are almost all Wolfram Language code cells and their outputs - probability tables, generated text at different temperatures, letter and word n-gram samples, loss curves and weight landscapes, MNIST and cat/dog recognition examples, embedding projections, attention-weight matrices, a parse tree, and a parenthesis-language failure case - and they carry the essay's quantitative examples that the prose only summarizes.

## Key Claims
- ChatGPT is always producing a "reasonable continuation" of the text it has so far, and the published figures show the concrete form of that claim: the prompt "The best thing about AI is its ability to" returns learn at 4.5%, predict at 3.5%, make at 3.2%, understand at 3.1%, and do at 2.9%, over a vocabulary of roughly 50,000 tokens.
- Always taking the top-probability token is not enough. The inspected outputs show zero-temperature continuations drifting into repetition, while temperature-0.8 runs produce varied but sometimes "weird" text, which is why the essay reports 0.8 as the practical setting for essay generation and describes the choice as lore rather than theory.
- [[NGramLanguageModel|N-gram]] statistics give the intuition but cannot scale: with about 40,000 common English words there are 1.6 billion possible 2-grams and 60 trillion 3-grams, so probabilities for essay-length sequences can never be counted directly and must instead be estimated by a model trained on a few hundred billion words.
- The system is a [[NeuralNetwork]] of about 175 billion weights - a [[GPT3]] network - whose most important architectural feature is the [[TransformerArchitecture]], which uses [[AttentionMechanism|attention]] to look back over the whole token sequence instead of only a fixed local window.
- Almost nothing in the pipeline except the overall architecture is explicitly engineered: token and position [[Embeddings]], attention weights, and the final token probabilities are all learned end-to-end, and the remaining choices are described as engineering lore validated by trial and error.
- The network is feed-forward: generating each token pushes data once through every weight with no loops or recomputation, so the essay expects large language models to need outside computational tools such as [[WolframAlpha]] and [[WolframLanguage]] for genuinely irreducible computation.
- The human-feedback stage after raw training has a large effect on usefulness, and the essay treats the fact that a pre-trained network can follow a new instruction after seeing it once as a clue about how the model represents tasks.
- Wolfram's larger claim is scientific: because a network of this kind can generate recognizable human language at all, language and the thinking behind it are probably simpler and more law-like than expected, which makes an explicit [[ComputationalLanguage]]-based [[SemanticGrammar]] a plausible research programme.

## Key Quotes
> "what ChatGPT is always fundamentally trying to do is to produce a 'reasonable continuation' of whatever text it's got so far" - the essay's one-sentence thesis.

> "if we always pick the highest-ranked word, we'll typically get a very 'flat' essay" - on why random sampling below the top token is useful.

> "there just isn't even close to enough English text that's ever been written to be able to deduce those probabilities" - on the sparsity limit of n-gram counting.

> "there's never a 'model-less model'" - on parameters and the structure every model imposes.

> "the reason a neural net can be successful in writing an essay is because writing an essay turns out to be a 'computationally shallower' problem than we thought" - on the scientific reading of ChatGPT.

> "without, for example, accessing the 'computational superpowers' of Wolfram|Alpha, it's just saying things that 'sound right'" - on why fluent text is not the same as a correct computation.

## Connections
- [[StephenWolfram]] - author of the essay, and of the computational-language project the closing argument is built on.
- [[ChatGPT]] - the system being explained, from token prediction through human-feedback tuning.
- [[GPT2]] - the smaller open model used for the essay's runnable examples, including embeddings, attention weights, and the parenthesis-language experiment.
- [[GPT3]] - the 175-billion-weight network the essay says ChatGPT is based on.
- [[OpenAI]] - publisher of ChatGPT and of the instruction-following work the essay cites.
- [[WolframLanguage]] - the computational language used for every code cell in the essay.
- [[WolframAlpha]] - the knowledge engine the essay proposes as the tool neural nets need for irreducible computation.
- [[NeuralNetwork]] - the general model class: layered weighted neurons, attractors, universal approximation, and unreadable internal features.
- [[NeuralNetworkTraining]] - loss functions, gradient descent, epochs, data collection, transfer learning, augmentation, and GPU-bound training.
- [[StochasticGradientDescent]] - the loss-landscape descent picture, including local minima and many equivalent solutions.
- [[Embeddings]] - words, images, and token sequences represented as vectors whose neighbours are similar in meaning.
- [[MeaningSpace]] - the linguistic feature space in which a continuation becomes a trajectory with fans of probable next words.
- [[TransformerArchitecture]] - embedding module plus stacked attention blocks and a decode step to next-token probabilities.
- [[AttentionMechanism]] - the look-back weighting that lets a token relate to earlier words in the sequence.
- [[NGramLanguageModel]] - letters, words, and longer n-grams as the counting-based baseline the essay starts from.
- [[NaturalLanguageGeneration]] - the generation side: temperature, top-word decoding, repetition, and wandering.
- [[ComputationalIrreducibility]] - the trainability-versus-capability tradeoff that bounds what a network can learn.
- [[SemanticGrammar]] - the proposed layer of meaning rules above syntax.

## Contradictions
- The essay describes a pre-GPT-4 system: 175 billion weights, 96 attention blocks with 96 heads, and a ~50,000-token vocabulary. It does not cover later tool use, retrieval, multimodal training, or post-2023 model sizes, so it should be read as a 2023 explanation of ChatGPT's family rather than current product documentation.
- Its scientific thesis - that language is more law-like and computationally shallower than assumed - is an inference from a working system, not a measurement, and the essay itself states that no theory explains why the architecture works as well as it does.
- The claim that Wolfram|Alpha and Wolfram Language are "uniquely suitable" as the computational tool layer is the author's own product argument, and the essay's recommendations for [[SemanticGrammar]] and [[ComputationalLanguage]] are a research proposal rather than a demonstrated result.
- It qualifies the wiki's existing [[DeepLearningScaling]] caution rather than contradicting it: the essay accepts large-scale training as the mechanism behind ChatGPT while insisting that irreducible computation cannot be learned by scaling alone.

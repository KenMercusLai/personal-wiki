---
title: "Attention Mechanism"
type: concept
tags: [ai, neural-networks, language, mechanism]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[AttentionMechanism]] is the part of a transformer that lets each position in a sequence look back at earlier positions and recombine their embedding vectors with learned weights, so that the representation of the current token depends on selected parts of everything written before it.

## Current Synthesis
The source explains attention by contrast with n-grams. A bigram model chooses a word from its immediate predecessor; attention lets the model attend to tokens much further back, which is how it can, for example, connect a verb to a noun that appeared many words earlier. An attention block contains several heads that operate independently on different chunks of the embedding vector, and their weights are inspectable: the essay plots the look-back patterns of the twelve heads in GPT-2's first block on a fixed string, showing a lower-triangular structure in which each position distributes its attention over the past.

The essay's most concrete test of the mechanism is a toy language of balanced parentheses. With one attention block the network cannot learn much; with two blocks and about ten million examples it converges, and it then assigns sensible probabilities to continuations - but it also reports a 15% probability for a closing parenthesis in a position where that must unbalance the sequence, and its highest-probability completions start failing at longer lengths. The source reads this as the mechanism capturing nested tree-like structure approximately rather than performing an explicit count, and notes that even the full ChatGPT at the time struggled with long parenthesis matching. Attention is thus powerful for the regularities that show up in language, and not a substitute for algorithmic computation.

## Key Claims
- Attention weights how much of the past each position uses, which is a generalisation of the fixed local context used by n-gram models.
- A block splits its embedding vector across multiple heads that operate independently, and the split itself is a practical choice without a known explanation.
- Attention patterns are inspectable: the plotted look-back weights form structured, mostly upper-bounded patterns rather than uniform mixtures.
- Attention helps a model learn nested, tree-like structure, which the source argues is a major reason it works for human language.
- Attention is approximate rather than algorithmic: on parenthesis matching, a two-block transformer with about 400,000 weights still assigns substantial probability to a token that must break the grammar, and degrades as sequences lengthen.
- More training data is not automatically better - the source reports that beyond roughly ten million examples the parenthesis experiment's performance got worse.
- Knowing which parts of the sequence the model attends to does not explain what those parts mean, so attention inspection is not on its own an explanation of behaviour.

## Evidence
- Look-back framing: [[what-is-chatgpt-doing-and-why-does-it-work]] says attention heads "package up the past" in a form useful for finding the next token, generalising bigram prediction to much earlier words.
- Head structure: [[what-is-chatgpt-doing-and-why-does-it-work]] says GPT-2 has 12 heads per block operating on different chunks of the embedding vector, and states that the reason for splitting the vector is unknown.
- Inspected patterns: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the first block's twelve look-back-all-the-way-to-the-beginning recombination patterns for a hello/bye string, and a later figure shows the first head's attention weights across all twelve blocks.
- Parenthesis experiment setup: [[what-is-chatgpt-doing-and-why-does-it-work]] describes training a transformer on balanced parenthesis sequences with an End token, and says one attention block with eight heads and 128-wide feature vectors cannot learn much while two blocks converge after about ten million examples.
- Probability outputs: [[what-is-chatgpt-doing-and-why-does-it-work]] shows two next-token distributions - one where the sequence cannot end (roughly 46% open, 54% close, 0.038% End) and one where it can (51% open, 15% close, 34% End).
- Failure at length: [[what-is-chatgpt-doing-and-why-does-it-work]] lists highest-probability completions for progressively longer runs of open parentheses and marks the outputs that become unbalanced.
- Limits of counting: [[what-is-chatgpt-doing-and-why-does-it-work]] says cases needing explicit counting are "too computationally shallow" for the network, and that even the current ChatGPT struggled with long parentheses.

## Counterevidence & Qualifications
The evidence for attention as a language mechanism is one small toy task plus inspected weight plots; the source offers no quantitative benchmark and states that the reason splitting into heads helps is unknown. The parenthesis result is a negative example that bounds the mechanism's competence, not a general account of what attention computes, and the plotted weights are from GPT-2 rather than ChatGPT.

## What Changed
- Created the concept page for attention as the transformer's sequence-mixing mechanism.

## Related Concepts
- [[TransformerArchitecture]] - attention blocks are the repeating unit of this architecture.
- [[NeuralNetwork]] - attention is implemented with ordinary learned weights.
- [[Embeddings]] - attention recombines embedding vectors across positions.
- [[NGramLanguageModel]] - fixed local context is the baseline attention generalises.
- [[ComputationalIrreducibility]] - explicit counting is the kind of computation attention cannot approximate reliably.

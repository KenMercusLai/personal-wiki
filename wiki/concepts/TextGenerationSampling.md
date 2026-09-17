---
title: "Text Generation Sampling"
type: concept
tags: [ai, llm, generation, decoding]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[TextGenerationSampling]] is the rule a language model uses to pick the next token from its probability distribution, ranging from always taking the top-ranked token to randomly drawing lower-ranked tokens with a temperature parameter controlling how often that happens.

## Current Synthesis
The source makes sampling the difference between a technically correct predictor and a usable writer. A model always returns a ranked list of next-token probabilities; what varies is the choice made from that list. Taking the highest-probability token every time (temperature 0) is deterministic but produces text that the essay calls flat, and its inspected outputs show the failure mode directly - an essay continuation that repeats "It's a very good example of how to use AI to improve your life" and similar sentences rather than developing. Allowing sometimes-random lower-ranked choices produces more interesting text, and the essay shows several different essays generated from the same prompt at temperature 0.8, plus a long sample that is better than the greedy version but still, in the author's words, at best a bit weird.

The essay is explicit that this is practice rather than theory. Temperature 0.8 is reported as the setting that works best for essay generation, chosen because it seems to work rather than derived; the name comes from the exponential distributions familiar in statistical physics, with no physical connection claimed. The probability distribution itself is heavy-tailed: at the first step there are many possible next words, but their probabilities fall off quickly, and the log-log plot's roughly straight line corresponds to the power-law decay characteristic of language statistics (Zipf's law).

## Key Claims
- Generation always starts from a ranked probability list over the next token; sampling is the separate decision of which token to take.
- Always taking the top-ranked token produces deterministic text that tends to be flat, repetitive, and sometimes repeats phrases word for word.
- Randomly taking sometimes-lower-ranked tokens produces more varied and more interesting text, at the cost of output that can wander or read oddly.
- A temperature parameter controls how often lower-ranked tokens are used; the source reports 0.8 as the practical best setting for essay generation.
- Temperature is engineering lore, not derived theory: the name comes from exponential distributions in statistical physics, but no physical connection is claimed.
- Sampling makes the same prompt produce different outputs on different runs, which the essay demonstrates with five separate temperature-0.8 examples.
- The underlying distribution is long-tailed - many possible next words with rapidly falling probabilities following an approximately power-law decay - which is why random choice is meaningful rather than arbitrary.

## Evidence
- Deterministic continuation: [[what-is-chatgpt-doing-and-why-does-it-work]] builds text by repeatedly taking the model's top decision and shows a seven-step run ending in "... learn from experience. It's not".
- Repetition failure: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a longer zero-temperature continuation that loops on near-identical sentences about using AI to improve your life.
- Random sampling: [[what-is-chatgpt-doing-and-why-does-it-work]] says that randomly picking non-top words at temperature 0.8 gives a more interesting essay, and shows five different continuations produced from the same prompt.
- Practical setting: [[what-is-chatgpt-doing-and-why-does-it-work]] states that a temperature of 0.8 seems best for essay generation and notes there is no theory behind the choice.
- Temperature origin: [[what-is-chatgpt-doing-and-why-does-it-work]] explains that the concept exists because exponential distributions are being used, while denying any physical connection so far as is known.
- Model scale interaction: [[what-is-chatgpt-doing-and-why-does-it-work]] compares GPT-2 and the largest GPT-3 model at both zero temperature and temperature 0.8, and reports better results at the larger scale.
- Long tail of possibilities: [[what-is-chatgpt-doing-and-why-does-it-work]] plots next-word probabilities on log-log axes, notes that probabilities fall off quite quickly, and identifies the straight line as the power-law decay characteristic of language statistics.

## Counterevidence & Qualifications
The source gives one author's working setting, illustrated with a handful of samples from reference models, and says explicitly that the choice is empirical rather than explained. It does not cover other decoding methods - beam search, top-k or nucleus sampling, repetition penalties, or stopping criteria - and the reported temperature should be read as task- and model-specific rather than as a general recommendation.

## What Changed
- Created the concept page for how a language model's probability list becomes actual text.

## Related Concepts
- [[NaturalLanguageGeneration]] - sampling is the step that turns prediction into generation.
- [[LanguageModeling]] - the probability distribution being sampled comes from the model.
- [[NGramLanguageModel]] - the essay's n-gram samplers use the same repeated next-token choice.
- [[TransformerArchitecture]] - the decode step produces the distribution that sampling consumes.
- [[ChatGPT]] - the system whose essay-writing behaviour motivates the temperature discussion.

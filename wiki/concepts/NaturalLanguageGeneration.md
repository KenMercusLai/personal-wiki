---
title: "Natural Language Generation"
type: concept
tags: [nlp, generation, ai]
sources:
  - a-comprehensive-guide-to-build-your-own-language-model-in-python
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[NaturalLanguageGeneration]] is the use of language models to produce text continuations, sentences, or longer passages from learned linguistic patterns and prompts.

## Current Synthesis
Both sources treat generation as the visible demonstration of language modeling, and together they show the same loop at three scales. A trigram model samples next words and produces locally coherent Reuters-like text. A character-level GRU continues prompts after learning character sequences from the Declaration of Independence. GPT-2 then produces next-word completions and poem-like conditional text from a prompt. The ChatGPT source states the loop in its most general form and makes the sampling step explicit: generation is repeated next-token choice, and what distinguishes outputs is how the choice is made.

That last point is the main addition. Taking the top-probability token every time is deterministic and tends to produce flat, repetitive text; allowing random lower-ranked choices produces variety and sometimes wandering. The essay shows both failure modes and reports temperature 0.8 as the practical setting for essay generation, and it attributes the long tail of possible next words to the power-law statistics of language. It also notes the human-feedback stage after raw training, which tunes a text predictor towards the behaviours people want from a chat assistant, and observes that an assistant can "wander off" in ways human readers notice even when ordinary statistics on the text do not.

## Key Claims
- Text generation can be built by repeatedly predicting the next token or character.
- Even small statistical models can generate locally coherent but awkward output.
- Character-level neural models can produce unseen combinations by learning subword patterns.
- Pretrained transformers make longer prompt-conditioned generation accessible through library calls, and produce noticeably better output at larger scale.
- Generation quality depends on training data, context framing, model architecture, and decoding choices: greedy selection of the top token tends to be repetitive and flat, while temperature-based sampling trades determinism for variety and can drift away from human-like text.
- The distribution being sampled is long-tailed, with many possible continuations whose probabilities decay quickly.
- Raw next-token training is not enough for a good assistant: an additional human-feedback stage tunes the network towards output people judge useful.

## Evidence
- N-gram generation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] samples from trigram probabilities to generate Reuters-style sentence fragments.
- Character generation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] trains on the Declaration of Independence and observes sensitivity to seed text spacing.
- GPT-2 sentence completion: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] predicts "world" for the prompt "What is the fastest car in the".
- Conditional GPT-2 generation: [[a-comprehensive-guide-to-build-your-own-language-model-in-python]] uses a Robert Frost poem opening and generates a continuation with a similar poetic surface.
- Repeated prediction: [[what-is-chatgpt-doing-and-why-does-it-work]] describes essay writing as asking over and over what the next word should be, then adding one.
- Greedy repetition: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a long zero-temperature continuation that loops on near-identical sentences.
- Sampled variety: [[what-is-chatgpt-doing-and-why-does-it-work]] shows five different continuations from one prompt at temperature 0.8 and says the results are better than greedy output but still often a bit weird.
- Scale effect: [[what-is-chatgpt-doing-and-why-does-it-work]] compares GPT-2 and GPT-3 on the same prompt and reports better results from the larger model at both zero temperature and 0.8.
- Human feedback: [[what-is-chatgpt-doing-and-why-does-it-work]] describes building a model of human ratings and using it like a loss function to tune the network, and reports a large effect on producing human-like output.

## Counterevidence & Qualifications
The tutorial emphasizes impressive examples more than evaluation. It does not analyze factuality, repetition, prompt sensitivity, decoding parameters, copyright, safety, or whether generated text should be trusted beyond demonstration. The ChatGPT source's generation examples are single runs from reference models, and the essay itself frames the system as producing text that "sounds right" based on training material rather than text that has been verified as correct.

## What Changed
- Created a natural-language-generation concept page from the tutorial's sampling and GPT-2 examples.
- Added the decoding comparison, long-tailed probability structure, and human-feedback stage from the ChatGPT explanation.

## Related Concepts
- [[LanguageModeling]] - generation uses learned sequence probabilities.
- [[NGramLanguageModel]] - N-grams can generate text by iterative sampling.
- [[NeuralLanguageModel]] - neural models generate characters or text continuations.
- [[NaturalLanguageProcessing]] - generation is one NLP task family.
- [[TextGenerationSampling]] - the rule that chooses among probable tokens.
- [[MeaningSpace]] - generation also traces a path through the model's feature space.

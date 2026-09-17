---
title: "Semantic Grammar"
type: concept
tags: [language, meaning, computation, ai]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[SemanticGrammar]] is a proposed layer of rules about how meaningful units combine - not just how parts of speech may be ordered - so that a sentence can be judged not only grammatical but sensible with respect to some model of the world.

## Current Synthesis
The source reaches semantic grammar by asking what more than syntax a language model must have learned. Syntax constrains word order and can be captured by parse trees, and the essay shows a transformer learning nested, tree-like structure, including a toy parenthesis language it approximates rather than solves. But "Inquisitive electrons eat blue theories for fish" is syntactically fine and still meaningless, so something else must be constraining what can be said. The one corner of that something that has been studied for two millennia is logic: Aristotle's syllogisms are rules of the form "sentences that follow these patterns are reasonable", and the essay suggests ChatGPT may implicitly pick up that much from text while failing on more sophisticated formal logic.

The essay's proposal is to generalize that idea. A semantic grammar would operate on finer categories than nouns and verbs - a concept of "moving", a concept of an "object" that keeps its identity independent of location, and a general rule that objects can move - built on top of some model of the world. Such a grammar would still separate what is sayable from what is the case: "The elephant traveled to the Moon" would pass the grammar while not having been realized, and would be entirely at home in a fictional world. Wolfram frames ChatGPT as having implicitly assembled a surprising amount of this layer, and argues that its success makes an explicit, human-readable version both more plausible and more useful, in the same way that syllogistic logic later grew into formal logic and digital circuitry.

## Key Claims
- Syntax alone does not explain meaningfulness: grammatically correct sentences can be semantically empty.
- Meaning requires constraints of a second kind, which the source names semantic grammar.
- Semantic grammar operates on concepts finer than parts of speech, such as objects, movement, and identity preserved across locations.
- It implies an underlying model of the world, which supplies the skeleton that word-level language is layered onto.
- Semantic rules govern what can be sensibly said, not what actually exists: physically unrealized sentences can pass the grammar and belong to fiction.
- Logic is the oldest special case of such rules, and could not be generalized beyond its original patterns until formal logic was developed.
- The source argues that ChatGPT implicitly acquired a quantity of semantic grammar from training, and that making it explicit would make the same capabilities more direct, efficient, and transparent.

## Evidence
- The gap syntax leaves: [[what-is-chatgpt-doing-and-why-does-it-work]] says "Inquisitive electrons eat blue theories for fish" is grammatically correct but would not be considered a success if generated.
- Syntax as a constraint: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a parse tree for "The best thing about AI is its ability to learn from experience" and a parse tree for balanced parentheses.
- Logic as a special case: [[what-is-chatgpt-doing-and-why-does-it-work]] presents syllogistic logic as a small known corner of meaning rules and expects ChatGPT to reproduce simple inferences while failing at sophisticated formal logic.
- Categories and rules: [[what-is-chatgpt-doing-and-why-does-it-work]] proposes concepts such as "moving" and an "object" that maintains identity independent of location, with a general rule that objects can move.
- World model underneath: [[what-is-chatgpt-doing-and-why-does-it-work]] says semantic grammar necessarily engages a model of the world that serves as a skeleton for actual language.
- Sayable versus realized: [[what-is-chatgpt-doing-and-why-does-it-work]] says "The elephant traveled to the Moon" would pass a semantic grammar while remaining unrealized.
- Implicit acquisition: [[what-is-chatgpt-doing-and-why-does-it-work]] claims ChatGPT has effectively pieced together a rather impressive quantity of semantic grammar from training.
- Path from logic to towers: [[what-is-chatgpt-doing-and-why-does-it-work]] argues that formal logic let basic syllogistic constructs build structures such as digital circuitry, and expects generalized semantic logic to do the same.

## Counterevidence & Qualifications
Semantic grammar is a research proposal in the source, not a built artefact: no grammar, ontology, or evaluation is presented, and the claim that ChatGPT has implicitly learned one is an inference from its outputs. The essay also does not say how much of meaningfulness such rules could cover, and it concedes that ordinary language is vague because its meaning rests on a social contract rather than on an implementation.

## What Changed
- Created the concept page for semantic grammar as the proposed meaning layer above syntax.

## Related Concepts
- [[ComputationalLanguage]] - the precise symbolic medium in which semantic rules could be written and executed.
- [[WolframLanguage]] - the existing system the source treats as the starting point for that medium.
- [[MeaningSpace]] - the empirical picture of meaning; semantic grammar is the explicit counterpart the essay hopes for.
- [[NaturalLanguageGeneration]] - generation is where an implicit semantic grammar becomes visible.
- [[ComputationalIrreducibility]] - a reason some meaning-relevant computations cannot be learned as patterns.
- [[ChatGPT]] - the system presented as having acquired this layer implicitly.

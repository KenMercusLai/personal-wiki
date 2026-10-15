---
title: "Belief Revision"
type: concept
tags: [artificial-intelligence, knowledge-representation, epistemology, uncertainty]
sources:
  - "2309.02009"
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Definition
[[BeliefRevision]] is the rational incorporation of new information into an epistemic state while prioritizing that information, preserving consistency, and changing prior beliefs as little as the chosen revision policy requires.

## Current Synthesis
The current source uses AGM/Katsuno-Mendelzon revision to model how a listener interprets a joke. A listener's knowledge state is paired with an ordering of possible interpretations; revising by new information selects the most plausible models that satisfy it. The joke context first supports a defeasible expectation, while the punchline selects a different preferred state that can overturn the expectation yet retrospectively explain the context.

This is an ordinal, model-selection account rather than ordinary probabilistic updating. Default rules and strict constraints can induce the plausibility ordering through possibility theory, making revision and [[NonmonotonicReasoning]] two views of the same underlying preference structure.

## Key Claims
- Rational revision gives priority to consistent new information while minimizing disturbance to prior belief.
- A total plausibility preorder supplies a semantic representation of a revision operator by selecting the best models compatible with the new information.
- In joke comprehension, conflict between the preferred context models and preferred context-plus-punchline models formalizes surprise.
- Revision by the punchline is revealing when its preferred models entail the original context.
- The revision result depends on the listener's background knowledge and plausibility ordering.

## Evidence
- Revision principles: [[2309.02009]] restates consistency, minimal change, and priority to new information through the AGM and Katsuno-Mendelzon tradition.
- Model-selection semantics: [[2309.02009]] represents revision as choosing minimal models of the input under a faithful total preorder.
- Humor application: [[2309.02009]] defines surprise and revelation from the relationship among revision results for context and punchline.

## Counterevidence & Qualifications
The paper assumes propositional representations and a rational revision structure after the natural-language joke has already been encoded. It does not solve language interpretation, identify the listener's actual defaults, or establish that human joke comprehension literally implements the formal operator. Surprise plus revelation is not specific to humor, and absurd statements inconsistent with strict knowledge require the separate norm-disregard treatment. [[BayesianUpdating]] is related but uses priors and likelihoods rather than the paper's ordinal minimal-change semantics.

## What Changed
- Created the concept from the paper's revision-theoretic model of context and punchline integration.
- Distinguished ordinal belief revision from probabilistic Bayesian updating.
- Recorded listener dependence and the gap between formal encoding and human cognition.

## Related Concepts
- [[NonmonotonicReasoning]] - default rules can induce the plausibility ordering used by revision.
- [[ComputationalHumor]] - applies revision results to surprise and revelation in jokes.
- [[IncongruityResolution]] - handles cases where a norm must be disregarded before revelation succeeds.
- [[BayesianUpdating]] - alternative belief-change framework based on probabilistic evidence rather than ordinal minimal change.

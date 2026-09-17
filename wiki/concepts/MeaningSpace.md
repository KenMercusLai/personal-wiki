---
title: "Meaning Space"
type: concept
tags: [ai, language, geometry, embeddings]
sources:
  - what-is-chatgpt-doing-and-why-does-it-work
last_updated: 2026-09-17
knowledge_schema: synthesis-v1
---

## Definition
[[MeaningSpace]] is the geometric picture in which a piece of text is a point in an embedding space, semantically similar text sits nearby, and generating a continuation traces a trajectory from one point to the next.

## Current Synthesis
The source uses meaning space to ask whether there might be "semantic laws of motion" that constrain how a text can move while staying meaningful. The layout itself is already informative: when common nouns are projected into two dimensions, animals and fruits separate, parts of speech separate, and an ambiguous word such as "crane" splits into its bird and machine senses. Continuing a prompt then becomes a path through that layout, and at each point there is a "fan" of high-probability next words that tends to point in a fairly definite direction. The essay projects the prompt "The best thing about AI is its ability to" together with its continuation into 2D and 3D and shows successive fans as the path advances.

The essay is careful not to overclaim. There is no geometrically obvious law of motion in the pictures, and it says that is unsurprising given how complicated the underlying process is; the trajectory may simply not be stated in the right variables, just as a simpler law might appear if the right coordinate system were chosen. Its conclusion is that the wiki cannot currently read off from a model's internal behaviour what it has "discovered" about how language is put together: the space shows structure and local directionality, and it does not yet expose an interpretable dynamics.

## Key Claims
- Text is represented as a location in a high-dimensional feature space, and similarity of meaning corresponds to proximity in that space.
- A continuation is a trajectory: each generated token moves the representation to a new point, and the model's probabilities describe the possible next moves.
- At a given point, the high-probability next tokens form a fan that points in a more or less definite direction, rather than scattering uniformly.
- Readable structure exists in the projections - semantic categories separate and ambiguous words split by sense - which is what makes the geometric framing plausible.
- No simple law of motion is visible: the essay's 2D and 40-step 3D trajectories look messy and do not by themselves reveal a compact dynamics.
- The absence of a visible law may be a problem of variables rather than of principle; the essay raises geodesic-like descriptions as a possibility it is not ready to test.
- Meaning space is therefore an interpretive picture, not an explanation: it shows where text goes without saying why that path is the meaningful one.

## Evidence
- Category structure: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a 2D projection of common nouns in which related words group together and semantically similar words are placed nearby.
- Parts of speech: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a projection where nouns, verbs, adjectives, adverbs, and pronouns occupy distinguishable regions.
- Sense splitting: [[what-is-chatgpt-doing-and-why-does-it-work]] uses "crane" to show that sentences containing one word can separate into bird and machine clusters.
- Trajectory rendering: [[what-is-chatgpt-doing-and-why-does-it-work]] plots the prompt "The best thing about AI is its ability to" and its zero-temperature continuation as a path in a 2D projection.
- Fans of probable words: [[what-is-chatgpt-doing-and-why-does-it-work]] shows the fan of high-probability next words at a point on the trajectory, then the successive fans that appear as the model moves along it.
- Long-run messiness: [[what-is-chatgpt-doing-and-why-does-it-work]] shows a 3D representation of a 40-step trajectory and says it looks like a mess, which does not encourage the search for mathematical-physics-like laws by inspection.
- Wrong-variables hedge: [[what-is-chatgpt-doing-and-why-does-it-work]] says it may be that the right coordinate system would reveal something simple like movement along geodesics, but that it is not yet possible to decode this from the model's internal behaviour.

## Counterevidence & Qualifications
The evidence is a set of projections and hand-picked prompts, not a quantitative study: projecting a high-dimensional space down to two or three dimensions necessarily loses structure, and the essay says as much. The "fan" is a rendering of model probabilities rather than an observed physical drift, and the essay's own conclusion is that no law of motion has been found.

## What Changed
- Created the concept page for meaning space, trajectories, and the search for semantic laws of motion.

## Related Concepts
- [[Embeddings]] - meaning space is the geometry of an embedding.
- [[TransformerArchitecture]] - the blocks transform a point in this space into the next one.
- [[NaturalLanguageGeneration]] - generation is the process that traces the trajectory.
- [[SemanticGrammar]] - the essay hopes explicit meaning rules could replace an unreadable trajectory.
- [[ComputationalIrreducibility]] - a reason the trajectory may have no compact description.

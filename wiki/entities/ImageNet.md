---
title: "ImageNet"
type: entity
tags: [dataset, benchmark, computer-vision, deep-learning]
sources:
  - from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune
  - from-not-working-to-neural-networking-technology
  - inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[ImageNet]] is presented as a free collection of millions of hand-labeled images and an annual computer-vision competition that made data scale and model progress publicly comparable, while depending on a large and often hidden annotation workforce.

## Current Profile
Fei-Fei Li launched ImageNet to test the view that larger labeled datasets would change machine learning. The dataset went live in 2009 and gained an annual contest in 2010, training entrants on labeled examples before evaluating them on unseen test images and convening a follow-up workshop to exchange methods. A later journalistic account makes the construction layer explicit: nearly 50,000 people, most recruited through [[AmazonMechanicalTurk]], reportedly checked, sorted, and labeled almost one billion candidate images over two years to produce more than 14 million categorized images.

The sources place ImageNet's historical importance in the 2012 competition: one says a deep network built by Geoffrey Hinton's students performed almost twice as accurately as its nearest competitor, while the shorter Economist excerpt reports winning accuracy moving from 72% in 2010 to 85% in 2012 and then 96% in 2015. Both treat the 2012 discontinuity as a field-level opinion shift, but only the Economist excerpt extends that effect to rehabilitation of the broader “AI” label. The labor account qualifies that technical narrative: benchmark scale depended not only on models and compute, but also on the task design, screening, and repetitive judgments of a distributed workforce.

## Key Characteristics
- Combined a very large labeled-image collection with open access for research.
- Supplied supervised training data rather than asking systems to learn solely from unlabeled imagery.
- Required nearly 50,000 people to screen and label a much larger candidate pool, according to the TechRepublic account.
- Used an annual contest to create a common evaluation and publication event.
- Made the 2012 deep-learning performance discontinuity visible to the broader field.
- Supplied a public progress narrative through reported winning results of 72% in 2010, 85% in 2012, and 96% in 2015.
- Became a symbol of the joint importance of data, computation, and trainable model architecture.

## Evidence
- Scale and access: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] reports more than 14 million labeled images in a free database.
- Institutional timeline: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] dates project initiation to 2007, public availability to 2009, and the contest to 2010.
- 2012 result: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] reports that Hinton's students achieved nearly twice the accuracy of the closest competitor.
- Opinion shift: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] presents that result as evidence that persuaded previously skeptical researchers.
- Evaluation institution: [[from-not-working-to-neural-networking-technology]] describes labeled training images, previously unseen test images, and a follow-up workshop where winners shared techniques.
- Reported progression: [[from-not-working-to-neural-networking-technology]] gives winning accuracy as 72% in 2010, 85% in 2012, and 96% in 2015 against a stated 95% human average.
- Broader reputation: [[from-not-working-to-neural-networking-technology]] treats the 2012 result as a catalyst for renewed public use of the “AI” label.
- Annotation workforce: [[inside-amazons-clickworker-platform-how-half-a-million-people-are-being-paid-pennies-to-train-ai-techrepublic]] reports that nearly 50,000 people, most recruited through [[AmazonMechanicalTurk]], checked, sorted, and labeled almost one billion candidate images over two years.

## Qualifications
The sources simplify competition results to “accuracy” without consistently naming the error metric or experimental details. The Economist excerpt does not explain the class scope, evaluation protocol, or construction of its 95% human average, and its 96% machine result cannot be generalized beyond the benchmark task. The TechRepublic account reports labor scale but does not document task instructions, sampling, worker pay, annotation disagreement, quality controls, or whose categories shaped the dataset. ImageNet success measures performance on a curated labeled benchmark, not robust open-world vision, causal understanding, fairness, safe deployment, or fair labor conditions.

## What Changed
- Added the scale and platform provenance of the human labor used to screen and label ImageNet's candidate images.
- Reframed dataset scale as an achievement of task design and distributed judgment as well as data, models, and compute.

## Relationships
- [[FeiFeiLi]] - founder who organized the dataset and competition.
- [[DeepLearning]] - approach whose 2012 benchmark result made the dataset historically prominent.
- [[GeoffreyHinton]] - led the group whose students produced the highlighted winning system.
- [[NeuralNetworkTraining]] - uses ImageNet's labeled examples for supervised fitting.
- [[UnsupervisedLearning]] - contrasts with ImageNet's explicit labeling regime.
- [[DataAnnotationLabor]] - captures the screening, sorting, and labeling work that made the dataset usable.
- [[AmazonMechanicalTurk]] - platform through which most of the reported annotation workforce was recruited.

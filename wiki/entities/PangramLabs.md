---
title: "Pangram Labs"
type: entity
tags: [ai, detection, writing]
sources:
  - the-revolt-of-the-reader
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Overview
[[PangramLabs]] is represented here as the company behind Pangram 3 and Pangram 4, models intended to classify text as human- or AI-authored.

## Current Profile
In [[BryanCantrill]]'s account, Pangram Labs produced the first AI-writing detector he found reliable enough for regular use. He describes Pangram 3 as conservative, with a reassuringly low false-positive rate but a less satisfactory false-negative rate, and Pangram 4 as a step-function improvement on both error types. The classifier then becomes more than a diagnostic: Cantrill uses it as a publication gate for Oxide's public prose and recommends similar policies to institutions that value an authentic voice.

## Key Characteristics
- Develops classifiers for distinguishing human-authored from AI-authored text.
- Is valued in the source primarily for low reported false-positive and false-negative rates.
- Serves as both an individual screening tool and an institutional publication gate.
- Shapes trust policy by turning a subjective suspicion about prose into an actionable classification.

## Evidence
- Model progression: [[the-revolt-of-the-reader]] reports that Pangram 3 reduced false-positive concerns but still missed some AI-authored text, while Pangram 4 improved both dimensions.
- Known-origin use: [[the-revolt-of-the-reader]] says the author's confidence came partly from testing material whose provenance he otherwise knew.
- Policy adoption: [[the-revolt-of-the-reader]] says an Oxide public-writing rule requires a human-authored Pangram result.
- Public relevance: [[the-revolt-of-the-reader]] argues that readers will increasingly run suspicious prose through Pangram, changing the incentives for model-authored publication.

## Qualifications
The evidence here is one enthusiastic user's account, not Pangram Labs' technical documentation or an independent benchmark. No confusion matrix, evaluation corpus, language or genre coverage, operating threshold, adversarial robustness result, or comparison with edited and mixed-authorship text is supplied. A low observed error rate on known samples does not establish universal reliability, and using a changing proprietary classifier as a hard gate can produce governance and appeal problems when it errs.

## What Changed
- Established a source-scoped profile of Pangram Labs and the reported Pangram 3-to-4 capability change.
- Recorded its use as a detector-backed institutional publication control.

## Relationships
- [[BryanCantrill]] - user and advocate who supplies the wiki's current evidence about the company.
- [[AIWritingDetection]] - Pangram is the article's preferred implementation of this classifier category.
- [[AIAssistedWriting]] - the detector is used to police the boundary between editing assistance and delegated prose.
- [[SemanticAblation]] - generic or formulaic model style motivates detection, though style alone does not prove provenance.

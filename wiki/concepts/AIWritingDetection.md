---
title: "AI Writing Detection"
type: concept
tags: [ai, writing, detection, governance]
sources:
  - the-revolt-of-the-reader
last_updated: 2026-10-11
knowledge_schema: synthesis-v1
---

## Definition
[[AIWritingDetection]] is the classification of prose as human- or AI-authored, used here both to investigate suspected model involvement and to gate public writing under an institutional authorship policy.

## Current Synthesis
The source treats detection as an incentive mechanism rather than merely a forensic label. If readers can reliably recognize or classify substantially LLM-authored prose, they can stop reading, avoid the named author, or filter institutional output, making cheap text generation reputationally expensive in a way analogous to spam filtering. Low false positives matter especially because an accusation can damage a human writer, while low false negatives determine how easily AI prose passes as human. [[BryanCantrill]] reports that Pangram 4 performs well enough on both dimensions to support an Oxide public-writing gate, but his account supplies no independent benchmark or formal process for disputed results.

## Key Claims
- Detection can change the economics of AI-authored publishing by helping readers withdraw attention and trust.
- False positives and false negatives have different harms and must be evaluated separately.
- Known-origin samples can support practical calibration, but anecdotal use does not replace a blinded, representative benchmark.
- A detector-backed policy attempts to guarantee reader confidence, not merely enforce a hidden internal process rule.
- Hard publication gates inherit the classifier's coverage, threshold, drift, evasion, and appeal limitations.

## Evidence
- Incentive mechanism: [[the-revolt-of-the-reader]] compares scalable AI-writing identification with spam filtering, where reliable classification raised the cost of being labeled.
- Error tradeoff: [[the-revolt-of-the-reader]] describes Pangram 3 as low in false positives but weaker on false negatives, and Pangram 4 as improving both in the author's experience.
- Known-origin calibration: [[the-revolt-of-the-reader]] says some tested samples had provenance the author otherwise knew.
- Governance use: [[the-revolt-of-the-reader]] reports a requirement that Oxide public writing receive a human-authored classification from Pangram.

## Counterevidence & Qualifications
The article does not report independent tests across genres, languages, model families, editing intensities, document lengths, or mixed human-machine workflows. Its detector findings are experiential, and the underlying technical posts are linked rather than summarized as evaluated evidence. Detection can also confuse provenance with style: formulaic human prose may look machine-generated, while edited or adversarial machine prose may evade classification. A binary gate therefore needs versioning, documented thresholds, retesting rules, human review, and an appeal path if used for consequential decisions.

## What Changed
- Established AI-writing detection as both a classifier problem and an audience-trust governance mechanism.
- Added the distinct operational importance of false-positive and false-negative rates.
- Added the limitation that a detector-backed publication rule remains dependent on an imperfect and changing model.

## Related Concepts
- [[AIAssistedWriting]] - detection is used to police where editing support ends and delegated authorship begins.
- [[LearningByWriting]] - the policy protects the inference that the named writer personally performed the cognitive work of composition.
- [[SemanticAblation]] - stylistic flattening can motivate suspicion but is not by itself reliable evidence of AI provenance.
- [[AIDependencySkillAtrophy]] - widespread delegation may weaken the human reading and writing practice needed to judge prose independently.

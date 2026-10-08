---
title: "Memory Forgetting"
type: concept
tags: [ai, agents, memory, attention]
sources:
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryForgetting]] is the deliberate reduction of a memory's retrieval priority or active status so noise does not overwhelm limited agent and human attention.

## Current Synthesis
Forgetting is not identical to deletion or disbelief. The source separates a time-sensitive decay score from accumulated confidence: inactivity can make a well-supported item less salient without making it less established. An importance floor protects decisions and core insights, while search, display, opening, dwell, evolution links, and Crystal citation supply implicit evidence of continued value.

Archival is conservative and conjunctive rather than triggered by age alone. This protects rarely accessed but important knowledge, though the proposed rule that confidence never falls is too strong for discredited evidence and should not be generalized into an epistemic principle.

## Key Claims
- Unlimited retention without attention control turns memory into an increasingly noisy retrieval space.
- Decay and confidence represent different questions and should be scored separately.
- Important decisions and core insights need a minimum retrieval floor even after inactivity.
- Implicit behavior can inform attention when explicit spaced-repetition ratings are unavailable.
- Archival should require multiple weak-value signals rather than one age threshold.
- Forgetting policy should reduce salience without silently destroying recoverable evidence.

## Evidence
- Distinct scores: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] applies exponential decay with frequency adjustment while allowing confidence to rise from interactions and graph evidence.
- Importance floor: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] protects decisions and core insights from becoming undiscoverable solely through age.
- Implicit signals: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] names search hits, result display, opens, dwell, EVOLVES links, and Crystal citations.
- Conservative archive gate: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] requires very low decay, no interaction, more than 90 days, and active status together.

## Counterevidence & Qualifications
The source gives no retrieval-quality experiment, user study, calibrated decay curve, false-archive rate, or comparison with ACT-R, FSRS, learned ranking, or explicit feedback. Implicit interaction can reflect exposure bias rather than value. Confidence may need to decrease when provenance is discredited, a claim is challenged, or earlier corroboration is found non-independent.

## What Changed
- Established forgetting as attention allocation rather than automatic deletion.
- Separated decay, confidence, importance floors, implicit evidence, and archival gates.

## Related Concepts
- [[AgentMemory]] - forgetting keeps persistent memory usable under finite attention and context.
- [[MemoryCompaction]] - consolidation reduces redundancy while forgetting adjusts ongoing salience.
- [[MemoryEvolution]] - changed or superseded memories may remain historically recoverable at lower priority.
- [[MemoryConflictResolution]] - challenged evidence may require confidence revision rather than simple decay.
- [[AttentionManagement]] - both human and agent systems allocate scarce attention among retained information.
- [[NowledgeMem]] - supplies the described decay, confidence, and archival implementation.

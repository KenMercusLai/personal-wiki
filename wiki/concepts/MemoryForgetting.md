---
title: "Memory Forgetting"
type: concept
tags: [ai, agents, memory, attention]
sources:
  - wei-ai-agent-gou-jian-ji-yi-xi-tong
  - powermem-forgetting-design
last_updated: 2026-10-08
knowledge_schema: synthesis-v1
---

## Definition
[[MemoryForgetting]] is the deliberate reduction of a memory's retrieval priority or active status so noise does not overwhelm limited agent and human attention.

## Current Synthesis
Forgetting is not identical to deletion or disbelief. A time-sensitive decay score can lower an inactive memory's salience without making a well-supported item less established, while an importance floor protects decisions and core insights. Search, display, opening, dwell, evolution links, and citation can supply implicit evidence of continued value.

A tiered implementation can assign working, short-term, or long-term status from importance, vary decay speed by tier, promote a memory after repeated access, and multiply retrieval relevance by the current decay factor. Keeping deduplication and compression in a separate optimizer clarifies that forgetting, consolidation, and deletion are different controls.

Together the sources support soft forgetting as attention allocation over recoverable evidence. Archival should remain conservative and conjunctive rather than triggered by age alone, and a policy still needs a distinct way to revise confidence when provenance is discredited.

## Key Claims
- Unlimited retention without attention control turns memory into an increasingly noisy retrieval space.
- Decay and confidence represent different questions and should be scored separately.
- Memory tiers can express different expected lifetimes, but their boundaries and decay rates require calibration rather than biological analogy alone.
- Important decisions and core insights need a minimum retrieval floor even after inactivity.
- Implicit behavior can inform attention when explicit spaced-repetition ratings are unavailable.
- Forgetting policy should reduce salience without silently destroying recoverable evidence.

## Evidence
- Distinct scores: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] applies exponential decay with frequency adjustment while allowing confidence to rise from interactions and graph evidence.
- Importance floor: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] protects decisions and core insights from becoming undiscoverable solely through age.
- Implicit signals: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] names search hits, result display, opens, dwell, EVOLVES links, and Crystal citations.
- Conservative archive gate: [[wei-ai-agent-gou-jian-ji-yi-xi-tong]] requires very low decay, no interaction, more than 90 days, and active status together.
- Tiered decay and promotion: [[powermem-forgetting-design]] assigns importance-scored working, short-term, and long-term tiers, applies faster decay to lower tiers, and promotes on access or importance.
- Retrieval weighting: [[powermem-forgetting-design]] multiplies relevance by a continuous decay factor before ranking results.
- Separation from compaction: [[powermem-forgetting-design]] places exact deduplication, semantic deduplication, and LLM compression in a separate optimizer.

## Counterevidence & Qualifications
Neither source gives a retrieval-quality experiment, user study, calibrated decay curve, false-archive rate, or comparison with ACT-R, FSRS, learned ranking, or explicit feedback. Implicit interaction can reflect exposure bias rather than value. PowerMem's thresholds, tier multipliers, neuroscience analogies, and `relevance × decay` formula are source-specific design choices, and that product account does not represent confidence separately. Confidence may need to decrease when provenance is discredited, a claim is challenged, or earlier corroboration is found non-independent.

## What Changed
- Added tier-specific decay, access-driven promotion, and decay-weighted retrieval from [[PowerMem]].
- Distinguished forgetting from the project's separate deduplication and compression stage.

## Related Concepts
- [[AgentMemory]] - forgetting keeps persistent memory usable under finite attention and context.
- [[MemoryCompaction]] - consolidation reduces redundancy while forgetting adjusts ongoing salience.
- [[MemoryEvolution]] - changed or superseded memories may remain historically recoverable at lower priority.
- [[MemoryConflictResolution]] - challenged evidence may require confidence revision rather than simple decay.
- [[AttentionManagement]] - both human and agent systems allocate scarce attention among retained information.
- [[NowledgeMem]] - supplies the described decay, confidence, and archival implementation.
- [[PowerMem]] - supplies the tiered decay, promotion, and ranking implementation.

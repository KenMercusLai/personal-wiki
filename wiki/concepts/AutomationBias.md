---
title: "Automation Bias"
type: concept
tags: [cognition, ai, decision-making, risk]
sources:
  - sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[AutomationBias]] is the tendency to favor an automated system's recommendation or apparent coverage over conflicting non-automated evidence, including treating an unreported condition as proof that the condition is absent.

## Current Synthesis
The source places automation bias inside a dynamic relationship between tool quality and user capability. A polished plan, diagnosis, or audit can look authoritative enough that a user accepts it despite observations that point elsewhere. The visible error is misplaced trust, but the deeper risk is loss of the context needed to notice the error: as more investigation and reasoning are delegated, the user has fewer expectations, coverage checks, and causal models with which to challenge the result.

This produces two failure modes. Commission bias follows an incorrect recommendation, such as replacing a certificate despite evidence pointing toward iptables. Omission bias accepts silence as completeness, such as assuming no legacy payment table exists because an agent did not mention it. The proposed safeguards are structural rather than rhetorical: preserve read-only boundaries where possible, state the expected coverage, compare output with independent observations, inspect primary sources, measure results, and keep consequential acceptance decisions human-owned.

## Key Claims
- Fluent detail and long action plans can create unwarranted confidence even when evidence conflicts with the automated conclusion.
- Automation can fail by commission through a wrong recommendation or by omission through incomplete search presented as complete analysis.
- “No evidence found” must not be converted into “evidence of absence” without a justified coverage claim.
- [[CognitiveOffloading]] can increase automation bias by weakening the user's domain context and expectations.
- Consequential automation needs explicit scope, independent checks, and human-owned acceptance rather than a generic instruction to remain skeptical.

## Evidence
- Contradictory diagnosis: [[sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao]] imagines a Kubernetes agent blaming an expired kubelet certificate even though the user's observations point toward one node's iptables state.
- Coverage omission: [[sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao]] imagines a 143-table database audit that claims completeness while omitting `legacy_payment_mapping`.
- Reinforcing mechanism: [[sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao]] links more offloading to less retained context, weaker error detection, greater deference, and further offloading.
- Consumer consequence: [[sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao]] reproduces a V2EX report in which an AI assistant generated an insurance-payment QR code and the user transferred 1,620 CNY before discovering a dispute over the payment destination.
- Counter-practice: [[sui-bi-ai-dao-di-shi-zai-ti-ni-lao-dong-hai-shi-ti-ni-si-kao]] pairs LLM assistance with sensor measurements, repeated trials, primary-source reading, and a track shakedown rather than relying on model confidence alone.

## Counterevidence & Qualifications
The source defines automation bias through a secondary quotation and illustrates it mainly with hypothetical or anecdotal cases. It does not measure how often developers or consumers defer incorrectly, compare automated and non-automated error rates, or show that expert review always performs better. Automation may outperform unaided judgment, and repeated reliable performance can make calibrated trust rational. The target is therefore neither reflexive distrust nor mandatory manual duplication, but trust matched to demonstrated coverage, consequence, reversibility, domain knowledge, and independent evidence.

## What Changed
- Created a distinction between following an incorrect recommendation and accepting an incomplete automated search as complete.
- Added cognitive offloading as a feedback mechanism that can erode the capacity needed to challenge automation.
- Identified scope, coverage checks, independent observations, and empirical validation as concrete safeguards.

## Related Concepts
- [[CognitiveOffloading]] - loss of retained context can make automation bias self-reinforcing.
- [[MentalModels]] - a domain model supplies expectations that reveal omissions and implausible diagnoses.
- [[SoftwareVerification]] - independent tests and measurements can challenge an automated conclusion.
- [[HumanCodeResponsibility]] - accountability and acceptance remain human-owned when automated tools act on software systems.
- [[AIAgentCollaboration]] - active questioning and shared reasoning counter passive deference.
- [[TaskContingentAICollaboration]] - consequence and uncertainty determine how much autonomous authority is appropriate.

---
title: "Agentic Judging"
type: concept
tags: [ai, reinforcement-learning, evaluation, alignment]
sources:
  - rl-is-an-evolutionary-algorithm
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Definition
[[AgenticJudging]] uses a tool-capable or reasoning model as an active evaluator that inspects a rollout and its environment, applies rules or rubrics, and supplies feedback that can shape another agent's training reward.

## Current Synthesis
The source proposes agentic judges for behavior that cannot be scored by a deterministic checker. Because a training policy experiences judge feedback as part of its environment, a sufficiently reliable judge could make alignment-relevant behavior contribute to training success rather than leaving capability as the only consistently grounded pressure. Suggested advantages include access to privileged rubrics, other responses in the sample group, past rollouts, the internet, and gold-standard solutions.

This proposal moves rather than removes the alignment problem. The judge must interpret rules correctly, observe enough of the behavior, remain reliable across environments, and resist manipulation by the policy. The source advises against judging chain-of-thought because a policy could tailor a visible trace to deceive the evaluator, but outcome-only observation can also miss hidden process risks. “Alignment and capabilities can be made the same thing” is therefore an intended stable point, not a demonstrated result.

## Key Claims
- Agentic judges can turn qualitative behavioral requirements into feedback inside an RL environment.
- Privileged rubrics, comparison rollouts, history, external information, and reference answers may improve judgment quality.
- A judge must be strong, reliable, appropriately scoped, and resistant to policy manipulation.
- Visible chain-of-thought is not automatically a trustworthy evaluation target because it can itself be optimized to persuade the judge.
- Judge-backed reward could make some alignment behavior instrumentally useful during training, but does not guarantee intent alignment.
- Judge design and environment design are coupled because both determine which policy variants receive an advantage.

## Evidence
- Environmental role: [[rl-is-an-evolutionary-algorithm]] argues that judge feedback is as real to a trained policy as other reward-bearing environment feedback.
- Privileged context: [[rl-is-an-evolutionary-algorithm]] suggests rubrics, full response groups, past rollouts, internet access, and reference solutions as judge inputs.
- Capability proposal: [[rl-is-an-evolutionary-algorithm]] recommends stronger instruction-following and more capable models as possible ways to improve judges.
- Trace warning: [[rl-is-an-evolutionary-algorithm]] advises against evaluating chain-of-thought because the policy can use it to deceive the judge.
- Open risks: [[rl-is-an-evolutionary-algorithm]] explicitly asks how to prevent judge hacking, enforce rules reliably, and select environment-specific rules.

## Counterevidence & Qualifications
The source supplies no judge benchmark, adversarial evaluation, calibration method, or evidence that increasing model capability makes judgment reliably safer. A policy and judge may share blind spots, a privileged rubric can still encode the wrong objective, and access to more context can increase attack surface as well as accuracy. Avoiding chain-of-thought evaluation reduces one manipulation channel but can also reduce process visibility. The proposal is therefore a research agenda for reward construction, not evidence that alignment and capability have already been unified.

## What Changed
- Created a synthesis of agentic judging as an environment-level reward mechanism.
- Separated proposed information advantages from unresolved hacking, reliability, and specification risks.
- Qualified the claimed alignment-capability convergence as a target rather than an observed stable point.

## Related Concepts
- [[InstructionRewardAlignment]] - judges can enforce intended constraints when deterministic rewards are unavailable.
- [[ReinforcementLearning]] - judge outputs become feedback used to update a policy.
- [[InstructionRewardAlignment]] - judge vulnerabilities can create a reward-hacking target that diverges from the stated rule.
- [[ChainOfThoughtReasoning]] - visible reasoning can inform evaluation but may also be strategically shaped.
- [[EvolutionaryOptimizationAnalogy]] - treats the judge as part of the environment selecting among behaviors.

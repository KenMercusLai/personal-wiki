---
title: "Reinforcement Learning"
type: concept
tags: [machine-learning, ai, robotics, agents]
sources:
  - a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
last_updated: 2026-09-26
knowledge_schema: synthesis-v1
---

## Definition
[[ReinforcementLearning]] is a machine-learning approach in which an agent changes its policy over sequential actions using rewards or penalties tied to resulting outcomes.

## Current Synthesis
The sources show reinforcement learning at three levels of specificity. A simple game analogy describes an initially uncertain policy whose action probabilities improve from wins and losses despite imperfect credit assignment. A robotics case uses detected pleased or frustrated human expressions as feedback for [[ASIMO]]. [[SearchR1]] applies the same outcome-driven frame to language-model retrieval: the model generates a sequence of reasoning, search, information, and answer actions, then policy optimization uses final-answer correctness to reinforce better trajectories.

Search-R1 is important here because the learned behavior is not merely answer generation. The policy must decide whether more evidence is needed, formulate queries, consume returned information, and stop with an answer within an action budget. The article names PPO and GRPO as optimization options and states that the actual Search-R1 work uses GRPO, although its teaching code substitutes a simplified policy-gradient loss.

The career source also uses reinforcement learning metaphorically: repeated experiments under uncertainty can improve future decisions even when a person lacks a complete plan. That analogy captures iteration and feedback but should not be confused with a specified machine-learning objective.

## Key Claims
- Reinforcement learning is suited to sequences of decisions whose quality is evaluated through later outcomes.
- Coarse outcome reward can shape a policy even when assigning credit to every individual action is difficult.
- Human reactions can serve as feedback when task success is interpersonal rather than simple win/loss.
- Language-model agents can learn search timing, query formulation, evidence use, and stopping behavior through retrieval trajectories.
- Outcome-only reward simplifies supervision but leaves credit assignment, reward design, exploration, and training stability as central concerns.
- Reinforcement learning can serve as a useful metaphor for repeated career experiments, but the analogy is not a technical training specification.

## Evidence
- Sequential learning and coarse reward: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] uses a Pong-like agent whose actions are rewarded after wins and penalized after losses.
- Human-feedback robotics: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] describes pleased or frustrated expressions as feedback for work involving ASIMO.
- Learned retrieval policy: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] presents Search-R1 as learning when to search, what to search, and how to use results.
- Bounded trajectory: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] reproduces a rollout with explicit search and answer tags, an action budget, inserted retrieval results, and a rethink branch.
- Optimization scope: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] describes final-answer reward and identifies GRPO as the actual algorithm while using simplified policy-gradient pseudocode for instruction.
- Career metaphor: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] frames repeated career decisions as experiments that can improve judgment without a known final path.

## Counterevidence & Qualifications
Neither source is a technical reinforcement-learning survey. The career essay intentionally simplifies policies, rewards, and credit assignment. The Search-R1 article is a secondary tutorial and does not reproduce the original experiments, benchmark improvements, ablations, retrieval-token masking implementation, reward details, compute cost, or failure analysis; its sample code is explicitly not the actual GRPO training system. Outcome-only reward can also reinforce shortcuts or inefficient searches unless the environment, constraints, and evaluation are carefully designed.

## What Changed
- Added language-model retrieval as a concrete sequential-decision application of reinforcement learning.
- Added Search-R1's bounded tagged trajectory and final-answer reward framing.
- Distinguished the article's simplified policy-gradient teaching code from the named GRPO implementation.
- Preserved the earlier robotics example and career metaphor while clarifying their different evidentiary roles.

## Related Concepts
- [[AgenticRAG]] - retrieval behavior can be encoded in prompts or optimized as a learned policy.
- [[SearchR1]] - Search-R1 is the source's concrete RL-trained search framework.
- [[ActiveLearning]] - both emphasize improvement through action and feedback, though they use different learning setups.
- [[CareerPlanning]] - the career source uses reinforcement learning as a metaphor for exploratory decisions.
- [[CreativeTechnicalCareer]] - reinforcement learning is one technical and metaphorical strand in Wibowo's career account.

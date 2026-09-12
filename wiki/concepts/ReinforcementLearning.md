---
title: "Reinforcement Learning"
type: concept
tags: [machine-learning, ai, robotics]
sources:
  - a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[ReinforcementLearning]] is a machine-learning approach where an agent improves decisions by trying actions in states, receiving rewards or penalties, and adjusting future action probabilities to maximize expected reward.

## Current Synthesis
The source explains reinforcement learning through a simple game-like model: an AI begins with uncertain action probabilities, receives rewards for good outcomes and penalties for bad ones, and improves through many iterations even when it cannot initially identify which individual action caused success. The essay then extends the idea into robotics by using human emotional feedback for [[ASIMO]], and into life strategy by treating repeated career experiments as a way to become better at decisions under uncertainty.

## Key Claims
- Reinforcement learning is useful when a system must make sequences of decisions rather than one isolated classification.
- The agent can learn from coarse outcome feedback even when credit assignment across individual actions is imperfect.
- Iteration can make initially clueless decision-making better over time.
- Human feedback can be used as the reward signal for robot learning when task success is interpersonal rather than simply win/loss.
- As a metaphor, reinforcement learning can support exploratory [[CareerPlanning]] when the person lacks a clear plan.

## Evidence
- Sequential decisions: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] uses a Pong-like AI deciding how to move a paddle from current game state.
- Coarse rewards: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] explains that actions during wins are rewarded and actions during losses are penalized despite imperfect credit assignment.
- Iteration: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] argues that enough different circumstances can let the system identify beneficial actions.
- Human-feedback robotics: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] describes using detected pleased or frustrated human expressions as feedback for [[ASIMO]].
- Career metaphor: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] says the method made Wibowo more hopeful about making many career decisions without knowing the final path.

## Counterevidence & Qualifications
The source is an accessible career essay, not a technical survey. Its reinforcement-learning explanation is intentionally simplified and does not cover value functions, policies, exploration strategies, reward shaping, discounting, temporal-difference learning, or modern deep RL.

## What Changed
- Created the concept page for reinforcement learning as both a technical method and a life-metaphor source.

## Related Concepts
- [[ActiveLearning]] - both emphasize improvement through doing and feedback.
- [[CareerPlanning]] - the source uses reinforcement learning to frame career exploration.
- [[CreativeTechnicalCareer]] - reinforcement learning is one technical strand in Wibowo's art-and-technology path.

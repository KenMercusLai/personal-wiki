---
title: "Reinforcement Learning"
type: concept
tags: [machine-learning, ai, robotics, agents]
sources:
  - a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium
  - yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag
  - from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune
  - gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft
  - large-language-model-technical-reports-overview
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Definition
[[ReinforcementLearning]] is a machine-learning approach in which an agent changes its policy over sequential actions using rewards or penalties tied to resulting outcomes.

## Current Synthesis
The sources now span simple feedback analogies, robotics, games, retrieval agents, and reasoning-model training. A Pong-like career metaphor and pleased-or-frustrated reactions around [[ASIMO]] introduce the basic idea: actions change a policy when later feedback says whether an outcome was better or worse. [[AlphaGo]] adds the canonical bounded-game case, combining deep learning, expert games, and self-play, while the StarCraft analysis shows why success depends on the environment: hidden state, many simultaneous units, changing opponents, real-time action, and limited simulation access make policy learning much harder.

Language models turn generated tokens, searches, and answers into policy actions. [[SearchR1]] optimizes when to search, what to search for, how to incorporate returned evidence, and when to answer under an action budget. The newer reasoning-model overview adds the training architecture behind this pattern. Conventional RLHF combines supervised fine-tuning, a learned preference reward model, PPO policy updates, a critic/value model, and a frozen reference policy. [[GroupRelativePolicyOptimization]] instead samples multiple answers to one prompt and estimates advantage from group-relative rewards, eliminating the critic but increasing dependence on sampling and reward quality.

[[DeepSeekR1]] sharpens two distinctions. First, R1-Zero reports that outcome-verifiable RL can induce extended reasoning without initial SFT, but the practical R1 model adds cold-start examples, rejection-sampled SFT, language-consistency reward, and a second RL phase to improve readability and general behavior. Second, rule-based correctness and format rewards can be more robust than learned reward models on objectively checkable tasks, but they do not solve reward design for open-ended output. [[KimiK15]] similarly combines long-chain SFT and RL over curated verifiable prompts, then uses curriculum, prioritized sampling, and length penalties to balance difficulty and reasoning cost.

## Key Claims
- Reinforcement learning is suited to sequences of decisions whose quality is evaluated through later outcomes, but the environment and reward determine what behavior is learnable.
- Coarse outcome reward can shape policies without labeling every action, while leaving credit assignment, shortcut learning, and reward hacking unresolved.
- Self-play and simulation are powerful in bounded, observable environments; hidden state, large action spaces, real-time constraints, and limited simulation reduce that advantage.
- Language-model agents can learn multi-step retrieval and reasoning policies, including when to search, continue, stop, or answer.
- PPO stabilizes language-model policy updates with a critic/value estimate and reference-policy constraint; GRPO removes the critic by comparing multiple sampled outputs within a prompt group.
- Pure outcome-driven RL can induce reasoning in a base model, but usable systems may still require supervised cold starts, readability controls, general-task data, and preference alignment.
- Verifiable rewards fit mathematics, code, and constrained formats better than subjective open-ended tasks, so reward design and evaluation scope remain central limits.

## Evidence
- Feedback and human response: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] uses a Pong-like policy analogy and describes pleased or frustrated expressions as feedback in ASIMO work.
- Bounded self-play and operational control: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] says AlphaGo learned from professional games and extensive self-play and reports a DeepMind data-center efficiency application.
- Environment constraints: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] identifies closed simulation, partial observability, many heterogeneous units, changing strategies, rare tactics, and timing as coupled obstacles, motivating learned abstractions plus scripted control.
- Learned retrieval policy: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] presents Search-R1's tagged, bounded search-and-answer rollout with final-answer reward and names GRPO as its actual optimizer.
- RLHF and PPO: [[large-language-model-technical-reports-overview]] diagrams supervised fine-tuning, preference-model training, and PPO, then explains policy, critic, reward, and reference-model roles.
- Critic-free optimization: [[large-language-model-technical-reports-overview]] contrasts PPO with GRPO's grouped sampling, normalized relative rewards, and missing value model.
- Pure RL and staged usability: [[large-language-model-technical-reports-overview]] distinguishes R1-Zero's base-model RL from R1's cold start, rejection-sampled SFT, language consistency, and all-scenario RL.
- Reward scope and efficiency: [[large-language-model-technical-reports-overview]] describes accuracy and format rules, PRM/MCTS failure modes, Kimi's curated prompt set, and length-aware optimization.

## Counterevidence & Qualifications
The sources are a career essay, tutorials, historical journalism, a 2016 forecast, and a secondary overview of vendor technical reports rather than a unified experimental literature. The career metaphor is not a technical objective; the Search-R1 article substitutes teaching pseudocode for its named GRPO implementation; the AlphaGo and data-center accounts omit reproducible details; and the StarCraft piece is historically scoped. The reasoning-model claims rely on vendor benchmarks and checkable-task-heavy training, with no independent reproduction here. Removing a critic does not remove rollout cost, variance, or reward dependence, and rule rewards can be gamed or become unavailable for subjective work. More reasoning tokens can improve some benchmark answers while increasing latency, cost, and opportunities for unfaithful or redundant traces.

## What Changed
- Added the full RLHF/PPO training stack and distinguished reward, reference, critic, and policy roles.
- Added GRPO as a critic-free group-relative alternative with sampling and reward-design tradeoffs.
- Added the R1-Zero result that reasoning can emerge from pure RL while clarifying why practical DeepSeek-R1 restores supervised stages.
- Added Kimi's verifiable prompt curation, difficulty sampling, and length-aware optimization.
- Reframed reward verifiability and environment structure as the shared boundary across games, retrieval, and reasoning models.

## Related Concepts
- [[GroupRelativePolicyOptimization]] - removes PPO's learned critic and estimates advantage from grouped response rewards.
- [[ChainOfThoughtReasoning]] - reasoning trajectories can be reinforced from outcome-level feedback.
- [[ReasoningModelDistillation]] - transfers discovered reasoning behavior into smaller models rather than repeating full RL.
- [[AgenticRAG]] - retrieval behavior can be encoded in prompts or optimized as a learned policy.
- [[SearchR1]] - concrete RL-trained search framework using bounded retrieval trajectories.
- [[DeepLearning]] - supplies the learned representations and policy models used in the game and language-model cases.
- [[StarCraftAITestbed]] - combines environment constraints that make policy learning harder than in fully observable board games.

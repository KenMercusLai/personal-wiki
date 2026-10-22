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
  - rl-is-an-evolutionary-algorithm
  - training-100x-cheaper-retrieval-models-neon-and-castform
  - 2607.07508
  - policy-gradient
  - mai-thinking-1-continuous
  - rlbook
last_updated: 2026-10-22
knowledge_schema: synthesis-v1
---

## Definition
[[ReinforcementLearning]] is a machine-learning approach in which an agent changes its policy over sequential actions using rewards or penalties tied to resulting outcomes.

## Current Synthesis
The sources now span simple feedback analogies, robotics, games, retrieval agents, and reasoning-model training. A Pong-like career metaphor and pleased-or-frustrated reactions around [[ASIMO]] introduce the basic idea: actions change a policy when later feedback says whether an outcome was better or worse. [[AlphaGo]] adds the canonical bounded-game case, combining deep learning, expert games, and self-play, while the StarCraft analysis shows why success depends on the environment: hidden state, many simultaneous units, changing opponents, real-time action, and limited simulation access make policy learning much harder.

The new study notebook supplies the missing textbook bridge from this intuition to core mechanics. [[MultiArmedBandit]] isolates exploration from state transitions; [[MarkovDecisionProcess]] formalizes state, policy, reward, return, and value; dynamic programming computes model-based expectations; [[MonteCarloEstimation]] learns from complete sampled returns; and [[TemporalDifferenceLearning]] bootstraps online from sampled successors. [[FunctionApproximation]] replaces independent table entries with shared parameters, enabling continuous-state generalization while making representation, sampling distribution, and stability part of the problem.

The new mathematical tutorial supplies a missing mechanism beneath direct policy optimization. [[PolicyGradient]] parameterizes action probabilities and maximizes expected trajectory return. The [[LogDerivativeTrick]] turns the derivative of a trajectory distribution into a [[ScoreFunctionEstimator]], after which [[MonteCarloEstimation]] uses sampled trajectories to approximate the gradient. Factoring trajectory probability also separates policy-controlled action terms from initial-state and environment-transition terms whose gradients vanish when the environment does not depend on policy parameters.

Language models turn generated tokens, searches, and answers into policy actions. [[SearchR1]] optimizes when to search, what to search for, how to incorporate returned evidence, and when to answer under an action budget. The newer reasoning-model overview adds the training architecture behind this pattern. Conventional RLHF combines supervised fine-tuning, a learned preference reward model, PPO policy updates, a critic/value model, and a frozen reference policy. [[GroupRelativePolicyOptimization]] instead samples multiple answers to one prompt and estimates advantage from group-relative rewards, eliminating the critic but increasing dependence on sampling and reward quality.

[[DeepSeekR1]] sharpens two distinctions. First, R1-Zero reports that outcome-verifiable RL can induce extended reasoning without initial SFT, but the practical R1 model adds cold-start examples, rejection-sampled SFT, language-consistency reward, and a second RL phase to improve readability and general behavior. Second, rule-based correctness and format rewards can be more robust than learned reward models on objectively checkable tasks, but they do not solve reward design for open-ended output. [[KimiK15]] similarly combines long-chain SFT and RL over curated verifiable prompts, then uses curriculum, prioritized sampling, and length penalties to balance difficulty and reasoning cost.

Time and policy freshness become explicit concerns in [[AsynchronousReinforcementLearning]]. When agent trajectories have very different lengths, synchronous batches idle on stragglers, while asynchronous learners consume completed rollouts under increasing policy lag. [[SingleRolloutAsynchronousOptimization]] treats GRPO's prompt group as its own synchronization barrier and restores a critic so one rollout can train immediately. Its direct token masking, faster partly frozen critic, and observation-skipping GAE stabilize the reported runs, but the method trades group generation for value-model memory, compute, initialization, and bias.

A deliberately loose [[EvolutionaryOptimizationAnalogy]] adds a selection-pressure view: sampled behaviors vary, reward changes their future probability, and diverse tasks may favor strategies that transfer. Its practical contribution is the selection-pressure question rather than a new RL definition. [[InstructionRewardAlignment]] determines whether following a stated constraint is actually competitive; mismatched environments may reward cheating or broad avoidance. [[AgenticJudging]] is proposed for qualitative requirements that deterministic checks cannot score, but judge hacking, correlated errors, and rule misspecification remain unresolved.

The [[Castform]] case study grounds those reward-design concerns in a corpus-specific retrieval workflow. It synthetically derives questions and ground truths from documents, exposes a hybrid-search tool, and combines correct-source retrieval, correct-chunk citation, and answer correctness into the reward. The reported reward curve improves while remaining noisy, and individual rollout inspection is intended to reveal broken tools or reward hacking. This shows how proprietary data can define an environment without an existing hand-labeled task set, but inferred ground truth and synthetic questions can also carry generation errors and coverage bias into the policy.

Sustained, multi-domain RL from a mid-trained checkpoint with no prior reasoning traces makes stability, environment design, and continuity first-class concerns. The [[MAIThinking1]] recipe modifies GRPO with adaptive entropy control, a hard outer importance-ratio clip, top-p mask replay, staged rollout-length expansion, and pass-rate filtering; task-specific rewards are combined with language-consistency and difficulty-aware length terms. Verifiable STEM and code tasks, stateful software and tool environments, and subjective preference and safety tasks share one core objective but require different graders. Self-distillation transfers later successful traces into a fresh or newer base after collapse or model updates, while specialist models are consolidated by SFT and refined by a final RL stage.

## Key Claims
- Reinforcement learning spans model-based expected updates and model-free sampled learning; its main objects are policies, returns, state or action values, and reward-shaped behavior over sequential decisions.
- Coarse outcome reward can shape policies without labeling every action, while leaving credit assignment, shortcut learning, evaluation awareness, and reward hacking unresolved.
- Self-play and simulation are powerful in bounded, observable environments; hidden state, large action spaces, real-time constraints, and limited simulation reduce that advantage.
- Language-model agents can learn multi-step retrieval and reasoning policies, including when to search, continue, stop, or answer.
- PPO stabilizes language-model policy updates with a critic/value estimate and reference-policy constraint; GRPO removes the critic through grouped rewards, while asynchronous single-rollout training restores a critic to avoid waiting for that group.
- Pure outcome-driven RL can induce reasoning in a base model, but usable systems may still require supervised cold starts, readability controls, general-task data, and preference alignment.
- Verifiable rewards fit mathematics, code, and constrained formats better than subjective open-ended tasks; agentic judges extend feedback to qualitative behavior but add an attack and reliability surface, while sustained frontier-scale RL also depends on rollout freshness, inference/learner agreement, recovery, expert routing, isolation, and weight transfer.

## Evidence
- Textbook mechanism map: [[rlbook]] connects bandits, finite MDPs, Bellman updates, Monte Carlo returns, TD bootstrapping, Sarsa, function approximation, average reward, and policy gradients through worked questions.
- Feedback and human response: [[a-career-retrospective-10-years-working-in-tech-sailor-mercury-medium]] uses a Pong-like policy analogy and describes pleased or frustrated expressions as feedback in ASIMO work.
- Bounded self-play and operational control: [[from-2016-why-deep-learning-is-suddenly-changing-your-life-fortune]] says AlphaGo learned from professional games and extensive self-play and reports a DeepMind data-center efficiency application.
- Environment constraints: [[gamasutra-ben-webers-blog-deepmind-challenges-for-starcraft]] identifies closed simulation, partial observability, many heterogeneous units, changing strategies, rare tactics, and timing as coupled obstacles, motivating learned abstractions plus scripted control.
- Learned retrieval policy: [[yuan-chao-fa-rag-jin-hua-zhi-lu-chuan-tong-rag-dao-gong-ju-yu-qiang-hua-xue-xi-shuang-lun-qu-dong-de-agentic-rag]] presents Search-R1's tagged, bounded search-and-answer rollout with final-answer reward and names GRPO as its actual optimizer.
- RLHF and PPO: [[large-language-model-technical-reports-overview]] diagrams supervised fine-tuning, preference-model training, and PPO, then explains policy, critic, reward, and reference-model roles.
- Critic-free optimization: [[large-language-model-technical-reports-overview]] contrasts PPO with GRPO's grouped sampling, normalized relative rewards, and missing value model.
- Pure RL and staged usability: [[large-language-model-technical-reports-overview]] distinguishes R1-Zero's base-model RL from R1's cold start, rejection-sampled SFT, language consistency, and all-scenario RL.
- Reward scope and efficiency: [[large-language-model-technical-reports-overview]] describes accuracy and format rules, PRM/MCTS failure modes, Kimi's curated prompt set, and length-aware optimization.
- Selection-pressure framing: [[rl-is-an-evolutionary-algorithm]] maps sampled behavior to variation and reward to selection, then predicts that diverse tasks should favor more transferable strategies.
- Instruction and reward consistency: [[rl-is-an-evolutionary-algorithm]] contrasts unrewarded instructions with unstated penalties and argues that localized mismatch can select environment-sensitive cheating.
- Qualitative feedback: [[rl-is-an-evolutionary-algorithm]] proposes privileged agentic judges while explicitly retaining judge hacking, enforcement reliability, and rule choice as open problems.
- Corpus-specific post-training: [[training-100x-cheaper-retrieval-models-neon-and-castform]] constructs synthetic tasks from documents and scores retrieval, citation, and final-answer correctness over a hybrid search environment.
- Learning and infrastructure trace: [[training-100x-cheaper-retrieval-models-neon-and-castform]] shows a rising but noisy average-reward curve and a bursty database workload created by thousands of parallel multi-search rollouts.
- Asynchronous optimization: [[2607.07508]] contrasts the grouped completion barrier with immediate single-rollout consumption, then reports direct off-policy masking, critic and action-granularity ablations, and stable reasoning and coding training.
- Direct policy-gradient mechanism: [[policy-gradient]] derives expected trajectory return, the likelihood-ratio gradient, trajectory factorization, Monte Carlo sampling, and a negative return-weighted log-probability loss.
- Long multi-domain climb: [[mai-thinking-1-continuous]] reports entropy-controlled and outer-clipped GRPO, top-p and MoE-routing replay, curriculum length extension, specialist climbs, self-distillation recovery, and verifiable or judged rewards across STEM, agents, helpfulness, and safety.

## Counterevidence & Qualifications
The sources are a career essay, tutorials, historical journalism, a 2016 forecast, secondary overviews, vendor reports, primary but first-party RL papers, and speculative practitioner material rather than a unified experimental literature. The new notebook is a learner's record whose explanations are mostly generated by several AI assistants and not systematically verified against the textbook; it is useful for conceptual coverage, not authority. The policy-gradient source is a pedagogical derivation, not an experimental comparison; its vanilla estimator gives every action the same undiscounted trajectory return and omits baselines, reward-to-go, advantage estimates, and other variance controls. The career metaphor is not a technical objective; the Search-R1 article substitutes teaching pseudocode for its named GRPO implementation; the AlphaGo and data-center accounts omit reproducible details; and the StarCraft piece is historically scoped. The reasoning-model claims rely heavily on vendor benchmarks and checkable-task-heavy training. SAO uses one MoE backbone, bundles several optimization changes, omits full throughput and compute accounting, and does not publish evidence for its named GLM-5.2 deployment. The MAI report is more operationally detailed but still withholds weights, complete data, training code, private evaluations, and equal-budget comparisons; its success does not isolate the causal contribution of the many bundled algorithmic and infrastructure changes. Castform likewise omits evaluation and training details, while corpus-derived synthetic questions and inferred answers can encode errors, blind spots, and reward shortcuts. A rising training reward does not establish held-out generalization. Removing a critic does not remove rollout cost, variance, or reward dependence; restoring one adds memory, compute, and estimation error; and rule rewards can be gamed or become unavailable for subjective work. The evolutionary essay explicitly uses nonstandard agent/policy terminology and does not experimentally establish its claims about multi-domain generalization, deception, evaluation awareness, or agentic judging. More reasoning or tool actions can improve some tasks while increasing latency, cost, infrastructure load, and opportunities for unfaithful or redundant traces.

## What Changed
- Added the core progression from bandits and MDPs through model-based expectation, sampled returns, TD bootstrapping, and approximation.
- Distinguished model-free learning from an inability to observe outcomes after action.
- Added partial observability, coverage, and state-distribution weighting as foundational boundaries.

## Related Concepts
- [[MultiArmedBandit]] - isolates action-value estimation and exploration without changing state.
- [[MarkovDecisionProcess]] - formalizes sequential state, action, reward, policy, and value relationships.
- [[TemporalDifferenceLearning]] - learns values online from sampled reward-plus-successor targets.
- [[FunctionApproximation]] - generalizes value or policy estimates across large or continuous state spaces.
- [[PolicyGradient]] - directly optimizes a stochastic policy using return-weighted action log-probability gradients.
- [[ScoreFunctionEstimator]] - supplies the general expectation-gradient identity used by vanilla policy gradients.
- [[LogDerivativeTrick]] - restores a sampling distribution inside a differentiated expectation.
- [[MonteCarloEstimation]] - approximates policy expectations from sampled trajectories.
- [[GroupRelativePolicyOptimization]] - removes PPO's learned critic and estimates advantage from grouped response rewards.
- [[ChainOfThoughtReasoning]] - reasoning trajectories can be reinforced from outcome-level feedback.
- [[ReasoningModelDistillation]] - transfers discovered reasoning behavior into smaller models rather than repeating full RL.
- [[AgenticRAG]] - retrieval behavior can be encoded in prompts or optimized as a learned policy.
- [[SearchR1]] - concrete RL-trained search framework using bounded retrieval trajectories.
- [[DeepLearning]] - supplies the learned representations and policy models used in the game and language-model cases.
- [[StarCraftAITestbed]] - combines environment constraints that make policy learning harder than in fully observable board games.
- [[EvolutionaryOptimizationAnalogy]] - reframes stochastic behavior and reward updates as variation and selection.
- [[InstructionRewardAlignment]] - asks whether rewarded behavior matches the constraints given to the policy.
- [[AgenticJudging]] - supplies qualitative feedback when deterministic outcome checks are insufficient.
- [[Castform]] - manages the corpus-derived task, tool, reward, and rollout workflow in the Neon case study.
- [[Neon]] - supplies the searchable environment queried repeatedly during the retrieval-policy rollouts.
- [[AsynchronousReinforcementLearning]] - decouples rollout generation and learning while introducing policy-lag and freshness problems.
- [[SingleRolloutAsynchronousOptimization]] - source-specific actor-critic response to grouped asynchronous training barriers.
- [[MAIThinking1]] - model-level case combining reasoning, agentic, preference, and safety RL.
- [[HillClimbingMachine]] - places RL inside a broader data, infrastructure, evaluation, and safety improvement loop.

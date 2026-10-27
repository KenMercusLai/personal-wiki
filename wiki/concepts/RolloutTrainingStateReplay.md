---
title: "Rollout-Training State Replay"
type: concept
tags: [reinforcement-learning, distributed-training, sparse-attention, mixture-of-experts, dataflow]
sources:
  - rl-r3-best-implementation
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[RolloutTrainingStateReplay]] records discrete per-token choices made during model rollout and reuses them during training so kernel, batching, and parallel-layout differences do not independently change sparse-attention positions or MoE expert selections.

## Current Synthesis
Replay has two separate responsibilities: preserve the semantic choice made by the rollout model and preserve its alignment with tokens after training reshapes the batch. The source's key systems move is to separate heavy choice records from lightweight layout metadata. Immutable, layer-sharded payload chunks travel directly from the rollout producer to shared storage and then to the training consumer; object-and-range references travel through response handling, sample assembly, scheduling, packing, unpadding, rank partitioning, and collectives.

Late materialization makes the existing token-layout machinery reusable. A sample manifest expands into fixed-width per-token handles only when a micro-batch is arranged. Those handles follow the same verified fused transformations as hidden states, and the trainer fetches the referenced payload rows only after final positions and stage ownership are known. This reduces intermediate memory and communication without claiming that the payload itself disappears: it is still copied off the rollout GPU, persisted, read by training, and replayed once.

Correctness depends on lifecycle design as much as byte volume. Speculative decoding needs a mutable tail before stable chunks become write-once objects; asynchronous writes need backpressure; exactly one rank must own object creation; missing payloads must fail closed rather than silently weakening replay; and the batch manifest must enumerate even overwritten objects so consumption can be the single reclamation authority.

## Key Claims
- Replaying discrete rollout choices can reduce inference-training mismatch that token identity alone does not eliminate.
- Heavy per-token state should bypass intermediate components that need only token ownership and final placement.
- Immutable payload objects plus range manifests compress the control representation without repeatedly decoding, merging, sorting, or copying the payload.
- Fixed-width token handles can reuse a proven layout path and preserve alignment through padding removal, packing, partitioning, and collectives.
- Materializing only after final placement lets each pipeline stage read only its required layers and keeps resident payload scope to one micro-batch.
- Backpressure, single-writer ownership, fail-closed reads, and manifest-driven deletion are part of replay correctness.
- The pattern generalizes to rollout-produced token state only when intermediate decisions do not depend on the state's contents.

## Evidence
Mismatch and semantic replay:
- [[rl-r3-best-implementation]] explains how small numerical and execution differences can alter discrete Top-K expert or attention choices and thereby later log probabilities and gradients.

Control-payload separation:
- [[rl-r3-best-implementation]] reports replacing a 3.7-GB trajectory payload on the control path with KB-scale object-and-range manifests while leaving immutable payloads in shared storage.

Alignment and late materialization:
- [[rl-r3-best-implementation]] expands manifests into 24-byte token handles, runs them through the existing fused layout path, and fetches stage-specific payload rows only after final token placement.

Lifecycle and outcome:
- [[rl-r3-best-implementation]] describes speculative-tail overwrite, write backpressure, one owner rank, fail-closed reads, manifest-complete reclamation, and total reported overhead below 7%.

## Counterevidence & Qualifications
The evidence is one first-person production account with no released implementation, benchmark setup, run variance, hardware inventory, correctness audit, or independent reproduction. The missing proof-of-concept code prevents direct verification of its reported eightfold slowdown, and the final result bundles recording, storage, reading, layout, and replay changes. Exact savings depend on payload width, object-store behavior, chunk size, stage partitioning, token count, and how much intermediate logic genuinely ignores payload contents. A handle path is unsafe if layout transformations can separate references from tokens, while aggressive late reads can trade control-path efficiency for storage latency or stalls. Reusing rollout choices also intentionally constrains training behavior; the source argues that this reduces unwanted mismatch but does not quantify its effect on learning quality.

## What Changed
- Created the concept around semantic replay, control-payload separation, handle-based layout, and consumer-side materialization.
- Added lifecycle ownership and fail-closed behavior as correctness conditions rather than cleanup details.
- Preserved that the performance and learning claims are first-party and not independently reproduced.

## Related Concepts
- [[ReinforcementLearning]] - supplies the rollout producer and policy-training consumer connected by replay.
- [[AsynchronousReinforcementLearning]] - addresses policy lag, while state replay addresses execution-level choice mismatch for a recorded trajectory.
- [[DistributedNeuralNetworkTraining]] - supplies the stage, tensor, and context layouts through which token handles must remain aligned.
- [[AttentionMechanism]] - sparse position selection is one discrete state replayed by the source.
- [[MixtureOfExpertsLoadBalancing]] - MoE expert selection is the analogous router state used to motivate and implement replay.
- [[ReceiverDrivenFlowControl]] - shares the principle that downstream capacity should constrain admitted data movement through explicit backpressure.

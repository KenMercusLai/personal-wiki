---
title: "Prefill/Decode Disaggregation"
type: concept
tags: [ai, inference, tts, gpu, distributed-systems]
sources:
  - qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[PrefillDecodeDisaggregation]] assigns prompt prefill and token-by-token decode to separate accelerators, transferring the resulting KV cache and first token between them so each phase can be scheduled independently.

## Current Synthesis
The source's strongest case for disaggregation is not universally lower first-token latency but workload isolation. In streaming TTS, occasional long reference-audio prefills pause every decode stream sharing a monolithic GPU. Separating the phases protects a hard per-stream generation-rate floor and lets the decode GPU sustain overlapping work close to its memory-bandwidth limit.

That benefit is conditional on a cheap, safe transfer boundary. Where cross-host links made a roughly 288 MiB KV handoff take 85-104 ms, the viable design paired prefill and decode within one host and used B300 FABRIC/NVLink or RTX 5090 PCIe P2P through a visibility-broadening sidecar. Production performance depended on gathering fragmented KV rows into a contiguous staging region, avoiding shared-proxy queues, and measuring end-to-end stages under replayed traffic rather than extrapolating from copy or decode microbenchmarks.

Correctness also extends beyond copying bytes. A timed-out write can arrive after decode has recycled the destination pages, silently corrupting a different request. Safe reclamation therefore requires proof that the old writer can no longer modify those pages, plus bounded self-removal or draining when proof cannot be obtained. The resulting topology deliberately trades some idle prefill capacity for a fixed 1P1D operational unit whose routing, scaling, rollout, and failure boundaries are easier to reason about.

## Key Claims
- PD can raise per-GPU usable streaming capacity when intermittent prefill work starves latency-sensitive decode streams.
- Same-host placement can make disaggregation viable without RDMA when PCIe P2P or NVLink keeps KV handoff small relative to decode latency.
- Fragmentation, scheduler admission, host serialization, and proxy queueing can dominate a fast raw transfer path under real traffic.
- Denser P:D ratios improve utilization but transfer routing, cache locality, health, rollout, and scaling complexity into the load balancer and control plane.
- Transfer failure is a memory-ownership problem: destination pages are unsafe to reuse until writer quiescence or writer replacement is proven.
- Workload replay, stage timing, output-equivalence checks, KV validation, canaries, and fault injection are complementary production evidence.

## Evidence
Workload isolation and capacity:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] reports zero stuttering through 40 1P1D streams versus stuttering from eight monolithic streams, and 16 versus eight qualifying streams per GPU under its 42-token/s floor.

Transfer locality and fragmentation:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] measures same-host handoff at 0.54 ms on B300 and 5.6 ms on RTX 5090 versus 85 ms and 104 ms across the available networks, then shows gather-transfer-scatter restoring a fragmented transfer from 48.5 ms to 3.79 ms.

End-to-end scheduling:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] uses a 78,000-request replay and stage waterfall to locate larger delays in admission and decode scheduling; compact prompt representation and overlap scheduling materially reduced those stages.

Topology and operation:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] reports higher 1P2D density but selects fixed 1P1D pods to simplify locality, readiness, autoscaling, draining, and rolling replacement.

Failure safety:
- [[qiong-ren-ban-pd-fen-li-zai-xiao-fei-ji-xian-ka-shang-ba-tts-tui-li-chai-cheng-liang-ban]] reproduces post-quiescence late data, replaces timeout-based page reuse with protocol-level terminal proof, and reports zero mismatch across more than 13,000 fault-injection KV checks.

## Counterevidence & Qualifications
The evidence is a first-party practitioner account of one streaming TTS workload, two GPU platforms, and a custom [[Mooncake]] fork; it is not an independently reproduced comparison across models or serving stacks. PD consumes at least two GPUs per unit and left the chosen prefill GPU about 70% idle at 40 streams. Short prompts, low concurrency, workloads without a hard decode-rate floor, or systems whose bottleneck lies outside prefill interference may be simpler and cheaper as monoliths. The 1P2D result shows that 1P1D is an operational preference rather than a throughput optimum. Several comparisons use different measurement scopes, and the reported online correctness test establishes ASR-CER equivalence within the chosen margin rather than identical audio.

## What Changed
- Established host-local PD as a decode-isolation pattern for streaming workloads without usable cross-host RDMA.
- Added fragmentation-aware KV staging and per-unit transfer proxies as production performance requirements.
- Added proof-based page reclamation as a correctness invariant after transfer failure.
- Distinguished density-optimal 1P2D from operationally simpler 1P1D deployment.

## Related Concepts
- [[InferenceLoadBalancing]] - routes requests among phase-specific workers and absorbs topology complexity when P:D ratios expand.
- [[KVCacheAwareRouting]] - prefix locality affects prefill placement and reuse within a disaggregated fleet.
- [[AdaptiveBackpressure]] - burst headroom and decode in-flight counts bound admission before streams fall below their rate floor.
- [[MicroserviceFailureContainment]] - health gating, draining, and bounded self-restart contain unsafe or overloaded units.
- [[ServiceObservability]] - stage-level timing and end-to-end replay reveal delays hidden by component microbenchmarks.

---
title: "Personal Agent Retrieval"
type: concept
tags: [ai, agents, search, memory, multi-tenancy]
sources:
  - wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi
last_updated: 2026-10-27
knowledge_schema: synthesis-v1
---

## Definition
[[PersonalAgentRetrieval]] is the storage, indexing, authorization, and evidence-selection layer that helps an agent locate relevant historical material across long-lived personal and shared data without treating retrieval alone as a judgment about current truth or task relevance.

## Current Synthesis
The source identifies a workload different from both a small local history and one uniformly hot global index. Each person, agent, workspace, or permission scope can produce a durable dataset that is modest alone, inactive for long periods, and suddenly queried years later. Total retained data can therefore grow much faster than concurrent demand, making per-tenant resident processes and indexes wasteful while making an unscoped shared vector index awkward to filter correctly and efficiently.

Retrieval is only the locator layer. A returned passage retains its source, date, version, and scope; the agent or application must decide whether to read the original, compare later revisions, include it in the active context, or treat it as superseded exploration rather than a stable user belief. Prebuilt indexes, source-system search, and runtime agent exploration are complementary: recent known files may be cheaper to read directly, while years of dispersed history need a directory or index before selective source reading becomes feasible.

The architecture must also preserve authority boundaries. A user, a team workspace, and a shared document set need not map one-to-one to search namespaces, because queries can cross some scopes but not others and access can change over time. Search isolation, product identity, and authorization are related but distinct models.

## Key Claims
- Long-lived sparse tenants separate durable storage growth from concurrent query demand.
- Retrieval locates candidate evidence; it does not determine current truth, user belief, or whether evidence belongs in the active context.
- Direct source reading, source-system search, prebuilt indexes, and model-directed exploration fit different corpus sizes, freshness needs, and latency budgets.
- Namespace boundaries should follow search and management needs without being assumed identical to user IDs or authorization policy.
- Object-storage-backed shared compute can reduce idle per-tenant cost but introduces cold reads, cache competition, index lag, and physical-layout constraints.
- A specialized search service is justified only when its workload advantages exceed synchronization, consistency, fallback, authorization, and operational costs relative to an incumbent database.

## Evidence
Workload shape and tiering:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes many persistent but intermittently queried personal-agent datasets and Turbopuffer's shared query tier over object storage and caches.

Interpretation boundary:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] uses changing author opinions and task-specific writing requests to show that historical similarity does not determine current validity or context inclusion.

Authorization and namespace boundary:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] distinguishes personal history, team-shared files, changing organization membership, customer namespaces, and product user IDs.

Index-versus-source composition:
- [[wei-shen-me-wo-kan-hao-turbopuffer-cong-personal-agent-shuo-qi]] describes Mem0 and Linear keeping complete authoritative records in PostgreSQL while using Turbopuffer to narrow candidates, plus direct and source-system retrieval alternatives.

## Counterevidence & Qualifications
The workload model comes from one practitioner analysis rather than a measured population of personal-agent products. It does not establish the tenant-size distribution, cold-query rate, authorization complexity, recall target, total cost, or scale threshold at which a specialized system wins. Larger context windows and cheaper model inference may move some work from indexes to runtime reading, while source-system search can hide an existing index behind an API. Conversely, years of history still require a way to locate originals before a model can inspect them. Product interaction can prewarm cold data, but this masks rather than eliminates the storage and cache cost.

## What Changed
- Established sparse, durable, bursty tenant history as a distinct personal-agent retrieval workload.
- Separated evidence location from present-tense memory interpretation and context admission.
- Made namespace, identity, authorization, and source-of-truth boundaries explicit and non-identical.

## Related Concepts
- [[AgentMemory]] - consumes retrieved history but adds admission, temporal interpretation, conflict handling, and context-use decisions.
- [[AgenticRAG]] - lets a model decide how to explore and refine retrieval at runtime.
- [[LLMContextManagement]] - decides which located evidence enters the finite active context.
- [[ObjectStorageNativeDatabase]] - explains why remote requests, cache granularity, manifests, and physical layout become architectural constraints.
- [[VectorDatabase]] - supplies similarity retrieval for some histories but not source authority or memory semantics.
- [[HybridSearch]] - combines lexical and semantic candidate signals within the broader retrieval layer.
- [[SearchRelevance]] - evaluates how well candidates satisfy a query, distinct from whether they are safe to interpret as current beliefs.

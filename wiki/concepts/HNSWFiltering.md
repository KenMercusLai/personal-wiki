---
title: "HNSW Filtering"
type: concept
tags: [vector-search, hnsw, filtering, approximate-nearest-neighbor]
sources:
  - revisit-hnsw-shang-de-guo-lu-suan-fa
last_updated: 2026-10-13
knowledge_schema: synthesis-v1
---

## Definition
[[HNSWFiltering]] is the integration of an eligibility predicate into [[HNSWIndex]] search while balancing result completeness, approximate recall, graph navigability, and execution cost.

## Current Synthesis
Filtering changes HNSW from a pure nearest-neighbor problem into a constrained one. Post-filtering preserves ordinary search but may return fewer than `k` eligible results, while pre-filtering identifies the eligible set first and loses the graph's navigation benefit. Their usefulness therefore changes with selectivity: pre-filtering can be fastest for a tiny eligible set, but approaches a full scan when most vectors match.

Integrated graph methods make a different routing choice. Result-gate lets every discovered point enter the candidate set and use the original graph for navigation, but only eligible points enter the ranked result set. ACORN-1 instead calculates distances and routes mainly through eligible points, using two-hop or multi-hop expansion through filtered bridge nodes to reconnect eligible regions. This can reduce distance work but also adds pointer-heavy expansion and weakens routing when eligible points are sparse or geometrically scattered.

The source's measurements make algorithm selection workload-dependent. Result-gate usually has the better recall-QPS curve and is the safer default when workload shape is unknown. ACORN becomes plausible when vectors are high-dimensional, the filter is selective, and filter membership correlates with vector neighborhoods. A quota hybrid can restore full-graph routing when too few eligible neighbors are available, but it does not eliminate the need to benchmark recall, throughput, tail latency, selectivity, and filter-vector correlation together.

## Key Claims
- Post-filtering cannot guarantee `k` eligible results, while oversampling cannot guarantee completeness and increases work.
- Pre-filtering is efficient for very selective predicates but degenerates toward exhaustive distance computation as match rate rises.
- Result-gate preserves original HNSW navigability by separating candidate-set admission from result-set eligibility.
- ACORN trades fewer distance computations for bridge expansion and weaker routing on a filtered subgraph.
- Filter selectivity, vector dimensionality, and correlation between eligibility and vector geometry jointly determine which strategy performs well.
- Recall-QPS and tail behavior matter more than distance-count reduction alone because HNSW can be memory- and expansion-bound.
- No single filtering method dominates every workload; result-gate is the source's default under uncertainty.

## Evidence
- Result completeness: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] illustrates post-filter TopK shrinkage and explains why fixed oversampling cannot guarantee `k` eligible hits.
- Selectivity boundary: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] contrasts a cheap small pre-filter candidate set with a high-match-rate near-full scan.
- Routing mechanics: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] shows result-gate traversing ineligible stepping stones, whereas ACORN repairs filtered graph islands with two-hop Neighbor Expansion.
- Comparative performance: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] reports recall-QPS sweeps across SIFT1M, GIST1M, YFCC1M, and Cohere1M where result-gate usually leads no-budget ACORN.
- Cost mechanism: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] decomposes modeled latency into distance and expansion time, showing that ACORN's distance savings can be outweighed by graph traversal.
- Conditional fit: [[revisit-hnsw-shang-de-guo-lu-suan-fa]] argues and diagrams that ACORN works best when eligible points cluster in vector space, then tests a quota fusion that does not universally dominate.

## Counterevidence & Qualifications
The comparisons are author-run experiments rather than independent reproduction. Dataset dimension, filter construction, selectivity, graph parameters, SIMD and prefetch behavior, cache hierarchy, hardware, implementation details, `ef` sweep, and recall target all affect the result. SIFT and GIST use random filters, while YFCC and Cohere use dataset labels; this is useful variation but not a complete production workload distribution. The latency decomposition is modeled against measured latency rather than a direct hardware-counter attribution, and a bounded exploration budget may still be preferable when predictable tail latency matters more than mean QPS. The quota threshold is empirical and the supplied probability derivation is an approximation, not a universal optimum.

## What Changed
- Established selectivity as the boundary between pre-filter scanning and graph-integrated filtering.
- Distinguished result-gate full-graph routing from ACORN eligible-subgraph routing and bridge expansion.
- Made memory access, expansion cost, and routing quality explicit alongside distance-computation count.
- Added vector dimensionality and filter-vector correlation as algorithm-selection variables.
- Recorded result-gate as a qualified default rather than a universal winner.

## Related Concepts
- [[HNSWIndex]] - supplies the layered graph and candidate/result-set search state that filtering modifies.
- [[ApproximateNearestNeighborSearch]] - filtered HNSW remains an approximate recall-latency optimization problem.
- [[VectorDatabase]] - metadata predicates commonly require constrained vector retrieval.
- [[FilterPushdown]] - both move predicates into execution, but HNSW filtering must also preserve graph navigability.

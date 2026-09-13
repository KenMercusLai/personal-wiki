---
title: "Back of the Envelope Calculation | Better Programmer"
type: source
tags: [system-design, performance, estimation]
date: 2026-04-04
source_file: /mnt/ken_personal_wiki/Articles/Back of the Envelope Calculation - Better Programmer.md
---

## Summary
This Better Programmer article distills [[JeffDean]]'s Stanford advice on using rough latency numbers and design decomposition to estimate system performance before implementation. It argues that order-of-magnitude thinking is more important than the exact 2009 figures: cache, memory, datacenter network, disk, and intercontinental network costs differ enough that a sketch calculation can reject poor designs early. The worked examples compare serial disk reads, parallel disk reads, in-memory thumbnails, and quicksort of 1GB of integers.

## Key Claims
- [[BackOfEnvelopeEstimation]] lets engineers compare system designs before building them by decomposing work into basic operations and multiplying by rough costs.
- [[LatencyHierarchy]] matters because L1/L2 cache, main memory, same-datacenter network, disk seek, sequential disk read, and long-haul network round trips operate at very different time scales.
- Performance estimates should use magnitude and bottleneck reasoning rather than treating old reference tables as exact modern measurements.
- Disk-bound thumbnail generation improves dramatically when independent reads are parallelized, and improves further when small working sets are cached in memory.
- Estimating quicksort on 1GB of four-byte numbers combines algorithmic complexity, branch misprediction, and memory-bandwidth passes into an approximate runtime.
- Network and datacenter round trips are not free; distributed systems must include communication latency even when machines are in the same cluster.

## Key Quotes
> "choose the best solution without building it" - the article's core reason for estimation.

> "the exact numbers here are not as important as the differences in magnitude" - why stale timing tables can still teach design intuition.

## Connections
- [[JeffDean]] - source of the Stanford talk and the "numbers everyone should know" framing used by the article.
- [[BackOfEnvelopeEstimation]] - central method of estimating design time cost from decomposed operations.
- [[LatencyHierarchy]] - reference model behind the article's cache, memory, network, and disk comparisons.
- [[ComputationalThinking]] - the article applies decomposition and algorithmic complexity to practical system-design judgment.
- [[SystemReliability]] - performance-critical systems need capacity and latency reasoning before implementation, not only after incidents.
- [[CloudCostOptimization]] - both concepts use rough unit figures to sanity-check architecture before exact measurement.

## Contradictions
- No direct contradictions found. The article complements [[aws-costs-every-programmer-should-know]]: both use rough numbers for architectural intuition, but this source focuses on latency and throughput rather than cloud spend.

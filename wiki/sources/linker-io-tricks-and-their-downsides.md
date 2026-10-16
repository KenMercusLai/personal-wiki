---
title: "Linker I/O tricks and their downsides"
type: source
tags: [linkers, linux, performance, filesystems, benchmarking, hugepages]
date: 2026-09-20
source_file: "/mnt/ken_personal_wiki/Articles/Linker I:O tricks and their downsides.md"
---

## Summary
[[MaskRay]] benchmarks three default [[MoldLinker|mold]] and [[WildLinker|wild]] optimizations: reusing an output inode, letting a forked parent report completion before the linking child finishes teardown, and requesting transparent huge pages. Each can shorten a favorable edit-relink path, but [[LinkerOptimizationTradeoffs]] shows that the gains depend on cache, memory, and kernel state while violating assumptions made by hard links, mapped executables, build schedulers, debuggers, profilers, and resource accounting. The article therefore argues for end-to-end measurements and conservative defaults rather than treating a lower reported wall time as sufficient evidence.

## Key Claims
- Rewriting an existing output inode can save roughly 40–120 ms per GiB when its pages are resident, but a cold 2 GiB output took 3.89 seconds in place versus 0.38 seconds through a new inode because the old file first had to be read from disk.
- In-place output reuse mutates every hard link, can leave a hard-linked alias holding a partially written failed result, and can change or crash processes that map the inode without triggering Linux's `ETXTBSY` protection.
- The Linux 6.11 removal and 6.13 restoration of executable write denial exposed an undocumented dependency consistent with [[AbstractionLeakage|Hyrum's Law]]; version checks also could not distinguish distribution backports reliably.
- Forking lets the spawned parent exit once the output is published while the child tears down its address space, saving about 60–70 ms for a 1.5 GB 4 KiB-page heap but only about 10 ms when huge pages already make teardown cheap.
- Early parent exit hides CPU time and peak RSS from `wait4`-based tools, can release a make or ninja job slot while cgroup memory is still occupied, changes debugger and tracer behavior, and cannot report errors after notification.
- `MADV_HUGEPAGE` can improve translation locality when contiguous memory is available, but under `defrag=madvise` it can also put synchronous compaction and reclaim into page faults; on the tested fragmented host, the hint added about 550 compaction stalls and made the Chromium link slower and noisier.
- Fair linker evaluation must control output-cache warmth, inode reuse, page size, fragmentation, fork mode, storage medium, workload size, and the boundary at which wall time and resource use are considered complete.

## Key Quotes
> "Each saves a few percent of wall time in an edit-relink loop. Each also breaks an assumption" — the article's framing of local speed gains versus system contracts.

> "If you benchmark, profile, debug, or memory-budget a build with mold or wild, pass `--no-fork`." — practical guidance for restoring normal process-lifecycle observability.

## Connections
- [[MaskRay]] — author and experimenter comparing linker implementations with kernel and filesystem behavior.
- [[MoldLinker]] — high-speed linker using all three examined optimizations by default in the tested configuration.
- [[WildLinker]] — linker with similar in-place update, early-parent-exit, and hugepage behavior.
- [[LinkerOptimizationTradeoffs]] — synthesis of the three mechanisms, benefits, and broken assumptions.
- [[StoragePerformanceBenchmarking]] — cache state, physical I/O, negative controls, and completion boundaries materially change the benchmark result.
- [[AbstractionLeakage]] — observable inode and process-lifecycle behavior becomes a practical compatibility surface.

## Contradictions
- The article challenges minimum-of-repeated-relinks benchmarks: they select the warm-cache condition most favorable to inode reuse and can conceal a roughly tenfold cold-cache cliff in the tested 2 GiB case.
- Faster reported completion is not necessarily less total work. Fork mode changes which process `wait4` observes and may overlap teardown with the next scheduled job.
- Huge pages helped the separate NVMe-to-RDMA buffer-scan case already in the wiki, but an explicit hugepage hint did not help these tested linker workloads and triggered costly compaction on a fragmented machine.
- Results come from one Linux 6.18 system, one ext4 SATA setup, selected synthetic and Chromium workloads, mold's in-development Rust port, and one wild commit. The article supplies no data for `enabled=madvise`, network storage, other kernels, other filesystems, or broad production populations.

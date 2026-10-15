---
title: "wild"
type: entity
tags: [linker, linux, performance, open-source]
sources:
  - linker-io-tricks-and-their-downsides
last_updated: 2026-10-15
knowledge_schema: synthesis-v1
---

## Overview
[[WildLinker|wild]] is a linker whose tested Linux behavior includes in-place output updates, fork-based asynchronous teardown, and a hugepage hint on its output mapping.

## Current Profile
The source places wild beside mold as an aggressive visible-latency design. Its in-place update became a Linux default after an earlier benchmark found about a 4% rustc improvement and little measurable clang change; it offers `--no-update-in-place`, avoids reuse for shared objects and on macOS, and falls back on `ETXTBSY`. It also uses the early-parent-exit pipe protocol and, since the cited September 2026 change, hints its output mapping for huge pages. The same filesystem, accounting, scheduling, and fragmentation qualifications therefore apply, though the article does not claim identical internal implementations everywhere.

## Key Characteristics
- Updates existing Linux output files in place by default in the examined revision, with an explicit opt-out.
- Avoids in-place updates for shared objects and macOS outputs but does not check hard-link count in the examined code.
- Uses fork and pipe notification to hide post-publication address-space teardown.
- Requests huge pages for its output mapping in the cited 2026 revision.
- Shows workload-dependent gains rather than a uniform performance advantage.

## Evidence
- Output policy: [[linker-io-tricks-and-their-downsides]] traces the feature's benchmark history, default change, opt-out, platform guards, and warm-versus-cold 2 GiB results.
- Process policy: [[linker-io-tricks-and-their-downsides]] identifies the same pipe protocol and `--no-fork` control as mold and reports a 4 MB measured RSS versus 1.65 GB actual use in one run.
- Memory policy: [[linker-io-tricks-and-their-downsides]] records the output-mapping hugepage hint and explains why its outcome depends on kernel policy and fragmentation.

## Qualifications
The profile is bounded to one author-run study and wild commit `47cc8e8e`; implementation and defaults can change. Some measurements are shared mechanism tests or comparisons rather than full wild-specific replications. The reported 4% rustc gain comes from the project's commit message, while the article's own cold-output result strongly reverses the benefit; neither establishes typical performance across real build populations.

## What Changed
- Established wild's examined output, process, and hugepage policies.
- Added the explicit opt-outs and platform or output-type exceptions.
- Qualified the speed claims by cache and observability state.

## Relationships
- [[MaskRay]] - authored the study used for this profile.
- [[MoldLinker]] - closest compared linker using analogous latency techniques.
- [[LinkerOptimizationTradeoffs]] - captures the shared semantic and measurement costs.
- [[StoragePerformanceBenchmarking]] - explains why cache and physical-I/O state reverse measured outcomes.

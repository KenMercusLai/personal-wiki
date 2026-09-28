---
title: "Andrew Baumann"
type: entity
tags: [person, systems-research, processor-architecture, microsoft-research]
sources:
  - hardware-is-the-new-software-the-morning-paper
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[AndrewBaumann]] is the Microsoft Research systems researcher whose HotOS 2017 paper “Hardware is the new software” is summarized in the source.

## Current Profile
In this wiki's evidence, Baumann examines the growth of Intel x86 extensions and argues that their software-like specification and interaction complexity is difficult to reconcile with hardware deployment cycles and indefinite backward compatibility. He uses SGX and CET as security-focused examples, then proposes treating the ISA as a translation layer whose features might sometimes be decoupled from new physical processors through microcode.

## Key Characteristics
- Systems researcher focused here on processor architecture and operating-system consequences.
- Evaluates ISA growth through interaction complexity rather than instruction count alone.
- Connects processor features to the obligations of operating systems, virtual machines, compilers, and analysis tools.
- Treats the established hardware–software boundary as a design choice open to revision.
- Offers microcode-based decoupling as a speculative direction rather than a completed design.

## Evidence
- Authorship and affiliation: [[hardware-is-the-new-software-the-morning-paper]] identifies Baumann's HotOS 2017 paper and notes that its author was at Microsoft Research.
- Architectural diagnosis: [[hardware-is-the-new-software-the-morning-paper]] attributes to Baumann the claim that security-oriented x86 extensions introduce software-scale specifications and complex interactions.
- Alternative direction: [[hardware-is-the-new-software-the-morning-paper]] presents his proposal to reconsider the ISA as a translation layer and explore microcoded feature availability on existing processors.

## Qualifications
The profile is intentionally limited to one 2017 position paper as represented by a secondary article. It does not cover Baumann's broader research record, later views, or whether the proposed direction was adopted. Claims about Intel's incentives and the feasibility of microcode-based deployment remain arguments in the paper rather than independently demonstrated facts about corporate decisions or processor implementations.

## What Changed
- Established Baumann's profile around ISA complexity, compatibility, and the programmable hardware–software boundary.
- Recorded microcode-based feature decoupling as a speculative research direction with unresolved constraints.

## Relationships
- [[ISAExtensionComplexity]] - principal systems problem developed in Baumann's paper.
- [[HardwareSoftwareBoundary]] - architectural boundary his paper argues should be reconsidered.
- [[Intel]] - processor vendor whose x86 extensions supply the paper's cases.
- [[Microsoft]] - corporate context for the Microsoft Research affiliation stated by the source.

---
title: "Chris Lattner"
type: entity
tags: [compiler-engineer, llvm, clang, mlir]
sources:
  - llvm-compiler
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[ChrisLattner]] is a compiler engineer, [[LLVM]] co-creator, and co-author of the retrospective source; the article identifies him as CEO of Modular Inc.

## Current Profile
Lattner joined the UIUC Ph.D. program in 2000 and began LLVM's detailed design and implementation after discussions with [[VikramAdve]] about a compiler infrastructure for both static and dynamic compilation. He later joined Apple, continued open-source LLVM work, developed Clang with company support, and helped lead LLVM adoption and derivative systems including Swift and MLIR. The source treats his technical and community leadership as a major factor in LLVM's commercial spread.

## Key Characteristics
- Co-designed LLVM's founding goals with Vikram Adve.
- Produced the initial implementation skeleton with modular libraries, equivalent IR forms, transformation tools, and a flexible pass pipeline.
- Continued open-source LLVM development while at Apple.
- Developed Clang as an open-source C-family front end built around LLVM.
- Led or helped establish derivative systems including Swift and MLIR.

## Evidence
Founding implementation:
- [[llvm-compiler]] attributes the winter 2000–2001 implementation skeleton and its enduring architectural features to Lattner.

Adoption leadership:
- [[llvm-compiler]] connects his Apple work to the OpenGL JIT, Clang, replacement of GCC across Apple platforms, and later coordination with other companies.

Derivative projects:
- [[llvm-compiler]] identifies Clang, Swift, and MLIR as successful LLVM-related systems led by Lattner.

## Qualifications
The profile comes from a retrospective Lattner co-authored and therefore reflects a participant's account of technical decisions, leadership, and causal impact. The source does not independently compare individual contributions across the broader LLVM community, and its present-tense employer information is dated to publication.

## What Changed
- Established Lattner's role in LLVM's design and initial implementation.
- Added his Apple-era adoption work and leadership of derivative systems.
- Qualified the profile as a co-authored participant history.

## Relationships
- [[VikramAdve]] - research collaborator and LLVM co-creator.
- [[LLVM]] - project Lattner co-designed, implemented, and helped scale.
- [[LLVMIntermediateRepresentation]] - foundational representation embodied in his initial implementation.
- [[ModularCompilerArchitecture]] - architectural style implemented in the earliest LLVM code.

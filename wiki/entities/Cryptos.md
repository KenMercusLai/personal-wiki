---
title: "cryptos"
type: entity
tags: [software, bitcoin, education]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Cryptos]] is [[AndrejKarpathy]]'s reference library for the Bitcoin code explored in the from-scratch tutorial.

## Current Profile
The article positions Cryptos as the cleaner, separated, tested, and more extensive version of the educational code shown inline. It is not the tutorial's main artifact; rather, it is the follow-up project readers can inspect after seeing the complete path from cryptographic identity to broadcast testnet transactions.

## Key Characteristics
- Provides a more organized implementation of the Bitcoin mechanics demonstrated in the article.
- Complements the notebook-style walkthrough rather than replacing its educational step-by-step structure.
- Includes networking code, such as a SimpleNode implementation, for communicating with Bitcoin nodes over sockets.
- Serves as a reference point for readers who want to continue their blockchain learning beyond the article.

## Evidence
- Cleaner implementation: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] describes [[Cryptos]] as separated, tested, and more extensive than the inline tutorial code.
- Network reference: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] points to SimpleNode in [[Cryptos]] as the path for raw Bitcoin protocol broadcasting.
- Learning continuation: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] sends readers to [[Cryptos]] alongside Mastering Bitcoin and Programming Bitcoin for deeper study.

## Qualifications
The wiki has not inspected the repository itself; this page reflects only how the article describes it.

## What Changed
- Created Cryptos as Karpathy's follow-up Bitcoin learning codebase.

## Relationships
- [[AndrejKarpathy]] - author and maintainer associated with the library in the source.
- [[Bitcoin]] - protocol implemented and explored by the library.
- [[FromScratchProtocolLearning]] - project artifact that extends the article's reconstruction approach.

---
title: "Andrej Karpathy"
type: entity
tags: [software, ai, education, cryptocurrency]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[AndrejKarpathy]] appears in this source as a technical educator using a from-scratch implementation to make [[Bitcoin]]'s transaction and cryptographic machinery understandable.

## Current Profile
The article presents Karpathy as both learner and explainer: he starts from curiosity about blockchain as open software with shared state, then rebuilds the Bitcoin path from key generation to a testnet transaction in pure [[Python]]. His stance is explicitly educational rather than production-oriented. He repeatedly warns that the cryptographic code is for understanding, while pointing readers toward [[Cryptos]], Mastering Bitcoin, and Programming Bitcoin for cleaner follow-up study.

## Key Characteristics
- Uses implementation as a learning method for understanding complex systems.
- Frames blockchain as a computing paradigm that extends open source code into open, shared state.
- Explains Bitcoin through concrete protocol artifacts: keys, addresses, hashes, scripts, serialized transactions, and testnet broadcasts.
- Keeps the tutorial candid about omitted production details and unsafe educational shortcuts.
- Connects the article to a cleaner reference implementation in [[Cryptos]].

## Evidence
- Implementation-first learning: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] builds key generation, hashing, address derivation, transaction serialization, signing, and broadcasting in one walkthrough.
- Blockchain framing: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] presents Bitcoin as a seed example of open software plus shared running state.
- Safety boundaries: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] warns against using the educational cryptography in production and notes skipped standards such as RFC 6979.
- Reference-project link: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] points to [[Cryptos]] as a cleaner, separated, tested implementation.

## Qualifications
This profile is limited to one Bitcoin tutorial. It does not summarize Karpathy's broader AI research, teaching, or industry work.

## What Changed
- Created Karpathy as an implementation-first technical educator in the wiki's Bitcoin and protocol-learning material.

## Relationships
- [[Bitcoin]] - Karpathy reconstructs Bitcoin's identity, transaction, and proof-of-work mechanisms.
- [[Python]] - tutorial implementation language.
- [[Cryptos]] - related reference codebase maintained by Karpathy.
- [[FromScratchProtocolLearning]] - learning mode exemplified by the article.

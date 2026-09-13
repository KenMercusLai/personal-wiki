---
title: "Bitcoin Proof of Work"
type: concept
tags: [bitcoin, cryptocurrency, consensus]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[BitcoinProofOfWork]] is Bitcoin's miner-selection mechanism in which participants search for block data whose SHA-256-derived hash satisfies the network difficulty target.

## Current Synthesis
The article treats proof of work as the economic and computational layer around the transaction machinery. SHA-256's hash properties make the search for a low block hash brute-force, so mining advantage is proportional to hashing power. Miners are incentivized by block rewards and fees, and Bitcoin adjusts difficulty so mainnet blocks arrive at roughly ten-minute intervals.

## Key Claims
- Proof of work depends on SHA-256 behaving like a non-invertible, random-looking digest function.
- Miners search by modifying block data until the interpreted hash is sufficiently low.
- ASIC mining is specialized acceleration of the same hashing operation shown educationally in Python.
- Fees incentivize miners to include transactions when block space is limited.
- Block production probability is proportional to a miner's share of network hashing power.
- Difficulty adjustment targets roughly ten-minute block intervals on Bitcoin mainnet.

## Evidence
- Hash-search framing: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] explains proof of work as modifying a transaction block until its hash is low enough.
- Miner incentives: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] describes fees and coinbase rewards in testnet block examples.
- Hashpower proportionality: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] summarizes decentralization economics as probability proportional to total SHA-256 hashing power share.
- Timing target: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] notes mainnet's roughly ten-minute block cadence.

## Counterevidence & Qualifications
The source does not implement mining or full block validation. It also mentions historical quirks in difficulty adjustment without giving a complete consensus-rule treatment.

## What Changed
- Added Bitcoin proof of work as the incentive and miner-selection layer around transaction inclusion.

## Related Concepts
- [[BitcoinTransactionModel]] - proof of work packages valid transactions into blocks.
- [[UTXOModel]] - miners include transactions that consume and create UTXOs.
- [[CryptocurrencyMerchantAdoption]] - payment usability depends partly on confirmation latency and fee markets.
- [[DistributedConsensus]] - proof of work is a Bitcoin-specific mechanism for coordinating block history.

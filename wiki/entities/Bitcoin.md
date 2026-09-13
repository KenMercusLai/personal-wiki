---
title: "Bitcoin"
type: entity
tags: [cryptocurrency, payments]
sources:
  - amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Bitcoin]] is presented both as an incumbent cryptocurrency vulnerable to merchant-adoption choices and as a concrete protocol where value is represented by UTXOs, ownership by cryptographic signatures, and block inclusion by proof-of-work incentives.

## Current Profile
The market-adoption source treats Bitcoin as a popular speculative asset and aspirational currency whose practical payment ambitions could be constrained by volatility, recovery risk, throughput, and large-platform choices by [[Amazon]]. Karpathy's tutorial adds the protocol layer underneath that payment story: Bitcoin funds are not account balances but spendable [[UTXOModel]] outputs with amounts and locking scripts. Users control funds through [[CryptographicIdentity]], construct spends through [[BitcoinTransactionModel]], satisfy P2PKH locking conditions through [[BitcoinScript]], and rely on [[BitcoinProofOfWork]] miners to package valid transactions into blocks.

## Key Characteristics
- Held the incumbent "number one cryptocurrency" position in the source's framing.
- Drew speculative investment attention despite severe volatility and recovery risks.
- Was presented as too slow for Amazon-scale checkout demand at roughly seven transactions per second.
- Needed widespread merchant adoption to function as currency rather than only as an investment vehicle.
- Represents spendable value as fully consumed and newly created UTXOs rather than mutable account rows.
- Secures ordinary P2PKH spends through public-key hashes, unlocking scripts, and ECDSA-style signatures.
- Uses proof of work, block rewards, and transaction fees to coordinate transaction inclusion.

## Evidence
- Investment hype and risk: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] describes teenagers, families, and billionaires putting money into Bitcoin while warning about volatility and hacks.
- Throughput constraint: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] contrasts Bitcoin's transaction speed with Amazon's peak retail transaction volume.
- Merchant-adoption dependence: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] argues Bitcoin must move from investment asset to merchant-accepted currency to sustain currency ambitions.
- Platform-threat scenario: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] says Amazon adopting a rival or creating its own coin could weaken Bitcoin's top position.
- Value representation: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] describes Bitcoin as a DAG of UTXOs with amounts and locking scripts.
- Spend authorization: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] constructs P2PKH transactions where public keys and signatures satisfy locking scripts.
- Mining incentives: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] explains fees, coinbase rewards, proof-of-work hashing, and roughly ten-minute mainnet block timing.

## Qualifications
This page still does not attempt a complete monetary, regulatory, market, or consensus history of Bitcoin. The Amazon scenarios are speculative, and the Karpathy tutorial intentionally focuses on legacy P2PKH-style testnet transactions while omitting modern features such as Segwit, bech32, Taproot, mining implementation, and full validation.

## What Changed
- Expanded Bitcoin from a market-adoption incumbent into a technical protocol profile centered on UTXOs, scripts, signatures, serialization, fees, and proof of work.

## Relationships
- [[Amazon]] - retailer whose cryptocurrency choice is framed as a possible threat to Bitcoin's leadership.
- [[Ethereum]] - competing cryptocurrency compared on transaction throughput.
- [[CryptocurrencyMerchantAdoption]] - Bitcoin's currency ambitions depend on merchant acceptance and usable payment experience.
- [[CorporateGiantFragility]] - large-platform choices can reshape market narratives around incumbent technologies.
- [[UTXOModel]] - Bitcoin's value representation in the technical tutorial.
- [[BitcoinTransactionModel]] - Bitcoin spend construction and serialization model.
- [[BitcoinScript]] - authorization layer for common P2PKH outputs.
- [[BitcoinProofOfWork]] - mining and transaction-inclusion mechanism.

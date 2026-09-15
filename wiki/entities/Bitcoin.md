---
title: "Bitcoin"
type: entity
tags: [cryptocurrency, payments]
sources:
  - amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
  - balaji-srinivasan-silicon-valleys-ultimate-exit-genius
  - coinbase-wants-to-be-too-big-to-fail-fortune
last_updated: 2026-09-15
knowledge_schema: synthesis-v1
---

## Overview
[[Bitcoin]] is presented as an incumbent cryptocurrency vulnerable to merchant-adoption choices, as a concrete protocol where value is represented by UTXOs and proof-of-work-secured transactions, as a technology that could reduce state control over capital movement, and as the asset that created Coinbase's mainstream on-ramp opportunity.

## Current Profile
The market-adoption source treats Bitcoin as a popular speculative asset and aspirational currency whose practical payment ambitions could be constrained by volatility, recovery risk, throughput, and large-platform choices by [[Amazon]]. Karpathy's tutorial adds the protocol layer underneath that payment story: Bitcoin funds are not account balances but spendable [[UTXOModel]] outputs with amounts and locking scripts. Users control funds through [[CryptographicIdentity]], construct spends through [[BitcoinTransactionModel]], satisfy P2PKH locking conditions through [[BitcoinScript]], and rely on [[BitcoinProofOfWork]] miners to package valid transactions into blocks. Srinivasan's talk adds a political-technology frame: Bitcoin is an exit tool because it can make capital controls, bail-ins, and money seizure more like packet filtering than centralized financial command. Fortune adds the institutionalization layer: Bitcoin's difficulty for ordinary buyers created room for [[Coinbase]], while the 2017 boom and subsequent bust showed how Bitcoin speculation could build and then stress a regulated intermediary.

## Key Characteristics
- Held the incumbent "number one cryptocurrency" position in the source's framing.
- Drew speculative investment attention despite severe volatility and recovery risks.
- Was presented as too slow for Amazon-scale checkout demand at roughly seven transactions per second.
- Needed widespread merchant adoption to function as currency rather than only as an investment vehicle, and functions in Srinivasan's thesis as exit infrastructure for moving capital outside conventional controls.
- Represents spendable value as fully consumed and newly created UTXOs, with ordinary P2PKH spends authorized through public-key hashes, unlocking scripts, and ECDSA-style signatures.
- Uses proof of work, block rewards, and transaction fees to coordinate transaction inclusion.
- Created mainstream exchange demand because early Bitcoin buying and custody were difficult, then exposed intermediaries to boom-bust risk after 2017.

## Evidence
- Investment hype and risk: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] describes teenagers, families, and billionaires putting money into Bitcoin while warning about volatility and hacks.
- Throughput constraint: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] contrasts Bitcoin's transaction speed with Amazon's peak retail transaction volume.
- Merchant-adoption dependence: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] argues Bitcoin must move from investment asset to merchant-accepted currency to sustain currency ambitions.
- Platform-threat scenario: [[amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto]] says Amazon adopting a rival or creating its own coin could weaken Bitcoin's top position.
- Value representation: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] describes Bitcoin as a DAG of UTXOs with amounts and locking scripts.
- Spend authorization: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] constructs P2PKH transactions where public keys and signatures satisfy locking scripts.
- Mining incentives: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] explains fees, coinbase rewards, proof-of-work hashing, and roughly ten-minute mainnet block timing.
- Capital-control resistance: [[balaji-srinivasan-silicon-valleys-ultimate-exit-genius]] says Bitcoin can make capital controls resemble packet filtering and make bail-ins harder if many people use it.
- Paper Belt disruption: [[balaji-srinivasan-silicon-valleys-ultimate-exit-genius]] lists Bitcoin among technologies threatening Washington, D.C.'s regulatory power.
- Coinbase on-ramp demand: [[coinbase-wants-to-be-too-big-to-fail-fortune]] says early Bitcoin buying required wallet software, offshore transfers, or shadowy middlemen, motivating a simpler Coinbase purchase and custody flow.
- Boom-bust exposure: [[coinbase-wants-to-be-too-big-to-fail-fortune]] reports Bitcoin's 2017 surge, its later fall to about $6,410 by September 13, 2018, and the resulting threat to Coinbase trading revenue.

## Qualifications
This page still does not attempt a complete monetary, regulatory, market, or consensus history of Bitcoin. The Amazon scenarios are speculative, the Karpathy tutorial intentionally focuses on legacy P2PKH-style testnet transactions while omitting modern features such as Segwit, bech32, Taproot, mining implementation, and full validation, Srinivasan's capital-control claim is a political forecast rather than proof that governments cannot regulate cryptocurrency, and the Fortune article reflects a 2018 market cycle rather than current Bitcoin adoption or Coinbase performance.

## What Changed
- Added Srinivasan's frame of Bitcoin as exit infrastructure against capital controls and bail-ins.
- Added Bitcoin's role as the asset that created Coinbase's mainstream on-ramp opportunity and boom-bust revenue exposure.

## Relationships
- [[Amazon]] - retailer whose cryptocurrency choice is framed as a possible threat to Bitcoin's leadership.
- [[Ethereum]] - competing cryptocurrency compared on transaction throughput.
- [[CryptocurrencyMerchantAdoption]] - Bitcoin's currency ambitions depend on merchant acceptance and usable payment experience.
- [[CorporateGiantFragility]] - large-platform choices can reshape market narratives around incumbent technologies.
- [[UTXOModel]] - Bitcoin's value representation in the technical tutorial.
- [[BitcoinTransactionModel]] - Bitcoin spend construction and serialization model.
- [[BitcoinScript]] - authorization layer for common P2PKH outputs.
- [[BitcoinProofOfWork]] - mining and transaction-inclusion mechanism.
- [[ExitAsGovernance]] - Bitcoin is one monetary example in Srinivasan's exit-technology stack.
- [[PaperBelt]] - Bitcoin is framed as part of Silicon Valley's challenge to D.C.-centered regulatory power.
- [[Coinbase]] - regulated intermediary that made Bitcoin easier to buy and custody for ordinary users.
- [[BrianArmstrong]] - founder whose Bitcoin thesis led to Coinbase.

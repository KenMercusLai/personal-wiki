---
title: "Bitcoin"
type: entity
tags: [cryptocurrency, payments]
sources:
  - amazon-is-the-biggest-threat-to-bitcoin-right-now-by-coin-and-crypto
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
  - balaji-srinivasan-silicon-valleys-ultimate-exit-genius
  - coinbase-wants-to-be-too-big-to-fail-fortune
  - cnbc-erik-finman-bitcoin-millionaire-who-skipped-college
  - inside-the-wild-west-world-of-gift-card-bitcoin-brokering
last_updated: 2026-09-30
knowledge_schema: synthesis-v1
---

## Overview
[[Bitcoin]] is presented as an incumbent cryptocurrency shaped by merchant and access choices, a concrete UTXO and proof-of-work protocol, a potential exit from centralized control, the asset behind Coinbase's regulated on-ramp, a volatile concentrated investment, and inventory in an informal gift-card brokerage market.

## Current Profile
The market-adoption source treats Bitcoin as a popular speculative asset and aspirational currency whose practical payment ambitions could be constrained by volatility, recovery risk, throughput, and large-platform choices by [[Amazon]]. Karpathy's tutorial adds the protocol layer underneath that payment story: Bitcoin funds are spendable [[UTXOModel]] outputs with amounts and locking scripts, controlled through [[CryptographicIdentity]], spent through [[BitcoinTransactionModel]] and [[BitcoinScript]], and included by [[BitcoinProofOfWork]] miners. Srinivasan frames Bitcoin as exit infrastructure against capital controls and bail-ins. Fortune adds institutionalization: difficult early access created room for [[Coinbase]], while the 2017 boom and bust exposed intermediary fragility. Finman's profile supplies an exceptional early-holder case in which gains financed [[Botangle]] and a technology sale returned 300 bitcoin.

The gift-card brokerage case adds an informal access and circulation layer. On [[Paxful]], buyers who apparently had few convenient acquisition options paid a bitcoin premium with gift-card codes. A broker redeemed those balances for gaming cards, resold them, and used the proceeds to replenish bitcoin. Bitcoin was therefore both the inventory being sold and the asset closing the conversion loop. Platform reputation and delayed release managed counterparty risk, while retailer policy determined whether the payment instrument could be converted; neither mechanism established that card value was lawfully acquired.

## Key Characteristics
- Held the incumbent "number one cryptocurrency" position in the source's framing while drawing speculative attention and exceptional early-holder gains despite severe volatility, concentration, and recovery risks.
- Was presented as too slow for Amazon-scale checkout demand at roughly seven transactions per second.
- Needed widespread merchant adoption to function as currency rather than only as an investment vehicle, and functions in Srinivasan's thesis as exit infrastructure for moving capital outside conventional controls.
- Represents spendable value as fully consumed and newly created UTXOs, with ordinary P2PKH spends authorized through public-key hashes, unlocking scripts, and ECDSA-style signatures.
- Uses proof of work, block rewards, and transaction fees to coordinate transaction inclusion.
- Created mainstream exchange demand because early Bitcoin buying and custody were difficult, then exposed intermediaries to boom-bust risk after 2017.
- Supported peer-to-peer access through nonstandard payment instruments, with brokers earning residual spreads while bearing fraud and conversion risk.

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
- Entrepreneurial financing: [[cnbc-erik-finman-bitcoin-millionaire-who-skipped-college]] reports that Finman converted an early Bitcoin position into roughly $100,000 for Botangle, then accepted 300 bitcoin when selling its technology.
- Concentrated-holder outcome: [[cnbc-erik-finman-bitcoin-millionaire-who-skipped-college]] valued Finman's 403 bitcoin at about $1.09 million in June 2017.
- Peer-to-peer thesis: [[cnbc-erik-finman-bitcoin-millionaire-who-skipped-college]] presents Bitcoin and blockchain as infrastructure for removing service intermediaries, but supplies no operating deployment evidence.
- Informal access: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] documents a broker selling bitcoin internationally for gift-card codes through Paxful.
- Spread economics: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] reports that a 28 percent sale premium and 25 percent repurchase premium left the broker a 3 percent margin on one trade.
- Conversion dependence: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] shows bitcoin inventory being replenished through retailer gift-card conversion and downstream resale.
- Provenance risk: [[inside-the-wild-west-world-of-gift-card-bitcoin-brokering]] distinguishes broker protections from evidence that a gift card was lawfully acquired.

## Qualifications
This page does not attempt a complete monetary, regulatory, market, or consensus history of Bitcoin. The Amazon scenarios are speculative; the Karpathy tutorial focuses on legacy P2PKH-style testnet transactions and omits modern features and full validation; Srinivasan's claim is a political forecast, not proof that governments cannot regulate cryptocurrency; and the Coinbase and Finman accounts are historical boom-era cases rather than current adoption, performance, or general investment evidence. The gift-card source profiles one anonymous broker and one observed trade; it does not establish representative premiums, lawful provenance, market size, current Paxful practice, or current retailer controls.

## What Changed
- Added Srinivasan's frame of Bitcoin as exit infrastructure against capital controls and bail-ins.
- Added Bitcoin's role as the asset that created Coinbase's mainstream on-ramp opportunity and boom-bust revenue exposure.
- Added an individual case in which early Bitcoin gains financed a startup and a later Bitcoin-denominated sale amplified concentrated exposure.
- Added gift-card-settled peer-to-peer brokerage as an informal access route with narrow spreads, retailer dependence, and provenance risk.

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
- [[ErikFinman]] - early holder whose reported gains financed Botangle and crossed a nominal million-dollar threshold in 2017.
- [[Botangle]] - education startup financed and sold through Bitcoin-linked transactions.
- [[Paxful]] - marketplace coordinating the documented bitcoin-for-gift-card trade.
- [[PeerToPeerCryptoTrading]] - informal access model in which bitcoin is sold and replenished through negotiated spreads.
- [[GiftCardFraud]] - provenance risk attached to the payment instrument used in the brokerage loop.

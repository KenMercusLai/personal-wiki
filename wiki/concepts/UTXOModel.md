---
title: "UTXO Model"
type: concept
tags: [bitcoin, cryptocurrency, accounting]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[UTXOModel]] is a cryptocurrency value model in which spendable money exists as unspent transaction outputs that must be consumed in full and replaced by new outputs.

## Current Synthesis
Karpathy's Bitcoin walkthrough makes the UTXO model concrete by spending a faucet output, splitting it into a payment output, a change output, and an implied miner fee. A wallet balance is therefore not a mutable account row; it is the sum of outputs the owner can unlock. Spending value means referencing previous outputs as inputs, proving authority, and creating new outputs with new locking conditions.

## Key Claims
- Bitcoin value is represented by transaction outputs rather than mutable account balances.
- A UTXO is spent in full; partial payment is modeled by creating separate payment and change outputs.
- Inputs reference earlier transaction IDs and output indexes to identify the exact output being consumed.
- Transaction fees are implied by the difference between total input value and total output value.
- The model forms a directed acyclic graph of consumed and newly created outputs.

## Evidence
- Full-spend rule: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] emphasizes that every Bitcoin input/output must be fully spent.
- Payment plus change: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] sends 50,000 sat to a second wallet and 47,500 sat back as change from a 100,000 sat input.
- Fee accounting: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] treats the 2,500 sat remainder as the miner fee.
- DAG framing: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] summarizes Bitcoin as a DAG of UTXOs with amounts and locking scripts.

## Counterevidence & Qualifications
The source explains a simple P2PKH testnet flow. It does not cover account-based cryptocurrency designs, coin selection algorithms, privacy implications, or newer Bitcoin transaction forms.

## What Changed
- Added the UTXO model as the wiki's technical value-representation concept for Bitcoin.

## Related Concepts
- [[BitcoinTransactionModel]] - transactions consume and create UTXOs.
- [[BitcoinScript]] - each UTXO carries a locking script that controls who can spend it.
- [[BitcoinProofOfWork]] - miners package valid UTXO spends into blocks and claim fees.
- [[DoubleEntryAccounting]] - related accounting contrast where value movement is also modeled structurally rather than as casual balance mutation.

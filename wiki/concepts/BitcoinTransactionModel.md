---
title: "Bitcoin Transaction Model"
type: concept
tags: [bitcoin, cryptocurrency, protocol]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[BitcoinTransactionModel]] is the protocol structure by which Bitcoin spends previous outputs, creates new outputs, serializes the intent into bytes, and proves spend authority with signatures.

## Current Synthesis
The tutorial models a Bitcoin transaction as version metadata, inputs, outputs, locktime, and serialization rules. Inputs point at previous transaction outputs by transaction ID and output index; outputs specify amounts and locking scripts. For signing, the transaction is serialized with a special script substitution for the input being signed, then hashed and signed. Once the unlocking script is attached, the final byte sequence has a transaction ID derived from double-SHA-256 hashing.

## Key Claims
- Transaction inputs identify previous outputs; they do not specify partial spend amounts.
- Transaction outputs create new UTXOs with satoshi amounts and locking scripts.
- Serialization details, byte order, varints, and script encoding are core protocol behavior, not cosmetic packaging.
- Signing uses a transaction-derived message that substitutes the referenced output's locking script for the input being signed.
- Final transaction IDs are computed from the fully serialized transaction via double SHA-256 with Bitcoin byte-order conventions.
- Broadcast can happen through a helper endpoint or through raw Bitcoin peer protocol messages.

## Evidence
- Input and output structures: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] defines TxIn, TxOut, and Tx data classes to craft testnet transactions.
- Serialization mechanics: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] implements integer encoding, varints, scripts, and transaction byte encoding.
- Signature message: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] signs a version of the transaction where the selected input receives the previous output's scriptPubKey.
- Transaction ID and broadcast: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] computes transaction IDs and broadcasts raw hex through a testnet push endpoint.

## Counterevidence & Qualifications
The source intentionally keeps to simple legacy P2PKH transactions and does not cover full node validation, mempool policy, Segwit digest rules, P2SH, bech32, replace-by-fee, or modern wallet behavior.

## What Changed
- Added Bitcoin transaction construction as a protocol-level model connecting UTXOs, scripts, signatures, serialization, and broadcast.

## Related Concepts
- [[UTXOModel]] - transaction inputs consume prior outputs and create new outputs.
- [[BitcoinScript]] - locking and unlocking scripts authorize the transaction's spends.
- [[CryptographicIdentity]] - private keys create signatures proving spend authority.
- [[BitcoinAddressEncoding]] - output ownership is commonly declared through public-key hashes derived from addresses.
- [[BitcoinProofOfWork]] - valid transactions are eventually packaged into mined blocks.

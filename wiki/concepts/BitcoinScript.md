---
title: "Bitcoin Script"
type: concept
tags: [bitcoin, cryptocurrency, scripting]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[BitcoinScript]] is Bitcoin's stack-based scripting mechanism for locking transaction outputs and later proving that an input is allowed to spend them.

## Current Synthesis
Karpathy focuses on the common P2PKH pattern: a locking script duplicates and hashes the provided public key, compares it with the stored public-key hash, and checks that the transaction signature matches the public key. The unlocking script supplies the encoded signature and public key. During validation, the two scripts are effectively evaluated together, making ownership a programmable condition attached to UTXOs.

## Key Claims
- Bitcoin outputs are locked by scripts rather than by account database permissions.
- P2PKH scripts encode a public-key-hash check and a signature check.
- Unlocking scripts commonly provide the signature and public key required by the locking script.
- The public key is revealed when a matching output is spent, while the output can initially store only its hash.
- Script is powerful but much of that power is unused in ordinary point-to-point transactions.

## Evidence
- P2PKH locking form: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] shows OP_DUP, OP_HASH160, a public-key hash, OP_EQUALVERIFY, and OP_CHECKSIG.
- Unlocking script: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] constructs scriptSig from a DER-encoded signature plus public-key bytes.
- Validation flow: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] explains the concatenated script stack behavior that checks hash equality and signature validity.
- Scope caveat: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] notes that Bitcoin has many opcodes but simple transactions use a few common script templates.

## Counterevidence & Qualifications
The source does not deeply explore multisig, P2SH, Segwit, Taproot, covenant-like designs, full script validation, or consensus edge cases. It also notes historical quirks and bugs in old opcode behavior without cataloging them.

## What Changed
- Added Bitcoin Script as the programmable authorization layer attached to UTXOs.

## Related Concepts
- [[UTXOModel]] - each output carries a locking script.
- [[BitcoinTransactionModel]] - each input supplies an unlocking script to satisfy the referenced output.
- [[CryptographicIdentity]] - signatures and public keys are the usual P2PKH proof material.
- [[SmartContracts]] - broader category of code-mediated contractual mechanisms, though Bitcoin Script is narrower in this source.

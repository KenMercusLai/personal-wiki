---
title: "A from-scratch tour of Bitcoin in Python"
type: source
tags: [bitcoin, cryptocurrency, python, cryptography, protocol-learning]
date: 2021-06-21
source_file: /mnt/ken_personal_wiki/Articles/Andrej Karpathy - A from-scratch tour of Bitcoin in Python.md
---

## Summary
[[AndrejKarpathy]] walks through a zero-dependency [[Python]] implementation that generates Bitcoin keypairs, derives addresses, constructs P2PKH transactions, signs them, and broadcasts them on Bitcoin testnet. The article reframes [[Bitcoin]] as inspectable protocol machinery: value lives in [[UTXOModel]] outputs, ownership is enforced through [[BitcoinScript]] plus digital signatures, and miners include transactions through fee and [[BitcoinProofOfWork]] incentives. The source has no image references to inspect.

## Key Claims
- [[CryptographicIdentity]] in Bitcoin begins with a random secret integer and derives a public key through secp256k1 elliptic-curve scalar multiplication.
- Bitcoin addresses are derived from encoded public keys using SHA-256, RIPEMD-160, version bytes, checksum, and Base58Check-style [[BitcoinAddressEncoding]].
- [[UTXOModel]] means a transaction output is spent in full; partial payment requires new outputs, often including change back to the sender.
- [[BitcoinTransactionModel]] represents a spend as references to previous outputs plus newly created outputs, with miner fees implied by the input-output difference.
- [[BitcoinScript]] commonly locks P2PKH outputs with public-key-hash and signature checks, while each input provides an unlocking script with a signature and public key.
- [[BitcoinProofOfWork]] ties block production to SHA-256 hashing power and fee incentives, while the article leaves mining, block validation, Segwit, P2SH, and broader consensus details mostly out of scope.
- [[FromScratchProtocolLearning]] can make intimidating systems legible by rebuilding core data structures, serialization, hashing, signing, and network-facing artifacts in a small educational implementation.

## Key Quotes
> "open source + state" - Karpathy's frame for blockchain as shared running computation.

> "Every Input/Output of any bitcoin transaction must always be fully spent." - core UTXO model explanation.

> "don't roll your own crypto" - production warning after the educational implementation.

## Connections
- [[AndrejKarpathy]] - author of the tutorial and the related [[Cryptos]] library.
- [[Cryptos]] - Karpathy's cleaner reference implementation for the article's Bitcoin code.
- [[Bitcoin]] - protocol whose identity, transaction, script, fee, and proof-of-work mechanisms are reconstructed.
- [[Python]] - implementation language used for the dependency-free walkthrough.
- [[CryptographicIdentity]] - Bitcoin private/public keypair model explained through secp256k1.
- [[BitcoinAddressEncoding]] - address derivation from public key encoding, hashes, version byte, checksum, and Base58.
- [[UTXOModel]] - representation of spendable value as fully consumed transaction outputs.
- [[BitcoinTransactionModel]] - transaction structure joining previous-output references, outputs, serialized bytes, signatures, and IDs.
- [[BitcoinScript]] - locking and unlocking scripts used to authorize P2PKH spends.
- [[BitcoinProofOfWork]] - miner-selection and block-inclusion mechanism grounded in SHA-256 hashing power and fees.
- [[FromScratchProtocolLearning]] - learning method of rebuilding a live protocol from primitives.

## Contradictions
- No direct contradictions found. The source adds a technical-protocol view of Bitcoin and qualifies older market-adoption framing by showing the underlying transaction machinery rather than replacing it.

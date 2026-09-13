---
title: "Bitcoin Address Encoding"
type: concept
tags: [bitcoin, cryptography, serialization]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[BitcoinAddressEncoding]] is the process of turning Bitcoin public-key material into a shorter, checksummed, network-specific string that users can share as a payment destination.

## Current Synthesis
The tutorial derives a testnet P2PKH-style address by encoding a public key, hashing it with SHA-256 and RIPEMD-160, prefixing a network version byte, appending a double-SHA-256 checksum, and converting the resulting bytes to Base58. This makes an address more usable than a raw public key while preserving a validation path back to the public-key hash required by common locking scripts.

## Key Claims
- Bitcoin addresses are derived from public keys rather than identical to public keys.
- Compressed public-key encoding can represent an elliptic-curve point using x plus one parity bit.
- P2PKH address generation uses SHA-256 followed by RIPEMD-160 to create a public-key hash.
- Version bytes separate mainnet and testnet address spaces.
- A checksum helps detect mistyped addresses with very high probability.
- Base58 avoids visually ambiguous characters in user-facing address strings.

## Evidence
- Public-key encoding: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] implements compressed and uncompressed SEC encodings.
- Hash and version pipeline: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] derives a testnet address from HASH160 plus a version byte.
- Checksum and Base58: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] appends four checksum bytes and encodes the result with a Base58 alphabet.

## Counterevidence & Qualifications
The article focuses on a P2PKH-era address path and explicitly excludes newer address and transaction forms such as Segwit and bech32.

## What Changed
- Added Bitcoin address encoding as the user-facing layer above public-key cryptography.

## Related Concepts
- [[CryptographicIdentity]] - supplies the public key being encoded.
- [[BitcoinScript]] - P2PKH scripts lock outputs to the public-key hash produced by this encoding path.
- [[BitcoinTransactionModel]] - outputs use address-derived public-key hashes to declare future spend authority.

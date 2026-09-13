---
title: "Cryptographic Identity"
type: concept
tags: [cryptography, bitcoin, security]
sources:
  - andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Definition
[[CryptographicIdentity]] is an identity model where control is represented by a secret key and a mathematically related public key that can verify signatures without revealing the secret.

## Current Synthesis
In the Bitcoin tutorial, cryptographic identity starts as a random integer in the valid secp256k1 range. The corresponding public key is an elliptic-curve point produced by scalar multiplication of the generator point, and control over funds depends on keeping the secret key private. The source emphasizes that the integer looks ordinary but can authorize any spend tied to the derived wallet address.

## Key Claims
- A Bitcoin secret key is simply a valid random integer, but knowledge of it controls associated funds.
- The public key is deterministically derived from the secret key by elliptic-curve scalar multiplication.
- The one-way relationship between private and public key lets the public key verify authority without exposing the secret.
- Bitcoin addresses add another derived layer over public keys rather than being the public keys themselves.
- Educational implementations can show the mechanics, but real systems should not use improvised cryptography.

## Evidence
- Secret integer: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] defines the private key as an integer between 1 and the generator order.
- Public derivation: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] computes the public key as repeated generator-point addition accelerated by double-and-add.
- Control boundary: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] notes that anyone who knows the secret key can control the funds associated with it.
- Production warning: [[andrej-karpathy-a-from-scratch-tour-of-bitcoin-in-python]] cautions readers not to use the educational crypto implementation for serious systems.

## Counterevidence & Qualifications
The source does not provide a full mathematical proof of elliptic-curve cryptography, nor does it cover modern wallet management, hardware custody, multisignature setups, seed phrases, or operational key security.

## What Changed
- Added cryptographic identity as the keypair model underneath Bitcoin wallet control.

## Related Concepts
- [[BitcoinAddressEncoding]] - derives shareable wallet addresses from public-key material.
- [[BitcoinTransactionModel]] - uses signatures from cryptographic identities to authorize spends.
- [[BitcoinScript]] - checks public-key hashes and signatures during transaction validation.
- [[SoftwareVerification]] - educational crypto code still needs verification boundaries before production use.

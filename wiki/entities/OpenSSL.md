---
title: "OpenSSL"
type: entity
tags: [cryptography, tls, certificates, command-line-tool]
sources:
  - how-can-i-generate-a-self-signed-ssl-certificate-using-openssl
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Overview
[[OpenSSL]] is a cryptographic toolkit represented here through its command-line support for generating private keys, certificate requests, and self-signed X.509 certificates.

## Current Profile
The source uses `openssl req -x509 -newkey` as the direct generation path. Options select the key algorithm, output files, digest where applicable, validity period, subject, and certificate extensions. `-addext` supplies Subject Alternative Names on newer releases, while older releases require configuration-based extension handling. OpenSSL 3 uses `-noenc` for an unencrypted output key; older examples use `-nodes`.

The toolkit can create the cryptographic objects, but it does not make an arbitrary issuer trusted by browsers. Trust-anchor installation, hostname coverage, certificate profiles, key custody, renewal, and client compatibility remain deployment responsibilities outside the mere success of the command.

## Key Characteristics
- Generates a private key and self-signed certificate in one `req -x509` invocation.
- Supports RSA, elliptic-curve, and Edwards-curve key-generation examples, subject fields, and X.509 extensions.
- Uses version-sensitive flags and extension mechanisms that make copied commands compatibility-dependent.
- Can write an unencrypted server key for unattended startup, shifting protection to file permissions and host controls.
- Produces certificates whose client acceptance still depends on trust anchors and identity validation.

## Evidence
- Direct generation: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] supplies interactive and non-interactive `req -x509 -newkey` commands.
- Names and extensions: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] shows `-addext` SAN entries and a configuration-based fallback for older versions.
- Version boundary: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] distinguishes OpenSSL 3's `-noenc`, older `-nodes`, and pre-1.1.1 extension handling.
- Trust boundary: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] explains that locally generated certificates are not automatically accepted by third-party clients.

## Qualifications
The source is a curated Stack Overflow answer set rather than official versioned documentation or a complete PKI operating guide. Its commands omit several deployment controls, and its algorithm, digest, expiry, and key-encryption recommendations should be checked against the actual OpenSSL release, client population, threat model, and current policy.

## What Changed
- Created a command-line and trust-boundary profile from the self-signed-certificate examples.

## Relationships
- [[SelfSignedCertificates]] - OpenSSL is the generation tool used in the source's direct and private-CA workflows.
- [[HTTPSMigration]] - OpenSSL can supply certificate artifacts for HTTPS, while migration includes many additional system dependencies.
- [[CertificateBasedDeviceIdentity]] - OpenSSL-generated keys and CSRs can participate in the broader CA-chain identity model.

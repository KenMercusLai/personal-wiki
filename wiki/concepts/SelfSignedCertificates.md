---
title: "Self-Signed Certificates"
type: concept
tags: [tls, x509, pki, trust, certificates]
sources:
  - how-can-i-generate-a-self-signed-ssl-certificate-using-openssl
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Definition
[[SelfSignedCertificates]] are certificates whose own private key signs their identity claims, rather than a separate issuer in a certificate chain trusted by the client.

## Current Synthesis
A self-signed certificate can provide encryption and prove possession of its corresponding private key, but those properties do not tell a client that the asserted hostname or operator is trustworthy. Browser warnings are therefore expected unless the certificate is deliberately installed as a trust anchor. Certificate generation and certificate trust are separate operations.

For a single controlled endpoint, a client can explicitly trust the leaf certificate. For multiple managed services, a private certificate authority creates a cleaner separation: protect and distribute one CA trust anchor, then issue replaceable leaf certificates from server CSRs. In either case, the certificate must cover each intended DNS name or IP address in Subject Alternative Name entries. The private key's encryption, permissions, lifetime, renewal, and compromise response remain operating decisions rather than command-line trivia.

## Key Claims
- Successful self-signing does not create browser or operating-system trust.
- Hostname and IP validation requires complete Subject Alternative Name coverage for the identities clients use.
- A private CA separates a stable client trust anchor from replaceable server leaf certificates.
- Unencrypted server keys enable unattended startup but require compensating host and filesystem protection.
- Generation commands are version-sensitive and do not replace certificate lifecycle management.

## Evidence
- Direct generation and warning boundary: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] pairs one-command OpenSSL examples with the explicit warning that third parties do not validate the result.
- Identity coverage: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] supplies DNS, wildcard-DNS, and IP SAN examples and describes CN-only names as deprecated for validation.
- Private-CA path: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] lays out CA creation, CSR signing, leaf deployment, and CA installation on the client.
- Key handling: [[how-can-i-generate-a-self-signed-ssl-certificate-using-openssl]] explains why unattended servers often use unencrypted key files while acknowledging the flag's version change.

## Counterevidence & Qualifications
The source demonstrates mechanics rather than measuring security outcomes. A private CA expands governance duties: its key must be strongly protected, its issuance constrained, and trust removed or certificates replaced after compromise. The examples do not specify basic constraints, key usage, revocation, automated renewal, minimum client support, or production-safe file permissions. Their long lifetimes and algorithm rankings are answer-specific opinions, not universal policy. Public services normally need a publicly trusted CA rather than manual client installation.

## What Changed
- Created the concept by separating cryptographic self-signing from client trust and hostname validation.
- Added private-CA issuance as the scalable managed-client alternative to trusting individual leaf certificates.

## Related Concepts
- [[CertificateBasedDeviceIdentity]] - shows how trusted CA chains bind keys to managed device identities.
- [[HTTPSMigration]] - treats certificates as one dependency within a broader secure-web transition.
- [[AuthenticationInfrastructure]] - trust-anchor distribution and certificate lifecycle are parts of identity operations.
- [[OpenSSL]] - supplies the concrete key and certificate generation commands in the source.

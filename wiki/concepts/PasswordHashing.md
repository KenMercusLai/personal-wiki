---
title: "Password Hashing"
type: concept
tags: [security, authentication, credentials, cryptography]
sources:
  - valentin-mouret-simple-authentication-with-only-postgresql
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Definition
[[PasswordHashing]] is the one-way transformation of a password with a purpose-built, deliberately expensive algorithm and a unique salt so an application can verify a submitted password without storing the original plaintext.

## Current Synthesis
The source explains the central database-compromise model clearly: plaintext gives an attacker every password immediately, while a deterministic unsalted digest enables precomputed lookup and exposes shared passwords. A distinct random salt per credential prevents identical passwords from producing identical stored values and makes precomputed tables far less reusable.

In PostgreSQL `pgcrypto`, `gen_salt('bf')` creates parameters for a bcrypt hash and `crypt(candidate, stored_hash)` reuses the algorithm, salt, and cost encoded in that stored value for verification. This is a sound mechanism in outline, but secure password storage is adaptive rather than finished: the algorithm and cost must remain suitable for current hardware, and a real login system still needs throttling, recovery, session security, rehashing, and careful query and function design.

## Key Claims
- Plaintext password storage turns a database disclosure directly into reusable credentials.
- Fast deterministic hashes alone do not sufficiently slow password guessing and reveal equal-password records.
- A unique random salt per credential prevents identical passwords from sharing one stored representation and defeats reusable precomputed tables.
- A stored password hash should carry the parameters needed to verify a candidate and support coexistence or later upgrades.
- Password hashing protects stored credentials but does not by itself constitute a complete authentication system.

## Evidence
- Plaintext risk: [[valentin-mouret-simple-authentication-with-only-postgresql]] warns that database readers could impersonate users and try exposed passwords elsewhere.
- Deterministic-hash limit: [[valentin-mouret-simple-authentication-with-only-postgresql]] demonstrates SHA-256 before explaining precomputed rainbow-table lookup.
- Salt progression: [[valentin-mouret-simple-authentication-with-only-postgresql]] contrasts one visible shared salt with a different bcrypt salt for each row.
- PostgreSQL mechanism: [[valentin-mouret-simple-authentication-with-only-postgresql]] stores `crypt(password, gen_salt('bf'))` and verifies with `crypt(candidate, stored_hash)`.
- System boundary: [[valentin-mouret-simple-authentication-with-only-postgresql]] explicitly excludes password recovery and leaves other account and login controls unspecified.

## Counterevidence & Qualifications
The article is a short 2023 tutorial, not a security standard or audited implementation. Its SHA-256 step is educational, not an acceptable final password-storage scheme. Its bcrypt call omits an explicit cost, its final SQL function mishandles the email identifier and volatility declaration, and the design does not cover brute-force controls, rehashing, password limits, session management, multi-factor authentication, recovery, or breach response. Database-side hashing can reduce application code, but it also places plaintext candidate passwords and security-sensitive logic at the database boundary.

## What Changed
- Created the concept from the article's progression from plaintext to uniquely salted bcrypt hashes.
- Separated the valid storage mechanism from defects and omissions in the sample authentication function.

## Related Concepts
- [[AuthenticationInfrastructure]] - password verification is one component of a larger identity and session system.
- [[WeakCredentialExposure]] - secure hashing limits the immediate value of a stolen credential database.
- [[PostgreSQL]] - `pgcrypto` supplies the source's hash generation and verification primitives.
- [[EmailMagicLinkAuthentication]] - passwordless email login relocates the credential boundary instead of maintaining a local password hash.

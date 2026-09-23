---
title: "Simple Authentication with only PostgreSQL"
type: source
tags: [postgresql, authentication, security, password-hashing]
date: 2023-01-14
source_file: /mnt/ken_personal_wiki/Articles/Valentin Mouret - Simple Authentication with only PostgreSQL.md
---

## Summary
[[ValentinMouret]] demonstrates a small password-authentication design implemented inside [[PostgreSQL]] with the `pgcrypto` extension. The useful core is [[PasswordHashing]] with a distinct bcrypt salt per stored credential and verification by passing the stored hash back to `crypt()`, but the article is not a complete authentication design and its final SQL function contains correctness and security hazards.

## Key Claims
- Plaintext passwords should never be stored because database readers could immediately impersonate users and reuse exposed credentials against other services.
- A one-way password hash lets an application compare a submitted password without retaining the original plaintext.
- Unsalted deterministic hashes remain vulnerable to precomputed lookup and reveal when users share the same password.
- PostgreSQL `pgcrypto` can generate a distinct bcrypt salt per credential with `gen_salt('bf')`, encode the salt and parameters in the stored hash, and verify a candidate with `crypt(candidate, stored_hash)`.
- Keeping password verification in PostgreSQL can make a minimal application's registration, login, and password-change operations compact, but it does not supply recovery, throttling, sessions, multi-factor authentication, or the rest of an account-security lifecycle.
- The sample `authenticate_user` function should not be copied as written: `email = email` does not safely bind the function argument, `IMMUTABLE` is inconsistent with reading a table, and a failed lookup produces `NULL` rather than an explicit `false`.

## Key Quotes
> "This only covers authentication." - the author's explicit boundary around the example.

> "Security is a tradeoff and you cannot reach a perfect setup." - the conclusion's reminder to evaluate the design in context.

## Connections
- [[ValentinMouret]] - author of the PostgreSQL-only authentication walkthrough.
- [[PostgreSQL]] - database and execution environment used to store and verify password hashes.
- [[PasswordHashing]] - central credential-storage technique demonstrated with `pgcrypto`, unique salts, and bcrypt.
- [[AuthenticationInfrastructure]] - broader system boundary that the compact database example only partially covers.
- [[WeakCredentialExposure]] - plaintext or poorly protected credential stores increase the damage of database compromise and cross-service password reuse.

## Contradictions
- The article's intermediate description of SHA-256 as an acceptable password hash is unsafe if separated from its pedagogical role: a fast general-purpose digest is not a substitute for a deliberately expensive password-hashing scheme.
- The final function does not reliably constrain the lookup by the supplied email because its parameter and table column have the same name. The example also declares a table-reading function `IMMUTABLE` and returns `NULL` on no match, despite presenting it as a boolean authenticator.
- The bcrypt outline matches PostgreSQL's documented `crypt(candidate, stored_hash)` verification pattern, but `gen_salt('bf')` without an explicit cost uses PostgreSQL's default cost. Cost selection, future rehashing, password-length behavior, and brute-force throttling are absent, so the snippet is not a current production-ready recipe.

---
title: "Zero-Width Text Fingerprinting"
type: concept
tags: [security, privacy, unicode, fingerprinting]
sources:
  - be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[ZeroWidthTextFingerprinting]] is the insertion of an invisible, recipient-specific identifier into text by encoding data with zero-width Unicode characters so copied text can later be attributed.

## Current Synthesis
The source presents zero-width fingerprinting as a lightweight leak-attribution mechanism. A system converts a viewer's username to binary, represents bits and character boundaries with different invisible Unicode code points, and inserts that sequence into confidential text. If the text appears elsewhere with those code points intact, the system can extract and decode the marker to identify the account for which that copy was rendered.

The mechanism is attribution evidence, not authenticated proof. Its reported forum deployment successfully identified one leaking account, but a person who knows the encoding can remove the marker, corrupt it, or substitute another user's public username. A non-public per-user identifier reduces simple impersonation but does not by itself provide cryptographic integrity, establish who performed the copy, or guarantee that the marker survives normalization and reformatting.

## Key Claims
- Zero-width Unicode characters can carry recipient-specific data without visibly changing ordinary text.
- A reversible mapping from text to binary and from bits to zero-width characters enables later decoding.
- Per-recipient rendering can turn a redistributed text copy into an account-attribution signal.
- The technique depends on the copied channel preserving the invisible code points.
- A forgeable public identifier makes the marker vulnerable to tampering and false attribution.

## Evidence
- Encoding mechanism: [[be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters]] describes converting a username to binary, mapping bits and boundaries to distinct zero-width characters, and inserting the sequence into displayed text.
- Recovery path: [[be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters]] reverses the process by extracting the invisible sequence, reconstructing binary, and decoding the username.
- Reported use: [[be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters]] says a copied private-forum announcement retained its marker and led to the account that was then banned.
- Tampering risk: [[be-careful-what-you-copy-invisibly-inserting-usernames-into-text-with-zero-width-characters]] warns that an informed user could insert another marker and recommends encoding a non-public unique ID rather than a username.

## Counterevidence & Qualifications
The evidence is one author's implementation account and one reported success, not an independent evaluation. The source does not test survival across editors, messaging systems, Unicode normalization, sanitizers, retyping, screenshots, or deliberate stripping. It also does not add a signature or message-authentication code, specify collision and key-management behavior, distinguish the rendered recipient from the human who redistributed the text, or examine consent and whistleblower-safety implications. A decoded marker should therefore be treated as a potentially useful investigative signal rather than conclusive identity proof.

## What Changed
- Created the concept from the article's reversible encoding method, reported forum deployment, and explicit framing caveat.

## Related Concepts
- [[IdentityResolution]] - both connect indirect digital traces to a durable person or account identity.
- [[AnonymousSourcing]] - recipient-specific markers can expose or chill people who redistribute sensitive material anonymously.
- [[SecretManagement]] - prevents sensitive material from leaking through unsafe handling, while text fingerprinting attempts to attribute a leak after copying occurs.

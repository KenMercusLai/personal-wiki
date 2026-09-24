---
title: "Be careful what you copy: Invisibly inserting usernames into text with Zero-Width Characters"
type: source
tags: [security, privacy, unicode, fingerprinting]
date: 2018-04-03
source_file: raw/Be careful what you copy- Invisibly inserting usernames into text with Zero-Width Characters.md
---

## Summary
The article describes a [[ZeroWidthTextFingerprinting]] technique that converts a viewer's username into binary, maps the bits and separators to invisible Unicode characters, and inserts the result into displayed text so a later copy can be attributed. A private gaming forum reportedly used the technique to identify a member who reposted confidential announcements, but the author also notes that a knowledgeable copier could tamper with the marker and frame another user.

## Key Claims
- Per-recipient text can carry an invisible identifier through ordinary copy and paste.
- The demonstrated encoding maps username characters to binary and then maps bits and character boundaries to distinct zero-width Unicode characters.
- A leaked copy can be decoded by extracting the zero-width sequence and reversing the mapping.
- The author's private-forum deployment reportedly identified the account that copied an announcement posted elsewhere.
- A public username is a weak payload because an attacker who understands the scheme can forge another user's marker; the author recommends a non-public unique user ID instead.
- Applications commonly fail to render zero-width characters visibly, so users may not notice that copied text contains extra data.

## Key Quotes
> "Depending on your line of work, it could be vitally important to understand the risks associated with copying text."

## Connections
- [[ZeroWidthTextFingerprinting]] - the article's reversible per-user attribution mechanism and its main tampering limitation.
- [[IdentityResolution]] - both connect otherwise indirect traces to a person or account, with consequential privacy and misuse risks.
- [[AnonymousSourcing]] - invisible per-recipient markers can undermine a source's anonymity when text is shared.

## Contradictions
- No direct contradiction found. The source does qualify its own success case by acknowledging that an informed user could alter the marker and falsely implicate another account.

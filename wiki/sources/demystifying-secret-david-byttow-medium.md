---
title: "Demystifying Secret"
type: source
tags: [secret, anonymity, privacy, security, social-networking]
date: 2014-02-03
source_file: "/mnt/ken_personal_wiki/Articles/Demystifying Secret - David Byttow - Medium.md"
---

## Summary
[[DavidByttow]] describes the early architecture of [[Secret]], an anonymous social app designed to distribute posts through a social graph without routinely attaching author identity to message records. The system combined Google-hosted infrastructure, TLS, server-side encryption, locally hashed contacts, per-recipient access tokens, dual-admin access, and thresholded delivery intended to make simple identity-isolation attacks harder. The account is a founder-authored design explanation, not an independent audit, and it acknowledges that shared-salt contact hashes can be guessed if the salt is known.

## Key Claims
- Secret ran on Google App Engine with Go, Java, and Python components, stored data in a non-relational system built on Bigtable, kept images in Google Cloud Storage, and planned to migrate backend services to AWS by early 2015.
- Network traffic used TLS, while message content was encrypted before datastore writes with keys held by an off-site rotating keystore; this was server-side protection rather than end-to-end encryption because the service decrypted content for delivery.
- Contact phone numbers and email addresses were hashed locally with a shared salt before upload, reducing routine raw-data collection but remaining vulnerable to matching attacks over guessable inputs when the salt is known.
- Secret metadata avoided direct user references: each recipient received a unique token whose access lived in the secret's ACL, and user, post, and ACL structures were logically separated.
- Administrative access to specific-user information required two founders to authenticate with two-factor-protected Google accounts and request the same resource within a time window.
- Delivery was asynchronous, relevance-scored, unique per recipient, and reversible; contacts were one signal rather than a rule that every post reached every address-book entry.
- Visibility increased with social-graph size, withholding posts and friend-versus-friend-of-friend detail from sparse accounts to make simple author-isolation attacks harder.

## Key Quotes
> "We don't know the phone number or email address that corresponds to the hash value." - the intended contact-discovery privacy boundary, qualified by the article's own matching warning.

> "This abstraction provides no physical security" - on the limit of logically separating users, posts, and access-control records.

## Connections
- [[DavidByttow]] - Secret cofounder and author describing the system's design.
- [[Secret]] - anonymous social product whose storage, identity, and delivery controls are documented.
- [[Google]] - historical hosting and security substrate through App Engine, Bigtable, Cloud Storage, Google accounts, and two-factor authentication.
- [[AnonymousSocialPrivacyArchitecture]] - combines data minimization, unlinkability, dual control, and disclosure thresholds while retaining important server-side trust assumptions.
- [[IdentityResolution]] - inverse design problem: Secret sought useful social-graph matching without directly storing raw contact identifiers beside content.
- [[ProductionAccessControl]] - the two-person administrative rule is a narrow privileged-access control.
- [[AuthenticationInfrastructure]] - founder Google accounts and two-factor authentication supported the dual-admin rule.

## Contradictions
- The article calls salted contact hashing a one-way transformation but also acknowledges that phone numbers can be matched to hashes, especially if the shared salt is known; hashing a small, enumerable identifier space is therefore not equivalent to irreversible anonymization.
- The architecture reduces direct identity-content linkage but does not establish end-to-end anonymity: Secret's servers could decrypt messages, the structures shared infrastructure, and authorized administrators could access information under a two-person rule.
- The source gives no independent security audit, cryptographic construction details, key-compromise analysis, abuse outcomes, or measurements showing that its delivery thresholds actually prevented deanonymization.

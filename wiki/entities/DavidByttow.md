---
title: "David Byttow"
type: entity
tags: [person, founder, engineering, privacy]
sources:
  - demystifying-secret-david-byttow-medium
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Overview
[[DavidByttow]] is represented as a [[Secret]] cofounder and former Google engineer explaining the anonymous social app's early privacy, security, storage, and delivery architecture.

## Current Profile
Byttow presents product trust as an architecture-and-disclosure problem. His account connects infrastructure choices to specific identity boundaries: contacts are transformed on-device before upload, content and user records are not directly joined, recipients receive scoped access tokens, administrators need dual authorization, and sparse social graphs reveal less delivery information. He also states the limits of some choices, particularly guessable contact hashes and logical rather than physical data separation.

## Key Characteristics
- Cofounded [[Secret]] and authored its early public architecture explanation.
- Brought prior Google backend experience to the choice of Google-hosted infrastructure.
- Treated anonymity as a layered product and delivery property rather than a single encryption feature.
- Publicly acknowledged weaknesses in the contact-hashing approach and invited security proposals.

## Evidence
- Founder role and purpose: [[demystifying-secret-david-byttow-medium]] identifies Byttow as Secret's cofounder and frames the article as a trust-building explanation of identity protection.
- Infrastructure judgment: [[demystifying-secret-david-byttow-medium]] says his Google backend experience informed the decision to host Secret on Google's infrastructure.
- Layered anonymity controls: [[demystifying-secret-david-byttow-medium]] describes local contact hashing, per-recipient ACL tokens, logical record separation, dual-admin access, and thresholded disclosure.
- Limit acknowledgment: [[demystifying-secret-david-byttow-medium]] concedes that a known shared salt can permit phone-number matching and names stronger approaches as active research.

## Qualifications
This profile rests on one founder-authored 2014 article. It does not independently verify Byttow's career, the implementation of the described controls, Secret's later architecture, the planned AWS migration, or the system's real-world resistance to deanonymization and administrative abuse.

## What Changed
- Created a profile centered on Byttow's documented role in Secret and his layered, explicitly qualified privacy architecture.

## Relationships
- [[Secret]] - company and anonymous social product Byttow cofounded.
- [[Google]] - former employer and infrastructure context informing his hosting decision.
- [[AnonymousSocialPrivacyArchitecture]] - design pattern assembled from the controls in his account.
- [[ProductionAccessControl]] - the dual-admin rule limits privileged access to user-specific information.

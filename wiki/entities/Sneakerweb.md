---
title: "Sneakerweb"
type: entity
tags: [web, offline, archiving, protocol]
sources:
  - sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin
last_updated: 2026-10-16
knowledge_schema: synthesis-v1
---

## Overview
[[Sneakerweb]] is an experimental system for packaging a publisher-built website into an importable SNK archive that can be replayed locally and exchanged without continuous internet access.

## Current Profile
In the available source, Sneakerweb combines complete-site packaging, browser replay, public-key-derived site addresses, hyperlinks among archived sites, and an intended Willow-based synchronization layer. The publisher can distribute a site over ordinary downloads, physical media, or local networks, while a reader receives a usable local copy rather than a provider-controlled permission to revisit the live service. This joins [[OfflineWebDistribution]], [[DigitalContentDurability]], and [[LocalFirstSoftware]], but the project is described as early, slow, and uncertain to gain adoption.

## Key Characteristics
- Packages an already-built website as a publisher-generated SNK archive rather than making every reader crawl the live site.
- Replays imported sites through ordinary browser technology, preserving more layout and interaction than document-oriented formats may support.
- Uses long public-key-derived addresses intended to remain stable without DNS renewal or certificate-authority trust chains.
- Intends to synchronize incrementally through Willow across physical media, local networks, or internet transports.
- Allows archived sites to link to one another, making a network of reader-held copies possible rather than treating each archive as an isolated page list.
- Transfers practical custody and some distribution power from the publisher to readers while leaving copyright unchanged.

## Evidence
- Packaging and replay: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] describes handing a compiled website to Sneakerweb, producing an SNK package, and importing it for local replay.
- Address and trust model: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] says a site's address is derived from its public key and does not depend on renewable DNS or expiring CA certificates.
- Synchronization path: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] presents Willow as the basis for future incremental synchronization over USB, Bluetooth, infrared, QR codes, LANs, and internet connections.
- Product surface: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] includes an inspected Walky6 screenshot with import, navigation, archive sorting, dated copies, and long Sneaker addresses.
- Publisher commitment: [[sneakerweb-hu-lian-wang-de-cui-ruo-yu-ren-xing-luo-li-li-de-shu-ju-zhong-xin]] reports that RORIRI published a roughly 300 MB archive of the blog, including comments, while accepting possible traffic loss.

## Qualifications
The evidence is one enthusiastic community participant's account and prototype, not the protocol specification, interoperability tests, an independent security review, or measured adoption. The source itself says Willow remains draft-like and performs poorly. Stable key identity does not solve discovery, key compromise or rotation, revocation, malicious archives, renderer obsolescence, external dependencies, seeding incentives, moderation, lawful removal, or private-data leakage. The comparison with WACZ, Kage, ZIP, Web Bundles, and ZeroNet reflects the author's priorities rather than controlled evaluation.

## What Changed
- Created Sneakerweb as the project's canonical entity page.
- Distinguished publisher-generated site packaging from reader-side crawling.
- Captured public-key addressing, transport-independent synchronization intent, and reader custody as separate design properties.

## Relationships
- [[OfflineWebDistribution]] - Sneakerweb is a concrete publisher-to-reader offline web packaging system.
- [[DigitalContentDurability]] - local, replayable archives reduce dependence on continued operation of the original service.
- [[LocalFirstSoftware]] - imported replicas remain usable locally and may synchronize later through multiple transports.
- [[WebCentralization]] - key identity and reader-held replicas reduce selected dependencies on centralized naming, certificate, hosting, and platform infrastructure.
- [[RORIRI]] - source author, archive publisher, and builder of the Walky6 prototype interface.

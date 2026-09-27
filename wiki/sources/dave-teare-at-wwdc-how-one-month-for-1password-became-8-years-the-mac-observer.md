---
title: "Dave Teare at WWDC: How One Month for 1Password Became 8 Years"
type: source
tags: [1password, product-development, ios, privacy, customer-feedback]
date: 2013-06-19
source_file: "/mnt/ken_personal_wiki/Articles/Dave Teare at WWDC- How One Month for 1Password Became 8 Years – The Mac Observer.md"
---

## Summary
In a 2013 WWDC interview, [[DaveTeare]] and [[JeffShiner]] describe how [[AgileBits]] grew [[OnePassword]] from a one-month form-filling utility into its flagship product through direct customer feedback and repeated platform adaptation. The account connects the product's move from Mac to iOS with a complete 1Password 4 rewrite, desktop-free Dropbox and iCloud sync, a widening nontechnical user base, and a privacy choice that limited usage measurement. It is a founder and company retrospective rather than an independent assessment of product quality, security, adoption, or the causes of commercial success.

## Key Claims
- [[DaveTeare]] and [[RoustemKarimov]] left World Vision Canada after adopting Macs and experimenting with independent work; their eventual product began as OS X Form, a tool for saving repetitive web-test form entries.
- Password storage began as an adjacent form-field feature, but feedback after distribution through VersionTracker and MacUpdate kept the planned one-month project alive for roughly eight years.
- AgileBits initially treated iOS as an add-on to a Mac product, first using a bookmarklet and then iterating as Apple exposed more application capabilities.
- 1Password 4 for iOS was a complete rewrite targeting iOS 6, intended to replace an accreted codebase with a new foundation that could absorb platform capabilities learned over earlier iterations.
- Support requests from people with iPods and iPads but no desktop revealed a distinct segment, leading 1Password 4 to support Dropbox and iCloud synchronization without a Mac or Windows computer.
- AgileBits deliberately avoided extensive user data collection, which supported its security posture but prevented Teare from precisely measuring desktop-free usage or confidently allocating resources by segment.
- Teare estimated that desktop-free users were around 10% of the iOS base, while sales were close to evenly split between desktop and iOS; these were historical estimates, not audited usage measures.
- The forthcoming Mac beta reportedly attracted more than 20,000 signups, including 10,000 in the first six hours largely through Twitter, illustrating a large change from AgileBits' early struggle to recruit testers.

## Key Quotes
> "we’ll spend another month on it" - Teare on extending the original project through customer feedback.

> "I don’t have a desktop." - support request that exposed a desktop-free user segment.

## Connections
- [[DaveTeare]] - cofounder and principal interview subject recounting AgileBits' and 1Password's origin.
- [[JeffShiner]] - AgileBits participant who explains the use of document syncing and reports early beta demand.
- [[RoustemKarimov]] - Teare's cofounder in the origin story.
- [[AgileBits]] - company that developed and commercialized 1Password.
- [[OnePassword]] - product whose origin, iOS evolution, synchronization design, and 2013 demand are discussed.
- [[CustomerLedProductDevelopment]] - direct users and support cases changed product commitment, features, and platform scope.
- [[ProductUserSegmentation]] - desktop-free and less-technical customers required a different setup and synchronization experience.
- [[PrivacyPreservingProductMeasurement]] - limiting user-data collection protected a security-company principle while weakening segment measurement.

## Contradictions
- The interview's success, sales, usage, and signup claims come from AgileBits participants and are not independently audited; the desktop-free share is explicitly a rough guess.
- The article reports that document-based iCloud sync worked for 1Password while acknowledging support complaints and system complexity, so it does not establish that the implementation was failure-free or generally superior to Core Data sync.
- Both effective image references are absent from the local export, and the publisher's original JPEG endpoints now return HTTP 404. The live article labels the first as a Dave Teare image but gives no useful description for the second; neither could be opened or interpreted, so no visual evidence or asset manifest was created.

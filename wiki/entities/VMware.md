---
title: "VMware"
type: entity
tags: [startup, infrastructure, company]
sources:
  - 16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more
  - culture-is-the-behavior-you-reward-and-punish-jocelyngoldfein
  - gal-zellermayer-0-bugs-policy
  - network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[VMware]] is presented through source-bounded accounts of high-growth hiring, communication, culture, engineering management, and one virtual-network loop incident.

## Current Profile
VMware's profile shows that early hiring can be difficult when the company idea is not yet well-defined, while later scale can make high-volume hiring easier without requiring lower standards. Weekly writeups provided one mechanism for spreading context across teams.

By a 2008 leadership offsite, VMware had doubled revenue and headcount for four consecutive years. When [[CharlesOReilly]] asked leaders what a new hire should do to succeed, they named innovation, hard work, collaboration, quality, constant email availability, sounding smart, and consensus, but not customers. The omission exposes a gap between stated customer orientation and the behavior associated with internal success.

A later source-scoped VMware Israel engineering-management context comes from [[GalZellermayer]]. Drawing on several Scrum teams, he proposes the [[ZeroBugsPolicy]] and credits VMware Israel colleagues and partners as a major influence. The article reports that prompt fix-or-close decisions reduced recurring bug management and encouraged higher quality, but does not identify the teams, period, products, or measured organizational outcomes.

In a separate 2012 networking article, [[NetworkJanitor]] reports that a Microsoft guest bridged vNICs on separate VLANs inside a VMware environment, allowing a BPDU to cross the physical host connection until BPDU Guard disabled the port. The author also attributes a recommendation to apply BPDU Filter on VMware-facing ports to VMware, but provides no document, product, version, or named representative. The useful evidence is therefore the practitioner's loop and containment account, not a verified company-wide policy.

## Key Characteristics
- Shows the contrast between ambiguous early hiring and high-volume later hiring.
- Treats hiring standards as non-negotiable even when hiring more than 100 people a month.
- Uses weekly written updates to help teams know what is happening across the organization.
- Reveals implicit norms by comparing the behavior associated with internal success against stated customer orientation.
- Shows rapid growth as a cultural replication risk when role models and rewards become inconsistent.
- Supplies the professional context for a manager's practitioner proposal to eliminate indefinitely deferred bug inventory.
- Appears in a practitioner account showing how guest bridging can extend a Layer 2 loop beyond a virtualization host.

## Evidence
- Hiring difficulty: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] says Greene found it harder to hire when VMware was small and less defined.
- Hiring volume: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] says VMware later hired more than 100 people per month.
- Written updates: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] describes weekly team updates that spread across VMware.
- High-growth context: [[culture-is-the-behavior-you-reward-and-punish-jocelyngoldfein]] says VMware had doubled revenue and headcount for four years before the 2008 offsite.
- Revealed norms: [[culture-is-the-behavior-you-reward-and-punish-jocelyngoldfein]] reports that leaders' success criteria included innovation, quality, responsiveness, appearing smart, and consensus but omitted customers.
- Culture mechanism: [[culture-is-the-behavior-you-reward-and-punish-jocelyngoldfein]] uses VMware to show how public rewards, consequences, and role models teach employees what conduct succeeds.
- Engineering-practice context: [[gal-zellermayer-0-bugs-policy]] identifies Zellermayer as a VMware R&D manager and credits VMware Israel colleagues and partners with influencing the policy.
- Virtual-network boundary: [[network-janitor-on-the-premature-death-of-spanning-tree-and-the-indiscriminate-killing-of-canaries]] reports a guest bridging vNICs across VLANs and BPDU Guard containing the loop at the host-facing switch port.

## Qualifications
This profile does not comprehensively cover VMware's product category, acquisition history, or technical architecture; it captures source-specific scaling, culture, engineering-management, and networking anecdotes. Goldfein's retrospective does not measure how widespread the listed behaviors were or whether VMware later changed them. Zellermayer's essay does not establish that the policy was company-wide or report comparative quality, throughput, or defect data. Network Janitor's polemical article supplies no configuration records or vendor documentation, so its attributed BPDU Filter advice is not treated as verified VMware policy.

## What Changed
- Added VMware Israel as the source-bounded setting and influence network for Zellermayer's zero-bugs proposal.
- Added a qualified practitioner account of guest bridging across VLANs and BPDU Guard containment.

## Relationships
- [[DianeGreene]] - VMware operator cited in the source.
- [[StartupHiringAtScale]] - VMware supplies early and high-volume hiring examples.
- [[ScalingCommunication]] - VMware's weekly writeups are a communication practice.
- [[JocelynGoldfein]] - author and participant recounting the offsite.
- [[CharlesOReilly]] - workshop leader who elicited VMware's implicit success norms.
- [[StartupCulture]] - VMware is a case of culture revealed through rewarded behavior.
- [[GalZellermayer]] - VMware Israel R&D manager proposing the zero-bugs practice.
- [[ZeroBugsPolicy]] - source-scoped software-quality policy associated with VMware Israel colleagues.
- [[NetworkJanitor]] - practitioner reporting a loop in a VMware environment and criticizing attributed BPDU Filter guidance.
- [[EdgeNetworkLoopProtection]] - control problem illustrated by the guest-bridging incident.

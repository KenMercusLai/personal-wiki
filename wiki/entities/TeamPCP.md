---
title: "TeamPCP"
type: entity
tags: [threat-actor, cybercrime, supply-chain]
sources:
  - github-3800-repos
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[TeamPCP]] is a self-identified cybercriminal group represented here through its claim to possess and sell GitHub internal source code and thousands of private repositories.

## Current Profile
The retained forum screenshot shows a TeamPCP account advertising GitHub source code and internal organizations, claiming around 4,000 private repositories, offering samples as authenticity evidence, and seeking offers of at least $50,000. GitHub said the attacker's repository count was directionally consistent with its investigation, but the archived report says GitHub had not attributed the breach. The same report links TeamPCP to earlier attacks on developer-code platforms, but does not supply the primary evidence needed to independently assess those attributions.

## Key Characteristics
- Publicly claimed possession of GitHub internal source code and approximately 4,000 private repositories.
- Presented data samples as a proposed means for buyers to verify authenticity.
- Sought at least $50,000 and threatened a free leak if no buyer emerged.
- Was associated by the article with attacks involving GitHub, PyPI, npm, Docker, and the Mini Shai-Hulud campaign.
- Was not publicly attributed the GitHub intrusion by GitHub in the archived article.

## Evidence
- Breach claim: [[github-3800-repos]] reproduces a forum screenshot in which a TeamPCP account advertises GitHub internal source code and around 4,000 private repositories.
- Sale terms: [[github-3800-repos]] reports and visually records the offer of samples, the minimum price, and the threat to leak the material if no buyer appeared.
- Partial corroboration: [[github-3800-repos]] quotes GitHub describing the attacker's repository count as directionally consistent with its investigation.
- Broader association: [[github-3800-repos]] reports prior links to attacks across several developer-code ecosystems without reproducing their underlying attribution evidence.

## Qualifications
The source establishes TeamPCP's public claim and GitHub's broad agreement with the claimed repository count, not the group's authorship of the intrusion. GitHub had not publicly attributed the breach, and a sale advertisement can exaggerate ownership, completeness, exclusivity, or authenticity. The article's history of earlier TeamPCP campaigns is secondary reporting and is not independently reconstructed here.

## What Changed
- Created a qualified profile separating TeamPCP's public possession-and-sale claim from confirmed GitHub attribution.
- Recorded the retained forum screenshot as direct evidence of the advertised scope and terms.

## Relationships
- [[GitHub]] - target whose internal repositories TeamPCP claimed to possess and sell.
- [[VisualStudioCode]] - editor whose poisoned extension was the confirmed initial compromise path.
- [[DeveloperExtensionSupplyChainAttack]] - attack pattern associated with the GitHub incident and the group's reported campaign history.

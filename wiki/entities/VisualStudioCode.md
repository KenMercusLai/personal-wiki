---
title: "Visual Studio Code"
type: entity
tags: [software, code-editor, extensions, marketplace]
sources:
  - github-3800-repos
last_updated: 2026-10-24
knowledge_schema: synthesis-v1
---

## Overview
[[VisualStudioCode|Visual Studio Code]] is Microsoft's code editor, represented here through its extension system and the security boundary created when developer-installed plugins receive access to privileged workstations.

## Current Profile
VS Code supports plugins distributed through the official VS Code Marketplace. In the GitHub incident, an employee installed a poisoned extension version that compromised the endpoint and enabled exfiltration of internal repositories. GitHub removed the unnamed malicious version from the marketplace. The report places this event in a wider history of malicious extensions used for credential theft, cryptomining, basic ransomware, cryptocurrency theft, and data exfiltration, making extension trust a developer-workstation and software-supply-chain concern rather than a cosmetic editor preference.

## Key Characteristics
- Extensible code editor whose plugins can add tools and integrations.
- Uses an official marketplace as a distribution and discovery channel for extensions.
- Can expose high-value source code and credentials when a malicious extension executes on a developer workstation.
- Has hosted malicious extensions with large reported install counts, demonstrating that marketplace presence and popularity are incomplete trust signals.

## Evidence
- Compromise path: [[github-3800-repos]] reports GitHub's confirmation that a poisoned VS Code extension compromised an employee endpoint.
- Consequence: [[github-3800-repos]] says the compromise enabled exfiltration of roughly 3,800 GitHub-internal repositories.
- Containment: [[github-3800-repos]] reports removal of the malicious extension version and isolation of the endpoint.
- Recurring ecosystem risk: [[github-3800-repos]] summarizes earlier malicious extensions associated with credential theft, cryptomining, ransomware, cryptocurrency theft, and external data exfiltration.

## Qualifications
The report does not name the extension, explain its requested permissions, document the marketplace review failure, identify the employee's access scope, or show whether platform controls could have prevented the exfiltration. Earlier install and malware figures are secondary historical examples in the same news article rather than a systematic measurement of marketplace prevalence or comparative editor risk.

## What Changed
- Created a security-focused profile of VS Code's extension and marketplace boundary.
- Connected developer-plugin trust to the confirmed GitHub repository-exfiltration incident.

## Relationships
- [[GitHub]] - organization whose employee endpoint was compromised through a poisoned VS Code extension.
- [[TeamPCP]] - group that claimed possession of the resulting internal repository data without confirmed attribution.
- [[DeveloperExtensionSupplyChainAttack]] - security pattern that turns editor plugins into an access path to development assets.

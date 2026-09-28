---
title: "Code Spaces"
type: entity
tags: [code-hosting, software-collaboration, cloud-security, business-failure]
sources:
  - hacker-puts-hosting-service-code-spaces-out-of-business-threatpost
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Overview
[[CodeSpaces]] was a code-hosting and software-collaboration service that ceased trading in June 2014 after an attacker gained access to its [[AWS]] control panel and deleted most production data, configurations, repositories, and backups.

## Current Profile
Threatpost presents Code Spaces as an extreme business-continuity case in which cloud administrative access mattered more than direct machine access. The attacker reportedly paired a DDoS attack and extortion demand with control-panel access, created additional logins, and destroyed assets when the company attempted to recover the account.

The company had advertised geographic redundancy and described its recovery plan as practiced and proven. Those assurances did not survive a shared administrative failure boundary: EBS snapshots and volumes, S3 buckets, AMIs, instances, configurations, SVN repositories, and most backups were within the attacker's deletion scope. Code Spaces said the financial cost, customer refunds, and loss of credibility made continued operation impossible.

## Key Characteristics
- Offered hosted source-code repositories and software-collaboration services.
- Ran production and recovery assets through AWS services including EC2, EBS, S3, and AMIs.
- Faced a combined DDoS, extortion, and cloud-account intrusion in June 2014.
- Reported that the attacker created persistent logins and deleted assets after recovery attempts began.
- Lost nearly all SVN repositories, database volumes, snapshots, configurations, and backups within about 12 hours.
- Ceased trading because technical loss became an irreversible financial and credibility crisis.

## Evidence
- Service role: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] identifies Code Spaces as a code-hosting and software-collaboration platform.
- Attack path: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] reports a DDoS attack, extortion demand, EC2 control-panel intrusion, and additional attacker-created logins.
- Destructive scope: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] lists deleted EBS snapshots and volumes, S3 buckets, AMIs, instances, configurations, repositories, and backups.
- Business outcome: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] says recovery cost, customer refunds, and damaged credibility forced the company to cease trading.
- Assurance gap: [[hacker-puts-hosting-service-code-spaces-out-of-business-threatpost]] contrasts advertised three-continent redundancy and a reportedly practiced recovery plan with the loss of most recoverable assets.

## Qualifications
The profile rests on one 2014 Threatpost report that relies heavily on Code Spaces' own public statement during the crisis. It does not establish the initial-access method, independently reconstruct the attack, identify which AWS identity protections were configured, quantify customer losses, or show whether any later recovery occurred. The incident supports claims about shared administrative failure boundaries, not a conclusion that AWS itself failed or that any single control would certainly have prevented the outcome.

## What Changed
- Created a profile that treats Code Spaces as a control-plane compromise and business-continuity case rather than only a data-loss anecdote.

## Relationships
- [[AWS]] - hosted the control plane and storage, compute, image, and snapshot resources involved in the reported incident.
- [[BackupAndRecovery]] - Code Spaces' nominally redundant and offsite copies remained vulnerable to the same destructive authority.
- [[CloudAccountSegmentation]] - the incident illustrates why production and recovery assets need separate administrative failure boundaries.
- [[ProductionAccessControl]] - persistent privileged access determined the attacker's ability to delete infrastructure.

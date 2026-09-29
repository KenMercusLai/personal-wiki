---
title: "Hacker Puts Hosting Service Code Spaces Out of Business"
type: source
tags: [cloud-security, incident-response, backups, aws, business-continuity]
date: 2014-06-18
source_file: "/mnt/ken_personal_wiki/Articles/Hacker Puts Hosting Service Code Spaces Out of Business - Threatpost.md"
---

## Summary
Threatpost reports that an attacker combined a DDoS attack and extortion demand with access to [[CodeSpaces]]'s [[AWS]] control panel, created persistent logins, and deleted production infrastructure together with backups. The incident turned an account compromise into an existential [[BackupAndRecovery]] failure within about 12 hours: EBS snapshots and volumes, S3 buckets, AMIs, instances, machine configurations, and most repositories were deleted, after which Code Spaces said it could no longer operate or preserve customer confidence.

## Key Claims
- Control-plane access can be more consequential than direct server access because administrative credentials can authorize deletion of compute, storage, configuration, snapshots, and backups across a cloud account.
- Changing the known EC2 password did not end the intrusion because the attacker had created additional logins and began deleting assets after noticing recovery attempts.
- Keeping production data, snapshots, and nominally offsite backups inside one deletable administrative boundary left them vulnerable to the same compromise.
- Code Spaces reported losing all SVN repositories and their backups and snapshots, all EBS volumes containing database files, and most other AWS-hosted assets; only a few old SVN nodes and one Git node remained.
- Redundancy claims and a reportedly practiced recovery plan did not prevent business failure when the recoverable copies were inside the attacker's effective deletion scope.
- AWS offered two-factor authentication and IAM controls for individual credentials, role separation, and least privilege, while customers remained responsible for credential management.

## Key Quotes
> "Backing up data is one thing, but it is meaningless without a recovery plan" - Code Spaces on the distinction between copies and recoverability.

> "most of our data, backups, machine configurations and offsite backups were either partially or completely deleted" - Code Spaces on the attack's scope.

## Connections
- [[CodeSpaces]] - code-hosting and collaboration company forced to cease trading after the destructive compromise.
- [[AWS]] - cloud provider whose EC2 control panel and EBS, S3, and AMI resources were used and deleted in the incident.
- [[BackupAndRecovery]] - the event shows that backups are not independent when the same compromised administrative authority can delete them.
- [[CloudAccountSegmentation]] - separate administrative boundaries can reduce the chance that one account compromise reaches production and every recovery copy.
- [[ProductionAccessControl]] - privileged control-panel access and persistent backup logins determined the attacker's destructive scope.
- [[SecretManagement]] - account credentials were the reported access boundary, although the article does not establish how the attacker obtained them.

## Contradictions
- Code Spaces had advertised geographic redundancy and said its recovery plan was practiced and proven, yet the attacker could delete production data and most recovery assets through the compromised control plane.
- The report does not establish the initial credential-compromise method, independently verify the company's incident account, or show whether multi-factor authentication, IAM separation, cross-account backups, or deletion protections were configured.

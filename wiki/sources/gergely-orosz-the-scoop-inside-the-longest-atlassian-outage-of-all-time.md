---
title: "The Scoop: Inside the Longest Atlassian Outage of All Time"
type: source
tags: [software-engineering, reliability, incident-response, outage, atlassian]
date: 2022-04-14
source_file: "/mnt/ken_personal_wiki/Articles/Gergely Orosz - The Scoop Inside the Longest Atlassian Outage of All Time.md"
---

## Summary
[[GergelyOrosz]] reports on [[Atlassian]]'s April 2022 cloud outage, in which a deprecation script run with the wrong mode and tenant identifiers permanently deleted data for about 400 customers and disrupted Jira, Confluence, Opsgenie, and related services for as long as nine days. The account links the duration to missing selective-restore tooling and treats Atlassian's delayed, repetitive, and technically vague customer communication as a second failure alongside the destructive change. The source Markdown contains no effective image references.

## Key Claims
- The incident began on April 4, 2022 when an Insight-plugin deprecation script was run with both the wrong execution mode and the wrong list of tenant IDs, deleting customer data instead of marking it for later deletion.
- Atlassian reportedly retained recoverable data, but its restoration process could not safely recover hundreds of affected tenants without changing unaffected customers, turning a destructive command into a prolonged [[SystemReliability]] incident.
- [[ChangeSafety]] for destructive maintenance needs dry runs, validated target sets, reversible deletion states, bounded blast radius, and a tested restoration path at the same tenancy granularity as likely failures.
- [[IncidentCommunication]] failed for much of the outage: affected customers received repetitive status language, little direct technical context, and no executive acknowledgment until day nine.
- Jira Service Management created a support catch-22 for some customers because the channel used to report problems depended on the unavailable Atlassian service.
- Opsgenie customers faced a particularly consequential dependency failure, and three customers interviewed by the author said they moved incident management to PagerDuty.
- Migration cost made an immediate full-suite exit unlikely for many customers, but interviewees planned independent backups and the outage weakened trust in Atlassian's cloud-migration push.

## Key Quotes
> "The script was executed with the wrong execution mode and the wrong list of IDs." - Atlassian's root-cause explanation as reproduced by the article.

> "this incident and our response time are not up to our standard." - CTO Sri Viswanath's day-nine acknowledgment as reproduced by the article.

## Connections
- [[GergelyOrosz]] - author who combined Atlassian statements, public updates, and customer interviews into the incident account.
- [[Atlassian]] - cloud-software provider responsible for the destructive change, restoration, and customer response.
- [[SystemReliability]] - the outage shows that recoverable backups are insufficient without selective, practiced restoration.
- [[ChangeSafety]] - wrong execution parameters and permanent deletion bypassed reversible, bounded change controls.
- [[IncidentCommunication]] - delayed ownership and low-information updates compounded technical harm and customer uncertainty.
- [[ReliabilityInvestment]] - granular restoration tooling and independent recovery paths require work before an incident makes their absence visible.

## Contradictions
- No direct contradiction was found. The source strengthens the wiki's existing distinction between stopping a faulty change and restoring the state it already damaged.
- The article's estimate of 50,000 to 800,000 affected users is unusually broad, so the customer count is firmer than the end-user estimate.
- This is a second-party incident account based on public material and selected interviews rather than Atlassian's complete internal timeline; claims about leadership attention, customer intentions, and competitive effects should remain source-scoped.

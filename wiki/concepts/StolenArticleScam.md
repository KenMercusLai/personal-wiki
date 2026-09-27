---
title: "Stolen Article Scam"
type: concept
tags: [dmca, censorship, fraud, reputation-management]
sources:
  - data-from-the-lumen-database-highlights-how-companies-use-fake-websites-and-backdated-articles-to-censor-googles-search-results-blog-lumen
last_updated: 2026-09-27
knowledge_schema: synthesis-v1
---

## Definition
The [[StolenArticleScam]] is a form of [[DMCATakedownAbuse]] in which an actor copies an unwanted article onto a fake publication, backdates the copy so it appears older, and files a copyright notice claiming that the genuine article stole the manufactured “original.”

## Current Synthesis
The tactic exploits an evidence asymmetry: a visible timestamp is easy to fabricate, while the platform handling a removal request may not reconstruct domain ownership, hosting changes, archives, and the true publication sequence. The 2017 [[LumenDatabase]] study found 42 suspicious notices targeting 52 URLs and reports that Google approved 16 requests. Its worked Fox18 News example shows how WHOIS, name-server, IP, and archive evidence can reverse the displayed chronology, while repeated language and registration details can reveal possible coordination across nominal senders.

## Key Claims
- The attack manufactures apparent priority rather than merely denying authorship.
- Domain and archive chronology can be more probative than page-level display dates.
- Repeated notice language, punctuation, infrastructure, and registration details can expose coordinated campaigns.
- A low-cost false claim can impose a high verification burden on platforms and targeted publishers.
- Search delisting can create meaningful censorship even when the underlying page remains online.

## Evidence
- Mechanism and sample: [[data-from-the-lumen-database-highlights-how-companies-use-fake-websites-and-backdated-articles-to-censor-googles-search-results-blog-lumen]] identifies 42 suspicious notices aimed at 52 URLs and describes the copy-backdate-notice sequence.
- Chronology test: [[data-from-the-lumen-database-highlights-how-companies-use-fake-websites-and-backdated-articles-to-censor-googles-search-results-blog-lumen]] places Fox18News.com's relevant registration and infrastructure changes after the real New York Daily News article despite the fake article's earlier displayed date.
- Coordination signals: [[data-from-the-lumen-database-highlights-how-companies-use-fake-websites-and-backdated-articles-to-censor-googles-search-results-blog-lumen]] finds that 11 of 42 notices shared unusual punctuation and that multiple nominal publishers used the same Scottsdale registration location.
- Platform effect: [[data-from-the-lumen-database-highlights-how-companies-use-fake-websites-and-backdated-articles-to-censor-googles-search-results-blog-lumen]] reports 16 of 52 requested removals approved as of August 15, 2017.

## Counterevidence & Qualifications
The sample was purposively assembled from suspicious notices and is too small to estimate prevalence across all DMCA requests. A registration change, archive gap, writing quirk, or shared privacy-proxy address is not conclusive alone. The study does not establish that every client knew the method, that every notice was legally fraudulent, or that the 2017 approval rate persisted after platform-policy changes.

## What Changed
- Created the concept and separated its copy-backdate-notice mechanism from broader takedown abuse.
- Added domain-history and archive triangulation as the main way to test manufactured publication priority.
- Added search delisting as the harm, distinct from deletion of the underlying page.

## Related Concepts
- [[DMCATakedownAbuse]] - broader category of using copyright-removal procedures for unsupported suppression.
- [[LumenDatabase]] - transparency archive through which suspicious notice patterns can be discovered.
- [[Google]] - search intermediary whose removal decisions determine whether the tactic affects discovery.

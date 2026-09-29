---
title: "Personal CRM"
type: concept
tags: [relationships, contact-management, information-retrieval, spreadsheets]
sources:
  - i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[PersonalCRM]] is a personally maintained system for recording, retrieving, and acting on relationship context across friends, peers, advisers, and other contacts rather than managing a commercial sales pipeline.

## Current Synthesis
The source's spreadsheet implementation treats relationship maintenance as an information-retrieval problem. A contact record contains name and email plus up to ten descriptors drawn from four families: industry, job function, passions, and personal attributes. The resulting queries support finding expertise, sharing material with a relevant subset, and introducing people around common interests.

Consistency is the system's core design tradeoff. A controlled vocabulary and typeahead reduce duplicate spellings and make filter queries dependable, while a notes field captures details that do not yet justify a permanent tag. The vocabulary remains personal and domain-sensitive: categories can be detailed where the user has expertise and coarse elsewhere. This makes the system easier to build and adapt than a dedicated database, but also ties its quality to disciplined manual entry, category judgment, and maintenance.

## Key Claims
- A personal CRM can turn a growing contact list into a queryable aid for introductions, targeted sharing, and event coordination.
- Professional descriptors alone are insufficient for the intended relationship work; interests and personal traits provide additional matching context.
- Controlled tags improve retrieval consistency by limiting spelling variants and near-synonyms.
- A free-form field can serve as a staging area for attributes that are too specific or too new for the controlled vocabulary.
- Familiar spreadsheet validation, typeahead, formulas, and filters can support a useful single-user system without database programming.
- Recording more relationship data does not by itself establish deeper relationships or overcome cognitive, privacy, and maintenance limits.

## Evidence
- Use cases: [[i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads]] describes expertise searches, targeted article sharing, and interest-based event introductions.
- Data model: [[i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads]] and its retained taxonomy image organize tags into industry, function, passions, and traits.
- Retrieval mechanism: [[i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads]] and its screenshots show validated typeahead selection followed by a named filter view that returns matching rows.
- Vocabulary governance: [[i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads]] recommends coarse categories outside the user's domain, comments for ambiguous tags, delayed promotion of new tags, and free-form notes.
- Reported scale: [[i-couldnt-find-a-good-personal-crm-so-i-created-my-own-and-want-to-share-it-with-you-radreads]] says the author used the sheet multiple times daily with roughly 500 people.

## Counterevidence & Qualifications
This concept currently rests on one 2014 practitioner account and screenshots of a single private implementation. It supplies no independent usage data, longitudinal comparison, retrieval evaluation, or evidence that the system improves reciprocity, relationship quality, or social capacity. Manual trait labels can become stale, reductive, subjective, or sensitive; centralized names, email addresses, notes, interests, and attributes also create privacy and security obligations that the source does not discuss. Controlled tags reduce lexical inconsistency but cannot make overlapping social categories mutually exclusive. Spreadsheet convenience may deteriorate with multiple editors, more complex queries, reminders, mobile entry, automation, access control, or larger datasets.

## What Changed
- Created the concept from Khe Hy's controlled-tag Google Sheets implementation.
- Distinguished personal relationship retrieval from commercial pipeline management.
- Preserved manual maintenance, category judgment, privacy, and unmeasured relationship outcomes as central limits.

## Related Concepts
- [[EndUserComputing]] - a spreadsheet becomes a task-specific relationship application through validation, fields, and filters.
- [[DeliberateNetworkBuilding]] - a personal CRM supplies retrieval support for introductions and targeted relationship activity.
- [[NoCodeWorkflowAutomation]] - built-in spreadsheet behavior provides limited automation without a custom application.
- [[PersonalKnowledgeManagement]] - both practices externalize personally useful context, but this concept centers people and relationship actions.
- [[Homophily]] - matching people through shared attributes may enable connection while also reinforcing similarity-based selection.

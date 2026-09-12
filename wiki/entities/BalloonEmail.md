---
title: "Balloon Email"
type: entity
tags: [campaign-tech, email, fundraising, incident-response]
sources:
  - a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[BalloonEmail]] was the Hillary Clinton campaign's codename for an emergency email delivery application built after a vendor outage.

## Current Profile
The source frames [[BalloonEmail]] as one of the campaign technology team's biggest rapid-response wins. When a fundraising-critical vendor failed near an end-of-quarter FEC deadline, engineers worked with Digital email writers to build a minimum viable mass mailer in Python and AWS in about four hours. The tool sent more than 14 million emails in its first rough version and reportedly preserved more than $700,000 in donations.

## Key Characteristics
- Built in response to a vendor outage on a fundraising deadline.
- Joined engineers with Digital email writers for minimum viable scope.
- Used Python and AWS.
- Sent more than 14 million emails in its first hacked-together form.
- Reportedly saved over $700,000 in donations.

## Evidence
- Incident trigger: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] says a vendor product failed on an end-of-quarter fundraising deadline.
- Cross-functional build: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] describes engineers taking MVP guidance from Digital email writers.
- Implementation: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] says the team built the mass mailer in Python and AWS in about four hours.
- Impact: [[a-first-peek-behind-the-scenes-of-hillary-clintons-technology-operation]] reports more than 14 million emails sent and over $700,000 in donations saved.

## Qualifications
The source does not describe deliverability, compliance controls, later hardening, or how long [[BalloonEmail]] remained in production. The reported donation impact is campaign-internal and should be treated as source-scoped.

## What Changed
- Created the entity from the Clinton technology-operation source.

## Relationships
- [[HillaryClinton]] - campaign context for the tool.
- [[OfficialCampaignTechnology]] - example of staffed rapid-response infrastructure.
- [[StartupRunway]] - fundraising deadlines make infrastructure outages financially consequential.
- [[ChangeSafety]] - emergency software still needs later hardening after crisis deployment.

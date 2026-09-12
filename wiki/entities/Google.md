---
title: "Google"
type: entity
tags: [company, web, networking, startup]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
  - 16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more
  - 16-mobile-theses-benedict-evans
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Google]] appears in the wiki as a web-protocol actor, scaling-organization example, and mobile platform winner.

## Current Profile
Within the HTTP source, Google is represented as a web-platform actor whose experimental protocols and browser adoption helped shape HTTP's later performance evolution. The scaling source adds Google as an operating model for order-of-magnitude process change, small-team product creation, recruiting intensity, strong culture, and executive communication cadence. The mobile source adds a third profile: Google as the [[Android]] platform winner whose strategic need for reach is complicated by [[Apple]]'s control of [[IOS]] and by OEM attempts to shape non-Google Android experiences.

## Key Characteristics
- Developed SPDY, which the source frames as the basis or close precursor of [[HTTP2]].
- Developed [[QUIC]], which the source presents as the protocol basis for [[HTTP3]].
- Influenced adoption through Chrome support and by later aligning with standardized HTTP/2.
- Serves as a scaling example where processes break at each order of magnitude.
- Is used as an example of recruiting, small-team product development, and strong culture.
- Won mobile alongside [[Apple]] through [[Android]], but still faces reach and service-control constraints on iOS and within OEM-modified Android ecosystems.

## Evidence
- SPDY influence: [[chen-hao-http-de-qian-shi-jin-sheng]] says Google's 2010 SPDY experiment became the basis for [[HTTP2]].
- QUIC influence: [[chen-hao-http-de-qian-shi-jin-sheng]] describes [[QUIC]] as a Google protocol that entered the standardization path for [[HTTP3]].
- Browser adoption: [[chen-hao-http-de-qian-shi-jin-sheng]] notes Chrome support for HTTP/3 and Google's removal of SPDY support after HTTP/2 standardization.
- Congestion control: [[chen-hao-http-de-qian-shi-jin-sheng]] connects QUIC's congestion-control path with CUBIC and BBR.
- Process scaling: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] cites [[MarissaMayer]] relaying [[EricSchmidt]]'s warning that processes break at 1, 10, 100, and 1,000 scale.
- Operating cadence: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] describes Google's weekly staff meetings, strategy reviews, one-on-ones, and full-company meetings.
- Small teams and recruiting: [[16-lessons-on-scaling-from-eric-schmidt-reid-hoffman-marissa-mayer-brian-chesky-diane-greene-jeff-weiner-and-more]] cites [[EricSchmidt]] on great products starting with tiny teams and on recruiting as a major operating priority.
- Mobile platform reach: [[16-mobile-theses-benedict-evans]] argues that Google won mobile through Android's larger user base, but that Google's existential need for reach is constrained on iOS by what Apple allows.
- Android complexity: [[16-mobile-theses-benedict-evans]] says Android forks struggle without Google services, while OEM experiences such as Xiaomi-like Android customization still complicate a purely Google-controlled Android story.

## Qualifications
The HTTP source does not evaluate Google's broader standards strategy or the full history of SPDY, QUIC, Chrome, or BBR. The scaling source is a course-note synthesis and does not independently assess Google's culture, hiring outcomes, or management tradeoffs. The mobile source is a 2015 strategy snapshot and does not cover later Android, AI, search, assistant, antitrust, or hardware developments.

## What Changed
- Added Google as a mobile platform winner whose reach depends on Android scale, iOS access, and OEM ecosystem control.

## Relationships
- [[HTTP2]] - Google's SPDY is presented as HTTP/2's experimental precursor.
- [[HTTP3]] - Google's QUIC is presented as the transport basis for HTTP/3.
- [[QUIC]] - Google is associated with QUIC's origin and evolution.
- [[HeadOfLineBlocking]] - QUIC is discussed as a response to transport-level blocking in multiplexed HTTP.
- [[EricSchmidt]] - Google operator whose scaling advice appears in the source.
- [[MarissaMayer]] - Google and Yahoo operator who relays Google process and cadence lessons.
- [[StartupScaling]] - Google supplies order-of-magnitude process evidence.
- [[ScalingCommunication]] - Google's weekly operating cadence is a communication example.
- [[Android]] - Google's main mobile operating-system ecosystem.
- [[Apple]] - co-winner and strategic counterparty in mobile.
- [[MobilePlatformDiscovery]] - Google's search and Android reach are tied to mobile discovery control.

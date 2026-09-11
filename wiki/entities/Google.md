---
title: "Google"
type: entity
tags: [company, web, networking]
sources:
  - chen-hao-http-de-qian-shi-jin-sheng
last_updated: 2026-09-11
knowledge_schema: synthesis-v1
---

## Overview
[[Google]] appears in the HTTP history source as a major contributor to web-protocol experimentation that influenced [[HTTP2]] and [[HTTP3]].

## Current Profile
Within this wiki, Google is represented as a web-platform actor whose experimental protocols and browser adoption helped shape HTTP's later performance evolution. The article treats SPDY as the basis for HTTP/2 and QUIC as the transport foundation that entered the HTTP/3 standardization path.

## Key Characteristics
- Developed SPDY, which the source frames as the basis or close precursor of [[HTTP2]].
- Developed [[QUIC]], which the source presents as the protocol basis for [[HTTP3]].
- Influenced adoption through Chrome support and by later aligning with standardized HTTP/2.
- Is associated with newer congestion-control ideas through the article's discussion of BBR.

## Evidence
- SPDY influence: [[chen-hao-http-de-qian-shi-jin-sheng]] says Google's 2010 SPDY experiment became the basis for [[HTTP2]].
- QUIC influence: [[chen-hao-http-de-qian-shi-jin-sheng]] describes [[QUIC]] as a Google protocol that entered the standardization path for [[HTTP3]].
- Browser adoption: [[chen-hao-http-de-qian-shi-jin-sheng]] notes Chrome support for HTTP/3 and Google's removal of SPDY support after HTTP/2 standardization.
- Congestion control: [[chen-hao-http-de-qian-shi-jin-sheng]] connects QUIC's congestion-control path with CUBIC and BBR.

## Qualifications
This profile is limited to Google's role in the article's HTTP narrative. It does not evaluate Google's broader standards strategy or the full history of SPDY, QUIC, Chrome, or BBR.

## What Changed
- Created an entity profile for Google as a protocol-experimentation actor in HTTP/2 and HTTP/3 history.

## Relationships
- [[HTTP2]] - Google's SPDY is presented as HTTP/2's experimental precursor.
- [[HTTP3]] - Google's QUIC is presented as the transport basis for HTTP/3.
- [[QUIC]] - Google is associated with QUIC's origin and evolution.
- [[HeadOfLineBlocking]] - QUIC is discussed as a response to transport-level blocking in multiplexed HTTP.

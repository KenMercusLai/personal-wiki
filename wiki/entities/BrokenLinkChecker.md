---
title: "broken-link-checker"
type: entity
tags: [link-checker, crawler, nodejs, open-source]
sources:
  - link-checkers-recurse
last_updated: 2026-10-17
knowledge_schema: synthesis-v1
---

## Overview
[[BrokenLinkChecker]] is an event-driven JavaScript link checker whose site crawler composes nested site-level and page-level request queues.

## Current Profile
The project, called BLC in the source, marks a page in its URL cache before handing it to the page checker. Discovered links become pages only after tag and attribute support, broken and internal status, visited identity, include policy, and robots permission are evaluated.

Completion propagates as an event cascade: the page queue drains and ends the current site, its callback releases the site-queue slot, and draining the site queue emits public completion. Socket caps and rate limits are first-class, but recursion and termination behavior are distributed across multiple handlers and queues.

## Key Characteristics
- Claims each page in a URL cache before crawling it.
- Uses nested queues for sites and pages.
- Filters recursive admission through link type, internality, visited state, inclusion policy, and robots rules.
- Controls request concurrency and pacing through socket and rate limits.
- Detects completion through page-queue and site-queue drain events.
- Uses an event-driven control flow whose recursion state spans several handlers.

## Evidence
- Admission and policy: [[link-checkers-recurse]] traces page marking and the recursive filter over attributes, health, scope, cache, policy, and robots permission.
- Completion: [[link-checkers-recurse]] explains how the page queue's end event releases the current site and how site-queue drain signals final completion.
- Politeness: [[link-checkers-recurse]] describes robots support, `nofollow`, rate limiting, and maximum sockets as first-class controls.
- Tradeoffs: [[link-checkers-recurse]] characterizes the event cascade as harder to trace and notes single-thread and in-memory-cache limits.

## Qualifications
The profile comes from an external code reading and may not reflect later revisions. The source calls BLC widely used and server-friendly but supplies no comparative adoption, compliance, throughput, fairness, or crawl-completeness measurements. Respecting protocol and link-policy signals does not by itself cover all legal or operational obligations of crawling.

## What Changed
- Created the project profile from the comparative recursion teardown.
- Recorded its nested-queue completion cascade and policy-aware admission path.

## Relationships
- [[CrawlerArchitecture]] - separates page admission, crawl policy, nested execution queues, and drain-based completion.
- [[DistributedTerminationDetection]] - propagates quiescence through page and site queue-drain events.
- [[AdaptiveBackpressure]] - combines socket caps and explicit rate limits with recursive queueing.
- [[ConcurrencyFailureModes]] - illustrates the reasoning cost of completion logic distributed across event handlers.

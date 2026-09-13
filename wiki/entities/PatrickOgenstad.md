---
title: "Patrick Ogenstad"
type: entity
tags: [networking, automation, author]
sources:
  - ansible-vs-nornir-speed-challenge
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[PatrickOgenstad]] is the author of "Ansible vs. Nornir: Speed Challenge," where he compares the local processing cost of [[Ansible]] and [[Nornir]] for network-automation templating work.

## Current Profile
In this source, Ogenstad writes from practitioner experience with network data collection. He describes an earlier IOS XR data-collection job where an Ansible playbook scheduled every five minutes could not finish within that interval, then uses a controlled templating benchmark to illustrate why tool choice matters when inventories or device outputs become large.

## Key Characteristics
- Writes as a network-automation practitioner rather than as a vendor launch reporter.
- Uses benchmark data to clarify an often vague claim about Nornir being faster than Ansible.
- Frames speed as context-dependent, not as a universal reason to abandon Ansible.
- Connects tool choice to operational cadence, especially scheduled jobs that must finish inside a fixed interval.

## Evidence
- Practitioner context: [[ansible-vs-nornir-speed-challenge]] recounts Ogenstad using Ansible for many network problems before hitting a five-minute ceiling on IOS XR data collection.
- Benchmark method: [[ansible-vs-nornir-speed-challenge]] describes generated inventories, simple Jinja templates, a DigitalOcean dedicated-CPU droplet, and measured runs across four host counts.
- Context-dependent judgment: [[ansible-vs-nornir-speed-challenge]] says speed is not his main argument for Nornir and that many Ansible scenarios are unaffected by the benchmark.
- Tool-fit framing: [[ansible-vs-nornir-speed-challenge]] quotes Kelsey Hightower on understanding when a tool should not be used.

## Qualifications
This page reflects Ogenstad only through this single 2019 article. It does not summarize his broader work, projects, or later views on Ansible, Nornir, or network automation.

## What Changed
- Created the entity page for Ogenstad as the author of the Ansible-versus-Nornir benchmark.

## Relationships
- [[Ansible]] - Ogenstad benchmarks Ansible and recounts a practical ceiling in an earlier data-collection workflow.
- [[Nornir]] - Ogenstad presents Nornir as the faster benchmarked alternative.
- [[NetworkAutomation]] - Ogenstad's article contributes a tool-fit and performance perspective to network automation.

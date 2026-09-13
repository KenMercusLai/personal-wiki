---
title: "Nornir"
type: entity
tags: [networking, automation, python]
sources:
  - ansible-vs-nornir-speed-challenge
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[Nornir]] is presented as a Python network-automation framework that can run host-oriented tasks with much lower overhead than [[Ansible]] for the benchmarked local templating workload.

## Current Profile
In [[PatrickOgenstad]]'s benchmark, Nornir is used to render Jinja templates and write one generated configuration file per host. The test deliberately avoids network I/O, so the result isolates local inventory, task, template, and file-writing overhead rather than device latency. Nornir completes 100, 1,000, 5,000, and 10,000 host runs in 0.621, 2.005, 8.906, and 17.217 seconds respectively, which the author interprets as roughly linear scaling.

## Key Characteristics
- Operates as a Python-driven network-automation framework in the source's example.
- Uses host inventory data directly in templating tasks.
- Shows low local processing overhead in the benchmark.
- Scales approximately linearly across the tested inventory sizes.
- Is framed as especially relevant when network automation involves many hosts or large volumes of device data.

## Evidence
- Python framework role: [[ansible-vs-nornir-speed-challenge]] shows `InitNornir`, per-host template rendering, and file writing in Python code.
- Benchmark runtimes: [[ansible-vs-nornir-speed-challenge]] reports 0.621 seconds for 100 hosts, 2.005 seconds for 1,000 hosts, 8.906 seconds for 5,000 hosts, and 17.217 seconds for 10,000 hosts.
- Scaling pattern: [[ansible-vs-nornir-speed-challenge]] says Nornir more or less doubles in time when the number of hosts doubles.
- Chart evidence: [[ansible-vs-nornir-speed-challenge]] includes a Nornir-only chart where the bars rise from under one second at 100 hosts to roughly 17 seconds at 10,000 hosts.
- Tool-fit framing: [[ansible-vs-nornir-speed-challenge]] uses the comparison to show why some data-heavy network workflows are better handled outside Ansible.

## Qualifications
The source is a practitioner benchmark from 2019 using Nornir 2.3.0, Python 3.7.3, Debian 10, and a two-CPU DigitalOcean droplet. It tests local template generation and file output, not live device configuration, authentication, network latency, later Nornir releases, or a broad range of automation tasks.

## What Changed
- Created the entity page for Nornir as a Python network-automation framework contrasted with Ansible on high-volume local processing overhead.

## Relationships
- [[Ansible]] - Nornir is benchmarked against Ansible as the faster option for the tested workload.
- [[NetworkAutomation]] - Nornir is one tool option within network automation practice.
- [[PatrickOgenstad]] - Ogenstad authored the benchmark source.

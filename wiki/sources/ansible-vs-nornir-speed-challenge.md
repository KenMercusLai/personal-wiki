---
title: "Ansible vs. Nornir: Speed Challenge"
type: source
tags: [networking, automation, benchmarks]
date: 2019-11-05
source_file: /mnt/ken_personal_wiki/Articles/Ansible vs. Nornir Speed Challenge.md
---

## Summary
[[PatrickOgenstad]] compares [[Ansible]] and [[Nornir]] on a network-automation templating workload, arguing that speed differences become material when inventories or collected device data get large. The benchmark shows [[Nornir]] completing local template generation for 10,000 hosts in 17.217 seconds while [[Ansible]] takes 41 minutes 22.106 seconds, and the inspected charts reinforce the scale difference by making Nornir nearly invisible beside Ansible at the shared axis.

## Key Claims
- [[Ansible]] can be the wrong tool for high-volume data collection or processing-heavy network workflows even when it is useful for many configuration tasks.
- [[Nornir]] scales much more predictably on the benchmarked local template-generation workload, roughly doubling runtime when the host count doubles.
- [[Ansible]]'s runtime grows more than linearly in the benchmark, which the author attributes to JSON serialization and deserialization between tasks and inside Ansible core.
- Tool fit matters more than raw speed alone: some Ansible scenarios are unaffected by these numbers, while data-heavy scheduled jobs can hit practical ceilings.
- The chart comparing both tools shows Ansible dominating the y-axis so strongly that Nornir's bars are barely visible; the Nornir-only chart shows its own growth from under a second at 100 hosts to about 17 seconds at 10,000 hosts.

## Key Quotes
> "You haven't mastered a tool until you understand when it should not be used." - quoted from [[KelseyHightower]] as the article's framing principle.

> "After the first run, it all fell apart as it turned out that the playbook wasn't able to finish within five minutes." - [[PatrickOgenstad]] on an earlier Ansible-based data-collection job.

## Connections
- [[PatrickOgenstad]] - author of the benchmark and practitioner story.
- [[Ansible]] - compared as the slower tool in the high-volume templating and data-processing examples.
- [[Nornir]] - compared as the faster Python network-automation framework in the benchmark.
- [[NetworkAutomation]] - central domain where tool choice, data volume, and inventory size shape practicality.
- [[KelseyHightower]] - supplies the article's tool-fit quote.
- [[DigitalOcean]] - hosted the dedicated-CPU benchmark environment.

## Contradictions
- None identified. The source qualifies rather than contradicts the existing [[Ansible]] material: Ansible can be valuable for network automation while still being a poor fit for some high-volume data and templating workloads.

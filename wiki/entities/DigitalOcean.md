---
title: "DigitalOcean"
type: entity
tags: [cloud, infrastructure]
sources:
  - ansible-vs-nornir-speed-challenge
last_updated: 2026-09-13
knowledge_schema: synthesis-v1
---

## Overview
[[DigitalOcean]] is the cloud provider used by [[PatrickOgenstad]] to run the dedicated-CPU benchmark environment for the Ansible-versus-Nornir speed comparison.

## Current Profile
In this source, DigitalOcean appears only as benchmark infrastructure. Ogenstad uses a General Purpose Droplet with 8 GB of RAM, two dedicated CPUs, Debian 10, Python 3.7.3, Ansible 2.9.0, and Nornir 2.3.0 to make the timing comparison less dependent on his laptop's competing processes.

## Key Characteristics
- Provides the benchmark host environment in the source.
- Is represented by a General Purpose Droplet with dedicated CPUs.
- Serves as infrastructure context rather than as the subject of the article.

## Evidence
- Benchmark environment: [[ansible-vs-nornir-speed-challenge]] says the tests ran on a DigitalOcean General Purpose Droplet.
- Hardware and software context: [[ansible-vs-nornir-speed-challenge]] specifies 8 GB RAM, two CPUs, Debian 10, Python 3.7.3, Ansible 2.9.0, and Nornir 2.3.0.
- Reproducibility role: [[ansible-vs-nornir-speed-challenge]] uses the droplet to make the comparison fairer than laptop runs affected by unrelated local processes.

## Qualifications
This page reflects DigitalOcean only as the environment for one benchmark. It does not summarize DigitalOcean's broader cloud product line, pricing, reliability, or business strategy.

## What Changed
- Created the entity page for DigitalOcean as benchmark infrastructure context.

## Relationships
- [[PatrickOgenstad]] - Ogenstad used DigitalOcean for the benchmark environment.
- [[Ansible]] - Ansible was one of the benchmarked tools running on the DigitalOcean droplet.
- [[Nornir]] - Nornir was the other benchmarked tool running on the DigitalOcean droplet.

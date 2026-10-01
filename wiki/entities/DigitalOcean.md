---
title: "DigitalOcean"
type: entity
tags: [cloud, infrastructure]
sources:
  - ansible-vs-nornir-speed-challenge
  - pierce-freeman-go-ahead-self-host-postgres
last_updated: 2026-10-01
knowledge_schema: synthesis-v1
---

## Overview
[[DigitalOcean]] is represented as the provider for both [[PatrickOgenstad]]'s dedicated-CPU automation benchmark and [[PierceFreeman]]'s self-hosted PostgreSQL server.

## Current Profile
Ogenstad uses a General Purpose Droplet with 8 GB of RAM, two dedicated CPUs, Debian 10, Python 3.7.3, Ansible 2.9.0, and Nornir 2.3.0 to make the timing comparison less dependent on his laptop's competing processes. Freeman reports using a 16-vCPU, 32-GB-memory, 400-GB-disk DigitalOcean server as the destination for a PostgreSQL migration from RDS, followed by several weeks of performance observation before production cutover.

## Key Characteristics
- Provides the benchmark host environment in the source.
- Is represented by a General Purpose Droplet with dedicated CPUs.
- Provides the dedicated-server context for a self-hosted PostgreSQL case.
- Serves as infrastructure context rather than as the subject of either article.

## Evidence
- Benchmark environment: [[ansible-vs-nornir-speed-challenge]] says the tests ran on a DigitalOcean General Purpose Droplet.
- Hardware and software context: [[ansible-vs-nornir-speed-challenge]] specifies 8 GB RAM, two CPUs, Debian 10, Python 3.7.3, Ansible 2.9.0, and Nornir 2.3.0.
- Reproducibility role: [[ansible-vs-nornir-speed-challenge]] uses the droplet to make the comparison fairer than laptop runs affected by unrelated local processes.
- Database host: [[pierce-freeman-go-ahead-self-host-postgres]] names DigitalOcean as the provider of a 16-vCPU, 32-GB-memory, 400-GB-disk server used for self-hosted PostgreSQL.
- Migration context: [[pierce-freeman-go-ahead-self-host-postgres]] reports about four hours of hands-on migration work followed by several weeks of observation before live cutover.

## Qualifications
This page reflects DigitalOcean only as infrastructure in two practitioner accounts. It does not independently evaluate DigitalOcean's broader product line, current pricing, database suitability, reliability, support, or business strategy.

## What Changed
- Created the entity page for DigitalOcean as benchmark infrastructure context.
- Added its role as the dedicated-server provider in Freeman's self-hosted PostgreSQL case.

## Relationships
- [[PatrickOgenstad]] - Ogenstad used DigitalOcean for the benchmark environment.
- [[Ansible]] - Ansible was one of the benchmarked tools running on the DigitalOcean droplet.
- [[Nornir]] - Nornir was the other benchmarked tool running on the DigitalOcean droplet.
- [[PierceFreeman]] - Freeman reports hosting his PostgreSQL server on DigitalOcean.
- [[PostgreSQL]] - database operated on the reported dedicated server.
- [[SelfHostedDatabaseOperations]] - operating model for which the server supplies infrastructure.

---
title: "DeployBeta"
type: entity
tags: [side-project, deployment, open-source]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[DeployBeta]] is Wang Ziting's side project used in the retrospective as a negative example of a technically substantial project that remained unreleased too long.

## Current Profile
The project reached a v0.4 phase and was open-sourced before that release, with later work adding MySQL, Redis, and MongoDB support plus a rewritten Etcd-backed ORM. Its main significance in the source is process-oriented: the project continued for about two years without reaching an externally releasable standard, illustrating how delayed release can drain feedback and motivation.

## Key Characteristics
- Became the counterexample for unfocused, delayed side-project release.
- Added database support for MySQL, Redis, and MongoDB.
- Included an Etcd-backed ORM that stored JSON and wrapped simple relationships and transactions.
- Exposed Go limitations around arrays of interfaces or generic-like result arrays before the author's preferred abstraction was easy.

## Evidence
- Release-process problem: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says DeployBeta lasted two years but still did not meet an external release standard.
- Database support: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says v4 and later unreleased versions supported MySQL, Redis, and MongoDB.
- ORM design: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] describes a JSON-in-Etcd ORM with simple relationship and transaction wrappers.
- Go pain point: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the ORM had to use `interface{}` and reflection to fetch result arrays.

## Qualifications
The source does not describe DeployBeta's user base, exact product purpose, or later status. Its main role in the wiki is as evidence for release-focused side-project discipline.

## What Changed
- Created the DeployBeta entity page from the retrospective.

## Relationships
- [[WangZiting]] - creator and retrospective author.
- [[ReleaseFocusedSideProjects]] - DeployBeta is the negative example for this concept.
- [[Redis]] - one of the supported databases in later work.
- [[Etcd]] - storage layer behind the project's ORM.

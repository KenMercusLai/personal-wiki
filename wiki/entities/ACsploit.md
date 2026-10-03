---
title: "ACsploit"
type: entity
tags: [open-source, security-testing, algorithms, denial-of-service]
sources:
  - denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities
last_updated: 2026-10-03
knowledge_schema: synthesis-v1
---

## Overview
[[ACsploit]] is an open-source security-testing project presented as a generator of worst-case inputs for common algorithms and a tool for identifying regular-expression denial-of-service risks.

## Current Profile
ACsploit operationalizes the talk's argument that exposed algorithms should be tested against deliberately pathological rather than merely representative data. Its role is generative: construct inputs expected to exercise worst-case behavior so researchers, penetration testers, and developers can observe disproportionate resource consumption before an attacker does.

## Key Characteristics
- Generates worst-case inputs for common algorithm classes.
- Includes regular-expression denial-of-service identification in the presented scope.
- Supports adversarial complexity testing rather than ordinary functional correctness alone.
- Is presented as an open-source bridge between algorithm analysis and practical security testing.

## Evidence
- Stated purpose: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] describes ACsploit as generating worst-case inputs for common algorithms.
- Security scope: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] explicitly includes ReDoS identification.
- Intended users: [[denial-of-service-with-a-fistful-of-packets-exploiting-algorithmic-complexity-vulnerabilities]] asks penetration testers, developers, and researchers to incorporate algorithmic-complexity analysis into their work.

## Qualifications
The source provides a repository link and brief capability statements, not a versioned feature inventory, supported-algorithm list, evaluation, false-positive analysis, or evidence of adoption. This profile therefore describes the project as presented and makes no claim about its current maintenance or capabilities.

## What Changed
- Created a source-bounded project profile from the presentation's tooling section.

## Relationships
- [[AlgorithmicComplexityVulnerabilities]] - are the security weaknesses ACsploit is intended to help expose.
- [[NathanHauke]] - co-presented the research and tool context.
- [[DavidRenardy]] - co-presented the research and tool context.
- [[ChaosEngineering]] - shares deliberate adverse testing, but ACsploit focuses on crafted computational inputs.

---
title: "Marc Brooker"
type: entity
tags: [author, aws, distributed-systems]
sources:
  - seven-years-of-firecracker-marcs-blog
last_updated: 2026-10-07
knowledge_schema: synthesis-v1
---

## Overview
[[MarcBrooker]] is an AWS practitioner-author represented here through an explanation of Firecracker's use in agent runtime and serverless database systems.

## Current Profile
Brooker presents production infrastructure through concrete isolation, initialization, memory-sharing, and cleanup mechanisms. His account connects [[Firecracker]] to [[AmazonBedrockAgentCore]] and [[AuroraDSQL]], then draws a broader architectural lesson: system-level placement of state and lifetime bounds can make individual workers substantially simpler.

## Key Characteristics
- Writes from a first-party AWS systems perspective.
- Explains virtualization in terms of security, resource economics, and lifecycle design.
- Connects implementation mechanisms to wider system boundaries.

## Evidence
- Firecracker history: [[seven-years-of-firecracker-marcs-blog]] recounts Firecracker's 2018 release and subsequent AWS and open-source adoption.
- Agent runtime: [[seven-years-of-firecracker-marcs-blog]] explains AgentCore's per-session microVM model.
- Database runtime: [[seven-years-of-firecracker-marcs-blog]] explains DSQL query-processor cloning, page sharing, and age-based reclamation.

## Qualifications
This profile is limited to one self-authored technical article. It does not establish Brooker's full role, publication record, responsibility for the systems discussed, or an independent evaluation of the reported mechanisms.

## What Changed
- Created the entity page for the article's author.

## Relationships
- [[Firecracker]] - central technology in Brooker's seven-year retrospective.
- [[AmazonBedrockAgentCore]] - agent runtime example he explains.
- [[AuroraDSQL]] - database example he explains.
- [[AWS]] - organizational context for the described systems.

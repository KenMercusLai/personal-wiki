---
title: "Redis"
type: entity
tags: [database, cache, server-side, task-queue]
sources:
  - 2018-nian-du-xiao-jie-ji-shu-fang-mian
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[Redis]] is the server-side data system Wang Ziting used heavily for a cloud-engine task queue and praised for finding a narrow, simple, useful product position.

## Current Profile
The source presents Redis as both an implementation substrate and a design example. Operationally, it stores task-queue state, provides consistency guarantees, and supports Lua-scripted atomic operations. Conceptually, Wang Ziting treats Redis as one of the best server-side systems he has used because it chose a strong entry point and a clear position, making its design feel simple.

## Key Characteristics
- Stores queue state and coordination data for server-side task scheduling.
- Supports atomic multi-step operations through Lua scripts.
- Helps Node.js workers recover or coordinate asynchronous task execution.
- Serves as an example of narrow product positioning producing a simple-feeling design.
- Redis 5 Streams are identified as a promising basis for open-source task-queue projects.

## Evidence
- Queue substrate: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says all task-queue state was stored in Redis with consistency guarantees.
- Atomicity: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Lua scripts implemented atomic operations for the task queue.
- Node.js context: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says the author used Node.js workers and Redis-maintained critical state to avoid single points and recover interrupted tasks.
- Product-positioning praise: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] says Redis found a good entry point and position, which made its design look simple.
- Streams direction: [[2018-nian-du-xiao-jie-ji-shu-fang-mian]] interprets Redis 5 Streams as well-suited to task queues.

## Qualifications
The source is a practitioner's design reflection, not a benchmark or complete Redis evaluation. It emphasizes one task-queue use case and the author's subjective judgment of Redis's design.

## What Changed
- Created the Redis entity page from the task-queue implementation discussion.

## Relationships
- [[TaskQueueDesign]] - Redis is the queue state and atomicity substrate.
- [[NodeJS]] - Node.js workers use Redis-managed state in the author's implementation.
- [[LeanCloud]] - platform context where the task queue was implemented.
- [[DatabaseServiceExposure]] - separate security concept where Redis appears as a sensitive exposed data service.

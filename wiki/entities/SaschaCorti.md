---
title: "Sascha Corti"
type: entity
tags: [author, knowledge-management, developer-tools]
sources:
  - corti-ai-powered-knowledge-management-obsidian-claude-code
last_updated: 2026-09-23
knowledge_schema: synthesis-v1
---

## Overview
[[SaschaCorti]] is the author of a technical article proposing an AI-assisted, CI/CD-managed [[Obsidian]] knowledge vault.

## Current Profile
Corti presents personal knowledge management as an operational software problem: a growing Markdown vault accumulates maintenance overhead, content drift, and discovery friction, so it can be governed through versioned scripts, automated tests, graph generation, export pipelines, backups, and scheduled health checks. [[ClaudeCode]] is positioned as the agent layer for bounded semantic tasks such as summarization, tagging, connection suggestions, vault analysis, and project compilation.

## Key Characteristics
- Frames a Markdown knowledge vault as a versioned software project.
- Combines [[Obsidian]], [[ClaudeCode]], Node.js tooling, and CI/CD in one proposed architecture.
- Treats validation, export, backup, and graph generation as repeatable operational workflows.
- Advocates AI assistance for semantic maintenance while retaining deterministic checks for structure and links.

## Evidence
- Knowledge-as-code framing: [[corti-ai-powered-knowledge-management-obsidian-claude-code]] proposes package scripts, project instructions, tests, and CI/CD for a Markdown vault.
- Agent role: [[corti-ai-powered-knowledge-management-obsidian-claude-code]] assigns Claude Code bounded summarization, tagging, linking, analysis, and compilation tasks.
- Operational scope: [[corti-ai-powered-knowledge-management-obsidian-claude-code]] includes graph generation, multi-format export, scheduled health checks, backups, batching, retries, and deployment.

## Qualifications
The profile is based on one prescriptive article. The source provides illustrative configuration and code, not production measurements, a maintained reference implementation, or evidence that the full architecture improves knowledge quality relative to a smaller workflow.

## What Changed
- Created the author profile and captured Corti's knowledge-as-code architecture.

## Relationships
- [[KnowledgeAsCode]] - Corti's article is the defining source for the concept in this wiki.
- [[Obsidian]] - supplies the Markdown vault and note interface in the proposed system.
- [[ClaudeCode]] - supplies the proposed AI maintenance and analysis layer.
- [[PersonalKnowledgeManagement]] - is the problem domain the architecture is intended to support.

---
title: "mihomo-rust"
type: entity
tags: [software-engineering, rust, networking, proxy]
sources:
  - yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua
last_updated: 2026-09-12
knowledge_schema: synthesis-v1
---

## Overview
[[MihomoRust]] is the Rust port of the Go-based mihomo/Clash Meta proxy core described in the Claude Code Agent Team case study.

## Current Profile
The source presents mihomo-rust as a substantial Rust workspace created to reduce binary size and memory use while benefiting from Rust's type system for network protocol implementation. The M1-stage project contained 11 workspace crates, more than 31,000 Rust lines, 40 technical specs, two ADRs, and a CI pipeline with unit, integration, and Dockerized TProxy end-to-end tests.

## Key Characteristics
- Ports a Go rule-proxy core supporting protocols such as Shadowsocks, Trojan, and VLESS into Rust.
- Uses an 11-crate workspace with `mihomo-proxy`, `mihomo-transport`, `mihomo-config`, and related crates.
- Separates reusable transport concerns such as TLS, WebSocket, gRPC, HTTP/2, and HTTPUpgrade.
- Documents architecture through specs, ADRs, roadmaps, and test plans.
- Treats upstream behavioral divergence as an explicit policy decision rather than accidental incompatibility.
- Uses layered verification across unit, async, integration, E2E, and CI checks.

## Evidence
- Project scope: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] reports 31,178 Rust LOC, 117 source files, 11 crates, 40 specs, 2 ADRs, 619 tests, and 24 integration suites.
- Architecture: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] describes `mihomo-transport` as an independent leaf crate with a `Transport` trait and runtime-composable transport-layer chains.
- Divergence policy: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] uses ADR-0002 to classify upstream differences as hard errors or warning-compatible behavior.
- Verification: [[yong-claude-code-jiang-san-wan-hang-go-xiang-mu-yi-zhi-dao-rust-agent-team-shi-jian-yu-harness-xiao-lu-you-hua]] lists unit tests, API integration tests, rule tests, protocol integration tests, TProxy E2E tests, and MSRV checks.

## Qualifications
The page reflects the source's reported M1-era state, not a current audit of the GitHub repository. Later project status, crate counts, or test counts may differ.

## What Changed
- Created the project profile for mihomo-rust as the concrete case behind the Agent Team and harness workflow.

## Relationships
- [[MaxLv]] - author/site associated with the project case study.
- [[ClaudeCode]] - coding-agent environment used during the port.
- [[AgentTeam]] - role structure used to manage the port.
- [[SpecDrivenAgentDevelopment]] - document workflow used to coordinate implementation.
- [[UpstreamDivergencePolicy]] - policy used to decide compatibility differences from the Go upstream.
- [[SoftwareVerification]] - verification stack used to validate agent output.

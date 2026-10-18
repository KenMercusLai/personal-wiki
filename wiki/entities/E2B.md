---
title: "E2B"
type: entity
tags: [ai, agents, sandboxing, code-execution]
sources:
  - wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong
  - unikernel-agent
last_updated: 2026-10-18
knowledge_schema: synthesis-v1
---

## Overview
[[E2B]] is an agent code-execution sandbox discussed in the source as valuable but insufficient for capability isolation and side-effect recovery.

## Current Profile
The sources place E2B at two complementary layers. One recognizes its value for isolated code execution while separating that from control of external credentials and recoverable side effects. The other describes an implementation path in which Dockerfile-like inputs become ext4-rooted Firecracker templates, the guest is prepared across multiple boots, and the initialized filesystem plus running processes are snapshotted for later loading.

The newer account also describes E2B's sandbox orchestrator as using a best-of-k placement heuristic over sampled nodes, while Nomad manages the control plane rather than individual sandbox placement. This favors a lightweight scheduler for short-lived, high-concurrency environments, but the account is based on practitioner code reading rather than an E2B-authored architecture contract or measured comparison.

## Key Characteristics
- Provides a sandbox for agent code execution.
- Helps isolate code-running environments.
- Does not remove risk from external credentials held by the agent.
- Does not automatically supply effect logs, idempotent replay, or irreversible-action recovery.
- Builds prepared Firecracker templates from Docker-derived filesystems and can preserve initialized process state in snapshots.
- Uses a lightweight best-of-k sandbox placement policy in the described implementation.

## Evidence
- Sandbox role: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] describes E2B as explicitly positioned around safe agent code execution.
- Credential limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says an agent in a clean sandbox can still use real API keys against external services.
- Recovery limit: [[wei-shen-me-xian-you-de-agent-infra-wu-fa-zhi-cheng-sheng-chan-ji-ying-yong]] says side-effect logging and replay semantics remain unsolved by code sandboxes.
- Template path: [[unikernel-agent]] describes image pulling, configuration injection, ext4 extraction, preparation boots, sandbox finalization, snapshot creation, and upload.
- Resume path: [[unikernel-agent]] quotes E2B documentation describing snapshots that retain the filesystem and running processes for later loading.
- Placement: [[unikernel-agent]] traces random sampling plus heuristic scoring for best-of-k node selection and distinguishes that path from Nomad's control-plane role.

## Qualifications
The semantic-infrastructure source does not evaluate E2B's implementation in depth. The implementation details come from a separate practitioner's code reading, not a controlled benchmark or security audit, and may change with the platform. The source gives no end-to-end distribution, startup, resume, density, failure, or cost measurements under a shared methodology. Snapshotting local process state still does not record, authorize, or reverse external effects.

## What Changed
- Added the Docker-derived Firecracker template preparation and snapshot path.
- Added the described best-of-k placement policy and Nomad boundary.
- Preserved the distinction between local resume and semantic recovery of external effects.

## Relationships
- [[SemanticIsolation]] - E2B is contrasted with semantic isolation.
- [[ComputerUse]] - agent code-execution sandboxes can support broader agent action workflows.
- [[CapabilityGateway]] - external capability mediation addresses risks outside the sandbox.
- [[Firecracker]] - supplies E2B's described microVM isolation and snapshot mechanism.
- [[AgenticSandboxInfrastructure]] - covers the image, scheduling, lifecycle, and policy system surrounding E2B sandboxes.

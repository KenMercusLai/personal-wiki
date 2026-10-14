---
title: "小议 agent Harness 设计上的 tradeoff"
type: source
tags: [ai, agents, harness, architecture, multi-tenancy, context-management]
date: 2026-09-05
source_file: "/mnt/ken_personal_wiki/Articles/小议 agent Harness 设计上的 tradeoff.md"
---

## Summary
This practitioner essay argues that the single-user, sandbox-resident harness inherited from coding agents fits operating-system-heavy local work but is a poor default for general workplace agents delivered through web and mobile clients. It proposes a multi-tenant [[ServerSideAgentArchitecture]] that separates session, tools, sandbox, and orchestration, invokes isolated execution only when needed, and may serve most file or scripting work through a lightweight JavaScript runtime before falling back to a microVM. The essay also qualifies clean modularity: because context compaction, notes, history, reminders, and model-specific behavior are still evolving together, aggressively decoupling session policy can slow experimentation, while production fidelity makes offline agent evaluation harder.

## Key Claims
- The original coding-agent harness assumes one process and one operating-system environment per user because coding, compilation, debugging, and deployment are tightly coupled to a workspace.
- General workplace agents have a stronger cloud-computer use case than coding agents: remote web or mobile access is valuable, while reproducing and bidirectionally synchronizing a developer's customized local environment often has weak returns.
- Treating every user session as a long-lived all-in-one container creates a stateful “pet”: harness faults, event-stream failures, and container outages become hard to distinguish, recover, and debug without exposing user data.
- [[ServerSideAgentArchitecture]] moves the agent loop into a multi-tenant service, separates session, tools, sandbox, and orchestration, and treats the sandbox as conditional execution rather than the agent's identity.
- Many filesystem and scripting tasks may run in a lightweight JavaScript runtime; only workloads that truly need Linux compatibility or stronger isolation need a full microVM.
- Session design is inseparable from [[LLMContextManagement]] while compaction, notes, history tools, and system-reminder mechanisms vary across model families and versions.
- A server-side harness complicates [[SoftwareVerification]] because offline evaluation must exercise the same multi-tenant harness as production and reproduce its tool environment across repeated runs.

## Key Quotes
> “Context 工程是 agent 唯一重要的事情” — on why session policy remains a rapidly changing core of the harness.

> “干净地把 session 和其他模块解耦……是在 agent 本身工程架构还在快速变化的阶段做的过度设计。” — on the cost of premature modular separation.

> “如果一个用户的请求并没有使用 `bash` 或者 `python` 这样的工具，那么这个请求就不需要 sandbox。” — on making isolated execution conditional.

## Connections
- [[ServerSideAgentArchitecture]] — central proposal for a shared agent service with explicit session, tool, sandbox, and orchestration boundaries.
- [[HarnessEngineering]] — expands harness design from coding workflow scaffolds into runtime placement, tenancy, context policy, and evaluation fidelity.
- [[AgentLifecycleModel]] — the session becomes durable multi-tenant state rather than incidental state inside one user's container.
- [[AgenticSandboxInfrastructure]] — sandboxing remains an execution option, but the source argues against making a full operating system mandatory for every request.
- [[LLMContextManagement]] — compaction, notes, history, reminders, memory, tools, and skills all compete to shape the agent's working state.
- [[SoftwareVerification]] — production-equivalent, repeatable offline evaluation becomes a first-class architecture requirement.
- [[Anthropic]] — its managed-agent engineering account supplies the “pet container” failure and debugging example cited by the essay.
- [[ClaudeCode]] — exemplifies the local single-user coding-agent harness inherited by later products.
- [[Codex]] — its experimental notes and history mechanisms illustrate model-delegated context management and migration complexity.
- [[Cloudflare]] — its `computer` project is cited as exploration of lighter execution primitives beneath a full Linux sandbox.

## Contradictions
- The source predicts that one-agent-per-sandbox designs outside coding “will be eliminated,” but offers an architecture argument rather than adoption, cost, reliability, or security measurements; strong tenant isolation, simple operations, or data-locality requirements may preserve that design for some products.
- The lightweight-runtime proposal is exploratory. JavaScript can cover many file and process tasks, but the source does not benchmark compatibility, isolation, startup cost, debugging, package support, or the operational threshold for microVM fallback.
- The essay favors separating the sandbox from the agent service while warning that separating session policy too cleanly is premature. This is a deliberate layer-specific tradeoff, not a general endorsement or rejection of modularity.
- Product examples and descriptions of experimental Codex behavior are point-in-time practitioner observations. No effective image references are present in the supplied Markdown, so no visual evidence or asset manifest was required.

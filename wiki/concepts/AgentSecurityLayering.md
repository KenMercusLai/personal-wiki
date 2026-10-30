---
title: "Agent Security Layering"
type: concept
tags: [ai, agents, security, least-privilege]
sources:
  - mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li
  - dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan
  - ai-infra-quan-jing-tu-agent-framework-diao-du-bian-pai-sha-xiang-ji-yi-guan-li-tracing-fen-ceng-chai-jie
  - agent-policy-prover
last_updated: 2026-10-30
knowledge_schema: synthesis-v1
---

## Definition
[[AgentSecurityLayering]] assigns each agent control to the lowest trustworthy layer that can enforce it: operating systems, containers, and networks bound raw capability; trusted runtimes mediate credentials and tools; application guards handle content, workflow, and audit semantics.

## Current Synthesis
The source starts from a hostile-control assumption: an agent can read and write files, use networks, or run a shell while its language model can be mistaken or prompt-injected. A prompt can guide behavior, but it is not a sandbox. The damage ceiling therefore depends on boundaries the model cannot rewrite.

The proposed stack has three complementary layers. OS, container, systemd, and network controls enforce users, writable paths, executable capabilities, and egress. A trusted runtime holds secrets and injects them only into profile-authorized calls whose destinations, methods, redirects, proxies, private-address access, and binding locations are constrained. The application guard then addresses residual semantics through outbound allowlists, redaction, asynchronous approval, and audit.

This division also controls complexity. Encoding every tool, method, body, header, path, prompt pattern, and intrusion rule inside one guard produces a difficult policy cross-product. The source therefore prefers small, enforceable primitives and least privilege over the appearance of exhaustive application policy.

Ci Jian De Shan Lin supplies the broader infrastructure rationale: the acting subject is now partially trusted, probabilistic, autonomous, and machine-speed, so a system prompt cannot define the security perimeter. Isolation controls the blast radius and can enable greater autonomy; where private data or credentials cannot move to the cloud, the physical trust boundary also constrains execution placement and makes edge-cloud cooperation part of the security architecture.

The [[AIInfrastructureStack]] source extends the boundary across the complete platform. Identity and tenant isolation govern model and knowledge access; ACL inheritance must survive ingestion and retrieval; PII/DLP controls cover context, memory, traces, and logs; risky tools require approval and audit; and model or dependency provenance belongs to supply-chain governance. Security is therefore neither one sandbox layer nor one prompt filter, but a cross-cutting property whose enforcement points follow data and authority.

Formal reasoning provides another layer above those enforcement points. In the [[OpenShell]] case, a binary approved for cloning, raw network reach, and a broad GitHub credential composed into write authority that REST inspection could not constrain. Its [[Z3]] prover therefore encodes binary, endpoint, protocol layer, method, path, and credential interactions and searches for any action a proposed policy allows outside a reviewed maximum.

This does not collapse enforcement into proof. The runtime still has to implement the modeled sandbox, proxy, credential, filesystem, process, and inference boundaries faithfully. [[FormalPolicyVerification]] instead tests whether their combined declared authority contains an unexpected path and supplies a concrete witness to contextual reviewers.

## Key Claims
- Prompt instructions cannot serve as the root security boundary for a model that can be influenced or mistaken.
- Hard local capability limits belong in operating-system, container, service-manager, and network enforcement where practical.
- Models should request credentialed operations without seeing the underlying secret.
- Credential mediation must bind authority to destinations, methods, redirect and proxy behavior, private-network reachability, and injection points.
- Application guards should focus on content and workflow semantics that lower layers cannot express well, including PII/DLP, approvals, audit, and retrieval authorization.
- Redaction is a residual safeguard, not a substitute for preventing secret exposure.
- Least privilege and a small policy surface are more maintainable than a combinatorial guard matrix, while formal containment can test whether cross-layer combinations exceed a reviewed maximum without replacing the underlying enforcement or contextual approval.

## Evidence
- Threat boundary: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] groups agent risk into exfiltration, secret exposure, and unauthorized action and argues that bounded permissions limit prompt-injection damage.
- Hard enforcement: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] recommends an ordinary user, read-only roots or narrow writable directories, systemd hardening, removal of general HTTP clients, and lower-layer network egress controls.
- Secret isolation: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] places credentials in a trusted runtime that injects them into an approved tool rather than prompt or Skill context.
- Scoped authority: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] shows an `auth_profile` restricted to Moltbook API URL prefixes, enumerated methods, no redirects or proxy, denied private IPs, and bearer-header injection.
- Residual guard: [[mistermorph-de-agent-an-quan-kai-fa-zha-ji-ge-ci-jing-li]] limits application policy to outbound allowlists, redaction, and asynchronous approval plus audit.
- Autonomous blast radius: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] treats prompt injection, mistaken deletion, and overreach as reasons to place the boundary in infrastructure rather than model compliance.
- Physical placement: [[dang-agent-zou-xiang-sheng-chan-infra-mian-lin-na-xie-tiao-zhan]] argues that data gravity and credentials that cannot move to the cloud can place execution at the edge, while explicitly rejecting an all-agents-on-device conclusion.
- Cross-stack governance: [[ai-infra-quan-jing-tu-agent-framework-diao-du-bian-pai-sha-xiang-ji-yi-guan-li-tracing-fen-ceng-chai-jie]] applies authentication, authorization, tenant isolation, PII/DLP, prompt-injection defenses, approvals, audit, and model provenance across all nine layers.
- Retrieval authorization: [[ai-infra-quan-jing-tu-agent-framework-diao-du-bian-pai-sha-xiang-ji-yi-guan-li-tracing-fen-ceng-chai-jie]] includes document- and field-level ACL inheritance in the enterprise knowledge pipeline rather than treating retrieval relevance as sufficient.
- Cross-layer bypass: [[agent-policy-prover]] describes `git-remote-https`, raw GitHub reach, and a broad credential jointly bypassing REST-layer write restrictions.
- Formal containment: [[agent-policy-prover]] searches for an action allowed by a candidate policy but excluded by a reviewed maximum, returning the binary, host, layer, method, and path as a witness when one exists.
- Expert formulas: [[agent-policy-prover]] reuses the encoded policy language for link-local reach, credentialed layer-7 bypass, credential reach expansion, and HTTP-method expansion checks.
- Review composition: [[agent-policy-prover]] treats deterministic solver findings as evidence for human or trusted-model reviewers because the formulas do not understand asset criticality or business intent.

## Counterevidence & Qualifications
The sources are practitioner design arguments and do not establish complete defense. Layer assignment is deployment-specific: container and network policy may not express business legitimacy, while application allowlists may still permit harmful actions at an authorized destination. Credential non-disclosure does not prevent abuse of the mediated capability, and a trusted runtime becomes a high-value component whose parsing, redirect, DNS, proxy, logging, and injection behavior needs separate review. Edge placement can reduce data movement without automatically securing the device, supply chain, local network, or synchronization path. The broader checklist names PII/DLP and supply-chain controls without defining mechanisms or audit results. Formal containment adds assurance only for the current encoding and reviewed maximum; omitted surfaces, stale semantics, implementation drift, or an inappropriately broad maximum remain outside an `unsat` result. None of the sources evaluates covert channels, policy conflicts, approval fatigue, or end-to-end false-negative rates.

## What Changed
- Created a layered agent-security model separating hard capability enforcement, secret-bearing runtime mediation, and residual application guards.
- Added blast-radius control and physical execution placement as reasons infrastructure—not the model—must own the security boundary.
- Extended the model across identity, retrieval ACLs, memory, telemetry, approvals, tenant isolation, and model provenance.
- Added formal containment as a cross-layer composition check that returns concrete policy-expansion witnesses while remaining bounded by model fidelity.

## Related Concepts
- [[SemanticIsolation]] - agent security layering supplies concrete enforcement points for capability and credential semantics.
- [[AgentPermissionModel]] - risk tiers determine which actions can proceed, remain visible, or require approval.
- [[SecretManagement]] - credential custody and rotation remain separate from model-visible tool use.
- [[ProductionAgentInfrastructure]] - layered security bounds long-running agents exposed to hostile inputs and real side effects.
- [[ModelContextProtocol]] - an MCP server can act as a credential-holding bridge when its authority is independently scoped.
- [[StartupSecurityDebt]] - delayed boundary and secret design creates costly unsafe dependencies.
- [[AccountabilityInfrastructure]] - audit evidence records how enforced boundaries and mediated capabilities were actually used.
- [[AIInfrastructureStack]] - makes security a cross-cutting responsibility rather than a single sandbox or application layer.
- [[FormalPolicyVerification]] - tests whether combined layer declarations exceed a pre-reviewed authority envelope.
- [[OpenShell]] - supplies the source's sandbox, policy, and formal-prover case.

---
title: "API Error Handling"
type: concept
tags: [api, http, rest, developer-experience]
sources:
  - best-practices-for-api-error-handling-dzone-integration
  - wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell
last_updated: 2026-09-24
knowledge_schema: synthesis-v1
---

## Definition
[[APIErrorHandling]] is the design of API failure responses so clients can understand what failed, whether they can fix it, and how to recover or explain the failure in a larger application.

## Current Synthesis
The sources frame API error handling as both an integration contract and an operational control surface. A useful response combines the shared semantics of [[HTTP]] status codes with readable messages, linked help, and enough cause information to support client-side recovery. Standard 4xx-versus-5xx classification also lets monitoring, retry, and circuit-breaking systems act without parsing every response body.

The goal is not the largest possible status-code vocabulary or status codes without business detail. Teams should select codes that match real interaction patterns, preserve the distinction between client-correctable and server-side failures, and fill the remaining gap with actionable response data. Returning HTTP 200 for every outcome hides transport-level failure semantics from generic infrastructure even when an application-specific body code remains useful.

## Key Claims
- Error messages are part of the API's developer-facing interface, not incidental logging output.
- Documentation links can turn an error response into a recovery path when the fix is known.
- Client applications need detailed API failures because they must convert them into graceful user-facing behavior.
- Error responses should distinguish client-fixable problems from provider-side failures that require waiting or escalation.
- REST APIs should use a simple, evolving subset of HTTP status codes rather than chase a universal perfect list.
- Standard client-versus-server failure classes enable generic monitoring and recovery controls without application-body inspection.
- Application error details can supplement HTTP semantics but should not erase them by reporting every outcome as HTTP 200.

## Evidence
- Message quality: [[best-practices-for-api-error-handling-dzone-integration]] says opaque errors frustrate developers and should be readable and understandable.
- Recovery support: [[best-practices-for-api-error-handling-dzone-integration]] recommends including documentation or knowledge-base links when they help solve an error.
- Client workflow: [[best-practices-for-api-error-handling-dzone-integration]] notes that API clients integrate the API into a larger whole and need detailed failures for graceful handling.
- Responsibility boundary: [[best-practices-for-api-error-handling-dzone-integration]] says providers should tell clients when a problem is not under their control.
- Status-code selection: [[best-practices-for-api-error-handling-dzone-integration]] recommends starting with basic codes such as 200, 400, and 500, then adding codes like 401 and 403 as needed.
- Operational semantics: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] argues that 4xx and 5xx distinctions let monitoring, retry, and circuit-breaking systems classify failures without opening every response body.
- Anti-pattern boundary: [[wo-zuo-xi-tong-jia-gou-de-yi-xie-yuan-ze-ku-ke-coolshell]] criticizes returning HTTP 200 for failures and moving the entire success/failure contract into an application body.

## Counterevidence & Qualifications
Both sources are practical advice rather than standards documents. They do not specify an error-response schema, localization strategy, security redaction policy, idempotency model, or detailed retry contract. Reader comments on the architecture article also expose boundary questions—such as resource-not-found versus route-not-found and business rejection versus server failure—that require a documented domain policy rather than a mechanical 4xx/5xx rule.

## What Changed
- Added API errors as an operational control surface for monitoring, retry, and circuit breaking.
- Made explicit that body-level error detail should supplement rather than erase HTTP failure semantics.

## Related Concepts
- [[HTTP]] - API error handling commonly uses HTTP status codes as shared response semantics.
- [[DeveloperExperience]] - useful API errors reduce friction for client developers.
- [[DeveloperTooling]] - API responses are part of the tool surface developers work through.
- [[SystemReliability]] - clear failure boundaries support predictable recovery behavior.
- [[ServiceObservability]] - standard status classes make failure monitoring and aggregation cheaper and more reliable.
- [[SystemArchitecturePrinciples]] - treats shared API semantics as an organization-wide architecture standard.

---
title: "API Error Handling"
type: concept
tags: [api, http, rest, developer-experience]
sources:
  - best-practices-for-api-error-handling-dzone-integration
last_updated: 2026-09-14
knowledge_schema: synthesis-v1
---

## Definition
[[APIErrorHandling]] is the design of API failure responses so clients can understand what failed, whether they can fix it, and how to recover or explain the failure in a larger application.

## Current Synthesis
The DZone source frames API error handling as an integration contract between provider and client developer. A useful error response combines the coarse shared semantics of [[HTTP]] status codes with readable messages, linked help, and enough cause information to support client-side recovery. The goal is not to use the largest possible status-code vocabulary, but to select codes that match real interaction patterns and fill the rest of the gap with actionable detail.

## Key Claims
- Error messages are part of the API's developer-facing interface, not incidental logging output.
- Documentation links can turn an error response into a recovery path when the fix is known.
- Client applications need detailed API failures because they must convert them into graceful user-facing behavior.
- Error responses should distinguish client-fixable problems from provider-side failures that require waiting or escalation.
- REST APIs should use a simple, evolving subset of HTTP status codes rather than chase a universal perfect list.

## Evidence
- Message quality: [[best-practices-for-api-error-handling-dzone-integration]] says opaque errors frustrate developers and should be readable and understandable.
- Recovery support: [[best-practices-for-api-error-handling-dzone-integration]] recommends including documentation or knowledge-base links when they help solve an error.
- Client workflow: [[best-practices-for-api-error-handling-dzone-integration]] notes that API clients integrate the API into a larger whole and need detailed failures for graceful handling.
- Responsibility boundary: [[best-practices-for-api-error-handling-dzone-integration]] says providers should tell clients when a problem is not under their control.
- Status-code selection: [[best-practices-for-api-error-handling-dzone-integration]] recommends starting with basic codes such as 200, 400, and 500, then adding codes like 401 and 403 as needed.

## Counterevidence & Qualifications
The source is practical advice rather than a standards document. It does not specify an error-response schema, localization strategy, security redaction policy, retry semantics, observability requirements, or how to balance helpful detail against information leakage.

## What Changed
- Created the concept from the DZone source's treatment of API errors as integration guidance.

## Related Concepts
- [[HTTP]] - API error handling commonly uses HTTP status codes as shared response semantics.
- [[DeveloperExperience]] - useful API errors reduce friction for client developers.
- [[DeveloperTooling]] - API responses are part of the tool surface developers work through.
- [[SystemReliability]] - clear failure boundaries support predictable recovery behavior.

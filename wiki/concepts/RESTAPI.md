---
title: "REST API"
type: concept
tags: [api, rest, http, developer-experience]
sources:
  - best-practices-for-api-error-handling-dzone-integration
  - graphql-vs-rest-apollo-graphql
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[RESTAPI]] is an HTTP-oriented application interface that exposes resources through URLs, uses methods and status codes to communicate operations and outcomes, and returns representations whose default shape is commonly selected by the server.

## Current Synthesis
The available sources present REST through two complementary lenses. The error-handling article treats [[HTTP]] semantics as a practical shared contract: a deliberately chosen status-code subset, readable messages, documentation, and responsibility boundaries help clients recover. The GraphQL comparison treats REST as a resource-and-route interface in which URL, method, route handler, and response representation are commonly coupled.

This coupling makes ordinary HTTP infrastructure and URL-oriented caching comparatively direct, but nested client needs may require multiple requests, server-expanded responses, or additional query conventions. Those are common REST practices rather than universal constraints of the architectural style; the comparison source uses a simplified mainstream implementation model, not a complete account of REST, hypermedia, or every production API convention.

## Key Claims
- Resources are commonly identified by URLs and retrieved or changed through HTTP methods.
- Route and method combinations dispatch to server-side handler functions.
- Server-defined representations provide a predictable default but can over-fetch fields or require separate calls for related resources.
- HTTP status classes and actionable response bodies together support client recovery, monitoring, retry, and responsibility boundaries.
- REST's alignment with HTTP makes standard caching and generic infrastructure easier to apply directly than in the GraphQL model described by the source.
- REST APIs can add embedding, sparse-field, and expansion conventions, so fixed shapes and multiple round trips are tendencies rather than absolute rules.

## Evidence
- Error contract: [[best-practices-for-api-error-handling-dzone-integration]] recommends readable errors, linked help, client-versus-server responsibility, and a small evolving status-code vocabulary.
- Resource model: [[graphql-vs-rest-apollo-graphql]] identifies resources by URLs and illustrates retrieval with a `GET` request returning JSON.
- Route dispatch: [[graphql-vs-rest-apollo-graphql]] shows a framework matching an HTTP method and path to one handler function.
- Composition tradeoff: [[graphql-vs-rest-apollo-graphql]] says related data commonly requires multiple requests, inclusion in the first representation, or response-modifying URL parameters.
- Caching tradeoff: [[graphql-vs-rest-apollo-graphql]] says ordinary HTTP caching applies more easily to REST results than to GraphQL query results.

## Counterevidence & Qualifications
The GraphQL comparison explicitly leaves out object identification, hypermedia, and a full treatment of caching, so its REST model is intentionally incomplete. REST is an architectural style rather than a mandatory one-route/one-shape wire format, and real APIs often provide embedding, field selection, batch endpoints, content negotiation, or non-JSON representations. The error-handling source is practitioner guidance rather than a standards document and does not settle every status-code or business-error boundary.

## What Changed
- Created a combined synthesis of REST resource routing, representation shape, HTTP semantics, error recovery, and GraphQL-relative tradeoffs.

## Related Concepts
- [[GraphQL]] - alternative typed query model that moves field selection and relationship traversal into client operations.
- [[HTTP]] - protocol foundation supplying methods, URLs, status codes, caching, and shared infrastructure.
- [[APIErrorHandling]] - turns protocol outcomes into actionable client recovery guidance.
- [[CapabilityOrientedIntegration]] - encourages API boundaries around consumer capabilities rather than source-system mechanics.
- [[DeveloperExperience]] - predictable resources and useful failure contracts shape integration quality.

---
title: "REST API"
type: concept
tags: [api, rest, http, developer-experience]
sources:
  - best-practices-for-api-error-handling-dzone-integration
  - graphql-vs-rest-apollo-graphql
  - graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[RESTAPI]] is an HTTP-oriented application interface that exposes resources through URLs, uses methods and status codes to communicate operations and outcomes, and returns representations whose default shape is commonly selected by the server.

## Current Synthesis
The available sources present REST through two complementary lenses. The error-handling article treats [[HTTP]] semantics as a practical shared contract: a deliberately chosen status-code subset, readable messages, documentation, and responsibility boundaries help clients recover. The GraphQL comparison treats REST as a resource-and-route interface in which URL, method, route handler, and response representation are commonly coupled.

This coupling makes ordinary HTTP infrastructure and URL-oriented caching comparatively direct, but nested client needs may require multiple requests, server-expanded responses, or additional query conventions. PayPal's Checkout case makes the composition pressure concrete: small atomic endpoints caused repeated client round trips, a page-oriented orchestration response accumulated fields, and a dynamic Bulk REST request format reduced trips but was rarely used because it exposed underlying endpoints, verbs, parameters, and dependencies. Those are implementation tradeoffs rather than universal constraints of the architectural style.

## Key Claims
- Resources are commonly identified by URLs and retrieved or changed through HTTP methods.
- Route and method combinations dispatch to server-side handler functions.
- Server-defined representations provide a predictable default but can over-fetch fields or require separate calls for related resources.
- HTTP status classes and actionable response bodies together support client recovery, monitoring, retry, and responsibility boundaries.
- REST's alignment with HTTP makes standard caching and generic infrastructure easier to apply directly than in the GraphQL model described by the source.
- REST APIs can add embedding, sparse-field, and expansion conventions, so fixed shapes and multiple round trips are tendencies rather than absolute rules.
- Batch or bulk composition can reduce network trips while retaining REST resources, but its client complexity determines whether it becomes a usable primary interface.

## Evidence
- Error contract: [[best-practices-for-api-error-handling-dzone-integration]] recommends readable errors, linked help, client-versus-server responsibility, and a small evolving status-code vocabulary.
- Resource model: [[graphql-vs-rest-apollo-graphql]] identifies resources by URLs and illustrates retrieval with a `GET` request returning JSON.
- Route dispatch: [[graphql-vs-rest-apollo-graphql]] shows a framework matching an HTTP method and path to one handler function.
- Composition tradeoff: [[graphql-vs-rest-apollo-graphql]] says related data commonly requires multiple requests, inclusion in the first representation, or response-modifying URL parameters.
- Checkout latency: [[graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium]] reports at least 700 ms of network time at the 99th percentile for each Checkout round trip, excluding server processing.
- Orchestration tradeoff: [[graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium]] says PayPal's combined response grew as features and experiments accumulated, making every user pay for fields they did not necessarily need.
- Bulk composition: [[graphql-a-success-story-for-paypal-checkout-paypal-engineering-medium]] says clients could submit dependent REST operations in one request, but rarely did because the format demanded intimate knowledge of underlying APIs and selected whole resources rather than fields.
- Caching tradeoff: [[graphql-vs-rest-apollo-graphql]] says ordinary HTTP caching applies more easily to REST results than to GraphQL query results.

## Counterevidence & Qualifications
The GraphQL comparison explicitly leaves out object identification, hypermedia, and a full treatment of caching, so its REST model is intentionally incomplete. REST is an architectural style rather than a mandatory one-route/one-shape wire format, and real APIs often provide embedding, field selection, batch endpoints, content negotiation, or non-JSON representations. PayPal's conclusions come from one latency-sensitive product and do not compare a well-designed sparse-field, expansion, or standardized batch interface; its 700 ms figure is a reported tail network cost, not a complete application benchmark. The error-handling source is practitioner guidance rather than a standards document.

## What Changed
- Created a combined synthesis of REST resource routing, representation shape, HTTP semantics, error recovery, and GraphQL-relative tradeoffs.
- Added PayPal Checkout's atomic, orchestration, and Bulk REST variants as a concrete composition and usability case.

## Related Concepts
- [[GraphQL]] - alternative typed query model that moves field selection and relationship traversal into client operations.
- [[HTTP]] - protocol foundation supplying methods, URLs, status codes, caching, and shared infrastructure.
- [[APIErrorHandling]] - turns protocol outcomes into actionable client recovery guidance.
- [[CapabilityOrientedIntegration]] - encourages API boundaries around consumer capabilities rather than source-system mechanics.
- [[DeveloperExperience]] - predictable resources and useful failure contracts shape integration quality.

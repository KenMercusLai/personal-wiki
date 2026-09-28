---
title: "GraphQL"
type: concept
tags: [api, query-language, schema, developer-experience]
sources:
  - graphql-vs-rest-apollo-graphql
last_updated: 2026-09-29
knowledge_schema: synthesis-v1
---

## Definition
[[GraphQL]] is a typed API query and execution model in which a schema declares available objects and relationships, clients select fields through query or mutation operations, and resolvers assemble a response matching the operation's shape.

## Current Synthesis
The Apollo article presents GraphQL as close to [[RESTAPI]] at the network and implementation layers but different at the interface-composition layer. Both can send [[HTTP]] requests, identify resources, return JSON, and call ordinary server functions. GraphQL separates type identity from retrieval, exposes a schema rather than only a route list, and lets a client traverse declared relationships while choosing its response fields.

Execution follows the query tree. A root query or mutation field enters the graph, then field resolvers can run at multiple nested points; the GraphQL library assembles their values into the requested structure. This can reduce over-fetching and repeated network round trips, but it does not erase backend work and can make ordinary URL-oriented HTTP caching less direct.

## Key Claims
- Schema types describe resources independently from the root operations through which clients retrieve them.
- Clients select fields and traverse declared relationships, so one operation can request a nested response tailored to its immediate needs.
- Query and mutation root types distinguish read and write operations inside GraphQL's operation model.
- Resolvers attach implementation functions to fields, and one operation can invoke several resolvers, including the same resolver more than once through aliases.
- GraphQL execution constructs a response whose shape follows the submitted query.
- Fewer client-server round trips and less unnecessary field transfer are potential benefits, not proof of lower total backend cost.

## Evidence
- Resource separation: [[graphql-vs-rest-apollo-graphql]] separates `Book` and `Author` type definitions from root fields such as `book(id)` and `author(id)`.
- Client-selected shape: [[graphql-vs-rest-apollo-graphql]] shows a client requesting a book title and only an author's first name rather than accepting one fixed server response.
- Relationship traversal: [[graphql-vs-rest-apollo-graphql]] contrasts one nested GraphQL operation with multiple REST calls or custom response expansion.
- Resolver execution: [[graphql-vs-rest-apollo-graphql]] shows root and nested resolvers for an author and posts, plus an alias that invokes the same field twice.
- Diagram evidence: [[graphql-vs-rest-apollo-graphql]] depicts a single `/graphql` request passing through a schema to posts, comments, and authors.
- Tradeoff: [[graphql-vs-rest-apollo-graphql]] says conventional HTTP caching is less straightforward for GraphQL and names application-layer tooling as a response.

## Counterevidence & Qualifications
The source is a 2017 Apollo-associated explanation rather than a benchmark or neutral technology comparison. A single GraphQL network request may still trigger many resolver calls or downstream operations, so fewer round trips do not guarantee less server work, lower latency, or simpler operations. REST responses can support embedding, sparse fieldsets, and other conventions, while GraphQL deployments vary in transport, caching, authorization, batching, and query-cost controls; these are outside the article's scope.

## What Changed
- Created the concept around separation of schema identity, client-selected query shape, and resolver-based execution.

## Related Concepts
- [[RESTAPI]] - shares resource, HTTP, JSON, and server-function foundations but usually exposes different composition controls.
- [[HTTP]] - common network substrate whose standard caching model is easier to apply directly to URL-addressed REST resources.
- [[APIErrorHandling]] - failure contracts remain necessary even when data selection moves into a query language.
- [[CapabilityOrientedIntegration]] - both hide implementation details behind consumer-facing contracts, while GraphQL additionally standardizes field selection and traversal.
- [[DeveloperExperience]] - the article's central rationale for GraphQL's interface changes.

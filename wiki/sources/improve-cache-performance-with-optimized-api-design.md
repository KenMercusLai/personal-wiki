---
title: "Improve cache performance with optimized API design"
type: source
tags: [api, caching, http, cdn, web-performance]
date: 2026-04-08
source_file: "/mnt/ken_personal_wiki/Articles/Improve cache performance with optimized API design.md"
---

## Summary
Fastly argues that API traffic is ordinary [[HTTP]] traffic and can often be cached at the edge when interface design preserves reusable response units. The article applies that claim to comment, airline-seat, and ecommerce APIs, then connects cache-friendly [[RESTAPI]] design with bounded pagination, event-driven purging, surrogate-key tagging, and stale serving for availability. Its recommendations are useful design patterns rather than measured benchmarks, and its treatment of [[HTTP2]] and [[QUIC]] as emerging technologies dates the article's protocol context.

## Key Claims
- [[APIResponseCaching]] improves when reads use `GET`, authentication stays in headers, errors use meaningful HTTP status codes, and responses omit requester-specific details.
- Small resource-oriented endpoints can produce reusable cache objects, while batch wrappers and personalized response bodies collapse many requests into low-reuse variants.
- Separating user-specific booking data from flight-level seat availability lets many travelers share the cacheable availability response.
- Separating relatively stable product listings from frequently changing review aggregates reduces invalidation caused by unrelated change rates.
- Filtering and pagination create cache variants, so APIs should promote important filter dimensions into endpoints, bound page shapes, and normalize equivalent first-page requests.
- Event-driven purge requests and surrogate-key tags let one changed object invalidate the many API responses that contain it without flushing unrelated content.
- Serving stale cached responses during origin failure can preserve API availability when slightly old data is safer than an outage.

## Key Quotes
> "There's nothing inherently special about an API request" - on applying ordinary HTTP caching to APIs.

> "the same piece of data may end up in lots of different API responses" - on the need for tag-based invalidation.

## Connections
- [[Fastly]] - publisher and edge-cache platform used for the purge, tagging, and stale-serving examples.
- [[APIResponseCaching]] - central practice of designing reusable response objects and targeted invalidation.
- [[RESTAPI]] - method, URL, status, authentication, and resource-boundary conventions used to make reads cacheable.
- [[DynamicContentCaching]] - broader problem of preserving reuse while changing application data stays acceptably fresh.
- [[HTTP]] - supplies cache semantics, request methods, status codes, headers, and response representations.
- [[HTTP2]] - reduces the transport penalty of issuing several atomic API reads instead of one batch wrapper.
- [[QUIC]] - cited as part of the transport context that weakens the case for batching solely to reduce request overhead.

## Contradictions
- No direct contradiction was found. The source strengthens the wiki's existing REST and dynamic-caching material, while qualifying the idea that fewer HTTP requests are always better: a batch can save round trips yet reduce response reuse and make invalidation coarser.

## Image Notes
The sole effective local embed was opened. It is a Fastly-branded decorative hero illustration of a rocket carrying a package, contains no technical evidence, and was omitted without creating an asset manifest.

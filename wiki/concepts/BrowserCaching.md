---
title: "Browser Caching"
type: concept
tags: [browser, caching, http, web-performance]
sources:
  - blog-wulc-liu-lan-qi-huan-cun-ji-zhi
last_updated: 2026-09-25
knowledge_schema: synthesis-v1
---

## Definition
[[BrowserCaching]] is the reuse of locally stored HTTP responses according to freshness rules and server validators, reducing requests, transferred bytes, and user-visible latency without treating stored content as permanently current.

## Current Synthesis
Browser caching separates freshness from validation. A response that is still fresh under `Cache-Control: max-age` or, as a fallback, `Expires` can normally be reused without contacting the origin. Once it is stale, the browser may still avoid downloading the representation again by sending an entity tag in `If-None-Match` or a modification timestamp in `If-Modified-Since`; the server returns `304` when the stored response remains valid and `200` with a new representation when it does not.

The source's first-request diagram shows a cache miss reaching the server and storing both the body and metadata. Its repeat-request diagram then branches between a direct fresh-cache hit and conditional validation, with `ETag` checked before `Last-Modified`. This is a useful operational model, but the directive descriptions need modern precision: `no-cache` means reuse requires validation, whereas `no-store` prohibits storage. Browser reload behavior and validator generation also vary by implementation and context.

## Key Claims
- Freshness metadata determines when a stored response can be reused without a network round trip.
- `Cache-Control: max-age` expresses a relative freshness lifetime and takes precedence over `Expires` when both are present.
- Conditional requests let stale stored responses be revalidated through `ETag`/`If-None-Match` or `Last-Modified`/`If-Modified-Since`.
- A `304 Not Modified` response saves representation transfer while a `200` response supplies changed content.
- Entity tags can detect distinctions that second-granularity modification timestamps cannot represent reliably.
- Cache directives differ in semantics: `no-cache` requires validation before reuse, while `no-store` prohibits storage.

## Evidence
- Freshness headers: [[blog-wulc-liu-lan-qi-huan-cun-ji-zhi]] includes an inspected response-header screenshot where `Date` is 03:25:01 GMT, `Expires` is 03:30:01 GMT, and `Cache-Control` is `max-age=300`, all representing a five-minute freshness window.
- First-request storage: [[blog-wulc-liu-lan-qi-huan-cun-ji-zhi]] diagrams a cache miss reaching the web server, then storing the response body with `Expires`, `Cache-Control`, `ETag`, and `Last-Modified` metadata before presentation.
- Conditional validation: [[blog-wulc-liu-lan-qi-huan-cun-ji-zhi]] diagrams a stale response sending `If-None-Match` when an entity tag exists or `If-Modified-Since` when only a modification timestamp exists.
- Response outcomes: [[blog-wulc-liu-lan-qi-huan-cun-ji-zhi]] shows the server choosing `200` or `304`; a `200` response replaces the cached representation, while `304` returns the browser to its stored body.
- Validator motivation: [[blog-wulc-liu-lan-qi-huan-cun-ji-zhi]] identifies sub-second changes, content-stable file regeneration, and inaccurate modification clocks as cases where timestamps can be insufficient.

## Counterevidence & Qualifications
The source is a 2016 introductory article and sometimes turns common behavior into universal rules. `Expires` is not generally ignored merely because HTTP/1.1 is in use, `no-cache` does not forbid storage, and `If-Modified-Since` represents the cached resource's modification timestamp rather than the current request time. Validators can operate without an explicit `Cache-Control` lifetime, browser reload behavior is implementation-dependent, and server-specific entity-tag generation should not be generalized across versions or platforms.

## What Changed
- Created the concept by separating fresh-cache reuse from stale-response validation.
- Preserved the source's request-flow model while correcting its overly broad directive and implementation claims.

## Related Concepts
- [[HTTP]] - defines the request and response semantics used by browser caches.
- [[HTTP11]] - standardizes `Cache-Control` and entity-tag-based conditional requests.
- [[WebPerformanceOptimization]] - browser caching removes round trips and representation transfer from repeat loads.
- [[DynamicContentCaching]] - extends the freshness problem to resources that can change unpredictably before expiry.
- [[LatencyHierarchy]] - local cache reuse avoids comparatively expensive network communication.

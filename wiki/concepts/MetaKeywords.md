---
title: "Meta Keywords"
type: concept
tags: [seo, html, metadata, search-engines]
sources:
  - meta-keywords-shi-shi-me-wei-shen-me-bu
last_updated: 2026-10-09
knowledge_schema: synthesis-v1
---

## Definition
[[MetaKeywords]] is the HTML metadata field conventionally expressed as `<meta name="keywords" content="...">`, through which a publisher declares terms intended to describe a page.

## Current Synthesis
The field is historically important but operationally obsolete for mainstream search optimization. Because it is invisible to ordinary page readers and entirely controlled by the publisher, it became easy to stuff with irrelevant terms. Search systems therefore moved toward signals grounded in visible content, links, titles, descriptions, structure, and other evidence that is harder to manipulate through one declaration.

The key distinction is not whether an engine can parse or index the field, but whether the field materially changes retrieval or ranking. The article reports that Google and Bing ignore it, Yahoo historically retained it only as a lowest-priority fallback, Baidu had reduced or removed its importance, and Yandex documented it while practitioners reported little effect. On that evidence, maintaining the field creates no demonstrated search benefit and may expose a site's targeting vocabulary without improving discoverability.

## Key Claims
- Publisher-controlled keyword declarations became unreliable because irrelevant terms could be added without changing visible page content.
- Parsing or indexing a metadata field does not imply that it has useful ranking weight.
- Google and Bing publicly described the tag as ignored or devoid of SEO value in the historical statements collected by the source.
- Yahoo's historical clarification assigned the field its lowest signal and prioritized words found elsewhere in the document.
- Baidu and Yandex evidence in the source is weaker and dated, but does not demonstrate a material optimization benefit.
- Removing meta keywords is lower-risk than treating them as a ranking lever; effort belongs on supported content, metadata, structure, and measurement.

## Evidence
- Abuse and signal failure: [[meta-keywords-shi-shi-me-wei-shen-me-bu]] traces the tag from a 1995 information aid to widespread stuffing of irrelevant keywords by 1999.
- Explicit rejection: [[meta-keywords-shi-shi-me-wei-shen-me-bu]] quotes Google's 2009 statement that keyword meta tags have no web-ranking effect and Bing's 2014 description of the tag as dead for SEO value.
- Indexing-versus-ranking distinction: [[meta-keywords-shi-shi-me-wei-shen-me-bu]] quotes Yahoo saying it still indexed the field while assigning it the lowest ranking signal and giving priority to body, title, description, and anchor text.
- Cross-engine limit: [[meta-keywords-shi-shi-me-wei-shen-me-bu]] reports a third-party Baidu account and Yandex documentation plus practitioner opinion, neither of which establishes meaningful ranking lift.
- Replacement practice: [[meta-keywords-shi-shi-me-wei-shen-me-bu]] recommends attention to titles, descriptions, structured data, and content rather than the obsolete field.

## Counterevidence & Qualifications
The engine evidence is historical rather than a live test, and the Baidu and Yandex sections rely partly on secondary reporting or practitioner consensus. Yahoo's ability to index the field is a technical counterexample to the broad phrase “completely dead,” but its quoted clarification still denies useful boosting from repetition. The source does not run controlled ranking experiments or quantify maintenance cost, and its opening `<meta keywords="...">` example is not the standard HTML syntax. Its separate assertion that Google penalizes abuse is unsupported by the cited statement that Google disregards the field entirely.

## What Changed
- Created a concept separating metadata parsing and indexing from material ranking influence.
- Recorded the cross-engine evidence as historically strong for Google and Bing but weaker or more qualified for Yahoo, Baidu, and Yandex.

## Related Concepts
- [[TechnicalSEO]] - verifies whether page mechanisms are crawlable, supported, consolidated, and reflected in actual search evidence.
- [[AlgorithmicOptimizationArmsRace]] - explains why publishers continue to seek manipulable fields and inferred ranking advantages.
- [[PlatformDistributionDependence]] - creates pressure to follow search-platform preferences even when their effects are opaque.
- [[MarketingAttribution]] - requires downstream measurement rather than assuming a metadata change caused traffic or business outcomes.

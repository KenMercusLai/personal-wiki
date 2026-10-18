---
title: "中文独立博客的年化“腐烂率”——8%"
type: source
tags: [independent-blogs, link-rot, web-preservation, hosting]
date: 2022-02-05
source_file: "/mnt/ken_personal_wiki/Articles/chinese-blogs-link-rot-2022.md"
---

## Summary
[[YZQZSS]] estimates how quickly Chinese independent blogs and their article URLs disappear, using the Save the Web Project's blog list and a later article-level sample. The source reports an 8.41% annual site-loss rate over its first observation window and, in a 2023 update, a 10–12% annual article-link-loss rate, while showing that sample quality, redirects, hosting choices, and failure classification materially affect any [[LinkRot]] estimate.

## Key Claims
- Among 965 Chinese independent blogs observed for 17 months, 113 were classified as gone, yielding the author's calculated annual site-loss rate of 8.41% and an implied half-life of roughly eight years if that rate remained constant.
- The author's initial 20–30% estimate for annual article-link loss was explicitly subjective; a 2023 follow-up instead listed 25 failures among 196 article URLs and reported a 10–12% annual rate with a roughly six-year half-life.
- About half of the observed HTTP 404 responses followed permalink changes without redirects, so link continuity depends on migration practice as well as whether a blog still exists.
- The [[ForeverBlog]] cohort had 149 abnormal entries among 999 blogs collected from 2017-08-31 through 2022-02-05, producing an upper-bound estimate near 3.5% annual loss because some abnormalities concerned content rather than closure.
- Static-site hosting on services such as [[GitHub]] Pages can reduce individual operating burden and some failure modes, but concentration creates correlated platform risk; self-hosting has higher short-term cost and operational risk.
- A preserved copy elsewhere, including at Internet Archive, does not count as the original blog or link surviving under the source's definition.

## Key Quotes
> “每年约有8%的中文博客会消失” — the author's interpretation of the first site-level calculation.

> “其中，有约一半的404是博客换了永久链接，但没做重定向。” — on migration-induced link loss.

## Connections
- [[YZQZSS]] - author who assembled the calculations and qualifications.
- [[LinkRot]] - central failure phenomenon measured at both site and article-URL levels.
- [[DigitalContentDurability]] - the measurements quantify how live access decays and distinguish origin survival from preservation copies.
- [[ForeverBlog]] - curated comparison cohort whose stricter admission rules are associated with lower apparent loss.
- [[GitHub]] - named static-site host that can reduce individual maintenance risk while introducing shared platform dependence.
- [[WebCentralization]] - concentrated hosting converts many independent sites into a correlated infrastructure dependency.

## Contradictions
- The title's rounded 8% rate describes the author's 2022 site-level calculation, whereas the 2023 update reports 10–12% for article URLs; these measure different units and observation sets rather than a single revised rate.
- The 8.41% and half-life calculations assume a stable exponential hazard, but the source says future rates are uncertain and provides no confidence interval, repeat-sampling method, or independent replication.
- The 113 lost sites are defined by survival of the blog body rather than strict URL continuity, while the later article sample counts changed permalinks without redirects as failures. The two classifications are therefore not directly comparable.
- The 196-article update is small and does not explain sampling, follow-up duration, duplicate handling, recovery attempts, or whether TLS, DNS, and hosting failures were transient.
- The [[ForeverBlog]] abnormal count includes content-policy problems as well as closed sites, so 3.5% is presented as an overestimate of true disappearance rather than a directly observed closure rate.

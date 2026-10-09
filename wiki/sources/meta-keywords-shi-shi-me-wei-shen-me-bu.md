---
title: "Meta Keywords：是什么、为什么不"
type: source
tags: [seo, meta-keywords, search-engines, web-standards]
date: 2023-01-15
source_file: "/mnt/ken_personal_wiki/Articles/Meta Keywords：是什么、为什么不.md"
---

## Summary
[[Sukka]] argues that the HTML keywords meta tag should no longer be treated as an SEO technique because easy keyword stuffing destroyed its value as a trustworthy relevance signal. The article says Google and Bing ignore it, Yahoo historically retained it only as a very weak fallback, Baidu had deliberately reduced or removed its importance, and Yandex still documented it while practitioners described little effect. Its durable contribution to [[TechnicalSEO]] is the distinction between publisher-declared metadata and signals a search system can verify from content, links, and structure, although several engine-specific claims are historical or weakly sourced.

## Key Claims
- The keywords meta tag was intended to give search crawlers page-topic information that ordinary visitors would not see.
- Widespread stuffing of irrelevant terms made publisher-supplied keywords too easy to manipulate and encouraged search engines to rely on page content, links, titles, descriptions, and other signals.
- Google publicly said in 2009 that its web ranking disregarded keyword meta tags, while Bing described the tag in 2014 as having no SEO value.
- Yahoo's 2009 clarification distinguished indexing the field from giving it meaningful ranking weight: other document evidence took priority, and repetition in the tag did not boost ranking.
- The article characterizes Baidu as having deliberately weakened or ignored the tag and Yandex as still documenting it but assigning it little practical weight.
- Sites should omit meta keywords and invest instead in useful content, title and description metadata, structured data, and other supported search practices.

## Key Quotes
> "Meta Keywords 已死。网站应该停止使用 Meta Keywords 标签。" - the article's conclusion.

> "They simply don't have any effect in our search ranking at present." - Google's 2009 statement as quoted by the article.

## Connections
- [[Sukka]] - author assembling the historical and engine-specific case against using meta keywords.
- [[MetaKeywords]] - obsolete publisher-declared keyword field examined by the article.
- [[TechnicalSEO]] - broader discipline that should verify crawler support and ranking effects instead of preserving unsupported metadata rituals.
- [[Google]] - search operator whose 2009 statement says the keywords meta tag has no web-ranking effect.
- [[Yahoo]] - search operator whose historical clarification separates indexing the tag from assigning it meaningful ranking weight.

## Contradictions
- The article's opening `<meta keywords="...">` example is not the standard HTML form, which uses `name="keywords"` and a `content` attribute.
- The claim that Google penalizes sites for abusing meta keywords is not established by the cited Google material quoted in the article; saying the tag is completely disregarded points instead to no direct ranking effect from the field itself.
- Yahoo's retained indexing is not evidence of useful ranking influence: the quoted response assigns the field the lowest signal and says repetition does not boost recall or rank.
- The Baidu conclusion relies on a 2018 third-party article quoting a 2013 engineer, and the Yandex weighting claim relies partly on practitioner opinion. These historical statements should not be treated as current documentation without rechecking the engines.
- The archived Markdown reproduces a 2023 article from a Wayback snapshot retrieved in 2026; it is not an independently verified survey of current search behavior.

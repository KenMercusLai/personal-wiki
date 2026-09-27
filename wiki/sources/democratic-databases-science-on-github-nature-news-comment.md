---
title: "Democratic databases: science on GitHub"
type: source
tags: [github, git, open-science, scientific-data, version-control]
date: 2016-10-03
source_file: "/mnt/ken_personal_wiki/Articles/Democratic databases- science on GitHub - Nature News - Comment.md"
---

## Summary
Jeffrey Perkel describes how researchers adapted [[GitHub]] and Git from software development to the collaborative maintenance of scientific datasets and code. [[CaitlinRivers]]' Ebola repository shows the practical shift from ministry PDF updates to shared, machine-readable tables that collaborators could update and check, while [[VersionControlledScientificData]] captures the broader fit, limits, and need for separate permanent archiving.

## Key Claims
- Version history, attribution, forks, review, merging, and rollback make a repository more open to distributed contribution than a static online catalogue.
- Rivers' Ebola project let outside researchers convert daily reports, contribute tables, and add simple checks on patient-count consistency.
- Git works best for relatively small, actively maintained, text-based scientific materials such as code, XML, Markdown, LaTeX, and CSV; binary and very large files are a weaker fit.
- GitHub can disseminate draft data faster than a formal scientific archive, as illustrated by the ZiBRA project's real-time Zika surveillance work.
- A mutable GitHub repository is not by itself a permanent, citable archive; a publication snapshot should also be deposited with an archival service such as Zenodo or Figshare for a DOI.
- Git and GitHub have a substantial learning curve, so browser interfaces, training, and help from experienced users matter to adoption.
- The article's Scopus chart shows the share of papers citing GitHub rising from 2010 to 2016 across computer science, mathematics, agricultural and biological sciences, neuroscience, physics and astronomy, and biochemistry, genetics and molecular biology.

## Key Quotes
> "I figured if I needed it, other people would, too." - Rivers on publishing the Ebola data.

> "I don't know how I lived without it." - Emily Jane McTavish on GitHub in scientific work.

## Connections
- [[GitHub]] - collaboration platform used to publish, review, fork, and maintain scientific datasets and code.
- [[CaitlinRivers]] - epidemiologist whose Ebola data repository demonstrates rapid distributed curation and error checking.
- [[VersionControlledScientificData]] - operating pattern that separates collaborative working history from permanent scholarly archiving.
- [[DataScienceEngineeringPractice]] - version control, provenance, validation, and machine-readable formats are engineering foundations for scientific analysis.
- [[OrganizationalDataSharing]] - scientific repositories extend shared-data reasoning across institutions and public contributors.

## Contradictions
- Nature later corrected the article's statement that Git records changes line by line: Git maintains multiple versions of files. Text-oriented diffs remain useful, but that interface should not be confused with Git's underlying storage model.
- No direct contradiction with an existing wiki page was found. The source adds a scientific-collaboration use case to [[GitHub]] and qualifies repository sharing with format, size, usability, persistence, and citability limits.

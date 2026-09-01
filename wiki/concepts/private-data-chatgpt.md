---
title: "Private-Data ChatGPT"
description: "A ChatGPT-style assistant that answers questions against user-controlled documents or internal data."
type: "concept"
updated: "2026-09-02"
source_keys: ["build-chatgpt-with-private-data"]
---

[零基础｜搭建基于私域数据的ChatGPT]({{< relref "/wiki/sources/build-chatgpt-with-private-data.md" >}}) describes a private-data ChatGPT as an application pattern where the model's language understanding is applied to content supplied by the user rather than only to the model's built-in training data.

The source uses ChatPDF, ChatDocs, and ChatExcel as examples: the user uploads a document or spreadsheet, then asks natural-language questions about that material. In the tutorial version, the private corpus is a set of plain text files uploaded into a Replit project.

---
title: "Kubernetes"
description: "Container orchestration platform described as a RESTful resource and controller system for declaring desired state and reconciling actual state."
type: "entity"
updated: "2026-09-02"
source_keys: ["jysperm-2018-technical-year-review"]
entity_kind: "software"
---

来源：[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Kubernetes 是王子亭 2018 年工作中深度接触的容器平台。来源强调它不只是一个容器管理工具，而是一个平台：它用 RESTful API 将功能抽象为资源，并由每种资源的 Controller 将对象实际状态同步到预期状态。

这篇来源用 Kubernetes 解释容器平台为什么能简化管理。开发者用描述式定义文件表达期望的最终状态，平台持续调和实际状态和预期状态。这个模型也让 Kubernetes 能通过自定义资源和自定义 Controller 扩展功能，把同一套声明式控制机制用于新的业务对象。

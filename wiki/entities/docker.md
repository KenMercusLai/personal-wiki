---
title: "Docker"
description: "Container platform used in 12 Fractured Apps to show both the benefits of Twelve-Factor practices and the startup fragility of poorly adapted applications."
type: "entity"
updated: "2026-09-01"
source_keys: ["kelsey-hightower-12-fractured-apps"]
entity_kind: "software"
---

来源：[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})

Docker 是这篇来源讨论应用部署问题的主要技术背景。Kelsey Hightower 认为，Docker 让 Twelve-Factor App 的部分原则更容易落地，例如把日志写到 stdout、通过环境变量注入配置，并把应用打包成可运行的制品。

来源同时指出，Docker 也会放大应用启动阶段的设计缺陷。把旧应用直接搬进容器后，如果它要求配置文件、数据目录和外部数据库都已就绪，团队往往会用绑定挂载、配置管理或自定义 entrypoint 脚本来补救。Hightower 的建议是让应用直接处理这些启动条件，而不是把容器当作一层新的虚拟机或脚本运行环境。

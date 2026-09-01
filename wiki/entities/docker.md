---
title: "Docker"
description: "Container platform used to discuss Twelve-Factor deployment practices, startup fragility, Dockerfile generation, and the difference between merely containerized and Container Native applications."
type: "entity"
updated: "2026-09-02"
source_keys: ["kelsey-hightower-12-fractured-apps", "jysperm-2018-technical-year-review"]
entity_kind: "software"
---

来源：[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})；[2018 年度小结（技术方面）]({{< relref "/wiki/sources/jysperm-2018-technical-year-review.md" >}})

Docker 是这篇来源讨论应用部署问题的主要技术背景。Kelsey Hightower 认为，Docker 让 Twelve-Factor App 的部分原则更容易落地，例如把日志写到 stdout、通过环境变量注入配置，并把应用打包成可运行的制品。

来源同时指出，Docker 也会放大应用启动阶段的设计缺陷。把旧应用直接搬进容器后，如果它要求配置文件、数据目录和外部数据库都已就绪，团队往往会用绑定挂载、配置管理或自定义 entrypoint 脚本来补救。Hightower 的建议是让应用直接处理这些启动条件，而不是把容器当作一层新的虚拟机或脚本运行环境。

王子亭的年度小结把 Docker 放在生产平台和构建抽象的语境中。他用 Node.js 为 Dockerfile 做了一个简易 DSL，把 Dockerfile 分成多个段落并结构化保存指令，最后再生成规范格式的 Dockerfile，以便在跨应用、跨语言的构建中更好地利用缓存。来源同时提醒，许多生产容器只是把旧程序跑在容器里；只有应用处理好本地状态、健康检查和信号关闭等生命周期问题，Docker 才更接近 Container Native 的使用方式。

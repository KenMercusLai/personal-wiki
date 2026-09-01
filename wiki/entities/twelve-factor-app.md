---
title: "Twelve-Factor App"
description: "Application methodology used as a reference point for both CLI product design and Docker-oriented deployment practices."
type: "entity"
updated: "2026-09-01"
source_keys: ["jeff-dickey-twelve-factor-cli-apps", "kelsey-hightower-12-fractured-apps"]
entity_kind: "methodology"
---

来源：[12 Factor CLI Apps]({{< relref "/wiki/sources/jeff-dickey-twelve-factor-cli-apps.md" >}})；[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})

Twelve-Factor App 是 Jeff Dickey 来源的命名灵感和方法论背景。Jeff Dickey 将它描述为 Heroku 提出的一组原则，用来帮助 Web 应用更易维护。

Jeff Dickey 的来源并不展开 Twelve-Factor App 的原始十二条，而是借用其结构和精神，为 CLI 应用整理十二个设计因素。文章的转换重点在于：Web 应用关注部署、配置和运行环境的一致性，而 CLI 应用需要额外处理终端帮助、命令输入、流输出、错误诊断、交互与自动化之间的张力。

Kelsey Hightower 的来源则从 Docker 化应用的启动过程看 Twelve-Factor App。文章肯定日志写到 stdout、环境变量传配置等实践在 Docker 中更自然，但也指出许多应用仍然把配置文件、工作目录和数据库可用性当作启动前提，导致团队用容器 entrypoint、绑定挂载或配置管理工具补丁式地弥补应用脆弱性。

在这个语境下，Twelve-Factor App 不只是部署宣言，也是一种应用边界提醒：运行时配置应可注入，应用应直接处理可选配置和外部依赖的短暂不可用，而不是要求部署系统按固定顺序制造唯一的“快乐路径”。

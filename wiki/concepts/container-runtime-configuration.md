---
title: "Container runtime configuration"
description: "在容器启动时注入环境相关配置，而不是为每个环境构建带配置文件的专用镜像。"
type: "concept"
updated: "2026-09-01"
source_keys: ["kelsey-hightower-12-fractured-apps"]
---

来源：[12 Fractured Apps]({{< relref "/wiki/sources/kelsey-hightower-12-fractured-apps.md" >}})

Container runtime configuration 指把环境相关设置留到容器运行时注入，而不是提前打包进镜像。Kelsey Hightower 批评把生产、开发等配置文件烘焙到不同镜像的做法，因为这会制造大量环境专用镜像，并把镜像管理问题误当成部署流程问题。

在这篇来源中，环境变量是 Docker 与 Twelve-Factor App 配合良好的地方：应用可以从默认值或可选配置文件开始，再让 `APP_HOST`、`APP_PORT`、`APP_DATABASE` 等环境变量覆盖运行时差异。这样同一个应用制品可以在不同环境中启动，而不需要每次配置变化都重建镜像。

这个概念并不否认配置管理的价值，而是划清边界：构建镜像时应交付应用制品，运行容器时才注入环境配置。应用本身需要理解这些配置入口，否则部署脚本会被迫复制应用逻辑，并承担额外的同步和维护成本。

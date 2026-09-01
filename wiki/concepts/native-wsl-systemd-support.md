---
title: "Native WSL systemd support"
description: "在 WSL 发行版内通过 /etc/wsl.conf 启用 systemd，而不是继续依赖 Genie 等替代启动层。"
type: "concept"
updated: "2026-09-02"
source_keys: ["clean-wsl-reinstall-windows-10-systemd-support"]
---

来源：[Clean WSL Reinstall for Native systemd on Windows 10]({{< relref "/wiki/sources/clean-wsl-reinstall-windows-10-systemd-support.md" >}})

Native WSL systemd support 指 WSL 直接支持以 systemd 管理发行版内的服务，而不是通过 Genie 之类的兼容层绕开 WSL 的启动模型。来源把这次迁移描述为从长期可用的旧方案回到新的官方路径：Windows 10 获得相关 WSL 功能后，作者不再需要依赖 Genie。

启用方式集中在发行版内部的 `/etc/wsl.conf`。在 `[boot]` 段加入 `systemd=true` 后，需要从 Windows 侧执行 `wsl --shutdown`，让 WSL 重新启动并读取新的启动配置。重新进入发行版后，可以用 `sudo systemctl status time-sync.target` 验证 systemd 是否已经接管服务状态。

这个概念也体现了 WSL 配置的层级差异：`/etc/wsl.conf` 是发行版内配置，适合声明该发行版的启动和互操作行为；系统级 `.wslconfig` 不会随发行版重装自动归零，需要在排查旧环境问题时单独处理。

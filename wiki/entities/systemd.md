---
title: "systemd"
description: "Linux init and service manager; the source explains enabling it natively inside WSL through /etc/wsl.conf."
type: "entity"
updated: "2026-09-02"
source_keys: ["clean-wsl-reinstall-windows-10-systemd-support"]
entity_kind: "software"
---

来源：[Clean WSL Reinstall for Native systemd on Windows 10]({{< relref "/wiki/sources/clean-wsl-reinstall-windows-10-systemd-support.md" >}})

systemd 是这篇来源迁移目标中的核心组件。作者以前通过 Genie 在 WSL 2 中获得 systemd 相关能力，但在 Windows 10 获得 WSL 原生 systemd 支持后，改为使用 WSL 自身提供的启动配置。

来源中的启用方法是在发行版内部创建或编辑 `/etc/wsl.conf`，写入 `[boot]` 和 `systemd=true`。这说明 systemd 是否启用是发行版级启动行为，而不是仅靠重新安装 Windows 侧应用就会自动完成的设置。

修改配置后，作者使用 `wsl --shutdown` 从 Windows 侧干净关闭 WSL，再重新进入 Linux 发行版。验证方式是运行 `sudo systemctl status time-sync.target`，用 systemctl 查看目标单元状态。

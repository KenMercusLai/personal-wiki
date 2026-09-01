---
title: "Clean WSL Reinstall for Native systemd on Windows 10"
description: "A technical note documenting how to remove old WSL distributions, reinstall WSL on Windows 10, and enable native systemd support without Genie."
type: "source"
updated: "2026-09-02"
source_key: "clean-wsl-reinstall-windows-10-systemd-support"
image_status: "not_selected"
---

## 摘要

这篇笔记记录了一次从 Genie 辅助方案迁移到 WSL 原生 systemd 支持的过程。作者此前长期使用 WSL 2 和 Genie 来获得接近 systemd 的启动体验；当 Windows 10 获得与 Windows 11 接近的 WSL systemd 支持后，作者选择清理旧环境并改用官方路径。

卸载部分强调先在管理员 PowerShell 中查看发行版并用 `wsl --unregister` 删除旧发行版，再从 Windows 设置中卸载 Ubuntu、Debian 或其他 Linux 应用。随后在“Turn Windows Features on or off”中关闭 Virtual Machine Platform 和 Windows Subsystem for Linux，并重启系统。

重新安装流程比旧方案更简单：在管理员 PowerShell 中运行 `wsl --install`，重启后等待默认 Ubuntu 安装完成并创建 Linux 用户。如果要换发行版，可用 `wsl --list --online` 查看可用列表，用 `wsl --install -d Debian` 安装 Debian，并用 `wsl --set-default Debian` 设为默认发行版。笔记特别指出，`wsl --set-default-version 2` 已经不再需要。

systemd 的启用发生在发行版内部：创建或编辑 `/etc/wsl.conf`，在 `[boot]` 下设置 `systemd=true`。作者还顺手给出一个可选的 `[interop]` 配置，将 `appendWindowsPath = false` 用于避免 Windows PATH 进入 Linux 自动补全。最后回到管理员 PowerShell 执行 `wsl --shutdown`，重新进入发行版后可用 `sudo systemctl status time-sync.target` 检查 systemd 是否工作。

## 关键观点

- 从 Genie 迁移到 WSL 原生 systemd 时，干净重装可以把旧发行版、Windows Linux 应用和 WSL 相关 Windows Features 一并清理掉。
- 当前安装路径以 `wsl --install` 为核心，默认 WSL 2 行为已经足够，通常不需要再显式设置默认版本。
- WSL 的 systemd 开关属于发行版内的 `/etc/wsl.conf`，而全局 `.wslconfig` 不会因为重装 WSL 自动删除或重置。
- 修改 WSL 启动配置后，应使用 `wsl --shutdown` 做一次干净关闭，再重新进入发行版验证服务状态。

## 相关知识

- [Clean WSL reinstall workflow]({{< relref "/wiki/concepts/clean-wsl-reinstall-workflow.md" >}})
- [Native WSL systemd support]({{< relref "/wiki/concepts/native-wsl-systemd-support.md" >}})
- [Windows Subsystem for Linux]({{< relref "/wiki/entities/windows-subsystem-for-linux.md" >}})
- [systemd]({{< relref "/wiki/entities/systemd.md" >}})

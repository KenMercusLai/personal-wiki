---
title: "Ollama"
type: entity
tags: [ai, inference, local-llm, developer-tools]
sources:
  - using-local-coding-agents
last_updated: 2026-10-14
knowledge_schema: synthesis-v1
---

## Overview
[[Ollama]] is the local model-serving runtime used in the source to download, run, expose, and switch open-weight models for coding-agent harnesses.

## Current Profile
Ollama occupies the middle layer between model weights and an agent harness. It offers command-line and graphical model management, platform-specific variants such as MLX builds for Apple silicon, an OpenAI-compatible endpoint at the local `/v1` base URL, and launch integrations for Codex and Claude Code. The source chooses it for ease of use and interchangeability rather than claiming it is the fastest possible runtime.

## Key Characteristics
- Downloads and runs multiple open-weight models through named local packages.
- Exposes an OpenAI-compatible API that several coding harnesses can consume.
- Provides Apple-silicon MLX variants as well as conventional Linux model builds.
- Can be reached through an SSH tunnel when inference runs on a separate user-controlled host.
- Favors convenient setup and model swapping over maximum runtime specialization.

## Evidence
- Local serving: [[using-local-coding-agents]] uses `ollama pull` and `ollama run` for Qwen3.6 variants on macOS and Linux.
- Harness connection: [[using-local-coding-agents]] configures Qwen Code against `http://127.0.0.1:11434/v1` and uses Ollama with Codex and Claude Code.
- Measurement: [[using-local-coding-agents]] benchmarks long-context prefill, decode, and memory through Ollama metrics plus process and GPU observations.
- Remote host: [[using-local-coding-agents]] forwards local port 11434 over SSH to a DGX-hosted Ollama server.

## Qualifications
The source emphasizes convenience and does not benchmark Ollama against vLLM, SGLang, LM Studio, llama.cpp, or other runtimes under matched conditions. Its memory reporting is imperfect on macOS, and a tunneled or cloud-backed Ollama model is not literally executing on the harness machine. An OpenAI-compatible API also does not guarantee identical semantics or performance across providers.

## What Changed
- Added Ollama as the source's model-serving layer for local coding agents.
- Recorded its OpenAI-compatible harness integration and SSH-tunneled remote-host pattern.

## Relationships
- [[LocalCodingAgents]] - Ollama supplies the inference-runtime layer.
- [[QwenCode]] - Qwen Code connects to Ollama as a custom OpenAI-compatible provider.
- [[Codex]] - Codex can select Ollama through a dedicated profile or launch integration.
- [[ClaudeCode]] - Ollama provides a launch integration for using a local model with Claude Code.
- [[SebastianRaschka]] - practitioner who selected and benchmarked Ollama for the tutorial.

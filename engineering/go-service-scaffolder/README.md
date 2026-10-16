# go-service-scaffolder

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Scaffold a production-ready Go HTTP service with OpenTelemetry observability, TLS, lifecycle management, Dockerfile, GitHub Actions CI/CD, and golangci-lint. Use when creating or regenerating a full Go service skeleton (project layout, config package, server package, CI workflows, and container build files).

## When to use

- Scaffolding a new production Go HTTP service
- You want observability, TLS, graceful shutdown, and CI out of the box

## Contents

```
go-service-scaffolder/
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`golang-testing`](../engineering/golang-testing/) — to test the scaffold
- [`hexagonal-python`](../engineering/hexagonal-python/) — for the architecture inside

## Install

```sh
cp -r engineering/go-service-scaffolder ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [ItalyPaleAle/skills](https://github.com/ItalyPaleAle/skills) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

![Engineering — atlys](../../assets/banner-engineering.svg)

# android-architecture

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

*Activities calling the network directly is how Android apps become unmaintainable. Clean layers, Hilt wiring, boundaries that hold.*

Expert guidance on setting up and maintaining a modern Android application architecture using Clean Architecture and Hilt. Use this when asked about project structure, module setup, or dependency injection.

## When to use

- Structuring an Android app with Clean Architecture and Hilt
- Enforcing layer boundaries in a growing codebase

## Contents

```
android-architecture/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

```mermaid
flowchart LR
    me["android-architecture"]
    me -->|"to test the layers"| p0["android-testing"]
    me -->|"for the UI layer"| p1["android-compose-performance"]
    style me fill:#06b6d4,color:#fff,stroke:none
```

Also: [`android-testing`](../engineering/android-testing/), [`android-compose-performance`](../engineering/android-compose-performance/)

## Install

```sh
cp -r engineering/android-architecture ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

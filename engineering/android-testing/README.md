![Engineering — atlys](../../assets/banner-engineering.svg)

# android-testing

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

*Untested Android code rots fast. Unit, integration, Hilt, screenshots — the full strategy, not just write more tests.*

Comprehensive testing strategy involving Unit, Integration, Hilt, and Screenshot tests.

## When to use

- Setting up an Android testing strategy
- Unit, integration, Hilt, and screenshot tests

## Contents

```
android-testing/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

```mermaid
flowchart LR
    me["android-testing"]
    me -->|"for what you're testing"| p0["android-architecture"]
    style me fill:#06b6d4,color:#fff,stroke:none
```

Also: [`android-architecture`](../engineering/android-architecture/)

## Install

```sh
cp -r engineering/android-testing ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

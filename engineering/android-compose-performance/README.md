![Engineering — atlys](../../assets/banner-engineering.svg)

# android-compose-performance

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

*Jank is death by a thousand recompositions. This finds them from code review — before your users feel them.*

Audit and improve Jetpack Compose runtime performance from code review and architecture. Use when asked to diagnose slow rendering, janky scrolling, excessive recompositions, or performance issues in Compose UI.

> Important: Ensure profiling is done on a release build with R8 enabled. Debug builds have significant overhead.

## When to use

- Diagnosing jank or slow rendering in Jetpack Compose
- Auditing recomposition performance from code review

## Contents

```
android-compose-performance/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

```mermaid
flowchart LR
    me["android-compose-performance"]
    me -->|"for the app structure"| p0["android-architecture"]
    style me fill:#06b6d4,color:#fff,stroke:none
```

Also: [`android-architecture`](../android-architecture/)

## Install

```sh
cp -r engineering/android-compose-performance ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

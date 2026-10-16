![Writing — atlys](../../assets/banner-writing.svg)

# antislop-code

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*AI comments narrate the code back to you — increment counter next to i++. This keeps the comments that earn their place and strips the rest.*

Code comment hygiene for AI coding agents: remove generic AI-slop comments, keep the valuable ones, never touch the code.

> Anti Slop: Rules for AI Coding Agents. Code Comments skill Part of the antislop system. Read together with antislop.md (the core). This skill filters comments that read as generically AI (decorative, restating the obvious, stiff, loud) while preserving the comments that carry real information. It references core rules by number and never duplicates or renumbers them. Load it when the task writes or edits code comments.

## When to use

- Cleaning up AI-generated code comments
- You want comments that explain why, not restate what

## Contents

```
antislop-code/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

```mermaid
flowchart LR
    me["antislop-code"]
    me -->|"the base filter"| p0["antislop-core"]
    me -->|"to keep code complete"| p1["output-skill"]
    style me fill:#f59e0b,color:#fff,stroke:none
```

Also: [`antislop-core`](../writing/antislop-core/), [`output-skill`](../engineering/output-skill/)

## Install

```sh
cp -r writing/antislop-code ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

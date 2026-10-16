![Writing — atlys](../../assets/banner-writing.webp)

# antislop-code

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Code comment hygiene for AI coding agents: remove generic AI-slop comments, keep the valuable ones, never touch the code.

AI comments narrate the code back to you — increment counter next to i++. This keeps the comments that earn their place and strips the rest.

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

- [`antislop-core`](../writing/antislop-core/) — the base filter
- [`output-skill`](../engineering/output-skill/) — to keep code complete

## Install

```sh
cp -r writing/antislop-code ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

# antislop-human

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Human and accessibility skill for antislop. Contrast, keyboard, focus, and states for real people. Includes the contrast checker.

> Anti Slop: Rules for AI Coding Agents. Human skill Part of the antislop system. Read together with antislop.md (the core). This skill deep-dives the human concern: the UI must stay usable by people with different eyes, hands, and setups. Contrast, keyboard, focus, states, and the mobile details that exclude people.

## When to use

- Accessibility review: contrast, keyboard, focus, states
- Designing for real people, not screenshots

## Contents

```
antislop-human/
├── SKILL.md  # the playbook — when to load, how to apply
├── contrast-check.py
└── contrast-mcp.py
```

## Pairs well with

- [`antislop-core`](../writing/antislop-core/) — the base filter
- [`accessibility`](../design/accessibility/) — for deeper a11y QA

## Install

```sh
cp -r writing/antislop-human ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

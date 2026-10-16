# antislop-layoutmobile

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Mobile layout skill for antislop. Use for layouts that reflow across screen sizes, phone to desktop: grids, overflow, tap targets. Load with the core.

Desktop-first thinking breaks on phones: overflow, tiny tap targets, grids that collapse wrong. This is the reflow discipline.

> Anti Slop: Rules for AI Coding Agents. Mobile Layout skill Part of the antislop system. Read together with antislop.md (the core). This skill deep-dives the responsive layout concern: how a layout must reflow across screen sizes, phone to desktop. Breakpoints, scale, grids, overflow, tap targets, and navigation. It references core rules by number and never duplicates or renumbers them. Load it when the task builds or edits a layout that has to hold up at any screen width.

## When to use

- Making layouts reflow from phone to desktop
- Fixing overflow, tap targets, and grid breakage on small screens

## Contents

```
antislop-layoutmobile/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`antislop-core`](../writing/antislop-core/) — the base filter
- [`antislop-ui`](../writing/antislop-ui/) — for the visual layer

## Install

```sh
cp -r writing/antislop-layoutmobile ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

# taste-skill

![design](https://img.shields.io/badge/design-2563eb) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Anti-slop frontend skill for landing pages, portfolios, and redesigns. The agent reads the brief, infers the right design direction, and ships interfaces that do not look templated. Real design systems when applicable, audit-first on redesigns, strict pre-flight check.

> Landing pages, portfolios, and redesigns. Not dashboards, not data tables, not multi-step product UI. Every rule below is contextual. None of it fires automatically. First read the brief, then pull only what fits.

## When to use

- Building a landing page, portfolio, or marketing site from a loose brief
- You want the agent to infer a design direction instead of defaulting to generic AI aesthetics
- Redesigning something that currently looks AI-generated

## Contents

```
taste-skill/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`redesign-skill`](../design/redesign-skill/) — for upgrading existing UIs
- [`antislop-ui`](../writing/antislop-ui/) — to keep the visuals slop-free
- [`premium-frontend-engineering`](../design/premium-frontend-engineering/) — to hand-code the direction it infers

## Install

```sh
cp -r design/taste-skill ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

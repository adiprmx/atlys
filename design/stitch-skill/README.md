![Design — atlys](../../assets/banner-design.svg)

# stitch-skill

![design](https://img.shields.io/badge/design-2563eb) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Semantic Design System Skill for Google Stitch. Generates agent-friendly DESIGN.md files that enforce premium, anti-generic UI standards — strict typography, calibrated color, asymmetric layouts, perpetual micro-motion, and hardware-accelerated performance.

Google Stitch generates UI fast — and generic just as fast. This bakes a real design system into what Stitch produces, so the output has standards, not just speed.

## When to use

- Working with Google Stitch and need an agent-friendly DESIGN.md
- Enforcing a design system through generated UI

## Contents

```
stitch-skill/
├── DESIGN.md
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`taste-skill`](../design/taste-skill/) — for the underlying taste

## Install

```sh
cp -r design/stitch-skill ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

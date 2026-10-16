![Design — atlys](../../assets/banner-design.svg)

# image-to-code-skill

![design](https://img.shields.io/badge/design-2563eb) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Elite website image-to-code skill. Generate the design images first, deeply analyze them, then implement the website to match them as closely as possible.

When you already know what it should look like, don't let the agent reinterpret. Generate the reference, analyze it deeply, match it.

## When to use

- You have design images and want code that matches them closely
- Fidelity to a reference matters more than creative reinterpretation

## Contents

```
image-to-code-skill/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`taste-skill`](../design/taste-skill/) — to judge the result
- [`premium-frontend-engineering`](../design/premium-frontend-engineering/) — for the implementation pass

## Install

```sh
cp -r design/image-to-code-skill ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

# worker-resource-budgeting

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Budgets RAM before fanning out parallel workers that each load the full intent brain, so verification workers never starve the live bot — use before any parallel verification, dedupe, or probe fan-out.

Sixteen workers on a small box doesn't make things faster. This budgets RAM first so workers don't starve each other.

## When to use

- Fanning out parallel workers on a constrained machine
- Verification workers are starving the live system

## Contents

```
worker-resource-budgeting/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`batch-run-integrity`](../engineering/batch-run-integrity/) — for the batch discipline

## Install

```sh
cp -r engineering/worker-resource-budgeting ~/.claude/skills/  # or your agent's skills directory
```

## Source

Original to atlys — created and curated by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

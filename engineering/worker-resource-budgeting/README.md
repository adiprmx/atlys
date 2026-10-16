# worker-resource-budgeting

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Budgets RAM before fanning out parallel workers that each load the full intent brain, so verification workers never starve the live bot — use before any parallel verification, dedupe, or probe fan-out.

## Contents

```
worker-resource-budgeting/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Install

```sh
cp -r engineering/worker-resource-budgeting ~/.claude/skills/  # or your agent's skills directory
```

## Source

Original to atlys — created and curated by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

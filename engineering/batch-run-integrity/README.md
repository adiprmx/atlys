![Engineering — atlys](../../assets/banner-engineering.svg)

# batch-run-integrity

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*Long runs lie. Done when half the chunks failed, progress lost on interrupt. This makes batch jobs resumable and completion claims checkable.*

Keeps long multi-chunk batch jobs honest and resumable — incremental on-disk checkpoints, completion claims reconciled against artifacts on disk, race-sensitive allocations re-verified at deploy time; use for serapan, tumpah-ilmu, mining, or any batch run.

## When to use

- Running long multi-chunk batch jobs
- You need resumability and honest completion tracking

## Contents

```
batch-run-integrity/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`worker-resource-budgeting`](../engineering/worker-resource-budgeting/) — to size the worker pool
- [`intent-pattern-qa`](../engineering/intent-pattern-qa/) — to verify patterns

## Install

```sh
cp -r engineering/batch-run-integrity ~/.claude/skills/  # or your agent's skills directory
```

## Source

Original to atlys — created and curated by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

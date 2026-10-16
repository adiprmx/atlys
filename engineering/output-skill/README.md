# output-skill

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. Apply to any task requiring exhaustive, unabridged output.

## When to use

- The agent keeps truncating code or leaving placeholder comments
- Long generations that must survive token limits cleanly

## Contents

```
output-skill/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`intent-pattern-qa`](../engineering/intent-pattern-qa/) — to verify generated patterns
- [`batch-run-integrity`](../engineering/batch-run-integrity/) — for long honest runs

## Install

```sh
cp -r engineering/output-skill ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

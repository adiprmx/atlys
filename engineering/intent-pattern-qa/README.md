# intent-pattern-qa

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Dynamic QA checklist that catches silent regex-pattern death (patterns that compile but never match) via positive-match probes and byte-level asserts — use when authoring or verifying intent batches.

## Contents

```
intent-pattern-qa/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Install

```sh
cp -r engineering/intent-pattern-qa ~/.claude/skills/  # or your agent's skills directory
```

## Source

Original to atlys — created and curated by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

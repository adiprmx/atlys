![Engineering — atlys](../../assets/banner-engineering.svg)

# output-skill

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*The classic agent failure: code that trails off into placeholder comments. This bans truncation and placeholders, period.*

Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly.

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

```mermaid
flowchart LR
    me["output-skill"]
    me -->|"to verify generated patterns"| p0["intent-pattern-qa"]
    me -->|"for long honest runs"| p1["batch-run-integrity"]
    style me fill:#06b6d4,color:#fff,stroke:none
```

Also: [`intent-pattern-qa`](../intent-pattern-qa/), [`batch-run-integrity`](../batch-run-integrity/)

## Install

```sh
cp -r engineering/output-skill ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

# golang-error-handling

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Idiomatic Golang error handling — creation, wrapping with %w, errors.Is/As, errors.Join, custom error types, sentinel errors, panic/recover, the single handling rule, structured logging with slog, HTTP request logging middleware, and samber/oops for production errors. Built to make logs usable at scale with log aggregation 3rd-party tools. Apply when creating, wrapping, inspecting, or logging errors in Go code. For samber/oops specifics → See `samber/cc-skills-golang@golang-samber-oops` skill; for slog handler ecosystem → See `samber/cc-skills-golang@golang-samber-slog` skill.

> Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-error-handling skill takes precedence.

## Contents

```
golang-error-handling/
├── evals/  # evaluation cases
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Install

```sh
cp -r engineering/golang-error-handling ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

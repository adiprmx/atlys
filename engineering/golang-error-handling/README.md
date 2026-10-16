![Engineering — atlys](../../assets/banner-engineering.svg)

# golang-error-handling

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*if err != nil on every line isn't a strategy. Wrapping, sentinels, errors.Is and As — errors as design, not afterthought.*

Idiomatic Golang error handling — creation, wrapping with %w, errors.Is/As, errors.Join, custom error types, sentinel errors, panic/recover, the single handling rule, structured logging with slog, HTTP request logging middleware, and samber/oops for production errors. Built to make logs usable at scale with log aggregation 3rd-party tools.

> Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-error-handling skill takes precedence.

## When to use

- Designing error handling in a Go codebase
- Wrapping, sentinel errors, and errors.Is/As/Join usage

## Contents

```
golang-error-handling/
├── evals/  # evaluation cases
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

```mermaid
flowchart LR
    me["golang-error-handling"]
    me -->|"for the concurrency side"| p0["golang-concurrency"]
    me -->|"to test it"| p1["golang-testing"]
    style me fill:#06b6d4,color:#fff,stroke:none
```

Also: [`golang-concurrency`](../engineering/golang-concurrency/), [`golang-testing`](../engineering/golang-testing/)

## Install

```sh
cp -r engineering/golang-error-handling ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

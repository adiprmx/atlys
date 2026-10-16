# golang-concurrency

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Golang concurrency design — goroutine lifecycle and leak prevention, channels and `select`, channel ownership and direction, `sync.Mutex`/`RWMutex`/`sync.Map`/`sync.Once`/atomics, `errgroup`, `singleflight`, worker pools, and fan-out/fan-in pipelines. Use when writing or reviewing concurrent Go code, when choosing between channels and mutexes, when protecting a shared map or counter, or when a goroutine has no clear exit. Not for defensive coding unrelated to concurrency such as nil panics, slice aliasing, or numeric overflow (→ See `samber/cc-skills-golang@golang-safety` skill), and not for debugging a specific hung, crashing, or racing program after the fact (→ See `samber/cc-skills-golang@golang-troubleshooting` skill).

> Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-concurrency skill takes precedence.

## When to use

- Writing or reviewing concurrent Go code
- Choosing between channels and mutexes; preventing goroutine leaks

## Contents

```
golang-concurrency/
├── evals/  # evaluation cases
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`golang-error-handling`](../engineering/golang-error-handling/) — for error design in concurrent code
- [`golang-testing`](../engineering/golang-testing/) — to test it

## Install

```sh
cp -r engineering/golang-concurrency ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

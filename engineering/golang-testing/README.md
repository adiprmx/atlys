![Engineering — atlys](../../assets/banner-engineering.svg)

# golang-testing

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Production-ready Golang tests — table-driven tests, testify suites and mocks, parallel tests, fuzzing, fixtures, goroutine leak detection with goleak, snapshot testing, code coverage, integration tests, idiomatic test naming. Use when writing or reviewing Go tests, choosing a testing approach, setting up Go test CI, or debugging flaky/slow tests. For testify-specific APIs see `samber/cc-skills-golang@golang-stretchr-testify`; for measurement methodology see `samber/cc-skills-golang@golang-benchmark`.

Tests that actually protect a Go codebase: table-driven, parallel-safe, fuzzed where it matters, mocked where it must be.

> Community default. A company skill that explicitly supersedes samber/cc-skills-golang@golang-testing skill takes precedence.

## When to use

- Writing production-ready Go tests
- Table-driven tests, mocks, fuzzing, and parallel tests

## Contents

```
golang-testing/
├── evals/  # evaluation cases
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`golang-concurrency`](../engineering/golang-concurrency/) — for what you're testing
- [`go-service-scaffolder`](../engineering/go-service-scaffolder/) — for the service layout

## Install

```sh
cp -r engineering/golang-testing ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

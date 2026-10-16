<div align="center">
  <img src="../../assets/icon.webp" width="72" alt="atlys">
</div>

# golang-concurrency

![category](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

> Golang concurrency design — goroutine lifecycle and leak prevention, channels and `select`, channel ownership and direction, `sync.Mutex`/`RWMutex`/`sync.Map`/`sync.Once`/atomics, `errgroup`, `singleflight`, worker pools, and fan-out/fan-in pipelines. Use when writing or reviewing concurrent Go code, when choosing between channels and mutexes, when protecting a shared map or counter, or when a goroutine has no clear exit. Not for defensive coding unrelated to concurrency such as nil panics, slice aliasing, or numeric overflow (→ See `samber/cc-skills-golang@golang-safety` skill), and not for debugging a specific hung, crashing, or racing program after the fact (→ See `samber/cc-skills-golang@golang-troubleshooting` skill).

## 📂 What's inside

```
golang-concurrency/
├── evals/
├── references/
└── SKILL.md
```

**`SKILL.md`** is the full playbook — when to load this skill and how to apply it. Copy this whole folder into your agent's skills directory to install it.

## 📜 Source

Adapted from [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT). Curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [**atlys**](../../) — a curated collection of skills for AI coding agents.

![Design — atlys](../../assets/banner-design.svg)

# impeccable-design

![design](https://img.shields.io/badge/design-2563eb) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*The full teardown: UX, hierarchy, accessibility, responsive, theming, anti-patterns. Then iterate on the real thing in a live browser, not in theory.*

Use when the user wants to design, redesign, shape, critique, audit, polish, clarify, distill, harden, optimize, adapt, animate, colorize, extract, or otherwise improve a frontend interface. Covers websites, landing pages, dashboards, product UI, app shells, components, forms, settings, onboarding, and empty states. Handles UX review, visual hierarchy, information architecture, cognitive load, accessibility, performance, responsive behavior, theming, anti-patterns, typography, fonts, spacing, layout, alignment, color, motion, micro-interactions, UX copy, error states, edge cases, i18n, and reusable design systems or tokens. Also use for bland designs that need to become bolder or more delightful, loud designs that should become quieter, live browser iteration on UI elements, or ambitious visual effects that should feel technically extraordinary. Not for backend-only or non-UI tasks.

## When to use

- A full review pass: UX, hierarchy, accessibility, responsive behavior, theming
- Iterating on a live UI in the browser with real feedback

## Contents

```
impeccable-design/
├── agents/  # subagent definitions
├── reference/  # reference docs
├── scripts/  # helper scripts
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`antislop-ui`](../writing/antislop-ui/) — for the slop filter
- [`accessibility`](../design/accessibility/) — to cover a11y in the review

## Install

```sh
cp -r design/impeccable-design ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [pbakaus/impeccable](https://github.com/pbakaus/impeccable) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

![Design — atlys](../../assets/banner-design.webp)

# imagegen-frontend-mobile

![design](https://img.shields.io/badge/design-2563eb) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Elite mobile app image-generation skill for creating premium, app-native screen concepts and flows. Designed for iOS, Android, and cross-platform mobile products. Prioritizes clean hierarchy, comfortably readable text, strong multi-screen consistency, controlled color palettes, non-generic creative direction, textured surfaces, image-led composition, tasteful custom iconography, and clean phone mockup framing. By default, screens should be shown inside a subtle premium iPhone or similar phone mockup with a visible frame, while the main focus stays on the app content itself. This skill generates images only. It does not write code.

Mobile flows are hard to judge from descriptions. See the screens first — in phone frames, with a consistent hand — then decide what to build.

## When to use

- Concepting mobile app screens (iOS/Android) as image references
- Exploring app flows before committing to code

## Contents

```
imagegen-frontend-mobile/
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Pairs well with

- [`frontend-image-direction`](../design/frontend-image-direction/) — to implement without drift

## Install

```sh
cp -r design/imagegen-frontend-mobile ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

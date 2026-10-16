# AGENTS.md

Instructions for AI agents working in this repository.

## What this repo is

atlys is a curated collection of 47 skills for AI coding agents.
Skills live in three categories: `design/` (17), `writing/` (12), `engineering/` (18).
Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description` required),
an optional `skill.yaml`, and a hand-written `README.md`.

## Rules

- **Don't touch the brand visuals** unless explicitly asked: `assets/hero.svg`,
  `assets/icon.svg`, `assets/banner-design.svg`, `assets/banner-writing.svg`,
  `assets/banner-engineering.svg` are locked.
- **Keep the main README lean.** It was deliberately cut from 269 to 185 lines.
  No yapping, no generic cards, no emoji soup. Copy is human-voiced, mostly English.
- **Every skill needs real substance.** No thin stubs. The bar: each `SKILL.md`
  should be genuinely useful on its own (the collection averages ~12k characters).
- **Frontmatter is mandatory** on every `SKILL.md`: `name` and `description`.
- **Attribute sources.** Skills adapted from external work credit the source in
  their README and in the main Credits section.
- `skills/` contains symlinks to the category folders for Claude Code plugin
  discovery — don't edit through them, edit the real folders.

## Before pushing

Run the validator — it must pass clean:

```sh
python3 tools/validate.py
```

It checks frontmatter on all 47 skills, per-category counts, badge accuracy,
and relative links. Fix everything it flags.

## Versioning

Bump `CHANGELOG.md` with every user-facing change (newest entry on top,
format `## YYYY-MM-DD — vX.Y.Z`). The README's skills badge count must match
the real total.

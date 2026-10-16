<div align="center">

# atlys

**A curated collection of skills for AI coding agents.**

[![Skills](https://img.shields.io/badge/skills-29-2563eb)](https://github.com/adiprmx/atlys)
[![License: MIT](https://img.shields.io/badge/License-MIT-16a34a.svg)](LICENSE)

*Design taste, anti-slop writing, and engineering QA — as drop-in playbooks.*

</div>

---

## Why atlys exists

Most AI-generated output looks AI-generated: templated layouts, filler prose, placeholder comments, lifeless copy. atlys is a hand-picked arsenal against that — 28 field-tested skill playbooks that make agents produce work with **taste**: interfaces that feel designed, prose that reads human, and code that ships complete.

Each skill is a self-contained folder. No build step, no dependencies, no lock-in — just markdown (plus a few helper scripts) your agent reads when the task calls for it.

## Quick start

```sh
git clone https://github.com/adiprmx/atlys.git

# copy any skill into your agent's skills directory, e.g.:
cp -r atlys/local-taste-skill ~/.config/your-agent/skills/
cp -r atlys/antislop-core  ~/.config/your-agent/skills/
```

Then tell your agent to load the skill when relevant — or wire it into your agent's skill discovery so it's picked up automatically. See [Anatomy of a skill](#anatomy-of-a-skill).

## The collection

<details>
<summary><strong>🎨 Design & frontend</strong> — 15 skills</summary>

| Skill | What it does |
|---|---|
| `local-taste-skill` | Anti-slop frontend for landing pages, portfolios, and redesigns. Reads the brief, infers the right design direction, and ships interfaces that don't look templated. Strict pre-flight check included. |
| `local-taste-skill-v1` | The original v1 of taste-skill, preserved for projects depending on its exact behavior. |
| `local-redesign-skill` | Upgrades existing websites and apps to premium quality without breaking functionality. Audit-first; hunts down generic AI patterns. |
| `local-soft-skill` | High-end agency style: exact fonts, spacing, shadows, card structures, and animations that make a site feel expensive. |
| `local-minimalist-skill` | Clean editorial interfaces — warm monochrome, typographic contrast, flat bento grids. No gradients, no heavy shadows. |
| `local-brutalist-skill` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. For data-heavy dashboards and portfolios that should feel like declassified blueprints. |
| `local-stitch-skill` | Semantic design-system skill for Google Stitch. Generates agent-friendly `DESIGN.md` files enforcing premium, anti-generic UI standards. |
| `local-brandkit` | Premium brand-kit image generation: logo systems, identity decks, and brand-guideline boards across minimalist, cinematic, editorial, dark-tech, luxury, and more. |
| `local-gpt-tasteskill` | Elite UX/UI plus advanced GSAP motion engineering — AIDA page structure, wide editorial typography, gapless bento grids, strict ScrollTriggers. |
| `local-imagegen-frontend-web` | Generates premium, conversion-aware website design references — one horizontal image per section, one consistent palette. |
| `local-imagegen-frontend-mobile` | Premium mobile app screen concepts and flows (iOS/Android/cross-platform), presented in phone mockups. Image generation only. |
| `local_frontend_image_direction` | Section references, mobile screen concepts, and brand-consistent image sets with locked cross-image consistency — then implements from the references without design drift. |
| `local-image-to-code-skill` | Generates the design images first, analyzes them deeply, then implements the website to match as closely as possible. |
| `local_premium_frontend_engineering` | Premium hand-coded frontend: brief-driven design dials, bias-corrected typography and color, intentional GSAP/Motion choreography, strict pre-flight check. |
| `impeccable-design` | Full-spectrum frontend improvement — UX review, visual hierarchy, accessibility, responsive behavior, theming, anti-patterns — plus live-browser iteration on real UI. |

</details>

<details>
<summary><strong>✍️ Anti-AI-slop writing</strong> — 10 skills</summary>

| Skill | What it does |
|---|---|
| `antislop-core` | The core filter. Rules every AI coding agent should follow to stop generic AI slop. Load always. |
| `antislop-ui` | The visual companion to the core: color, layout, components, and motion without the slop. |
| `antislop-copywriting` | Headlines, tone, CTAs, and anti-AI-writing patterns for prose that persuades. |
| `antislop-code` | Code comment hygiene: strip generic AI-slop comments, keep the valuable ones, never touch the code. |
| `antislop-human` | Human-first and accessible: contrast, keyboard, focus, and states for real people. Ships a contrast checker. |
| `antislop-layoutmobile` | Layouts that reflow gracefully from phone to desktop: grids, overflow, tap targets. |
| `ext-humanizer` | Turns AI-scented writing into human-sounding prose without changing the content. Built on Wikipedia's *"Signs of AI writing"* research. |
| `ext-stop-slop` | Cuts AI rhetoric and filler: 8 core rules, banned-phrase lists, quick checks, and per-dimension scoring. |
| `ext-no-ai-slop` | Two modes — **Edit** (minimum effective edit, with a changelog) and **Detect** (name the pattern, quote the line, suggest the fix). |
| `ext-avoid-ai-writing` | A strict editing contract (detect ≠ judge ≠ edit), tiered pattern catalog, voice profiles, and iterate-to-convergence passes. |

</details>

<details>
<summary><strong>⚙️ Engineering & QA</strong> — 4 skills</summary>

| Skill | What it does |
|---|---|
| `local-output-skill` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. |
| `local-intent-pattern-qa` | Catches silent regex-pattern death — patterns that compile but never match — via positive-match probes and byte-level asserts. |
| `local-batch-run-integrity` | Keeps long multi-chunk batch jobs honest and resumable: incremental on-disk checkpoints, completion claims reconciled against artifacts on disk. |
| `local-worker-resource-budgeting` | Budgets RAM before fanning out parallel workers, so verification workers never starve the live system. |

</details>

> **Total: 29 skills.** The collection grows — check back for new additions.

## Anatomy of a skill

```
local-taste-skill/
├── SKILL.md        # the playbook: when to load it, how to apply it
├── skill.yaml      # machine-readable metadata (name, description)
└── scripts/        # optional helper scripts (only some skills)
```

`SKILL.md` starts with frontmatter (`name`, `description`, `allowed-tools`) so agents can index and auto-load it. Everything else is plain markdown written to be read by both humans and models.

## Credits

atlys is **curated and maintained by [adiprmx](https://github.com/adiprmx)** — skill selection, naming, `skill.yaml` metadata, Indonesian-language adaptations, and ongoing expansion of select skills.

Several skills are adapted from excellent open-source work. They retain their original licenses (see each skill folder), and this collection wouldn't exist without them:

- `antislop-*` family — [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)
- `local-*` design skills — [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- `ext-humanizer` — [blader/humanizer](https://github.com/blader/humanizer)
- `ext-stop-slop` — [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- `ext-no-ai-slop` — [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- `ext-avoid-ai-writing` — [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- `impeccable-design` — originally [pbakaus/impeccable](https://github.com/pbakaus/impeccable), significantly expanded

## Contributing

Found a skill worth including, or improved one that's here? Open an issue or PR with:

1. The skill folder (`SKILL.md` + `skill.yaml` required)
2. A one-paragraph description of what makes it non-generic
3. Its provenance — original work or adapted (with source link)

## License

MIT — see [LICENSE](LICENSE). Skills adapted from external sources remain under their original licenses.

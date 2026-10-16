# atlys

A curated collection of skills for AI coding agents — frontend design, anti-AI-slop writing, and engineering QA. Each skill is a self-contained folder with a `SKILL.md` playbook (plus `skill.yaml` metadata where available). Copy the ones you need into your agent's skills directory and go.

## Install

```sh
git clone https://github.com/adiprmx/atlys.git
# copy any skill folder into your agent's skills directory, e.g.:
cp -r atlys/local-taste-skill ~/.config/your-agent/skills/
```

No build step, no dependencies. A skill is just markdown (plus optional helper scripts).

## Design & frontend

| Skill | What it does |
|---|---|
| `local-taste-skill` | Anti-slop frontend for landing pages, portfolios, redesigns. Reads the brief, infers the right design direction, ships interfaces that don't look templated. |
| `local-taste-skill-v1` | Original v1 of taste-skill, kept for exact backward compatibility. |
| `local-redesign-skill` | Upgrades existing sites/apps to premium quality without breaking functionality. Audit-first, anti-generic-AI-patterns. |
| `local-soft-skill` | High-end agency style: exact fonts, spacing, shadows, card structures, animations that make a site feel expensive. |
| `local-minimalist-skill` | Clean editorial interfaces. Warm monochrome, typographic contrast, flat bento grids. No gradients, no heavy shadows. |
| `local-brutalist-skill` | Raw mechanical interfaces: Swiss typographic print meets military terminal aesthetics. For data-heavy dashboards and portfolios. |
| `local-stitch-skill` | Semantic design-system skill for Google Stitch. Generates agent-friendly `DESIGN.md` files enforcing premium, anti-generic UI standards. |
| `local-brandkit` | Premium brand-kit image generation: logo systems, identity decks, brand-guideline boards across 10+ visual styles. |
| `local-gpt-tasteskill` | Elite UX/UI plus advanced GSAP motion engineering with AIDA page structure and editorial typography. |
| `local-imagegen-frontend-web` | Generates premium, conversion-aware website design references — one image per section, consistent palette. |
| `local-imagegen-frontend-mobile` | Premium mobile app screen concepts and flows (iOS/Android), shown in phone mockups. Image generation only. |
| `local_frontend_image_direction` | Section references, mobile screen concepts, and brand-consistent image sets with locked cross-image consistency, then implements without design drift. |
| `local-image-to-code-skill` | Generates design images first, analyzes them deeply, then implements the website to match as closely as possible. |
| `local_premium_frontend_engineering` | Premium coded frontend with brief-driven design dials, bias-corrected typography/color, intentional motion choreography, strict pre-flight check. |
| `impeccable-design` | Full-spectrum frontend improvement: UX review, visual hierarchy, accessibility, responsive behavior, theming, anti-patterns, plus live-browser iteration. |

## Anti-AI-slop writing

| Skill | What it does |
|---|---|
| `antislop-core` | The core filter. Rules for AI coding agents to stop generic AI slop. Load always. |
| `antislop-ui` | UI/visual companion: color, layout, components, motion without the slop. |
| `antislop-copywriting` | Headlines, tone, CTAs, and anti-AI-writing patterns for prose. |
| `antislop-code` | Code comment hygiene: remove generic AI-slop comments, keep the valuable ones, never touch the code. |
| `antislop-human` | Human + accessibility: contrast, keyboard, focus, and states for real people. Includes a contrast checker. |
| `antislop-layoutmobile` | Layouts that reflow across screen sizes, phone to desktop: grids, overflow, tap targets. |
| `ext-humanizer` | Turns AI-scented writing into human-sounding prose without changing the content. Based on Wikipedia's "Signs of AI writing" research. |
| `ext-stop-slop` | Cuts AI rhetoric and filler: 8 core rules, banned-phrase lists, quick checks, per-dimension scoring. |
| `ext-no-ai-slop` | Two modes: Edit (minimum effective edit) and Detect (name the pattern, quote the line, suggest the fix). |
| `ext-avoid-ai-writing` | Strict editing contract (detect ≠ judge ≠ edit), tiered pattern catalog, voice profiles, iterate-to-convergence. Calibrated for English; structural guidance for other languages. |

## Engineering & QA

| Skill | What it does |
|---|---|
| `local-output-skill` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, handles token-limit splits cleanly. |
| `local-intent-pattern-qa` | Catches silent regex-pattern death (patterns that compile but never match) via positive-match probes and byte-level asserts. |
| `local-batch-run-integrity` | Keeps long multi-chunk batch jobs honest and resumable: incremental on-disk checkpoints, completion claims reconciled against artifacts on disk. |
| `local-worker-resource-budgeting` | Budgets RAM before fanning out parallel workers so verification workers never starve the live system. |

## Attribution

Original skills in this collection were created by [adiprmx](https://github.com/adiprmx). The following are adapted from external sources and retain their original licenses — see each skill folder for details:

- `antislop-*` family — adapted from [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)
- `ext-humanizer` — adapted from [blader/humanizer](https://github.com/blader/humanizer)
- `ext-stop-slop` — adapted from [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- `ext-no-ai-slop` — adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- `ext-avoid-ai-writing` — adapted from [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- `impeccable-design` — adapted from [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

## License

MIT — see [LICENSE](LICENSE). External skills above remain under their original licenses.

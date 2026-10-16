![atlys — a curated collection of skills for AI coding agents](assets/hero.svg)

<div align="center">

**A curated collection of skills for AI coding agents.**

[![Skills](https://img.shields.io/badge/skills-47-2563eb)](https://github.com/adiprmx/atlys)
[![Release](https://img.shields.io/github/v/release/adiprmx/atlys)](https://github.com/adiprmx/atlys/releases)
[![License: MIT](https://img.shields.io/badge/License-MIT-16a34a.svg)](LICENSE)

*Design taste, anti-slop writing, and engineering QA — as drop-in playbooks.*

</div>

---

## Why atlys exists

You know the look. The landing page with the centered hero, the three feature cards, the purple gradient. The paragraph that starts "In today's fast-paced digital landscape." The code comment that says `// increment the counter` next to `i++`.

That's AI slop — output shaped by the average of everything, reviewed by no one. And it's everywhere, because the default behavior of every AI agent is to produce it.

atlys is 47 skill playbooks that fight the default. Each one is a self-contained folder your agent reads when the task calls for it: how to read a design brief before touching code, how to hear the AI-ness in your own prose, how to structure a backend so it survives contact with reality.

No build step. No dependencies. No lock-in. Just markdown (plus a few helper scripts) — curated, not scraped.

### Slop vs taste

Same task, different input. Ask an agent to "make a landing page":

| Without atlys | With `taste-skill` |
|---|---|
| Centered hero, gradient text, three cards | Reads your brief first, picks a direction on purpose |
| "In today's fast-paced world…" | Copy that sounds like it was written by someone |
| Looks like the last 500 AI landing pages | Looks like a decision was made |

Ask it to "clean up this draft":

| Without atlys | With `humanizer` + `stop-slop` |
|---|---|
| Fixes typos, keeps the AI rhythm | Cuts the throat-clearing, fixes the voice |
| "Moreover, it's worth noting…" survives | Every sentence earns its place |

The difference isn't magic. It's just taste, written down.

### Start here

**I build interfaces** → `taste-skill` + `antislop-core`. The design direction and the slop filter. Add `redesign-skill` if you're fixing something existing, `accessibility` before you ship.

**I write** → `antislop-core` + `humanizer` + `stop-slop`. The filter, the voice fix, the cut. Add `avoid-ai-writing` when you need the process to be repeatable.

**I build backends** → `hexagonal-python` (or `golang-*`) + `docker-compose-patterns` + `output-skill`. Architecture, containers, and the guarantee the code comes out complete.

Then browse [the collection](#the-collection) and take what matches your work. You don't need all 47.

## Quick start

```sh
git clone https://github.com/adiprmx/atlys.git

# copy any skill into your agent's skills directory, e.g. for Claude Code:
cp -r atlys/design/taste-skill ~/.claude/skills/
cp -r atlys/writing/antislop-core ~/.claude/skills/
```

Then tell your agent to load the skill when relevant — or wire it into your agent's skill discovery so it's picked up automatically. Every skill ships with `SKILL.md` frontmatter (`name`, `description`) so agents that auto-index skills just work. See [Anatomy of a skill](#anatomy-of-a-skill).

```mermaid
flowchart LR
    A["Pick a skill<br/>from the collection"] --> B["Copy the folder<br/>to your agent's skills dir"]
    B --> C["Agent reads SKILL.md<br/>when the task matches"]
    C --> D["Output with taste:<br/>designed UI, human prose,<br/>complete code"]
```

## The atlys bar

Not every skill on the internet belongs here. A skill makes it into atlys only if:

1. **It changes the output.** Reading it must visibly change what the agent produces — not restate the obvious.
2. **It's specific.** Concrete rules, real examples, named anti-patterns. Vague advice ("write clean code") doesn't make the cut.
3. **It's field-tested.** Either proven in real projects or distilled from recognized expert sources.
4. **It respects the reader.** No filler, no motivational fluff, no 500 lines saying what 50 could.

Skills that are thin, generic, or duplicated by a stronger skill already in the collection get cut or merged. The collection is curated, not scraped.

## Repository structure

```
atlys/
├── assets/                  # brand visuals (hero, icon, category banners)
├── design/                  # 🎨 17 frontend & design skills
│   ├── taste-skill/
│   ├── redesign-skill/
│   └── ...
├── writing/                 # ✍️ 12 anti-AI-slop writing skills
│   ├── antislop-core/
│   ├── humanizer/
│   └── ...
├── engineering/             # ⚙️ 18 engineering, backend & QA skills
│   ├── output-skill/
│   └── ...
├── README.md
├── CHANGELOG.md
└── LICENSE
```

## Browse the collection

| [![Design — 17 skills](assets/banner-design.svg)](design/) | [![Writing — 12 skills](assets/banner-writing.svg)](writing/) | [![Engineering — 18 skills](assets/banner-engineering.svg)](engineering/) |
|:---:|:---:|:---:|
| **Design** — interfaces with taste<br/><sub>Start with `taste-skill` · `impeccable-design`</sub> | **Writing** — prose that reads human<br/><sub>Start with `antislop-core` · `humanizer`</sub> | **Engineering** — backends that ship<br/><sub>Start with `output-skill` · `hexagonal-python`</sub> |

## The collection

<details>
<summary><strong>🎨 Design & frontend</strong> — <a href="design/">design/</a> · 17 skills</summary>

| Skill | What it does |
|---|---|
| `taste-skill` | Anti-slop frontend for landing pages, portfolios, and redesigns. Reads the brief, infers the right design direction, and ships interfaces that don't look templated. Strict pre-flight check included. |
| `taste-skill-v1` | The original v1 of taste-skill, preserved for projects depending on its exact behavior. |
| `redesign-skill` | Upgrades existing websites and apps to premium quality without breaking functionality. Audit-first; hunts down generic AI patterns. |
| `soft-skill` | High-end agency style: exact fonts, spacing, shadows, card structures, and animations that make a site feel expensive. |
| `minimalist-skill` | Clean editorial interfaces — warm monochrome, typographic contrast, flat bento grids. No gradients, no heavy shadows. |
| `brutalist-skill` | Raw mechanical interfaces fusing Swiss typographic print with military terminal aesthetics. For data-heavy dashboards and portfolios that should feel like declassified blueprints. |
| `stitch-skill` | Semantic design-system skill for Google Stitch. Generates agent-friendly `DESIGN.md` files enforcing premium, anti-generic UI standards. |
| `brandkit` | Premium brand-kit image generation: logo systems, identity decks, and brand-guideline boards across minimalist, cinematic, editorial, dark-tech, luxury, and more. |
| `gpt-tasteskill` | Elite UX/UI plus advanced GSAP motion engineering — AIDA page structure, wide editorial typography, gapless bento grids, strict ScrollTriggers. |
| `imagegen-frontend-web` | Generates premium, conversion-aware website design references — one horizontal image per section, one consistent palette. |
| `imagegen-frontend-mobile` | Premium mobile app screen concepts and flows (iOS/Android/cross-platform), presented in phone mockups. Image generation only. |
| `frontend-image-direction` | Section references, mobile screen concepts, and brand-consistent image sets with locked cross-image consistency — then implements from the references without design drift. |
| `image-to-code-skill` | Generates the design images first, analyzes them deeply, then implements the website to match as closely as possible. |
| `premium-frontend-engineering` | Premium hand-coded frontend: brief-driven design dials, bias-corrected typography and color, intentional GSAP/Motion choreography, strict pre-flight check. |
| `impeccable-design` | Full-spectrum frontend improvement — UX review, visual hierarchy, accessibility, responsive behavior, theming, anti-patterns — plus live-browser iteration on real UI. |
| `accessibility` | Web accessibility and usability QA, especially for users with disabilities. Expert-curated guidance that catches the common pitfalls in AI-generated markup. |
| `accessibility-testing` | Practical methodology for testing the accessibility of a web project. |

</details>

<details>
<summary><strong>✍️ Anti-AI-slop writing</strong> — <a href="writing/">writing/</a> · 12 skills</summary>

| Skill | What it does |
|---|---|
| `antislop-core` | The core filter. Rules every AI coding agent should follow to stop generic AI slop. Load always. |
| `antislop-ui` | The visual companion to the core: color, layout, components, and motion without the slop. |
| `antislop-copywriting` | Headlines, tone, CTAs, and anti-AI-writing patterns for prose that persuades. |
| `antislop-code` | Code comment hygiene: strip generic AI-slop comments, keep the valuable ones, never touch the code. |
| `antislop-human` | Human-first and accessible: contrast, keyboard, focus, and states for real people. Ships a contrast checker. |
| `antislop-layoutmobile` | Layouts that reflow gracefully from phone to desktop: grids, overflow, tap targets. |
| `humanizer` | Turns AI-scented writing into human-sounding prose without changing the content. Built on Wikipedia's *"Signs of AI writing"* research. |
| `stop-slop` | Cuts AI rhetoric and filler: 8 core rules, banned-phrase lists, quick checks, and per-dimension scoring. |
| `no-ai-slop` | Two modes — **Edit** (minimum effective edit, with a changelog) and **Detect** (name the pattern, quote the line, suggest the fix). |
| `avoid-ai-writing` | A strict editing contract (detect ≠ judge ≠ edit), tiered pattern catalog, voice profiles, and iterate-to-convergence passes. |
| `crafting-effective-readmes` | README writing matched to your audience — templates and guidance for READMEs that actually get read. |
| `writing-quality` | Applies to every turn that drafts human-facing prose (chat replies, explanations, emails). Quality from a different angle than de-slopping. |

</details>

<details>
<summary><strong>⚙️ Engineering & QA</strong> — <a href="engineering/">engineering/</a> · 18 skills</summary>

| Skill | What it does |
|---|---|
| `output-skill` | Overrides default LLM truncation behavior. Enforces complete code generation, bans placeholder patterns, and handles token-limit splits cleanly. |
| `intent-pattern-qa` | Catches silent regex-pattern death — patterns that compile but never match — via positive-match probes and byte-level asserts. |
| `batch-run-integrity` | Keeps long multi-chunk batch jobs honest and resumable: incremental on-disk checkpoints, completion claims reconciled against artifacts on disk. |
| `worker-resource-budgeting` | Budgets RAM before fanning out parallel workers, so verification workers never starve the live system. |
| `hexagonal-python` | Hexagonal Architecture (Ports & Adapters) + DDD for Python backends (FastAPI/Flask, SQLAlchemy, pytest): use cases, aggregates, repositories, unit of work, domain events. |
| `docker-compose-patterns` | Docker Compose done right: service definitions, health checks, dependency ordering, volumes, networks, env vars, dev overrides. |
| `docker-build-strategies` | Writing, reviewing, and optimizing Dockerfiles: image size, build speed, layer caching, multi-stage builds. |
| `docker-project-foundations` | Setting up and Dockerizing a project from scratch: scaffolding, configuration, conventions. |
| `docker-destructive-guardrails` | Guardrails to check before running — or recommending — any Docker command that deletes, wipes, or irreversibly changes state. |
| `golang-concurrency` | Go concurrency design: goroutine lifecycle and leak prevention, channels and `select`, mutexes, `errgroup`, worker pools, fan-out/fan-in. |
| `golang-error-handling` | Idiomatic Go error handling: wrapping with `%w`, `errors.Is`/`As`/`Join`, custom types, sentinel errors, panic/recover. |
| `golang-testing` | Production-ready Go tests: table-driven tests, testify suites and mocks, parallel tests, fuzzing, fixtures. |
| `database-schema-designer` | Robust, scalable DB schema design for SQL and NoSQL: normalization, indexing strategies, migration patterns, with examples. |
| `c4-architecture` | Architecture documentation with C4-model Mermaid diagrams: context, container, component, code. |
| `go-service-scaffolder` | Scaffolds production-ready Go HTTP services: OpenTelemetry, TLS, lifecycle management, Dockerfile, GitHub Actions CI. |
| `android-architecture` | Modern Android app architecture with Clean Architecture + Hilt: strict layering, setup and maintenance guidance. |
| `android-compose-performance` | Audits and improves Jetpack Compose runtime performance — diagnoses slow rendering and jank from code review. |
| `android-testing` | Comprehensive Android testing strategy: unit, integration, Hilt, and screenshot tests. |

</details>

> **Total: 47 skills.** The collection grows — check back for new additions.

## Anatomy of a skill

```
design/taste-skill/
├── SKILL.md        # the playbook: when to load it, how to apply it
├── skill.yaml      # machine-readable metadata (name, description)
└── scripts/        # optional helper scripts (only some skills)
```

`SKILL.md` starts with frontmatter (`name`, `description`, `allowed-tools`) so agents can index and auto-load it. Everything else is plain markdown written to be read by both humans and models.

## FAQ

**Do I need all 47 skills?**
No. Copy the ones matching your work. A frontend agent might take `taste-skill` + `antislop-core`; a backend agent `hexagonal-python` + `docker-compose-patterns` + `output-skill`. Each folder is self-contained.

**Are these tied to a specific AI agent?**
No. A skill is just a folder with `SKILL.md` (markdown + YAML frontmatter) — the open Agent Skills convention. Any agent that reads markdown can use them: Claude Code, Cursor, Windsurf, Copilot, or your own harness.

**Can I use these commercially?**
The collection itself is MIT. Individual skills adapted from external sources keep their original licenses (MIT or Apache-2.0 — both permissive for commercial use). Check the Source section in each skill's README.

**Some descriptions are in Indonesian — why?**
A few skills were adapted and translated for Indonesian-speaking builders. The technical content stays in English where the source was English; the adaptation notes say what changed.

**How do I know what's new?**
See [CHANGELOG.md](CHANGELOG.md). Every addition, rename, or removal is recorded there.

**I found a bug or a better skill.**
Open an issue or PR — see [Contributing](#contributing).

## Credits

atlys is **curated and maintained by [adiprmx](https://github.com/adiprmx)** — skill selection, naming, `skill.yaml` metadata, Indonesian-language adaptations, and ongoing expansion of select skills.

Several skills are adapted from excellent open-source work. They retain their original licenses (see each skill folder), and this collection wouldn't exist without them:

- `antislop-*` family — [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop)
- `taste-skill` family (`taste-skill`, `redesign-skill`, `soft-skill`, `minimalist-skill`, `brutalist-skill`, `stitch-skill`, `brandkit`, `gpt-tasteskill`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `frontend-image-direction`, `image-to-code-skill`, `premium-frontend-engineering`, `output-skill`) — [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- `humanizer` — [blader/humanizer](https://github.com/blader/humanizer)
- `stop-slop` — [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop)
- `no-ai-slop` — [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- `avoid-ai-writing` — [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing)
- `impeccable-design` — originally [pbakaus/impeccable](https://github.com/pbakaus/impeccable), significantly expanded
- `hexagonal-python` — [Remy349/skills](https://github.com/Remy349/skills) (MIT)
- `docker-*` family — [docker/skills](https://github.com/docker/skills) (Apache-2.0)
- `golang-*` family — [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) (MIT)
- `accessibility`, `accessibility-testing` — [KreerC/ACCESSIBILITY.md](https://github.com/KreerC/ACCESSIBILITY.md) (MIT)
- `database-schema-designer`, `c4-architecture`, `crafting-effective-readmes` — [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) (MIT)
- `go-service-scaffolder`, `writing-quality` — [ItalyPaleAle/skills](https://github.com/ItalyPaleAle/skills) (MIT)
- `android-*` family — [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) (Apache-2.0)

## Contributing

Found a skill worth including, or improved one that's here? Open an issue or PR with:

1. The skill folder (`SKILL.md` + `skill.yaml` required) under the right category (`design/`, `writing/`, or `engineering/`)
2. A one-paragraph description of what makes it non-generic
3. Its provenance — original work or adapted (with source link)

## License

MIT — see [LICENSE](LICENSE). Skills adapted from external sources remain under their original licenses.

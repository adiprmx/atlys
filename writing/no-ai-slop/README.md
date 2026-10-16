![Writing — atlys](../../assets/banner-writing.svg)

# no-ai-slop

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*Two tools in one: a careful editor that changes as little as possible, and a detector that points at the exact line and names the pattern.*

No AI Slop: edit draf jadi tajam dan manusiawi sambil menjaga suara penulis, atau deteksi pola AI-slop tanpa menulis ulang. Dua mode: Edit (minimum effective edit + What changed) dan Detect (sebut pola, kutip baris, beri fix singkat). Pakai saat user minta draf lebih jelas, lebih direct, lebih beropini, atau bertanya apakah tulisannya terdengar AI.

> Sumber: petergyang/no-ai-slop (MIT). Diadaptasi ke Bahasa Indonesia; pola Inggris dipertahankan karena spesifik Bahasa Inggris.

## When to use

- Editing a draft with minimal changes (Edit mode)
- Auditing text to name exactly which AI patterns appear (Detect mode)

## Contents

```
no-ai-slop/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`humanizer`](../writing/humanizer/) — for the voice pass
- [`avoid-ai-writing`](../writing/avoid-ai-writing/) — for convergence across passes

## Install

```sh
cp -r writing/no-ai-slop ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

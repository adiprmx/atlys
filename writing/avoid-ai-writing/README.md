# avoid-ai-writing

![writing](https://img.shields.io/badge/writing-7c3aed) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Avoid AI Writing: audit & rewrite untuk menghapus pola tulisan AI ('AI-isms'). Mode detect-only, edit-in-place, profil suara (casual/professional/technical/warm/blunt), dan pass iterasi-sampai-konvergen. Punya kontrak editing ketat: deteksi bukan vonis, temuan bukan edit otomatis. Dikalibrasi untuk Bahasa Inggris; untuk Bahasa Indonesia pakai sebagai panduan pola struktural.

> Sumber: conorbronsdon/avoid-ai-writing v3.38.0 (MIT) oleh Conor Bronsdon. Diringkas dan diadaptasi ke Bahasa Indonesia; katalog pola penuh ada di repo sumber (references/patterns.md). Catatan bahasa: aturan dan detektor ini dikalibrasi untuk Bahasa Inggris. Untuk Bahasa Indonesia, pakai sebagai panduan pola STRUKTURAL (kontras biner, triad, staging, inflasi) — bukan daftar kata per kata.

## Contents

```
avoid-ai-writing/
└── SKILL.md  # the playbook — when to load, how to apply
```

## Install

```sh
cp -r writing/avoid-ai-writing ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

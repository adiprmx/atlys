# c4-architecture

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

Generate architecture documentation using C4 model Mermaid diagrams. Use when asked to create architecture diagrams, document system architecture, visualize software structure, create C4 diagrams, or generate context/container/component/deployment diagrams. Triggers include "architecture diagram", "C4 diagram", "system context", "container diagram", "component diagram", "deployment diagram", "document architecture", "visualize architecture".

## When to use

- Documenting system architecture with C4 diagrams
- Context, container, component, and code views

## Contents

```
c4-architecture/
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`hexagonal-python`](../engineering/hexagonal-python/) — as an architecture to document
- [`database-schema-designer`](../engineering/database-schema-designer/) — for the data view

## Install

```sh
cp -r engineering/c4-architecture ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [softaworks/agent-toolkit](https://github.com/softaworks/agent-toolkit) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

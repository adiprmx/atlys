![Engineering — atlys](../../assets/banner-engineering.svg)

# hexagonal-python

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-MIT-16a34a)

*Business logic tangled into framework code is how backends become unchangeable. Ports and adapters, done properly for Python.*

Hexagonal Architecture (Ports and Adapters) with Domain-Driven Design for Python backends built with FastAPI or Flask, SQLAlchemy and pytest. Use it to design, implement, review, refactor or migrate Python server-side code - REST APIs, use cases, aggregates, value objects, repositories, unit of work, domain events and outbox, bounded contexts, error handling, idempotency, pagination and tests per boundary. Trigger it when the project has pyproject.toml, requirements*.txt or setup.py and the user mentions hexagonal, ports and adapters, clean architecture, DDD, layers, use cases, repositories, services, a fat route or view, decoupling from FastAPI, Flask or the database, or how to structure a Python API, even if they never say "hexagonal". Also use it for architecture, SOLID or testability reviews of Python backend code. Not for other languages - use the matching hexagonal-<language> skill.

## When to use

- Structuring a Python backend with Hexagonal Architecture and DDD
- FastAPI/Flask projects that need clean port and adapter boundaries

## Contents

```
hexagonal-python/
├── references/  # reference docs
└── SKILL.md  # the playbook — when to load, how to apply
```

## Pairs well with

- [`database-schema-designer`](../engineering/database-schema-designer/) — for the persistence layer
- [`c4-architecture`](../engineering/c4-architecture/) — to document the architecture

## Install

```sh
cp -r engineering/hexagonal-python ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [Remy349/skills](https://github.com/Remy349/skills) (MIT), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

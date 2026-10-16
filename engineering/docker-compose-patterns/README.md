# docker-compose-patterns

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

Use this skill when creating, modifying, or debugging Docker Compose configurations, even if the user just says they need to wire services together, add a database to their stack, or set up a local development environment with multiple containers. Covers service definitions, health checks, dependency ordering, volumes, networks, environment variables, and development overrides.

## When to use

- Creating a new compose.yaml for a project
- Adding or modifying services in an existing Compose file
- Setting up development overrides with compose.override.yaml
- Debugging service startup ordering or connectivity issues

## Contents

```
docker-compose-patterns/
├── agents/  # subagent definitions
├── assets/  # assets
├── checks/  # check scripts
├── references/  # reference docs
├── scripts/  # helper scripts
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Install

```sh
cp -r engineering/docker-compose-patterns ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [docker/skills](https://github.com/docker/skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

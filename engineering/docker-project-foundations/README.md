# docker-project-foundations

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

Use this skill when setting up, initializing, or Dockerizing a project, even if the user doesn't explicitly mention Docker but describes a need for containerized local development, adding a database or cache dependency, or running services without host-level installs. Covers Dockerfile, compose.yaml, and .dockerignore creation with Docker best practices.

## When to use

- A user asks you to set up, initialize, or Dockerize a project
- A project needs an initial Dockerfile, compose.yaml, or .dockerignore and does not have one
- A user wants to add a service dependency (database, cache, message queue) to a project
- A user asks how to run or develop a project locally and Docker is available

## Contents

```
docker-project-foundations/
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
cp -r engineering/docker-project-foundations ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [docker/skills](https://github.com/docker/skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

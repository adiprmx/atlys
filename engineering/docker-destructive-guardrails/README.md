# docker-destructive-guardrails

![engineering](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

Use this skill before running, or recommending, any Docker command that deletes, wipes, resets, or otherwise irreversibly changes state — even if the user just says to "clean up", "clear the cache", "start fresh", "wipe everything", "nuke it", "reset", "force remove", or "tear down" Docker resources. Covers generic Docker CLI destructive operations not owned by a more specific skill — `docker rm`, `docker rm -f`, `docker container prune`, `docker kill`, `docker system prune`, `docker rmi`/`docker image rm`, `docker image prune -a`, `docker network rm`, `docker network prune`, `docker builder prune`, `docker buildx rm`, `docker context rm`, and standalone (non-Compose) `docker volume rm`/`docker volume prune`. Also indexes destructive commands owned by other Docker skills (Compose, sandbox, Desktop). Core rule — state exactly what will be lost and get explicit confirmation first, except narrow, low-friction Tier 1 container cleanup.

## When to use

- The user asks to "clean up", "clear the cache", "start fresh", "wipe everything", "nuke it", "reset", "force remove", or "tear down" Docker resources without naming a specific command
- The agent is considering docker rm, docker rm -f, docker container prune, docker kill, docker stop, docker system prune, docker rmi, docker image rm, docker image prune -a, docker network rm, docker network prune, docker builder prune, docker buildx rm, docker context rm, or standalone (non-Compose) docker volume rm/docker volume prune as a fix for an unrelated problem (disk space, a stuck container, a stale network, a broken build cache, an old builder or volume)
- The user wants a cross-product overview of destructive commands across Docker skills

## Contents

```
docker-destructive-guardrails/
├── agents/  # subagent definitions
├── checks/  # check scripts
├── references/  # reference docs
├── SKILL.md  # the playbook — when to load, how to apply
└── skill.yaml  # machine-readable metadata
```

## Install

```sh
cp -r engineering/docker-destructive-guardrails ~/.claude/skills/  # or your agent's skills directory
```

## Source

Adapted from [docker/skills](https://github.com/docker/skills) (Apache-2.0), curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [atlys](../../) — a curated collection of skills for AI coding agents.

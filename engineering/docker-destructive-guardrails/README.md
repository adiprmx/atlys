<div align="center">
  <img src="../../assets/icon.webp" width="72" alt="atlys">
</div>

# docker-destructive-guardrails

![category](https://img.shields.io/badge/engineering-0d9488) ![license](https://img.shields.io/badge/license-Apache--2.0-16a34a)

> Use this skill before running, or recommending, any Docker command that deletes, wipes, resets, or otherwise irreversibly changes state — even if the user just says to "clean up", "clear the cache", "start fresh", "wipe everything", "nuke it", "reset", "force remove", or "tear down" Docker resources. Covers generic Docker CLI destructive operations not owned by a more specific skill — `docker rm`, `docker rm -f`, `docker container prune`, `docker kill`, `docker system prune`, `docker rmi`/`docker image rm`, `docker image prune -a`, `docker network rm`, `docker network prune`, `docker builder prune`, `docker buildx rm`, `docker context rm`, and standalone (non-Compose) `docker volume rm`/`docker volume prune`. Also indexes destructive commands owned by other Docker skills (Compose, sandbox, Desktop). Core rule — state exactly what will be lost and get explicit confirmation first, except narrow, low-friction Tier 1 container cleanup.

## 📂 What's inside

```
docker-destructive-guardrails/
├── agents/
├── checks/
├── references/
├── SKILL.md
└── skill.yaml
```

**`SKILL.md`** is the full playbook — when to load this skill and how to apply it. Copy this whole folder into your agent's skills directory to install it.

## 📜 Source

Adapted from [docker/skills](https://github.com/docker/skills) (Apache-2.0). Curated into atlys by [adiprmx](https://github.com/adiprmx).

---

Part of [**atlys**](../../) — a curated collection of skills for AI coding agents.

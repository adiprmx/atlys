---
name: go-service-scaffolder
description: Scaffold a production-ready Go HTTP service with OpenTelemetry observability, TLS, lifecycle management, Dockerfile, GitHub Actions CI/CD, and golangci-lint. Use when creating or regenerating a full Go service skeleton (project layout, config package, server package, CI workflows, and container build files).
---

# Go Service Scaffolder

Create a production-ready Go HTTP service skeleton and keep outputs consistent.

## Workflow

1. Ask for required inputs:
- App name (kebab-case)
- Go module path
- GitHub owner/org
- If the user asks for database support, ask which database to scaffold: Postgres, SQLite, or both.

2. Derive:
- `CONFIG_ENV_VAR`: uppercase app name without hyphens + `_CONFIG`
- `METRICS_PREFIX`: lowercase app name without hyphens

3. Generate the full project file tree and file contents using the canonical spec in `references/go-service-scaffold-spec.md`.

4. Replace placeholders everywhere:
- `{{APP_NAME}}`
- `{{MODULE_PATH}}`
- `{{GITHUB_OWNER}}`
- `{{CONFIG_ENV_VAR}}`
- `{{METRICS_PREFIX}}`

Database constraints when database support is requested:
- Never use an ORM.
- For Postgres, use PGX: `github.com/jackc/pgx/v5`.
- For SQLite, use `modernc.org/sqlite`.

5. Run:
- `go mod init <module-path>` (only if `go.mod` does not already exist)
- `go mod tidy`
- `go get -tool github.com/italypaleale/go-kit/tools/gen-config` (adds the `tool` directive used by `make gen-config`)
- `make gen-config` to produce `config.md` and `config.sample.yaml` from the `Config` struct
- `go test ./...`

6. Initialize git only when needed:
- Run `git init` only if the target directory is not already a git repository.

Whenever `pkg/config.Config` (or any struct reachable from it) is regenerated or edited later, re-run `make gen-config` so `config.md` and `config.sample.yaml` stay in sync. CI enforces this with `make check-config-diff`.

## Reference

Use `references/go-service-scaffold-spec.md` as the single source of truth for:
- Required directory structure
- Exact file templates
- Post-scaffold steps and architecture notes

Load only the sections needed for the current task instead of reading the entire reference at once.

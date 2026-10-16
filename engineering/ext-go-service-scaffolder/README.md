# Go Service Scaffolder Skill

This skill provides structured guidance for scaffolding a production-ready Go HTTP service with:

- **OpenTelemetry observability**
- **TLS support**
- **Lifecycle management**
- **Dockerfile**
- **GitHub Actions CI/CD**
- **golangci-lint**

## What This Skill Covers

1. Service scaffolding inputs and naming conventions
2. Project layout and package structure
3. HTTP server bootstrap and lifecycle wiring
4. Configuration package and environment variable conventions
5. Observability setup with OpenTelemetry
6. Containerization with Dockerfile
7. CI workflows with GitHub Actions
8. Linting and test baseline
9. Optional database scaffolding (Postgres, SQLite, or both)

## Installation

### Using Claude Code CLI

```bash
npx skills add https://github.com/ItalyPaleAle/skills/tree/main/go-service-scaffolder
```

### Using Claude Projects (claude.ai)

Add the following URL to your Project knowledge:

```
https://raw.githubusercontent.com/ItalyPaleAle/skills/main/go-service-scaffolder/SKILL.md
```

### Manual Installation

Download [SKILL.md](./SKILL.md) and add it to your Claude Code project or Claude Project knowledge base.

## Usage

Once installed, you can invoke this skill by asking Claude to:

- "Scaffold a production-ready Go HTTP service"
- "Create a Go service skeleton with OpenTelemetry and CI"
- "Generate a Go API project with Docker and GitHub Actions"
- "Set up a Go service template with Postgres support"

Claude will gather required inputs (app name, module path, GitHub owner, and optional database choice) and generate a complete, consistent service scaffold.

## Features

### Production Baseline

- Standardized service structure for Go projects
- TLS-ready HTTP server setup
- Lifecycle hooks for startup and shutdown
- OpenTelemetry instrumentation baseline
- Docker build support

### Quality and Delivery

- GitHub Actions workflows for CI/CD
- `golangci-lint` integration
- `go test ./...` validation as part of scaffold flow
- Deterministic placeholder replacement for repeatable output

### Database Options

- Postgres scaffolding with `github.com/jackc/pgx/v5`
- SQLite scaffolding with `modernc.org/sqlite`
- Option to scaffold both when requested
- No ORM usage in generated database paths

## Requirements

- Go 1.25+
- Git (optional, for repository initialization)

## License

[MIT](../LICENSE.md)

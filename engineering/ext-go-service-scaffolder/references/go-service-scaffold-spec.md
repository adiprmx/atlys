# Go Service Scaffold Specification

Canonical specification for generating a production-ready Go service with an HTTP server, OpenTelemetry observability (logs, metrics, traces), TLS support, graceful lifecycle management, Dockerfile, GitHub Actions CI/publish workflows, and golangci-lint configuration.

## Table of Contents

- [Inputs](#inputs)
- [Files to Generate](#files-to-generate)
- [Placeholders](#placeholders)
- [File Contents](#file-contents)
- [Post-Scaffold Steps](#post-scaffold-steps)
- [Architecture Notes](#architecture-notes)

## Inputs

Before generating files, collect:

1. **App name** (kebab-case, e.g. `my-service`): Used for binary name, config directory, Docker image name, log messages.
2. **Go module path** (e.g. `github.com/username/my-service`): Used in `go.mod` and all import paths.
3. **GitHub owner** (e.g. `username`): Used for the container registry path `ghcr.io/<owner>/<app-name>`.

If the user requests database support, ask which database to scaffold:

- Postgres
- SQLite
- Both

Database constraints:

- Never use an ORM.
- For Postgres, use PGX: `github.com/jackc/pgx/v5`.
- For SQLite, use `modernc.org/sqlite`.

Derive from app name:

- **Config env var**: Convert app name to upper-case, remove hyphens, and append `_CONFIG`. Example: `my-service` becomes `MYSERVICE_CONFIG`.
- **Metrics prefix**: Convert app name to lower-case and remove hyphens. Example: `my-service` becomes `myservice`.

## Files to Generate

Generate all the files listed below. The directory structure is:

```
<project-root>/
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── build-and-publish.yaml
├── .gitignore
├── .golangci.yaml
├── .gomod-age.json
├── AGENTS.md
├── cmd/
│   └── main.go
├── pkg/
│   ├── buildinfo/
│   │   └── buildinfo.go
│   ├── config/
│   │   ├── config.go
│   │   ├── instance.go
│   │   ├── otel.go
│   │   └── testutils_unit.go
│   ├── metrics/
│   │   └── metrics.go
│   ├── server/
│   │   ├── server.go
│   │   └── errors.go
│   └── utils/
│       └── functions.go
├── Dockerfile
└── Makefile
```

After generating files, run `go mod init <module-path>` and `go mod tidy` to create `go.mod` and `go.sum`, register the `gen-config` tool with `go get -tool github.com/italypaleale/go-kit/tools/gen-config`, then run `make gen-config` (this produces `config.md` and `config.sample.yaml` from the `Config` struct annotations — do not author them by hand). Finally, run `git init` only if the target is not already a git repository.

---

## Placeholders

In all files below, replace these placeholders:

| Placeholder | Description |
|---|---|
| `{{APP_NAME}}` | App name in kebab-case (e.g. `my-service`) |
| `{{MODULE_PATH}}` | Full Go module path (e.g. `github.com/username/my-service`) |
| `{{GITHUB_OWNER}}` | GitHub owner/org for container registry |
| `{{CONFIG_ENV_VAR}}` | Config environment variable (e.g. `MYSERVICE_CONFIG`) |
| `{{METRICS_PREFIX}}` | Metrics prefix (e.g. `myservice`) |

---

## File Contents

---

### `cmd/main.go`

```go
package main

import (
	"context"
	"errors"
	"log/slog"
	"time"

	configkit "github.com/italypaleale/go-kit/config"
	"github.com/italypaleale/go-kit/observability"
	"github.com/italypaleale/go-kit/servicerunner"
	"github.com/italypaleale/go-kit/signals"
	slogkit "github.com/italypaleale/go-kit/slog"

	"github.com/italypaleale/sample-app/pkg/buildinfo"
	"github.com/italypaleale/sample-app/pkg/config"
	appmetrics "github.com/italypaleale/sample-app/pkg/metrics"
	"github.com/italypaleale/sample-app/pkg/server"
)

func main() {
	// Init a logger used for initialization only, to report initialization errors
	initLogger := slog.Default().
		With(slog.String("app", buildinfo.AppName)).
		With(slog.String("version", buildinfo.AppVersion))

	// Load config
	cfg := config.Get()
	err := configkit.LoadConfig(cfg, configkit.LoadConfigOpts{
		EnvVar:  "SAMPLEAPP_CONFIG",
		DirName: "sample-app",
	})
	if err != nil {
		ce, ok := errors.AsType[*configkit.ConfigError](err)
		if ok {
			ce.LogFatal(initLogger)
		} else {
			slogkit.FatalError(initLogger, "Failed to load configuration", err)
			return
		}
	}

	// List of services to run
	services := make([]servicerunner.Service, 0, 3)

	shutdowns := &shutdownManager{
		fns: make([]servicerunner.Service, 0, 3),
	}

	// Get the logger and set it in the context
	log, loggerShutdownFn, err := observability.InitLogs(context.Background(), observability.InitLogsOpts{
		Config:     cfg,
		Level:      cfg.Logs.Level,
		JSON:       cfg.Logs.JSON,
		AppName:    buildinfo.AppName,
		AppVersion: buildinfo.AppVersion,
	})
	if err != nil {
		slogkit.FatalError(initLogger, "Failed to create logger", err)
		return
	}
	slog.SetDefault(log)
	shutdowns.Add(loggerShutdownFn)

	// Validate the configuration
	err = cfg.Validate(log)
	if err != nil {
		shutdowns.Run(log)
		slogkit.FatalError(log, "Invalid configuration", err)
		return
	}

	log.Info("Starting sample-app", slog.String("build", buildinfo.BuildDescription))

	// Get a context that is canceled when the application receives a termination signal.
	ctx := signals.SignalContext(context.Background())

	// Init appMetrics
	appMetrics, metricsShutdownFn, err := appmetrics.NewAppMetrics(ctx)
	if err != nil {
		shutdowns.Run(log)
		slogkit.FatalError(log, "Failed to init metrics", err)
		return
	}
	shutdowns.Add(metricsShutdownFn)

	// Init tracing
	traceProvider, tracerShutdownFn, err := observability.InitTraces(ctx, observability.InitTracesOpts{
		Config:  cfg,
		AppName: buildinfo.AppName,
	})
	if err != nil {
		shutdowns.Run(log)
		slogkit.FatalError(log, "Failed to init tracing", err)
		return
	}
	shutdowns.Add(tracerShutdownFn)

	// Create HTTP server
	log.Info("Initializing API server")
	apiServer, err := server.NewServer(server.NewServerOpts{
		AppMetrics:    appMetrics,
		TraceProvider: traceProvider,
	})
	if err != nil {
		shutdowns.Run(log)
		slogkit.FatalError(log, "Failed to init API server", err)
		return
	}
	services = append(services, apiServer.Run)

	// Run all services
	// This call blocks until the context is canceled
	err = servicerunner.
		NewServiceRunner(services...).
		Run(ctx)
	if err != nil {
		shutdowns.Run(log)
		slogkit.FatalError(log, "Failed to run service", err)
		return
	}

	shutdowns.Run(log)
}

type shutdownManager struct {
	fns []servicerunner.Service
}

func (s *shutdownManager) Add(fn servicerunner.Service) {
	if fn == nil {
		return
	}
	s.fns = append(s.fns, fn)
}

func (s *shutdownManager) Run(log *slog.Logger) {
	shutdownCtx, shutdownCancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer shutdownCancel()
	err := servicerunner.
		NewServiceRunner(s.fns...).
		Run(shutdownCtx)
	if err != nil {
		log.Error("Error shutting down services", slog.Any("error", err))
	}
}
```

---

### `pkg/buildinfo/buildinfo.go`

```go
package buildinfo

import (
	"fmt"

	"{{MODULE_PATH}}/pkg/utils"
)

// These variables will be set at build time
var (
	AppName    string = "{{APP_NAME}}"
	AppVersion string = "canary"
	BuildId    string
	CommitHash string
	BuildDate  string
	Production string
)

// BuildDescription set during initialization
var BuildDescription string

func init() {
	if BuildId != "" && BuildDate != "" && CommitHash != "" {
		BuildDescription = fmt.Sprintf("%s, %s (%s)", BuildId, BuildDate, CommitHash)
	} else {
		BuildDescription = "null"
	}

	if !utils.IsTruthy(Production) {
		BuildDescription += " (non-production)"
	}
}
```

---

### `pkg/config/config.go`

```go
package config

import (
	"encoding/json"
	"errors"
	"log/slog"
)

// Config represents the application configuration
type Config struct {
	// Server configuration
	Server ConfigServer `yaml:"server"`

	// Logs contains configuration for logging
	Logs ConfigLogs `yaml:"logs"`

	// Dev is meant for development only; it's undocumented
	Dev ConfigDev `yaml:"-"`

	// Internal keys
	internal internal `yaml:"-"`
}

// ConfigLogs represents logging configuration
type ConfigLogs struct {
	// Controls log level and verbosity. Supported values: `debug`, `info` (default), `warn`, `error`.
	// +default "info"
	Level string `yaml:"level"`

	// If true, calls to the healthcheck endpoint (`/healthz`) are not included in the logs.
	// +default true
	OmitHealthChecks bool `yaml:"omitHealthChecks"`

	// If true, emits logs formatted as JSON, otherwise uses a text-based structured log format.
	// Defaults to false if a TTY is attached (e.g. when running the binary directly in the terminal or in development); true otherwise.
	JSON bool `yaml:"json"`
}

// ConfigServer represents server configuration
type ConfigServer struct {
	// Address to bind the API server to
	// Set to "0.0.0.0" for listening on all interfaces
	// +default "127.0.0.1"
	Bind string `yaml:"bind"`

	// Port for the API server to listen on
	// +default 3000
	Port int `yaml:"port"`

	// TLS configuration
	TLS ConfigServerTLS `yaml:"tls"`
}

// ConfigServerTLS holds TLS configuration for TCP listener
type ConfigServerTLS struct {
	// Path where to load TLS certificates from, when not using Let's Encrypt.
	// Within the folder, the files must be named `tls-cert.pem` and `tls-key.pem`. The application watches for changes in this folder and automatically reloads the TLS certificates when they're updated.
	// If empty, certificates are loaded from the same folder where the loaded `config.yaml` is located.
	// +default the same folder as the `config.yaml` file
	Path string `yaml:"path"`

	// Full, PEM-encoded TLS certificate, when not using Let's Encrypt.
	// Using `certPEM` and `keyPEM` is an alternative method of passing TLS certificates than using `path`.
	CertPEM string `yaml:"certPEM"` //nolint:tagliatelle

	// Full, PEM-encoded TLS key, when not using Let's Encrypt.
	// Using `certPEM` and `keyPEM` is an alternative method of passing TLS certificates than using `path`.
	KeyPEM string `yaml:"keyPEM"` //nolint:tagliatelle
}

// ConfigDev includes options using during development only
type ConfigDev struct {
}

// Internal properties
type internal struct {
	instanceID       string
	configFileLoaded string // Path to the config file that was loaded
}

// String implements fmt.Stringer and prints out the config for debugging
func (c *Config) String() string {
	//nolint:errchkjson,musttag
	enc, _ := json.Marshal(c)
	return string(enc)
}

// GetLoadedConfigPath returns the path to the config file that was loaded
func (c *Config) GetLoadedConfigPath() string {
	return c.internal.configFileLoaded
}

// SetLoadedConfigPath sets the path to the config file that was loaded
func (c *Config) SetLoadedConfigPath(filePath string) {
	c.internal.configFileLoaded = filePath
}

// GetInstanceID returns the instance ID
func (c *Config) GetInstanceID() string {
	return c.internal.instanceID
}

// Validate the configuration and performs some sanitization
func (c *Config) Validate(logger *slog.Logger) error {
	if c.Server.Port < 0 {
		return errors.New("configuration option 'server.port' must not be negative")
	}

	return nil
}
```

---

### `pkg/config/instance.go`

```go
package config

import (
	configkit "github.com/italypaleale/go-kit/config"
)

var (
	config *Config

	defaultDevConfig ConfigDev
)

func init() {
	// Set the default config at startup
	config = GetDefaultConfig()

	// Set the instance ID
	// This may panic if there's not enough entropy in the system
	var err error
	config.internal.instanceID, err = configkit.GetInstanceID()
	if err != nil {
		panic("failed to set instance ID: " + err.Error())
	}
}

// Get returns the singleton instance
func Get() *Config {
	return config
}

// GetDefaultConfig returns the default configuration.
func GetDefaultConfig() *Config {
	return &Config{
		Logs: ConfigLogs{
			Level:            "info",
			OmitHealthChecks: true,
		},
		Server: ConfigServer{
			Bind: "127.0.0.1",
			Port: 3000,
		},
		Dev: defaultDevConfig,
	}
}
```

---

### `pkg/config/otel.go`

```go
package config

import (
	"go.opentelemetry.io/otel/sdk/resource"
	semconv "go.opentelemetry.io/otel/semconv/v1.39.0"

	"{{MODULE_PATH}}/pkg/buildinfo"
)

// GetOtelResource returns the OpenTelemetry Resource object
func (c *Config) GetOtelResource(name string) (*resource.Resource, error) {
	//nolint:wrapcheck
	return resource.Merge(
		resource.Default(),
		resource.NewSchemaless(
			semconv.ServiceName(name),
			semconv.ServiceInstanceID(c.GetInstanceID()),
			semconv.ServiceVersion(buildinfo.BuildId),
		),
	)
}
```

---

### `pkg/config/testutils_unit.go`

```go
//go:build unit

// This file is only built when the "unit" tag is set

package config

import (
	"github.com/jinzhu/copier"
)

// SetTestConfig updates the configuration in the global config object for the test
// Returns a function that should be called with "defer" to restore the previous configuration
func SetTestConfig(updater func(c *Config)) func() {
	// Save the previous config
	prevConfig := config

	// Create a deep copy of the previous config
	// Note that this doesn't copy unexported fields
	config = &Config{}
	err := copier.CopyWithOption(config, prevConfig, copier.Option{
		DeepCopy: true,
	})
	if err != nil {
		// Panic in case of errors, since this function is used for testing only
		panic(err)
	}

	// Set the new values
	updater(config)

	// Return a function that restores the original value
	return func() {
		config = prevConfig
	}
}
```

---

### `pkg/metrics/metrics.go`

```go
package metrics

import (
	"context"
	"fmt"

	"go.opentelemetry.io/otel/attribute"
	api "go.opentelemetry.io/otel/metric"

	"github.com/italypaleale/go-kit/observability"
	"github.com/italypaleale/sample-app/pkg/buildinfo"
	"github.com/italypaleale/sample-app/pkg/config"
)

const prefix = "sample"

type AppMetrics struct {
	apiCall api.Int64Counter
}

func NewAppMetrics(ctx context.Context) (m *AppMetrics, shutdownFn func(ctx context.Context) error, err error) {
	cfg := config.Get()

	m = &AppMetrics{}

	meter, shutdownFn, err := observability.InitMetrics(ctx, observability.InitMetricsOpts{
		Config:  cfg,
		AppName: buildinfo.AppName,
		Prefix:  prefix,
	})
	if err != nil {
		return nil, nil, fmt.Errorf("failed to init metrics: %w", err)
	}

	m.apiCall, err = meter.Int64Counter(
		prefix+"_api_calls",
		api.WithDescription("The number of API calls (example)"),
	)
	if err != nil {
		return nil, nil, fmt.Errorf("failed to create "+prefix+"_api_calls meter: %w", err)
	}

	return m, shutdownFn, nil
}

//nolint:contextcheck
func (m *AppMetrics) RecordAPICall(ctx context.Context, method string) {
	if m == nil {
		return
	}
	if ctx == nil {
		ctx = context.Background()
	} else {
		ctx = context.WithoutCancel(ctx)
	}

	m.apiCall.Add(
		ctx,
		1,
		api.WithAttributeSet(
			attribute.NewSet(
				attribute.KeyValue{Key: "method", Value: attribute.StringValue(method)},
			),
		),
	)
}
```

---

### `pkg/server/server.go`

```go
package server

import (
	"context"
	"crypto/tls"
	"errors"
	"fmt"
	"log/slog"
	"net"
	"net/http"
	"path/filepath"
	"strconv"
	"sync"
	"sync/atomic"
	"time"

	httpserver "github.com/italypaleale/go-kit/httpserver"
	tlsconfig "github.com/italypaleale/go-kit/httpserver/tlsconfig"
	sloghttp "github.com/samber/slog-http"
	"go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"
	"go.opentelemetry.io/otel/sdk/trace"

	"github.com/italypaleale/sample-app/pkg/config"
	"github.com/italypaleale/sample-app/pkg/metrics"
)

// Max size for request bodies
// 1MB
const maxBodySize = 1 << 20

// Server is the server based on Gin
type Server struct {
	appSrv  *http.Server
	handler http.Handler
	running atomic.Bool
	wg      sync.WaitGroup

	appMetrics    *metrics.AppMetrics
	traceProvider *trace.TracerProvider

	// Method that forces a reload of TLS certificates from disk
	tlsCertWatchFn tlsconfig.CertWatchFn

	// TLS configuration for the app server
	tlsConfig *tls.Config

	// Listener for the app server
	// This can be used for testing without having to start an actual TCP listener
	appListener net.Listener
}

// NewServerOpts contains options for the NewServer method
type NewServerOpts struct {
	AppMetrics    *metrics.AppMetrics
	TraceProvider *trace.TracerProvider
}

// NewServer creates a new Server object and initializes it
func NewServer(opts NewServerOpts) (*Server, error) {
	s := &Server{
		appMetrics:    opts.AppMetrics,
		traceProvider: opts.TraceProvider,
	}

	// Init the object
	err := s.init()
	if err != nil {
		return nil, err
	}

	return s, nil
}

// Init the Server object and create the mux
func (s *Server) init() error {
	// Init the app server
	err := s.initAppServer()
	if err != nil {
		return err
	}

	return nil
}

func (s *Server) initAppServer() (err error) {
	cfg := config.Get()

	// If "tls.path" is empty, use the folder where the config file is located
	tlsPath := cfg.Server.TLS.Path
	if tlsPath == "" {
		file := cfg.GetLoadedConfigPath()
		if file != "" {
			tlsPath = filepath.Dir(file)
		}
	}

	// Load the TLS configuration
	s.tlsConfig, s.tlsCertWatchFn, err = tlsconfig.Load(tlsPath, cfg.Server.TLS.CertPEM, cfg.Server.TLS.KeyPEM)
	if err != nil {
		return fmt.Errorf("failed to load TLS configuration: %w", err)
	}

	// Create the mux
	mux := http.NewServeMux()

	// Register routes
	mux.HandleFunc("GET /healthz", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusNoContent)
	})

	middlewares := make([]httpserver.Middleware, 0, 4)
	middlewares = append(middlewares,
		// Recover from panics
		sloghttp.Recovery,
		// Limit request body to 1MB
		httpserver.MiddlewareMaxBodySize(maxBodySize),
	)

	filters := []sloghttp.Filter{
		sloghttp.IgnoreStatus(401, 404),
	}
	if cfg.Logs.OmitHealthChecks {
		filters = append(filters,
			func(w sloghttp.WrapResponseWriter, r *http.Request) bool {
				return r.URL.Path != "/healthz"
			},
		)
	}

	middlewares = append(middlewares,
		// Log requests
		sloghttp.NewWithFilters(slog.Default(), filters...),
	)

	if s.traceProvider != nil {
		middlewares = append(middlewares,
			otelhttp.NewMiddleware("/"),
		)
	}

	// Add middlewares
	s.handler = httpserver.Use(mux, middlewares...)

	return nil
}

// Run the web server
// Note this function is blocking, and will return only when the server is shut down via context cancellation.
func (s *Server) Run(ctx context.Context) error {
	if !s.running.CompareAndSwap(false, true) {
		return errors.New("server is already running")
	}
	defer s.running.Store(false)
	defer s.wg.Wait()

	// App server
	s.wg.Add(1)
	appSrvErrCh := make(chan error, 1)
	err := s.startAppServer(ctx, appSrvErrCh)
	if err != nil {
		return fmt.Errorf("failed to start app server: %w", err)
	}
	defer func() {
		// Handle graceful shutdown
		defer s.wg.Done()
		shutdownCtx, shutdownCancel := context.WithTimeout(context.WithoutCancel(ctx), 5*time.Second)
		err := s.appSrv.Shutdown(shutdownCtx)
		shutdownCancel()
		if err != nil {
			// Log the error only (could be context canceled)
			slog.WarnContext(shutdownCtx,
				"App server shutdown error",
				slog.Any("error", err),
			)
		}
	}()

	// If we have a tlsCertWatchFn, invoke that
	if s.tlsCertWatchFn != nil {
		err = s.tlsCertWatchFn(ctx)
		if err != nil {
			return fmt.Errorf("failed to watch for TLS certificates: %w", err)
		}
	}

	// Block until the context is canceled or the app server exits unexpectedly.
	select {
	case <-ctx.Done():
	case err = <-appSrvErrCh:
		return fmt.Errorf("app server failed: %w", err)
	}

	// Servers are stopped with deferred calls
	return nil
}

func (s *Server) startAppServer(ctx context.Context, appSrvErrCh chan<- error) error {
	cfg := config.Get()

	// Create the HTTP(S) server
	addr := net.JoinHostPort(cfg.Server.Bind, strconv.Itoa(cfg.Server.Port))
	s.appSrv = &http.Server{
		Addr:              addr,
		MaxHeaderBytes:    1 << 20,
		ReadHeaderTimeout: 10 * time.Second,
		ReadTimeout:       30 * time.Second,
		WriteTimeout:      30 * time.Second,
		IdleTimeout:       60 * time.Second,
		Handler:           s.handler,
	}

	// Create the listener if we don't have one already
	if s.appListener == nil {
		var err error
		// Configure TLS for the HTTP server (optional)
		if s.tlsConfig != nil {
			s.appSrv.TLSConfig = s.tlsConfig
		}

		s.appListener, err = net.Listen("tcp", s.appSrv.Addr) //nolint:noctx
		if err != nil {
			return fmt.Errorf("failed to create TCP listener: %w", err)
		}

		slog.InfoContext(ctx, "Starting app server",
			slog.String("bind", cfg.Server.Bind),
			slog.Int("port", cfg.Server.Port),
			slog.Bool("tls", s.tlsConfig != nil),
		)
	}

	// Start the HTTP(S) server in a background goroutine
	go func() {
		defer s.appListener.Close() //nolint:errcheck

		// Next call blocks until the server is shut down
		var srvErr error
		if s.tlsConfig != nil {
			srvErr = s.appSrv.ServeTLS(s.appListener, "", "")
		} else {
			srvErr = s.appSrv.Serve(s.appListener)
		}
		if !errors.Is(srvErr, http.ErrServerClosed) {
			select {
			case appSrvErrCh <- srvErr:
			default:
			}
		}
	}()

	return nil
}
```

---

### `pkg/server/errors.go`

```go
package server

import (
	"net/http"

	httpserver "github.com/italypaleale/go-kit/httpserver"
)

var (
	errInternal         = httpserver.NewApiError("internal", http.StatusInternalServerError, "Internal error")
	errInvalidBody      = httpserver.NewApiError("invalid_body", http.StatusBadRequest, "Invalid request body")
	errMissingBodyParam = httpserver.NewApiError("missing_body_param", http.StatusBadRequest, "Missing required parameter in request body")
)

// TODO: Remove
//
//nolint:godox
func init() {
	_ = errInternal
	_ = errInvalidBody
	_ = errMissingBodyParam
}
```

---

### `pkg/utils/functions.go`

```go
package utils

import (
	"strings"
)

// IsTruthy returns true if a string is truthy, such as "1", "on", "yes", "true", "t", "y"
func IsTruthy(str string) bool {
	if len(str) > 4 {
		// Short-circuit to avoid processing strings that can't be true
		return false
	}
	switch strings.ToLower(str) {
	case "1", "true", "t", "on", "yes", "y":
		return true
	default:
		return false
	}
}
```

---

### `Dockerfile`

```dockerfile
FROM gcr.io/distroless/static-debian12:nonroot
# TARGETARCH is set automatically when using BuildKit
ARG TARGETARCH
COPY .bin/linux-${TARGETARCH}/{{APP_NAME}} /bin
ENTRYPOINT [ "/bin/{{APP_NAME}}" ]
CMD ["/bin/{{APP_NAME}}"]
```

---

### `Makefile`

```makefile
.PHONY: test
test:
	go test -tags unit ./...

.PHONY: test-race
test-race:
	CGO_ENABLED=1 go test -race -tags unit ./...

.PHONY: lint
lint:
	golangci-lint run -c .golangci.yaml

.PHONY: gen-config
gen-config:
	go tool gen-config

# Ensure gen-config ran
.PHONY: check-config-diff
check-config-diff: gen-config
	git diff --exit-code config.sample.yaml config.md
```

---

### `.golangci.yaml`

```yaml
version: "2"

linters:
  default: all
  enable: []

  exclusions:
    paths:
      - "tools/gen-config"

  disable:
    - cyclop
    - depguard
    - dupl
    - exhaustruct
    - err113
    - funcorder
    - funlen
    - gochecknoglobals
    - gochecknoinits
    - gocognit
    - goconst
    - godot
    - ireturn
    - lll
    - maintidx
    - mnd
    - nestif
    - nlreturn
    - nolintlint
    - nonamedreturns
    - paralleltest
    - revive
    - testpackage
    - varnamelen
    - wsl
    - wsl_v5

formatters:
  enable: []

run:
  timeout: 5m
  relative-path-mode: cfg
  issues-exit-code: 1
  tests: true
  build-tags:
    - unit
```

---

### `.github/workflows/ci.yaml`

```yaml
name: Continuous Integration

on:
  push:
    branches:
      - master
      - main
      - v*
  pull_request:
    branches:
      - master
      - main
      - v*

jobs:

  test:
    name: Test
    runs-on: ubuntu-latest
    permissions:
      contents: read
    env:
      CGO_ENABLED: "0"
      GOLANGCI_LINT_VERSION: "v2.11.4"
    steps:

      - name: Check out code
        uses: actions/checkout@v6

      - name: Set up Go
        uses: actions/setup-go@v6
        with:
          go-version-file: 'go.mod'

      - name: Check Go dependency minimum age
        run: |
          go install github.com/fchimpan/gomod-age@09005169a4792ad1a4824e1fc6d85785d91cea36
          gomod-age

      - name: Run golangci-lint
        uses: golangci/golangci-lint-action@v9
        with:
          version: ${{ env.GOLANGCI_LINT_VERSION }}

      - name: Check diff
        run: |
          echo "If this fails, please run 'make gen-config' to fix"
          make check-config-diff

      - name: Test
        run: |
          make test-race
```

---

### `.github/workflows/build-and-publish.yaml`

Replace all occurrences of `sample-app` with `{{APP_NAME}}` and the buildinfo package path with `{{MODULE_PATH}}/pkg/buildinfo`.

```yaml
name: Build and publish

on:
  push:
    branches:
      - "main"
    tags:
      - "v*"

permissions:
  contents: read
  packages: write
  attestations: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v6

      - name: Set up Go
        uses: actions/setup-go@v6
        with:
          go-version-file: 'go.mod'
          # Do not cache in release workflows
          cache: false

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4
        with:
          # Do not cache in release workflows
          cache-binary: false

      # Lowercase REPO_OWNER which is required for containers
      - name: Set lowercase REPO_OWNER
        run: |
          REPO_OWNER=${{ github.repository_owner }}
          echo "REPO_OWNER=${REPO_OWNER,,}" >>${GITHUB_ENV}

      - name: Generate container tags and labels
        id: meta
        uses: docker/metadata-action@v6
        with:
          images: ghcr.io/${{ env.REPO_OWNER }}/{{APP_NAME}}
          # generate semver tags and 'latest' tag
          tags: |
            type=edge,branch=main
            type=semver,pattern=v{{version}}
            type=semver,pattern=v{{major}}.{{minor}}
            type=semver,pattern=v{{major}}

      - name: Set variables
        run: |
          BUILD_ID=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.version'] }}
          BUILD_VERSION=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.version'] }}
          BUILD_DATE=${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.created'] }}
          COMMIT_HASH=$(echo "${{ fromJSON(steps.meta.outputs.json).labels['org.opencontainers.image.revision'] }}" | head -c 7)

          echo "BUILD_ID=$BUILD_ID" >> $GITHUB_ENV
          echo "BUILD_VERSION=$BUILD_VERSION" >> $GITHUB_ENV
          echo "BUILD_DATE=$BUILD_DATE" >> $GITHUB_ENV
          echo "COMMIT_HASH=$COMMIT_HASH" >> $GITHUB_ENV

          echo "BUILD_ID: '$BUILD_ID'"
          echo "BUILD_VERSION: '$BUILD_VERSION'"
          echo "BUILD_DATE: '$BUILD_DATE'"
          echo "COMMIT_HASH: '$COMMIT_HASH'"

          BUILDINFO_PKG="{{MODULE_PATH}}/pkg/buildinfo"
          BUILD_LDFLAGS="-X ${BUILDINFO_PKG}.Production=1 -X ${BUILDINFO_PKG}.AppVersion=${BUILD_VERSION} -X ${BUILDINFO_PKG}.BuildId=${BUILD_ID} -X ${BUILDINFO_PKG}.BuildDate=${BUILD_DATE} -X ${BUILDINFO_PKG}.CommitHash=${COMMIT_HASH} -buildid=${BUILD_ID}"

          echo "BUILD_LDFLAGS=$BUILD_LDFLAGS" >> $GITHUB_ENV

          echo "BUILD_LDFLAGS: '$BUILD_LDFLAGS'"

      - name: Login to container registry
        uses: docker/login-action@v4
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Build for all platforms
        env:
          CGO_ENABLED: "0"
        run: |
          mkdir -p .bin .out

          echo -e "\n###\nBuilding linux/amd64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64
          GOOS=linux GOARCH=amd64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64/{{APP_NAME}} \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64
          (cd .bin && tar -czvf ../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64.tar.gz {{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64)

          echo -e "\n###\nBuilding linux/arm64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64
          GOOS=linux GOARCH=arm64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64/{{APP_NAME}} \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64
          (cd .bin && tar -czvf ../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64.tar.gz {{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64)

          echo -e "\n###\nBuilding linux/armv7\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7
          GOOS=linux GOARCH=arm GOARM=7 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7/{{APP_NAME}} \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7
          (cd .bin && tar -czvf ../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7.tar.gz {{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7)

          echo -e "\n###\nBuilding windows/amd64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64
          GOOS=windows GOARCH=amd64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64/{{APP_NAME}}.exe \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64
          (cd .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64 && zip -r ../../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-x64.zip .)

          echo -e "\n###\nBuilding windows/arm64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64
          GOOS=windows GOARCH=arm64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64/{{APP_NAME}}.exe \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64
          (cd .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64 && zip -r ../../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-windows-arm64.zip .)

          echo -e "\n###\nBuilding freebsd/amd64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64
          GOOS=freebsd GOARCH=amd64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64/{{APP_NAME}} \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64
          (cd .bin && tar -czvf ../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64.tar.gz {{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-amd64)

          echo -e "\n###\nBuilding freebsd/arm64\n"
          mkdir .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64
          GOOS=freebsd GOARCH=arm64 \
            go build \
              -ldflags "${{ env.BUILD_LDFLAGS }}" \
              -o .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64/{{APP_NAME}} \
              -trimpath \
              ./cmd
          cp LICENSE.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64
          cp -r README.md .bin/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64
          (cd .bin && tar -czvf ../.out/{{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64.tar.gz {{APP_NAME}}-${{ env.BUILD_ID }}-freebsd-arm64)

          echo -e "\n###\nLinks for Docker buildx\n"
          (
            cd .bin && \
            ln -v -s {{APP_NAME}}-${{ env.BUILD_ID }}-linux-amd64 linux-amd64 && \
            ln -v -s {{APP_NAME}}-${{ env.BUILD_ID }}-linux-arm64 linux-arm64 && \
            ln -v -s {{APP_NAME}}-${{ env.BUILD_ID }}-linux-armv7 linux-arm \
          )

          echo -e "\n###\nCompilation done\n"
          echo ".bin:"
          ls -al .bin
          echo ".out:"
          ls -al .out

      - name: Publish binaries as Actions Artifacts
        uses: actions/upload-artifact@v7
        with:
          name: artifacts
          path: .out
          include-hidden-files: true
          compression-level: 0

      - name: Build and push Container images
        uses: docker/build-push-action@v7
        id: docker-build-push
        with:
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          platforms: linux/amd64,linux/arm64/v8,linux/arm/v7
          context: .
          file: Dockerfile
          push: true

      - name: Binary attestation linux-amd64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: linux-amd64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-linux-amd64/{{APP_NAME}}

      - name: Binary attestation linux-arm64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: linux-arm64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-linux-arm64/{{APP_NAME}}

      - name: Binary attestation linux-armv7
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: linux-armv7/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-linux-armv7/{{APP_NAME}}

      - name: Binary attestation windows-x64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: windows-x64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-windows-x64/{{APP_NAME}}.exe

      - name: Binary attestation windows-arm64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: windows-arm64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-windows-arm64/{{APP_NAME}}.exe

      - name: Binary attestation freebsd-amd64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: freebsd-amd64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-freebsd-amd64/{{APP_NAME}}

      - name: Binary attestation freebsd-arm64
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: freebsd-arm64/{{APP_NAME}}
          subject-path: |
            .bin/{{APP_NAME}}-*-freebsd-arm64/{{APP_NAME}}

      - name: Container image attestation
        uses: actions/attest-build-provenance@v4
        if: startsWith(github.ref, 'refs/tags/v')
        with:
          subject-name: 'ghcr.io/${{ env.REPO_OWNER }}/{{APP_NAME}}'
          subject-digest: ${{ steps.docker-build-push.outputs.digest }}
          push-to-registry: true
```

**Important note for `build-and-publish.yaml`:** The `{{version}}`, `{{major}}.{{minor}}`, and `{{major}}` inside the `tags:` block under `docker/metadata-action` are **Docker metadata-action template expressions**, NOT skill placeholders. Leave them exactly as-is. Only replace `sample-app` with `{{APP_NAME}}` and the Go module buildinfo path with `{{MODULE_PATH}}/pkg/buildinfo`.

Note: in a release pipeline, which has access to the id-token, we must disable all shared caches.

---

### `.gitignore`

Generate `.gitignore` from:

`https://www.toptal.com/developers/gitignore/api/linux,macos,windows,visualstudiocode,go`

Then add the project-specific entries at the top:

```gitignore
/scratch
/config.yaml
/config.*.yaml
!/config.sample.yaml
```

---

### `.gomod-age.json`

Configures [`gomod-age`](https://github.com/fchimpan/gomod-age), used by CI to ensure no dependency is younger than the configured threshold. Ignore the project's own modules and the Go subrepositories.

```json
{
  "age": "7d",
  "ignore": [
    "github.com/italypaleale/*",
    "golang.org/x/*"
  ]
}
```

---

### `AGENTS.md`

Coding-style guardrails for assistants working on the repo. Generate verbatim (this file is not parameterized). The outer code block below uses four backticks so the embedded Go fences (three backticks) render correctly — in the written file, use normal triple-backtick fences.

````markdown
# Coding Style Guidelines

## Go

Never define variables inside `if` conditions. Always declare variables on a separate line before the conditional check.

```go
// Wrong
if err := something(); err != nil { ... }

// Wrong
if val, ok := something.(string); ok { ... }

// Right
err := something()
if err != nil { ... }

// Right
val, ok := something.(string)
if ok { ... }
```

If you modify `pkg/config.Config` or any struct referenced from it, always run `make gen-config` before finishing the task.

## Comments

- One sentence per line; do not wrap to a max line length
- No trailing period on single-line comments
- Prefer comments that explain intent, invariants, or why a branch exists
- Avoid comments that simply restate the next line of code
- For multi-step logic, use short section comments to separate the steps and explain why each step exists

```go
// Wrong — wrapped mid-sentence
// This function performs the main validation logic. It checks
// the input against the schema and returns an error if the
// input is invalid.

// Wrong — trailing period on single-line comment
// Validate the input.

// Right
// This function performs the main validation logic
// It checks the input against the schema and returns an error if the input is invalid

// Right
// Validate the input

// Right
// Normalize the request host so callers can pass either Host or X-Forwarded-Host values

// Right
// Browsers do not accept a cookie Domain attribute set to an IP address
// Returning an empty domain tells the caller to set a host-only cookie instead

// Wrong — restates the code
// Trim whitespace and lowercase the host
host = strings.TrimSpace(strings.ToLower(host))
```

## Git

Do not stage or unstage changes unless the user explicitly asks you to.
````

---

## Post-Scaffold Steps

After writing all files:

1. Run `go mod init {{MODULE_PATH}}` to create `go.mod`.
2. Run `go mod tidy` to resolve and download dependencies.
3. Register the `gen-config` tool: `go get -tool github.com/italypaleale/go-kit/tools/gen-config` (adds a `tool` directive to `go.mod`).
4. Run `make gen-config` to produce `config.md` and `config.sample.yaml` from the `Config` struct annotations.
5. Run `git init` if the directory is not already a git repository.
6. Verify the project compiles with `go build ./cmd`.
7. Run `make lint` to confirm the linter configuration works.
8. Run `make test` to confirm tests pass (there are none yet, but the command should succeed).
9. Run `make check-config-diff` to confirm the generated config files are in sync with the struct.

## Architecture Notes

This scaffold uses the following patterns and libraries:

- **`github.com/italypaleale/go-kit`**: Shared library for config loading, observability (logs/metrics/traces), HTTP server utilities, TLS config, service lifecycle, and signal handling.
- **Service runner pattern**: Services implement `func(ctx context.Context) error` and run via `servicerunner.NewServiceRunner`. Context cancellation triggers graceful shutdown.
- **Configuration**: YAML-based config loaded via env var (`{{CONFIG_ENV_VAR}}`) or standard config directories (`~/.config/{{APP_NAME}}/`, `/etc/{{APP_NAME}}/`). Singleton accessed via `config.Get()`. Field comments with `+default` and `+required` markers feed the `gen-config` tool, which emits `config.md` (documentation) and `config.sample.yaml` (annotated sample). CI fails if these drift from the struct (`make check-config-diff`).
- **Observability**: OpenTelemetry for metrics and traces; `slog` for structured logging with JSON or text output. Health check endpoint at `GET /healthz`.
- **TLS**: Automatic TLS certificate loading and hot-reloading from disk. Certificates can be provided via file path or inline PEM in config.
- **Build info**: Version, build ID, commit hash, and build date injected at compile time via `-ldflags`.
- **Container image**: Distroless base (`gcr.io/distroless/static-debian12:nonroot`), multi-arch (amd64, arm64, armv7).
- **CI/CD**: GitHub Actions for linting, dependency-age check (`gomod-age`), config-diff check, and testing on PRs; multi-platform build + container publish on push to main/tags.
- **Dependency age guard**: `gomod-age` (configured via `.gomod-age.json`) blocks CI when any non-ignored dependency is younger than the configured age threshold (default 7 days), reducing exposure to fresh supply-chain compromises.

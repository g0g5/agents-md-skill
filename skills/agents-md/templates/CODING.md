## Project Overview
[One sentence: what this project does and its core stack.]

## Tech Stack
- Language: [e.g. TypeScript, Python, Rust]
- Runtime / Framework: [e.g. Node.js, React, FastAPI]
- Key Dependencies: [e.g. PostgreSQL, Redis, Kafka]
- Package Manager: [e.g. pnpm, poetry, cargo]

## Structural Map
[Compact tree with short `#` comments explaining why each included path matters.]

Example:

```
my-ts-service/
|- src/                        # Runtime application modules for the service
|  |- server.ts                # Boots the HTTP server and application startup flow
|  |- config.ts                # Loads and validates environment and service config
|  |- auth/                    # Authentication and authorization module
|  |  |- routes.ts             # Registers auth HTTP routes
|  |  |- service.ts            # Coordinates login, token, and session logic
|  |  \- providers/           # External auth provider integrations
|  |     \- ...               # Folded provider implementations such as google.ts and github.ts
|  |- users/                   # User domain logic and related operations
|  |  |- repository.ts         # Shared persistence interface for user data access
|  |  \- profiles/            # Profile-related user flows
|  |     |- controller.ts      # Handles profile HTTP endpoints
|  |     \- service.ts         # Orchestrates profile read/write operations
|  \- common/                  # Shared utilities, types, and cross-cutting helpers
|     |- errors.ts             # Common application error types
|     \- ...                   # Folded helpers such as logging.ts and metrics.ts
|- docs/                       # Project documentation for developers and maintainers
|  |- api/                     # API contracts, endpoint behavior, and examples
|  \- architecture/           # System design, decisions, and module boundaries
\- tests/                      # Automated test modules
   |- unit/                    # Fast tests for isolated module behavior
   |  \- ...                   # Folded unit suites for auth, users, and common helpers
   \- integration/             # Tests for module interactions and external boundaries
```

Rules:
- Include meaningful directory hierarchy, including deeper nested directories when they clarify module boundaries.
- In monorepos, include each app and shared package as a top-level module.
- Include files only when architecturally important (entrypoints, shared foundations, registries, orchestration files).
- Omit leaf implementation files and repetitive sibling files that are mostly interchangeable, unless one is the canonical entrypoint or shared base.
- Exclude dot-prefixed internals and generated, build, cache, and vendor directories unless they are part of the core source layout.
- Use `- ...` or `- ...` to fold repetitive siblings.

## Development Guide
### Commands
[List only commands used in nearly every task. Prefer verified commands from package manifests, Makefiles, CI config, or repository docs.]

Example:

```
# Build (if applicable)
pnpm build

# Run all tests
pnpm test

# Typecheck
pnpm typecheck

# Lint
pnpm lint

# Run a single test file (fast verification loop)
pnpm test -- path/to/file.test.ts
```

Rules:
- Include build, tests, typechecks, and verification commands only when they exist or are clearly supported.
- Do not list every possible command — only those used in nearly every coding session.
- If a common command is not discoverable, say so briefly rather than inventing one.

### Workflows
[No content yet.]

Rules:
- Only fill this when an existing `AGENTS.md` explicitly documents development workflows. Use it for higher-level development processes, not extra command lists.
- Do not invent workflows from scripts, package names, or common project conventions.
- Preserve or refresh explicit existing workflows only when they remain accurate for the current project.

## Notes
[Free-form: anything important about the project that doesn't fit above — conventions, caveats, environment quirks, onboarding tips, external references, etc.]

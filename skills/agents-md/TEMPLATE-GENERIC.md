## Overview
[One sentence: what this project/repository is and its purpose.]

## Structural Map
[Compact tree with short `#` comments explaining each section's role and why it matters.]

Example:

```
my-docs-project/
|- docs/                       # Core documentation content
|  |- guides/                  # Step-by-step tutorials and how-tos
|  |  |- getting-started.md    # Onboarding entrypoint for new users
|  |  \- advanced-usage.md     # Power-user scenarios and deep dives
|  |- reference/               # API references, config specs, data dictionaries
|  |  |- api.md                # REST / gRPC endpoint descriptions
|  |  \- config.md             # Full configuration option reference
|  \- internals/               # Architecture, design decisions, contributor docs
|     |- architecture.md       # System design and component diagrams
|     \- decisions/            # Architecture Decision Records
|        \- ...                # ADRs in numbered markdown files
|- assets/                     # Images, diagrams, and other binary resources
|  |- diagrams/                # Excalidraw, Mermaid, or image files
|  \- screenshots/             # UI screenshots used in docs
|- scripts/                    # Automation helpers (link checks, deploy previews)
|  |- validate-links.sh        # Checks for broken internal links
|  \- deploy-preview.sh        # Pushes staging preview to hosting
\- .github/                    # CI/CD and repo governance
   |- workflows/               # GitHub Actions workflow definitions
   \- CODEOWNERS               # Review ownership per path
```

Rules:
- Include meaningful hierarchy, drilling into sections that define the project's organization.
- Include files only when they are entrypoints or serve a unique, architecturally significant role.
- Omit repetitive leaves and use `- ...` to fold interchangeable siblings.
- Exclude generated, cache, and deeply internal tooling unless core to the project.

## Working Guide
[How to perform the most common tasks for this project: editing, reviewing, validating, deploying, etc.]

Example:

```
# Validate internal links
./scripts/validate-links.sh

# Preview docs locally
npx vitepress dev docs

# Build for production
npx vitepress build docs
```

Rules:
- List only tasks an agent would perform in nearly every session.
- Prefer verified commands from project scripts, workflow files, or existing docs.
- Do not list every possible task.
- If a common task has no discoverable command, say so briefly rather than inventing one.

## Notes
[Free-form: anything important about the project that doesn't fit above — conventions, caveats, ownership, external references, environment quirks, etc.]

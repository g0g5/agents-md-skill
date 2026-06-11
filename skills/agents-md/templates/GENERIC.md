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
[No content yet.]

Example shape, only when explicitly present in an existing `AGENTS.md`:

```
### Content Update Flow
- Update the relevant source content and any linked assets together.
- Review downstream references before publishing.
- Use the documented validation or publishing step from the existing guide.

### Publishing Flow
- Prepare draft changes in the documented staging area.
- Request the documented owner review.
- Publish through the documented release path.
```

Rules:
- Use `[No content yet.]` when creating a new `AGENTS.md` or when the existing `AGENTS.md` does not already spell out workflows.
- Only fill this when an existing `AGENTS.md` explicitly documents higher-level project workflows or operation sets. Use it for working guidance, not a command inventory.
- Do not infer workflows from project structure, scripts, workflow files, documentation layout, or common project conventions.
- Preserve or refresh explicit existing workflows only when they remain accurate for the current project.
- If an explicit workflow includes commands, keep them only as supporting steps inside that workflow, not as a standalone command list.

## Notes
[Free-form: anything important about the project that doesn't fit above — conventions, caveats, ownership, external references, environment quirks, etc.]

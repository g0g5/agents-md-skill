## Overview
Repository for the `agents-md` Agent Skill, which guides agents to create, refresh, audit, and migrate concise `AGENTS.md` onboarding files.

## Tech Stack
- Language: Markdown skill instructions only
- Runtime / Framework: Agent skill packages for Claude Code, OpenCode, and compatible clients
- Key Dependencies: None
- Package Manager: None

## Structural Map
```
agents-md-skill/
|- README.md                         # Overview, manual install docs, and expected behavior
`- skills/
   `- agents-md/
      |- SKILL.md                    # Skill metadata, workflow, and `.agents/` index rules
      |- MIGRATION.md                # Legacy `AGENTS.md` detection, splitting, and reporting steps
      |- guides/
      |  |- CODING.md                # Inspection focus and quality bar for code projects
      |  `- GENERIC.md               # Inspection focus and quality bar for non-code projects
      `- templates/
         `- AGENTS.md                # Canonical AGENTS.md template for all projects
```

## Commands
No build, test, lint, typecheck, Makefile, or script-based validation commands are currently defined. Verify changes by reviewing the markdown files directly.

## Workflows
- [install.md](.agents/workflows/install.md) - Install a local copy of the skill for Claude Code, OpenCode, or other clients.

## Notes
- [generated-content-style.md](.agents/notes/generated-content-style.md) - Keep skill output and package guidance concise and project-specific.
- [skill-alignment.md](.agents/notes/skill-alignment.md) - Keep SKILL.md, guides, template, and README behavior aligned.

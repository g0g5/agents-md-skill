## Overview
This repository contains the `agents-md` skill, which helps OpenCode agents create, refresh, audit, fix, and maintain concise project `AGENTS.md` onboarding files.

## Structural Map
```
agents-md-skill/
|- README.md                         # Overview, manual install docs, and expected behavior
`- skills/
   `- agents-md/
      |- SKILL.md                    # Skill metadata and workflow for AGENTS.md creation/update tasks
      |- guides/
      |  |- CODING.md                # Guide for software/code projects
      |  `- GENERIC.md               # Guide for docs/config/non-code projects
      `- templates/
         |- CODING.md                # Canonical AGENTS.md template for coding projects
         `- GENERIC.md               # Canonical AGENTS.md template for generic projects
```

## Working Guide
```
# Install for Claude Code after cloning
mkdir -p ~/.claude/skills/agents-md
cp -R skills/agents-md/. ~/.claude/skills/agents-md/

# Install for OpenCode and other clients after cloning
mkdir -p ~/.agents/skills/agents-md
cp -R skills/agents-md/. ~/.agents/skills/agents-md/
```

No build, test, lint, typecheck, Makefile, or script-based validation commands are currently defined.

## Notes
- Keep `SKILL.md`, guides, templates, and README behavior aligned when changing the skill workflow.
- Generated AGENTS.md guidance in this package should stay concise, practical, and focused on project-specific onboarding details.

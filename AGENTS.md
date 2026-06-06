## Overview
This repository is an APM package for the `agents-md` skill, which helps OpenCode agents create, refresh, audit, fix, and maintain concise project `AGENTS.md` onboarding files.

## Structural Map
```
agents-md-skill/
|- README.md                         # Package overview, install docs, expected behavior, and preview commands
|- apm.yml                           # APM package metadata, target configuration, and included payload paths
`- .apm/                             # Core APM package payload despite the dot prefix
   `- skills/
      `- agents-md/
         |- SKILL.md                 # Skill metadata and workflow for AGENTS.md creation/update tasks
         |- guides/
         |  |- CODING.md             # Guide for software/code projects
         |  `- GENERIC.md            # Guide for docs/config/non-code projects
         `- templates/
            |- CODING.md             # Canonical AGENTS.md template for coding projects
            `- GENERIC.md            # Canonical AGENTS.md template for generic projects
```

## Working Guide
```
# Preview installation without writing files
apm install https://github.com/g0g5/agents-md-skill.git --dry-run --target opencode

# Preview packaged contents
apm pack --dry-run --verbose
```

No build, test, lint, typecheck, Makefile, or script-based validation commands are currently defined; `apm.yml` has `scripts: {}`.

## Notes
- Keep `SKILL.md`, guides, templates, and README behavior aligned when changing the skill workflow.
- If adding package payload files, check whether `apm.yml` `includes` must be updated.
- Generated AGENTS.md guidance in this package should stay concise, practical, and focused on project-specific onboarding details.

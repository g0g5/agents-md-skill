# agents-md-skill

APM package for installing the `agents-md` skill, which helps agents create, refresh, audit, fix, and maintain concise `AGENTS.md` project onboarding files.

## Install

From the project where you want to use the skill, install this repository with APM:

```bash
apm install https://github.com/g0g5/agents-md-skill.git --target opencode
```

GitHub shorthand also works:

```bash
apm install g0g5/agents-md-skill --target opencode
```

For OpenCode and other cross-client targets, APM deploys the skill to:

```text
.agents/skills/agents-md/
```

## Expected Behavior

The `agents-md` skill activates when the user asks an agent to create, update, refresh, audit, fix, or maintain an `AGENTS.md` file.

When activated, it guides the agent to:

- Keep a TODO list while working.
- Delegate workspace inspection to one `@explore` or equivalent inspection agent.
- Choose the coding or generic project guide based on the repository type.
- Use the bundled templates to produce a concise, practical `AGENTS.md`.
- Preserve useful existing content when updating an existing file.
- Summarize the changed path, whether the file was created or updated, and any verification performed.

The goal is to create an `AGENTS.md` that helps future coding agents understand the project quickly without adding broad, obvious, or rarely used details.

## Package Layout

This repository uses APM's Multiple primitives layout:

- `.apm/skills/agents-md/SKILL.md` - skill metadata and runtime workflow
- `.apm/skills/agents-md/guides/` - coding and generic project guidance
- `.apm/skills/agents-md/templates/` - canonical `AGENTS.md` templates
- `apm.yml` - APM package metadata and publish include list

## Preview And Pack

Preview installation without writing files:

```bash
apm install https://github.com/g0g5/agents-md-skill.git --dry-run --target opencode
```

Preview the package contents:

```bash
apm pack --dry-run --verbose
```

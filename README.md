# agents-md-skill

Repository for the `agents-md` skill, which helps agents create, refresh, audit, fix, and maintain concise `AGENTS.md` project onboarding files.

## Install

```bash
git clone https://github.com/g0g5/agents-md-skill.git
cd agents-md-skill
```

For Claude Code:

```bash
mkdir -p ~/.claude/skills/agents-md
cp -R skills/agents-md/. ~/.claude/skills/agents-md/
```

For OpenCode and other clients:

```bash
mkdir -p ~/.agents/skills/agents-md
cp -R skills/agents-md/. ~/.agents/skills/agents-md/
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

## Repository Layout

- `skills/agents-md/SKILL.md` - skill metadata and runtime workflow
- `skills/agents-md/guides/` - coding and generic project guidance
- `skills/agents-md/templates/` - canonical `AGENTS.md` templates

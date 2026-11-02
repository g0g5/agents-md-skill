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
- Choose the coding or generic project guide based on the repository type, while using the single bundled template for the section layout.
- Produce a concise, practical `AGENTS.md` with `Overview`, `Tech Stack`, `Structural Map`, `Commands`, `Workflows`, and `Notes`.
- Keep `Workflows` and `Notes` as one-line indexes of markdown files under `.agents/workflows/` and `.agents/notes/`, and never inline that content.
- Only read those directories during a routine update. Files there are created only when the user asks for it or when legacy content is migrated.
- Migrate legacy content by splitting existing workflow and note prose into short, topic-focused files under `.agents/`, following `MIGRATION.md`.
- Preserve useful existing content when updating an existing file.
- Summarize the changed path, whether the file was created, updated, or migrated, and any verification performed.

The goal is to create an `AGENTS.md` that helps future coding agents understand the project quickly without adding broad, obvious, or rarely used details.

## Repository Layout

- `skills/agents-md/SKILL.md` - skill metadata, runtime workflow, and `.agents/` index rules
- `skills/agents-md/MIGRATION.md` - legacy `AGENTS.md` detection, splitting, and reporting steps
- `skills/agents-md/guides/` - coding and generic project inspection guidance and quality bars
- `skills/agents-md/templates/AGENTS.md` - canonical `AGENTS.md` template

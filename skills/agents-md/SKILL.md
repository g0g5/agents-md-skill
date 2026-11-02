---
name: agents-md
description: Use when the user asks to create, refresh, audit, fix, or maintain AGENTS.md for a project. Create or update a concise, practical agent onboarding file.
compatibility: Requires an explore subagent or equivalent delegated workspace-inspection agent.
---

# AGENTS.md Workflow

Use this skill to create or update `AGENTS.md` in a project. The goal is a short, useful file that helps agents become productive quickly without burying them in obvious or rarely used details.

## Core Workflow

- Create a TODO list before starting and keep it current.
- Delegate workspace inspection to exactly one `@explore` agent. Do not inspect the workspace yourself before delegation.
- Treat the user's instructions and any existing `AGENTS.md` content rules as higher priority than this skill's instructions. When they conflict, follow the user's instructions and existing rules.
- Keep the final `AGENTS.md` concise and practical.
- Prefer the smallest correct update when an `AGENTS.md` already exists.
- Keep every template section heading even when there is no suitable content. Write `[No content yet.]` as the section content in that case.

## Guide Selection

Read the appropriate guide before writing, and use `templates/AGENTS.md` for the section layout in every case:

- `guides/CODING.md` - for software/code projects. It defines the inspection focus and quality bar for code repositories.
- `guides/GENERIC.md` - for documentation, configuration, and other non-code projects. It defines the inspection focus and quality bar for non-code repositories.

If the project type is unclear from the request, read both guides and ask the delegated inspection to classify the workspace before choosing the final guide.

## Delegated Inspection

Ask the single `@explore` agent to return a concise report covering WHAT (project type, stack or content areas, structure tree with one-line purpose per item), WHY (project purpose and role of each major component), and HOW (only the most universally needed commands).

Always add these inspection requirements on top of the guide-specific ones:

- List every markdown file under `.agents/workflows/` and `.agents/notes/`, including nested subdirectories, with its `#` heading or first summary sentence. `.agents/` is dot-prefixed, so it must not be skipped as an internal directory.
- When an `AGENTS.md` exists, return the verbatim body of its `Workflows`, `Notes`, `Working Guide`, and `Development Guide` sections so legacy content can be checked against the new layout.

## Workflows and Notes Files

`AGENTS.md` never stores workflow or note content itself. It only indexes files under `.agents/`.

- `Workflows` lists markdown files under `.agents/workflows/`.
- `Notes` lists markdown files under `.agents/notes/`.
- Subdirectories are allowed and scanned recursively.

Index entry format:

```markdown
- [release/publish.md](.agents/workflows/release/publish.md) - Release flow: bump version, update changelog, push tag.
```

- Use the path relative to `.agents/workflows/` or `.agents/notes/` as the link text, and sort entries by path.
- Prefer the markdown link form so editors and agents can open the file directly.
- Take the description from the file's `#` heading or its first summary sentence. If neither exists, summarize the file in one short sentence without editing the file.
- Write `[No content yet.]` when the directory is missing or contains no markdown files.

Default behavior: a routine `AGENTS.md` create or update only reads these directories and refreshes the index. Do not create, modify, delete, or move files under `.agents/` unless:

1. The user explicitly asks for it.
2. Existing `AGENTS.md` content is being migrated (see `MIGRATION.md`).

File conventions for workflow and note files:

- One topic per file, kebab-case filename, short body.
- Put `# Title` first, then one summary sentence, then concise steps or bullet points.
- Keep each file focused enough to be read on its own.

## Starting State

Identify which case applies from the user's request and the delegated inspection result:

- No existing `AGENTS.md`: create a new one from `templates/AGENTS.md`.
- Existing `AGENTS.md` already in the indexed layout: update it only where it is stale, incomplete, or conflicts with the current project structure, purpose, stack, tooling, or commands, and refresh the `Workflows` and `Notes` indexes.
- Existing `AGENTS.md` in the legacy layout: migrate it with `MIGRATION.md`.

When updating an existing file, preserve accurate useful content. Do not rewrite for style alone.

## Legacy Migration

Read `MIGRATION.md` before touching an existing `AGENTS.md` whose `Workflows`, `Working Guide`, or `Notes` sections hold prose instead of file links, or which still uses older section names. That file defines how to detect a legacy layout, how to split content into `.agents/workflows/` and `.agents/notes/` files, and how to report the result.

## Response Summary

After creating or updating the file, summarize:

- The path changed.
- Whether this was a new file, an update, or a migration.
- Any commands or verification steps run, or why they were not run.
- For a migration: the reporting items listed in `MIGRATION.md`.
